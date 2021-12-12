import sqlite3

from telegram import Bot
from env.config import TOKEN, CHAT_ID

def dif_to_str(dif):
    if dif < 0:
        text = "- "
    else:
        text = "+ "
    return text + f"{dif:.2f}"

def send_degiro():
    con         = sqlite3.connect("inversion.db")
    cur         = con.cursor()
    sel         = cur.execute("SELECT balance FROM degiro ORDER BY id DESC LIMIT 2").fetchall()
    
    bal, dif    = sel[0][0], sel[0][0] - sel[1][0]
    
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=f"Tu portfolio total en DEGIRO es {bal} ({dif_to_str(dif)})€")