import requests
from bs4 import BeautifulSoup

url = "https://www.alternate.de/html/product/listingAboveFourtyPercent.html?lk=17979&size=500&sort=PRICEADVANTAGE&order=DESC&outlet=0&outlet=1#listingResult"

def searchTerm():
	return input("What do you want to search? ")

def processSearch(search):
	pass

def getLinks(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	listings = soup.find("div", {"id" : "listingResult"})

def filterNames(listings):
	pass

def processNames(names):
	pass



if __name__ == "__main__":
