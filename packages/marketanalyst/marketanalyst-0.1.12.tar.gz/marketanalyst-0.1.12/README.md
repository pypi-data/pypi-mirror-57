This is how you can use this wrapper.

import marketanalyst

api_key = "your api key"
secret_key = "your secret key"

client = marketanalyst.client(api_key,secret_key,base_url="https://www.agrud.org/")

# or 

client = marketanalyst.client(api_key,secret_key)
# In this case base url will be = "https://www.marketanalyst.ai"

df1 = client.download_data("NASDAQ:AAPL","01/01/2012","01/01/2019","Price","EOD")

print(df1)

Websocket:

def receive_data(data):
    print(data)

client101.onDataEvent("nasdaq-aapl",receive_data)

receive_data will get the data