import requests
import json


API_KEY = "xxx"
SECRET_KEY = "xxxxx"
ENDPOINT_URL = "https://paper-api.alpaca.markets"

ORDERS_URL = "{}/v2/orders".format(ENDPOINT_URL)
ACCOUNT_URL = "{}/v2/account".format(ENDPOINT_URL)
POSITION_URL = "{}/v2/positions".format(ENDPOINT_URL)
HEADERS={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)


def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r= requests.post(ORDERS_URL, json=data,headers=HEADERS)
    return json.loads(r.content)

def get_order():
    r = requests.get(ORDERS_URL, headers = HEADERS)
    return json.loads(r.content)

def get_position():
    r = requests.get(POSITION_URL, headers = HEADERS)
    return json.loads(r.content)

print(get_position())
#print(get_order())
#response = create_order("MSFT",1000,"buy","market","gtc")
#print(response)