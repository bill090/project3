import requests
import pandas as pd

def get_crypto_data(crypto_currency, market, API_KEY):
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&interval=5min&symbol=' + crypto_currency + '&market=' + market + '&apikey=' + API_KEY
    r = requests.get(url)
    dataIntraday = r.json()

    return dataIntraday['Time Series (Digital Currency Weekly)']

def convert_to_df_crypto(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.reset_index()

    df = df.rename(index=str, columns={"index": "date", "1b. open (USD)" : "open", "2b. high (USD)" : "high", "3b. low (USD)" : "low", "4b. close (USD)" : "close"})
    
    df['date'] = pd.to_datetime(df['date'])

    df = df.sort_values(by=['date'])

    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.close.astype(float)
    df.low = df.close.astype(float)

    return df