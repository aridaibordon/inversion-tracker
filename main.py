import os.path

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

from datetime import date

from scripts.degiro import get_degiro_balance
from scripts.database import update_degiro_db, create_database
from scripts.bot import send_daily_report, send_weekly_report


def main(debug=False):
    create_database()
    if date.today().weekday() < 5 or debug:
        update_degiro_db(get_degiro_balance())
        send_daily_report()

    if date.today().weekday() == 5 or debug:
        send_weekly_report()


if __name__ == "__main__":
    main()
