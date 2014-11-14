import requests
import bs4

class CoinMarket:
	def __init__(self):
		self.site = requests.get("http://www.coinmarketcap.com")
		self.soup = bs4.BeautifulSoup(self.site.text)

	def get_coins(self):
		headers = False
		currencies = {}
		for element in self.soup.select('#currencies tr'):
			if(headers == False):
				headers = True
				continue
			coin = element.find_all('a')
			currencies[coin[0].text] = coin[1].text
		return currencies

coins = CoinMarket()
currencies = coins.get_coins()
print(currencies)
