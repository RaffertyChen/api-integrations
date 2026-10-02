# c5
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")
API_KEY = os.getenv("MASSIVE_API_KEY")

url = "https://api.massive.com/v3/reference/tickers/AAPL"
params = {"apiKey": API_KEY}
response = requests.get(url, params=params)
data = response.json()

name = data["results"]["name"]
print("Company:", name)

website = data["results"]["homepage_url"]
print("Website:", website)