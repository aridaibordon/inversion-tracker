import schedule
import time

from get_balance import get_degiro_balance
from database import update_degiro
from bot import send_degiro

def main_task(hour=None):
    degiro_balance = get_degiro_balance()
    update_degiro(degiro_balance)

    if hour == "21:00":
        send_degiro(degiro_balance)

def main():
    for hour in ["08:00", "14:30", "21:00"]:
        schedule.every().monday.at(hour).do(main_task, hour)
        schedule.every().tuesday.at(hour).do(main_task, hour)
        schedule.every().wednesday.at(hour).do(main_task, hour)
        schedule.every().thursday.at(hour).do(main_task, hour)
        schedule.every().friday.at(hour).do(main_task, hour)

    while True:
        schedule.run_pending()
        time.sleep(300)

if __name__ == "__main__":
    main_task()