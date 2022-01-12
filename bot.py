import os
import dotenv

dotenv.load_dotenv()

from telegram import Bot

TOKEN, CHAT_ID = os.environ["TOKEN"], os.environ["CHAT_ID"]


def dif_to_str(dif):
    if dif > 0:
        return "+" + dif
    return dif


def send_degiro(balance):
    bot = Bot(token=TOKEN)
    bot.send_message(
        chat_id=CHAT_ID,
        text=f"Tu portfolio total en DEGIRO es {balance}€",
    )