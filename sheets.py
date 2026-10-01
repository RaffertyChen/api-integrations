#c4
import os
import smtplib
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

import gspread
import requests
from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")
API_KEY = os.getenv("COINGECKO_API_KEY")
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_RECIPIENT = os.getenv("GMAIL_RECIPIENT")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

if os.getenv("GOOGLE_SHEETS_KEY"):
    with open(folder / "robot_key.json", "w") as f:
        f.write(os.getenv("GOOGLE_SHEETS_KEY"))

def send_alert(problem):
    try:
        msg = EmailMessage()
        msg["From"] = GMAIL_USER
        msg["To"] = GMAIL_RECIPIENT
        msg["Subject"] = "Price logger error"
        msg.set_content(f"Error: {problem}")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as smtp:
            smtp.login(GMAIL_USER, GMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Sent alert email")
    except (smtplib.SMTPException, OSError, ValueError) as e:
        print("Could not send alert email", type(e).__name__, str(e))

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
headers = {"x-cg-demo-api-key": API_KEY}

try:
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()
    price = data["bitcoin"]["usd"]
except (requests.RequestException, KeyError, TypeError, ValueError) as e:
    problem = f"Could not get price from CoinGecko: {type(e).__name__} {str(e)}"
    print(problem)
    send_alert(problem)
    sys.exit(1)

try:
    price = float(price)
    gc = gspread.service_account(filename=folder / "robot_key.json")
    sheet = gc.open("Automation practicex")
    ws = sheet.sheet1
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    ws.append_row([now, price])
    print("Added:", now, price)

except (OSError, gspread.exceptions.GSpreadException, ValueError) as e:
    problem = f"Could not write to Google Sheet: {type(e).__name__} {str(e)}"
    print(problem)
    send_alert(problem)
    sys.exit(1)

