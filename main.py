import os

import time
import threading
import yagmail
import pymysql
import schedule
from discord import Intents, Client, Message
from discord import HTTPException
from dotenv import load_dotenv
from src.responses import get_response
from src.command_executor import CommandExecutor
from src.routine import routine


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
HOST = os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD  = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')
APP_PASS = os.getenv('APP_PASS')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
conn = pymysql.connect(host=HOST, user=USER,
                           password=PASSWORD, database=NAME)
executor = CommandExecutor(conn)
yag = yagmail.SMTP("botnews1234@gmail.com", APP_PASS)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

schedule.every().day.at("09:00").do(routine, conn, yag)

scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()


async def send_message(message : Message, user_message : str, username : str) -> None:
    if not user_message:
        print('There was an error')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response = get_response(executor, user_message, username)
        if response == '':
            response = 'Sorry, your request is not possible'
        await message.author.send(response) if is_private else await message.channel.send(response)
    except HTTPException as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

@client.event
async def on_message(message : Message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content

    await send_message(message, user_message, username)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
