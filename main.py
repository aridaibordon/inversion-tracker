import schedule
import os.path
import time

from degiro import get_degiro_balance
from database import update_degiro, create_database
from bot import send_degiro

def main_task(hour=None):
    update_degiro(get_degiro_balance())
    send_degiro()

def main():
    for hour in ["21:00"]:
        schedule.every().monday.at(hour).do(main_task, hour)
        schedule.every().tuesday.at(hour).do(main_task, hour)
        schedule.every().wednesday.at(hour).do(main_task, hour)
        schedule.every().thursday.at(hour).do(main_task, hour)
        schedule.every().friday.at(hour).do(main_task, hour)

    while True:
        schedule.run_pending()
        time.sleep(300)

if __name__ == "__main__":
    if not(os.path.isfile("inverison.db")):
        create_database()

    main_task()