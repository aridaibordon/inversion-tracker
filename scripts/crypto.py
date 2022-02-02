import requests
import json

import yfinance as yf


def load_addresses() -> list:
    # Load all addresses in address.txt
    with open('scripts/address.txt', 'r') as file:
        return file.read().split()


def add_new_address(address) -> None:
    # Add new address to address.txt
    with open('scripts/address.txt', 'a') as file:
        file.write(f'{address}\n')


def get_address_balance(address: int) -> float:
    # Return address balance in euros.
    r       = requests.get(f"https://blockchain.info/rawaddr/{address}")
    data    = json.loads(r.text)

    btc_value = yf.Ticker('BTC-EUR').history(period='1d')['Close'][0]

    if "final_balance" in data.keys():
        return data["final_balance"]*btc_value*1e-8
    raise ValueError("'address' is not valid or have not been found")


def get_total_balance() -> float:
    # Return balance of all addresses in address.txt
    balance = 0
    for address in load_addresses():
        balance += get_address_balance(address)
    return balance


if __name__ == '__main__':
    get_total_balance()