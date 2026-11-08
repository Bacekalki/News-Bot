import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
from pymysql.connections import Connection
from pymysql.cursors import Cursor
from src.news_obj import NewsObj


load_dotenv()
MY_KEY = os.getenv('MY_KEY')
api = NewsApiClient(api_key=MY_KEY)

def convert_to_list(json_response, category : str = 'None') -> list[NewsObj]:
    results = json_response['articles']
    return [NewsObj(news['title'], news['source']['name'],
                     news['description'], news['url'], category) for news in results]

def get_top_news_api(preference : str, keywords = '') -> list[NewsObj]:
    if keywords != '':
        keywords = keywords.replace(',', 'AND')

    if preference == 'None':
        top_news = api.get_top_headlines(q=keywords, page_size=9)
    else:
        top_news = api.get_top_headlines(category=preference, q=keywords, page_size=9)

    return convert_to_list(top_news, preference)

def get_top_news_database(conn : Connection, preference  : str = 'None') -> list[NewsObj]:
    cursor : Cursor = conn.cursor()
    get_query = f"""SELECT Title, Source, Description, URL, Category
    FROM news WHERE Category = '{preference}'"""

    cursor.execute(get_query)

    rows = cursor.fetchall()
    cursor.close()

    return [NewsObj(title, source, description, URL, category)
            for title, source, description, URL, category in rows]

def get_top_news(
    conn : Connection, source : str, keywords : str, preference : str
    ) -> list[NewsObj]:
    if source == 'database':
        return get_top_news_database(conn, preference)

    return get_top_news_api(preference, keywords)

def get_everything(
    keywords: str, domain : str, language : str, sort_by : str, page_size : int
    ) -> list[NewsObj]:
    keywords = keywords.replace(',', 'AND')
    results = api.get_everything(q=keywords, domains=domain, language=language,
                                 sort_by=sort_by, page_size=page_size)

    print(len(convert_to_list(results)))
    return convert_to_list(results)

def insert_into_db(conn : Connection, news_list : list[NewsObj]) -> None:
    cursor : Cursor = conn.cursor()
    insert_query = """ INSERT INTO news (Title, Source, Description, URL, Category)
    VALUES (%s, %s, %s, %s, %s)"""

    cursor.executemany(insert_query, [(news.title, news.source,
                                       news.description, news.url, news.category)
                                      for news in news_list])
    conn.commit()
    cursor.close()
