import os
import yfinance as yf

from datetime import date
from telegram import ParseMode, Bot

from scripts.plot import create_weekly_plot
from scripts.database import return_balance

TOKEN, CHAT_ID = os.environ["TOKEN"], os.environ["CHAT_ID"]


def send_daily_report():
    bot = Bot(token=TOKEN)

    today       = date.today().strftime('%d/%m/%Y')
    now, last   = return_balance(2)
    dif         = (now - last) / last

    text   = f'<b>Daily report</b> ({today})\n\nYour account\'s balance is {now:.2f}€ ({dif:+.2%}).'
    text  += f'\n\n<pre>Watchlist\n'

    for stock in ['^IBEX', '^GSPC', '^IXIC', 'BTC-USD']:
        ticker  = yf.Ticker(stock)
        per     = ticker.history()['Close'].pct_change()[today]
        text   += f'\n{stock:<15} {per:+.2%}'

    bot.send_message(chat_id=CHAT_ID, text=text+'</pre>', parse_mode=ParseMode.HTML)

def send_weekly_report():
    create_weekly_plot()

    bot     = Bot(token=TOKEN)

    week    = date.today().strftime('%U/%Y')
    balance = return_balance(5)
    dif     = (balance[0] - balance[-1]) / balance[-1]

    text    = f'<b>Weekly report</b> ({week})\nDuring this week, your investment have yield a total of {dif:+.2%}.'
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode=ParseMode.HTML)
    bot.send_photo(chat_id=CHAT_ID, photo=open('plots/weekly-report.png', 'rb'))
