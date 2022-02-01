import requests
import json

import yfinance as yf


def get_address_balance(address: int) -> int:
    # Return address balance in euros.
    r       = requests.get(f"https://blockchain.info/rawaddr/{address}")
    data    = json.loads(r.text)

    btc_value = yf.Ticker('BTC-EUR').history(period='1d')['Close'][0]

    if "final_balance" in data.keys():
        return data["final_balance"]*btc_value*1e-8
    raise ValueError("'address' is not valid or have not been found")
