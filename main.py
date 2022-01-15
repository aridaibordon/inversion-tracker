from datetime import date

from degiro import get_degiro_balance
from database import update_degiro_db, create_database
from bot import send_degiro


def main(hour=None):
    create_database()
    if date.today().weekday() < 6:
        balance = get_degiro_balance()

        update_degiro_db(balance)
        send_degiro(balance)


if __name__ == "__main__":
    main()
