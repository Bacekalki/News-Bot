import yagmail
from pymysql.connections import Connection
from pymysql.cursors import Cursor
from src.subscription_manager import get_emails
from src.news_retriever import insert_into_db, get_top_news_api, get_top_news_database
from src.preference_manager import get_user_preferences


def update_database(conn : Connection) -> None:
    cursor : Cursor = conn.cursor()
    delete_querry = """DELETE FROM news"""

    cursor.execute(delete_querry)
    conn.commit()

    categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology', 'None']

    for category in categories:
        insert_into_db(conn, get_top_news_api(category))

    cursor.close()


def create_newsletter(conn : Connection, username : str) -> str:
    preferences = get_user_preferences(conn, username)

    if len(preferences) == 0:
        news = get_top_news_database(conn)
        return '\n'.join(str(item) for item in news)

    res = []
    for preference in preferences:
        res += get_top_news_database(conn, preference)[:3]

    return '\n'.join(str(item) for item in res)

def send_mail(yag : yagmail.SMTP, recipient : str, content : str) -> None:
    yag.send(
        to=recipient,
        subject='Daily newsletter',
        contents=content
    )

def routine(conn : Connection, yag : yagmail.SMTP) -> None:
    update_database(conn)

    users = get_emails(conn)
    for username, mail in users:
        newsletter = create_newsletter(conn, username)
        send_mail(yag, mail, newsletter)
