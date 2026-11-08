from pymysql.connections import Connection
from pymysql.cursors import Cursor


def subscribe(conn : Connection, username : str, email : str) -> str:
    cursor : Cursor = conn.cursor()
    get_subsribed = """SELECT username FROM subscribed"""

    cursor.execute(get_subsribed)
    rows = cursor.fetchall()

    if username in {user for (user, ) in rows}:
        cursor.close()
        return 'You are already subscribed'

    insert_query = f""" INSERT INTO subscribed (username, email) VALUES ('{username}', '{email}')"""
    cursor.execute(insert_query)
    conn.commit()

    cursor.close()
    return 'Subscribed successfully'

def unsubscribe(conn : Connection, username : str) -> str:
    cursor : Cursor = conn.cursor()

    delete_query = f""" DELETE FROM subscribed WHERE username = '{username}'"""
    cursor.execute(delete_query)
    conn.commit()

    return 'Deleted successfully'

def get_emails(conn : Connection) -> list[tuple[str, str]]:
    cursor : Cursor = conn.cursor()
    sql = """Select username, email from subscribed"""
    cursor.execute(sql)

    rows = cursor.fetchall()
    cursor.close()
    return list(rows)
