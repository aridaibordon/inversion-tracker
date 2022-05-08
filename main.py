import os.path

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

from datetime import date

from scripts.degiro import get_degiro_balance
from scripts.crypto.personal import return_personal_crypto_balance
from scripts.crypto.coinbase import return_cb_balance
from scripts.crypto.coinbase_pro import return_cbpro_balance

from scripts.database import update_balance, create_tables
from scripts.bot import send_daily_report, send_weekly_report


def main(debug=False):
    create_tables()
    if date.today().weekday() < 5 or debug:
        degiro = get_degiro_balance()
        coinbase = return_cb_balance() + return_cbpro_balance()
        personal = return_personal_crypto_balance()

        update_balance(degiro, coinbase, personal)
        send_daily_report()

    if date.today().weekday() == 5 or debug:
        send_weekly_report()


if __name__ == "__main__":
    main()
