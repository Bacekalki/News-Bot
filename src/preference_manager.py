from pymysql.connections import Connection
from pymysql.cursors import Cursor


def is_valid_preference(preference: str) -> bool:
    return preference in {'business', 'entertainment', 'health', 'science', 'sports', 'technology'}

def get_user_preferences(conn : Connection, username : str) -> list[str]:
    cursor : Cursor = conn.cursor()
    check_query : str = f"SELECT preference FROM users WHERE username = '{username}'"
    cursor.execute(check_query)
    rows = cursor.fetchall()
    cursor.close()
    return [preference for (preference, ) in rows]

def add_preference(conn : Connection, username: str, preference: str) -> str:
    if not is_valid_preference(preference):
        return 'We do not support that preference'

    user_prefernces = get_user_preferences(conn, username)

    if preference in user_prefernces:
        return "You already have that preference"

    cursor : Cursor = conn.cursor()

    insert_query : str = f"""INSERT INTO users (username, preference)
    VALUES ('{username}', '{preference}')"""
    cursor.execute(insert_query)
    conn.commit()
    cursor.close()
    return "Preference addded successfully"

def remove_preference(conn: Connection, username: str, preference: str) -> str:
    if not is_valid_preference(preference):
        return 'We do not support that preference'

    user_prefernces = get_user_preferences(conn, username)

    if preference not in user_prefernces:
        return 'You do not have that preference'

    cursor : Cursor = conn.cursor()
    delete_querry : str = f""" DELETE FROM users WHERE username = '{username}'
    AND preference = '{preference}'"""

    cursor.execute(delete_querry)
    conn.commit()

    cursor.close()
    return 'Preference deleted successfully'
