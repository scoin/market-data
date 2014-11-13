Markit API Wrapper
===============

Today is your first challenge using an API. Cool!

First install 'requests' using pip. We'll be dependent on this library, as it is definitely the best [HTTP request library](http://docs.python-requests.org/en/latest/) in Python. Take a look at the code snippet and get an idea of what it's doing. We'll be using requests to get live stock market data.

The API we'll be using is [Markit on Demand](http://dev.markitondemand.com/)

How do HTTP requests work? Well, everytime you browse the web you are making http requests. You are asking for data from a URL. Your browser usually expects data in the form of HTML.

We could request HTML in our code also, but it's kind of a mess. Instead we're going to request [JSON](http://en.wikipedia.org/wiki/JSON), which Python will treat like a native object courtesy of the requests library. 

Take a look at these links so you know what to expect from the API. Read through the docs for Markit on Demand.

http://dev.markitondemand.com/Api/v2/Lookup/json?input=Netflix

http://dev.markitondemand.com/Api/v2/Quote/json?symbol=AAPL

###Step 1: Wrap the API calls in an object  
Wrap the calls to Markit on Demand in a class. I've already started it for you. Write the methods get_company_data and get_quote. get_company_data takes a company's name in English and returns some basic data, like the formal name, the exchange it is on, and most importantly it's ticker symbol. The API will likely return more than one. get_quote takes a ticker symbol and receives up to the minute quote data.

###Step 2:  
Test that your functions are working in the python interpreter. What happens if you send an incorrect string and it can't find the company, does it throw an error? Fix this - we don't want your program crashing on users.

Scraping the Web
=================

Have you ever wanted to use the information from a website? Alot of our favorite sites have public apis - but alot don't. The information is still out there though - we've just got to scrape for it.

[Coin Market Cap](http://www.coinmarketcap.com) is the gold standard for crypto-currency values. Unfortunately, they don't have an official API.

Several people have built APIs for them using web scrapers - and they were showered in bitcoin, dogecoin, and pizza. Time to get in on the action!

Use pip3 to install requests and beautifulsoup4.

		sudo pip3 install requests  
		sudo pip3 install beautifulsoup4

###Scrape Coin Market Cap

Use [this tutorial](http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python) as a guide to scraping using requests and bs4. This is for a different site and case, but you should skim and read enough of the code snippets to get the idea.

Your code should return the name of currency and it's current value as key-value pairs for all 100 coins on the market. 

You will need to remove the dollar-sign from the price string. We need it as a float so we can manipulate that data later.

The complete list should be ordered as they are ordered on the market.

###Save it to a CSV

Now export your list to a CSV file and save it in the directory. Push it up!
