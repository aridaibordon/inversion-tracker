import os

from telegram import Bot
from scripts.database import return_balance

TOKEN, CHAT_ID = os.environ["TOKEN"], os.environ["CHAT_ID"]


def dif_to_str(dif):
    if dif > 0:
        return "+" + dif
    return dif


def send_degiro():
    bot = Bot(token=TOKEN)
    data = return_balance()

    if len(data) == 2:
        bot.send_message(
            chat_id=CHAT_ID,
            text=f"Tu portfolio total en DEGIRO es {data[0]} ({dif_to_str(data[0]-data[1])})€"
        )
    else:
        bot.send_message(
            chat_id=CHAT_ID,
            text=f"Tu portfolio total en DEGIRO es {data[0]}€"
        )