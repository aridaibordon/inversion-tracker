from telegram import Bot
from env.config import TOKEN, CHAT_ID

def send_degiro(balance):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=f"Tu portfolio total en DEGIRO asciende a {balance}€")

if __name__=="__main__":
    pass