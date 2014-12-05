##save_prices.py

import sqlite3, datetime
from markit import Markit

def save_prices(api):
	db = "/home/greg/Desktop/market-data/stocks.db"
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT * FROM stocks")
	stocks = c.fetchall()
	for returned in stocks:
		stock_id = returned[0]
		symbol = returned[1]
		quote = api.get_quote(symbol)
		price = quote['LastPrice']
		c.execute("INSERT INTO prices(stock_id, price, time) VALUES (?,?,?)", (stock_id, price, datetime.datetime.now()))
	conn.commit()
	conn.close()
	return True

save_prices(Markit())
