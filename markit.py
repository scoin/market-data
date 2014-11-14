import requests

class Markit:
	def __init__(self):
		self.symbol_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def get_symbol(self, name):
		url = self.symbol_url + name
		symbol_object = requests.get(url).json()
		return(symbol_object)

	def get_quote(self, symbol):
		url = self.quote_url + symbol
		symbol_object = requests.get(url).json()
		return(symbol_object)

api = Markit()

print(api.get_symbol("Microsoft"))
print(api.get_quote("MSFT"))
