#c2 
import os
import requests
from pathlib import Path

from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")
API_KEY = os.getenv("COINGECKO_API_KEY")

print("Key found:", API_KEY is not None)

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
headers = {"x-cg-demo-api-key": API_KEY}

response = requests.get(url, headers=headers)
print(response.status_code)

data = response.json()
print(data)

price = data["bitcoin"]["usd"]
print("bitcoin price in USD", price)
