from datetime import datetime, timezone
import openmeteo_requests
import requests_cache
from retry_requests import retry
from src.geo_api import get_latitude_longitude


cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

URL = "https://api.open-meteo.com/v1/forecast"

def convert_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%d-%m-%Y')


def get_forecast(city : str, country : str) -> list[tuple[str, float, float]]:
    latitude, longitude = get_latitude_longitude(city, country)

    if (latitude, longitude) == (0, 0):
        raise ValueError(f"This city: {city} doesn't exist in our database")
    
    params = {
	"latitude": latitude,
	"longitude": longitude,
	"daily": ["temperature_2m_max", "temperature_2m_min"]
}
    responses = openmeteo.weather_api(URL, params=params)
    responses = responses[0]
    daily = responses.Daily()
    daily_temperature_max = daily.Variables(0)
    daily_temperature_min = daily.Variables(1)
    start = daily.Time()
    interval = daily.Interval()

    return [(convert_timestamp(start + interval * j), round(daily_temperature_min.Values(j=j), 1),
           round(daily_temperature_max.Values(j=j), 1)) for j in range(0, 7)]
