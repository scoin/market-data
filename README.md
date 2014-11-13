Byte Academy Workshop- HTTP Requests and Scraping
=======================================================

Welcome to Byte Academy! Thank you for joining us for this special workshop event.

Let's get started, shall we?

If you don't have it installed already, you'll need to download and install pip3. Pip is a package manager for Python3 libraries.

On Ubuntu:

		sudo apt-get install python3-pip

On Mac:
		
		Pip / Pip3 is automatically installed if you installed Python / Python3 with Homebrew

On Windows:

		Python3.4 ships with Pip.   
		If you don't have Python3.4, follow these instructions to install Pip for your version https://pip.pypa.io/en/latest/installing.html

Use pip3 to install requests and beautifulsoup4.

		sudo pip3 install requests  
		sudo pip3 install beautifulsoup4

If you only have Python 2, that's fine. Just remove the 3 use regular pip.

###Requests

We'll be dependent on these two libraries for consuming JSON APIs and web scraping.Requests is definitely the best [HTTP request library](http://docs.python-requests.org/en/latest/) in Python. Take a look at the code snippet and get an idea of what it's doing. We'll be using requests to get live stock market data.

The API we'll be using is [Markit on Demand](http://dev.markitondemand.com/)

How do HTTP requests work? Well, everytime you browse the web you are making http requests. You are asking for data from a URL. Your browser usually expects data in the form of HTML.

Instead of requesting HTML though, we're going to request [JSON](http://en.wikipedia.org/wiki/JSON), which Python will treat like a native object courtesy of the requests library. 

###Step 0: Know your Outputs and Inputs

Take a look at these links so you know what to expect from the API. Read through the docs for Markit on Demand.

http://dev.markitondemand.com/Api/v2/Lookup/json?input=Netflix

http://dev.markitondemand.com/Api/v2/Quote/json?symbol=AAPL

###Step 1: Wrap the API calls in an object  
We're going to wrap the calls to Markit on Demand in a class. This way it is portable and modular. Anybody can use our class and not be concerned with what is going on behind the scenes. If the API changes, this is the only place the code will break.

We're going to write the methods `get_symbols` and `get_quote`. `get_symbols` takes a company's name in English and returns some basic data, like the formal name, the exchange it is on, and most importantly it's ticker symbol. The API will likely return more than one. `get_quote` takes a ticker symbol and receives up to the minute quote data.

###Step 2:  
Run your code and that your functions are working. Alright! Now make a file in the same directory that will be our app - call it app.py.

Inside app.py:

		from markit import Markit

Make sure that your code is linked and working. Instantiate a new Markit object and print the results of get_symbols and get_quote.

Scraping the Web
=================

Have you ever wanted to use the information from a website? Alot of our favorite sites have public apis - but alot don't. The information is still out there though - we've just got to scrape for it.

[Coin Market Cap](http://www.coinmarketcap.com) is the gold standard for crypto-currency values. Unfortunately, they don't have an official API.

Several people have built APIs for them using web scrapers - and they were showered in bitcoin, dogecoin, and pizza. Time to get in on the action!

###Scrape Coin Market Cap

Web scraping is not an exact science. We are parsing through HTML for data that we want.

Beautiful Soup tries to make it easy as possible, by giving us objects based on html tags and css selectors.

Our goal for our code is to return the name of currency and it's current value as key-value pairs for all 100 coins on the market. This way, we can do the following:

		current_prices = CoinMarket().get_coins()
		current_prices['Bitcoin'] ## 422.09

Resources
==========
[Requests](http://docs.python-requests.org/en/latest/)
[Beautiful Soup Tutorial](http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python)
