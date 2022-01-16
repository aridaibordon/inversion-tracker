from datetime import date

from degiro import get_degiro_balance
from database import update_degiro_db, create_database
from bot import send_degiro


def main(hour=None):
    create_database()
    if date.today().weekday() < 5:
        update_degiro_db(get_degiro_balance())
        send_degiro()


if __name__ == "__main__":
    main()
