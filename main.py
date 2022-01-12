import os.path
from datetime import date

from degiro import get_degiro_balance
from database import update_degiro, create_database
from bot import send_degiro


def main(hour=None):
    if date.today().weekday() < 5:
        balance = get_degiro_balance()

        update_degiro(balance)
        send_degiro(balance)


if __name__ == "__main__":
    if not os.path.isfile("inversion.db"):
        create_database()
    main()
