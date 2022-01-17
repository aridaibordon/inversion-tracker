import os

from telegram import Bot
from scripts.database import return_balance

TOKEN, CHAT_ID = os.environ["TOKEN"], os.environ["CHAT_ID"]


def send_degiro():
    bot = Bot(token=TOKEN)
    
    data = return_balance(2)
    bot.send_message(chat_id=CHAT_ID, text=f"Tu portfolio total en DEGIRO es {data[0]}" + f" ({(data[0]-data[1])/data[1]:+.2%})"*(len(data)==2) + "€")


def send_weekly_report():
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text='Tu informe semanal está listo.')
    bot.send_photo(chat_id=CHAT_ID, photo=open('plots/weekly-report.png', 'rb'))