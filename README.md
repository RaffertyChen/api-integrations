# API Integrations

Scripts that connect to other websites and tools automatically, so nobody has to copy data by hand.

## What's inside

- `ai_orders.py`: reads messy customer order emails and uses AI(claude) to turn them into a clean spreadsheet, one row per product ordered
- `sheets.py`: gets the live Bitcoin price and adds it to a Google Sheet with the current time, building a price log
- `stock_info.py`: looks up a company's details, like its name and website, from a stock market data service
- `pages.py`: collects a long list that arrives one page at a time, and stops at the end
- `coin_price.py`: gets today's Bitcoin price using a private key
- `github_repos.py`: lists a GitHub (my personal) public projects
- `ai_hello.py`: a first test message to Claude
- `API_test.py`: gets Apple's stock data using a private key

## Why it matters

Most business tools, like online shops, payment systems and customer databases, share their data through APIs like these. The same approach can pull a shop's orders into a Google Sheet every day, or turn a pile of order emails into a clean spreadsheet in about a minute.

## Check the AI's work

The AI is great at reading messy emails, but it can still make mistakes, especially with dates like "next Friday". Always check the tricky rows before using the results.

## How to run it

1. Install Python from python.org.
2. In a terminal in this folder, run: `python -m pip install -r requirements.txt`
3. Copy `.env.example` to a new file called `.env`, and add your own keys from CoinGecko, Anthropic and Massive.
4. For `sheets.py`: create a Google service account, save its key as `robot_key.json` in this folder, and share a Google Sheet called "Automation practice" with the service account's email.
5. Run any script, for example: `python ai_orders.py`

## Files

- `order_emails.txt`: 20 practice order emails (made up)
- `clean_orders.xlsx`: the spreadsheet `ai_orders.py` produced from them, checked by hand