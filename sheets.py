#c4
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import gspread
import requests
from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")
API_KEY = os.getenv("COINGECKO_API_KEY")

if os.getenv("GOOGLE_SHEETS_KEY"):
    with open(folder / "robot_key.json", "w") as f:
        f.write(os.getenv("GOOGLE_SHEETS_KEY"))

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
headers = {"x-cg-demo-api-key": API_KEY}

try:
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    price = data["bitcoin"]["usd"]
except (requests.RequestException, KeyError, TypeError, ValueError) as e:
    print("Could not get the price", type(e).__name__, str(e))
    sys.exit(1)

try:
    price = float(price)
    gc = gspread.service_account(filename=folder / "robot_key.json")
    sheet = gc.open("Automation practice")
    ws = sheet.sheet1
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    ws.append_row([now, price])
    print("Added:", now, price)

except (OSError, gspread.exceptions.GSpreadException, ValueError) as e:
    print("Could not write to Google Sheets", type(e).__name__, str(e))
    sys.exit(1)

