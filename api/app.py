import requests
import json
#fuction for getting the live data 

def get_stock_data():
    url= f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    #checking if the response is sucessful
    if response.status_code ==200:
        data=response.json()
        last_refreshed =data["meta data"]["3. last response"]
        price= data['time seris  (5 mines)'][last_refreshed]["1.open"]
        return price
    
    else:
        return None
    
stock_prices ={}
price =get_stock_data()
symbol ="IBM"

if price is not none:
    stock_prices[symbol] =price
print(f"{symbol} :{price}")
