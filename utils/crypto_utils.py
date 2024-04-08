import requests
import pandas as pd
from datetime import datetime, timedelta

# Constants for API key and headers
API_KEY = 'CG-DnoEtgZyQAMKkQJ5KPCMyi6X'
HEADERS = {"x-cg-demo-api-key": API_KEY}

def fetch_all_coins_list():
    url = 'https://api.coingecko.com/api/v3/coins/list'
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else []

def fetch_historical_data(coin_id, days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    params = {
        'vs_currency': 'usd',
        'from': int(start_date.timestamp()),
        'to': int(end_date.timestamp())
    }

    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range", params=params, headers=HEADERS)
    if response.status_code == 200 and response.json().get('prices'):
        return response.json()['prices']
    return None


def unix_to_datetime(unix_timestamp):
    return datetime.utcfromtimestamp(unix_timestamp / 1000.0)
