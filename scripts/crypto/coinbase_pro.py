import os

from cbpro import AuthenticatedClient


FIAT = ['EUR', 'USD'] # list of fiat currencies

def load_cbpro_client():
    return AuthenticatedClient(os.environ['cbpro_api_key'], os.environ['cbpro_api_secret'], os.environ['cbpro_passphrase'])


def return_cbpro_balance():
    client = load_cbpro_client()

    balance = 0
    for wallet in client.get_accounts():
        if float(wallet['balance']) == 0 or wallet['currency'] in FIAT:
            continue
        
        change_price = float(client.get_product_24hr_stats(wallet['currency'] + '-EUR')['last'])
        balance += float(wallet['balance']) * change_price
        
        return balance