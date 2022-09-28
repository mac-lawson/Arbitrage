from logging import warning
import requests
import time
import sys
from colorama import Fore, Style
def errWarning(type):
	if(type == "noCmds"):
		warnPrint("No commands were provided, or if they were, the syntax was incorrect")
		warnPrint("Help: python3 run.py -h")
	if(type == "help"):
		warnPrint("HELP")
		warnPrint("_________________")
		warnPrint("-g Get Price (-g URL)")
		warnPrint("-c Compare Price (-c URL1, URL2, Price Margin)")	
def coolPrint(skk): 
	print("\033[94m {}\033[00m" .format(skk))



def warnPrint(skk): 
	print("\033[91m {}\033[00m" .format(skk))

# Get the price of a coin/token from a single exchange	
def getPrice(url):	
	coolPrint((requests.get(url).text))
	sys.exit()

# Compare the price of two exchanges

def comparePrice(url1, url2, priceMargin):

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
def run():
	if len(sys.argv) == 1:
		errWarning("noCmds")
		sys.exit()	
	if (sys.argv[1]) == "-g":
		getPrice(sys.argv[2])
	if (sys.argv[1]) == "-c":
		comparePrice(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])		
	if (sys.argv[1] == "-h"):
		errWarning("help")
		sys.exit()





