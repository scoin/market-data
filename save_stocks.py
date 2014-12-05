##save_stocks.py
import sqlite3

def save_stocks(*args):
	conn = sqlite3.connect('stocks.db')
	c = conn.cursor()
	for symbol in args:
		try:
			c.execute("INSERT INTO stocks(symbol) VALUES (?)", (symbol.upper(),))
			print("Successfully inserted {symbol}".format(symbol = symbol))
		except sqlite3.IntegrityError:
			print("{symbol} is already in the database!!".format(symbol = symbol))
	conn.commit()
	conn.close()
	return True

save_stocks("AAPL", "MSFT", "KO", "HAL")
