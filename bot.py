import os
import sqlite3

from telegram import Bot

TOKEN, CHAT_ID = os.environ["TOKEN"], os.environ["CHAT_ID"]

def dif_to_str(dif):
    if dif > 0:
        return "+" + dif
    else:
        return dif

def send_degiro():
    con         = sqlite3.connect("inversion.db")
    cur         = con.cursor()
    sel         = cur.execute("SELECT balance FROM degiro ORDER BY id DESC LIMIT 2").fetchall()
    
    bal, dif    = sel[0][0], f"{sel[0][0] - sel[1][0]:.2f}"
    
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=f"Tu portfolio total en DEGIRO es {bal} ({dif_to_str(dif)})€")