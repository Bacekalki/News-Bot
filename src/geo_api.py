import requests

def get_latitude_longitude(city : str, country : str) -> tuple[float, float]:
    url = f'https://nominatim.openstreetmap.org/search?q={city},{country}&format=json'

    headers = {
    "User-Agent": "News_Weather_Bot/1.0"
}

    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code == 200:
        data = response.json()
        return (data[0]['lat'], data[0]['lon'])

    return (0, 0)
