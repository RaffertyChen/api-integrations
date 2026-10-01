# c4b

import json
from pathlib import Path

import anthropic
import pandas as pd
from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")
client = anthropic.Anthropic()

emails = (folder / "order_emails.txt").read_text(encoding="utf-8")

instructions = """Below are customer emails. Some are orders and some are not.

Make one row for each product that someone orders, with these fields:
- company: the customer's company name
- product: one of these exact names: Steel bracket, Hex bolt pack (100), Door hinge, Rubber gasket, Ball bearing 608, Aluminium sheet 1m, Hydraulic hose 2m, Control panel enclosure
- quantity: a whole number
- needed_by: the date they need it by, as YYYY-MM-DD, or null if they don't give one

Rules:
- If someone changes their mind, use their final number.
- Work out dates like "next Friday" from the date the email was sent.
- Skip emails that aren't orders.

Reply with only a JSON list of rows, and nothing else.

Emails:
"""
print("Asking Claude... this can take up to a minute.")

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2000,
    messages=[{"role": "user", "content": instructions + emails}],
)

text = message.content[0].text
text = text.replace("```json","").replace("```","").strip()
rows = json.loads(text)
print("Rows", len(rows))

orders = pd.DataFrame(rows)
orders.to_excel(folder / "clean_orders.xlsx" , index=False)
print("Saved Clean_orders.xlsx")


