import requests
import json


def get_address_balance(address: int) -> int:
    # Return address balance in satoshi
    r       = requests.get(f"https://blockchain.info/rawaddr/{address}")
    data    = json.loads(r.text)

    if "final_balance" in data.keys():
        return data["final_balance"]
    raise ValueError("'address' is not valid or have not been found")


if __name__ == "__main__":
    address = "1H2ZrzYnXmf2Q1RRua4bADSWPSHXZPNtBX"
    print(get_address_balance(address))