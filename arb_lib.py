import requests
import time
import sys
from colorama import Fore, Back, Style

def coolPrint(skk): 
	print("\033[94m {}\033[00m" .format(skk))



def warnPrint(skk): 
	print("\033[91m {}\033[00m" .format(skk))
	
def getPrice(exName, url, coinName, coolDownTime):	
	coolPrint("price of " + coinName + " from " + exName)
	coolPrint((requests.get(url).text))
	time.sleep(coolDownTime)


def comparePrice(exName1, exName2, url1, url2, coinName, coolDownTime):
	coolPrint("comparing " + coinName + " between " + exName1 + " and " + exName2)

	price1 = float(requests.get(url1).text)
	price2 = float(requests.get(url2).text)
	price1 =- price2
	diffPrice = (abs(price1))

	
	print((Fore.BLUE) + "differance in price: " + str(diffPrice) + (Style.RESET_ALL))
	time.sleep(2)
	if diffPrice < 10:
		print((Fore.RED) + "[alert] differance to low, attack not reccomended" + (Style.RESET_ALL)) 
	if diffPrice > 10:
		print((Fore.GREEN) + "[alert] attack reccomended" + (Style.RESET_ALL))


	time.sleep(coolDownTime)
