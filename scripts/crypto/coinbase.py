import os

from coinbase.wallet.client import Client


def load_cb_client() -> Client:
    return Client(os.environ['api_key'], os.environ['api_secret'])


def check_cb_balance() -> float:
    client = load_cb_client()
    accounts = client.get_accounts()

    total_balance = 0

    for wallet in accounts.data:
        wallet_balance = float(str(wallet['native_balance']).split()[1])
        total_balance += wallet_balance

    return total_balance
