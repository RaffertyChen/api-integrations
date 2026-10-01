#c4
import os
from datetime import datetime
from pathlib import Path

import gspread
import requests
from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")
API_KEY = os.getenv("COINGECKO_API_KEY")

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
headers = {"x-cg-demo-api-key": API_KEY}
response = requests.get(url, headers=headers)
data = response.json()  
price = data["bitcoin"]["usd"]

gc = gspread.service_account(filename=folder / "robot_key.json")
sheet = gc.open("Automation practice")
ws = sheet.sheet1

now = datetime.now().strftime("%Y-%m-%d %H:%M")
ws.append_row([now, price])
print("Added:",now ,price)