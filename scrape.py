import requests ##python requests http://docs.python-requests.org/en/latest/
import bs4 ##beautiful soup 4 http://www.crummy.com/software/BeautifulSoup/bs4/doc/

###GO TO http://www.coinmarketcap.com and open up Dev Tools.

class CoinMarket:
	def __init__(self):
		self.site = requests.get("http://www.coinmarketcap.com") ##download html from site
		self.soup = bs4.BeautifulSoup(self.site.text) ##parse html

	def get_coins(self):
		headers = False
		currencies = {}
		for element in self.soup.select('#currencies tr'): ##select all table rows in the currencies div and iterate through
			if(headers == False): 
				headers = True
				continue ##skip headers row
			coin = element.find_all('a') ##get an array of a tags
			currencies[coin[0].text] = float(coin[1]['data-usd']) #key = Coin Name (ie: Bitcoin) value = Price
		return currencies

coins = CoinMarket()
currencies = coins.get_coins()
print(currencies)
