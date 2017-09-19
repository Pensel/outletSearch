import requests
from bs4 import BeautifulSoup

url = "https://www.alternate.de/html/product/listingAboveFourtyPercent.html?lk=17979&size=500&sort=PRICEADVANTAGE&order=DESC&outlet=0&outlet=1#listingResult"


#building data

def getSoup(url):
	r = requests.get(url)
	return BeautifulSoup(r.text, "html.parser")

def getListings(soup):	
	return soup.find("div", {"id" : "listingResult"})

def getData(listings, page=0):
	data = []
	links = listings.findAll("a", {"class": "productLink"})
	i = 0
	for link in links:
		data.append((i+page*500, link["title"].upper(), link["href"])) #add prices? 
		i += 1
	return data

def completeOnePage(url, page):
	return getData(getListings((getSoup(url))),page)


def getAllPages(url):
	soup = getSoup(url)
	results = soup.find("span",{"class":"results"}).text
	number = int(results[results.find("von ")+ 4:results.find(" Produkten")])
	needed = number // 500
	data = []
	if needed > 0:
		for i in range(0,needed +1):
			data += completeOnePage("https://www.alternate.de/html/product/listingAboveFourtyPercent.html?lk=17979&page=" +str((i+1)) + "&size=500&sort=PRICEADVANTAGE&order=DESC&outlet=0&outlet=1#listingResult", i)
	return data


def processNames(names):
	pass

#searching

def getSearchTerm():
	return input("What do you want to search? ").upper()

def search(searchTerm, data):
	results = []
	for e in data:
		if (e[1].find(searchTerm) != -1):
			results.append(e)
	return results

# runtime
if __name__ == "__main__":
	data = getAllPages(url)
	print(data)
	print("-"*40)
	while True:
		searchTerm = getSearchTerm()
		results = search(searchTerm, data)
		print(results)
		print("\n")
		print("-"*40)
		print("\n")
		
