import requests
import time
import sys

# Get the price of a coin/token from a single exchange
	
def getPrice(exName, url, coinName):	
	coolPrint("price of " + coinName + " from " + exName)
	coolPrint((requests.get(url).text))
	sys.exit()

# Compare the price of two exchanges

def comparePrice(exName1, exName2, url1, url2, coinName, priceMargin):
	coolPrint("comparing " + coinName + " between " + exName1 + " and " + exName2)

	price1 = float(requests.get(url1).text)
	price2 = float(requests.get(url2).text)
	price1 =- price2
	diffPrice = (abs(price1))

	
	print((Fore.BLUE) + "differance in price: " + str(diffPrice) + (Style.RESET_ALL))
	time.sleep(2)
	if diffPrice < (priceMargin):
		print((Fore.RED) + "[alert] differance to low, attack not reccomended" + (Style.RESET_ALL)) 
	if diffPrice > (priceMargin):
		print((Fore.GREEN) + "[alert] attack reccomended" + (Style.RESET_ALL))


	sys.exit()