import requests ##python requests http://docs.python-requests.org/en/latest/

##api wrapper
class Markit:
	def __init__(self):
		##api endpoint urls
		self.symbol_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def get_symbol(self, company_name):
		url = self.symbol_url + company_name ##join the url with the symbol input
		symbol_object = requests.get(url).json() ##parse json returned from the web
		return(symbol_object)

	def get_quote(self, symbol):
		url = self.quote_url + symbol ##join the url with the quote input
		symbol_object = requests.get(url).json() ##parse json returned from the web
		return(symbol_object)

# api = Markit() ##instantiate api wrapper

# print(api.get_symbol("Microsoft"))
# print(api.get_quote("MSFT"))
