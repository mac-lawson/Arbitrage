import requests
import time
import sys
from colorama import Fore, Back, Style
from attack import getPrice, comparePrice

def coolPrint(skk): 
	print("\033[94m {}\033[00m" .format(skk))



def warnPrint(skk): 
	print("\033[91m {}\033[00m" .format(skk))





acaii = '''

     ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\

ARBCrypto: by Mac Lawson
https://github.com/mac-lawson


'''



#############



def run():
	if len(sys.argv) == 1:
		warnPrint("NO COMMANDS PROVIDED")
		warnPrint("Help: python3 attack.py -h")

		sys.exit()
	if (sys.argv[1]) == "-g":
		attack.getPrice(sys.argv[2], sys.argv[3], sys.argv[4])
	if (sys.argv[1]) == "-c":
		attack.getPrice(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])		
	if (sys.argv[1] == "-h"):
		warnPrint("HELP")
		warnPrint("_________________")
		warnPrint("-g Get Price (-g exName url coinName coolDownTime)")
		warnPrint("-c Compare Price (-c exName1 exName2 url1 url2 coinName priceMargin)")

		sys.exit()



	


#############


# print(sys.argv)
# print(len(sys.argv))
coolPrint(acaii)
while True:
	run()


