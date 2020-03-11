#!/usr/bin/python3

import requests

stock = 'YOUR_STOCK_HERE'
rsus = 1

r = requests.get(f"https://finnhub.io/api/v1/quote?symbol={stock}")
# finnhub allows 30 requests per minute without an API key
p = r.json()

current = p['c']
total_value = rsus * current

print(f"Current price of {stock} is ${current:,.2f}")
print(f"Your {rsus} RSUs are worth a total of ${total_value:,.2f}")
