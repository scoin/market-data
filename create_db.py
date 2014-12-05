import sqlite3

def create_db():
	conn = sqlite3.connect('stocks.db')
	c = conn.cursor() ##create a cursor object
	c.execute("CREATE TABLE stocks(id integer primary key, symbol text UNIQUE)")
	c.execute("CREATE TABLE prices(id integer primary key, time text, price real, stock_id integer)")
	conn.commit()
	conn.close()
	return True

create_db()