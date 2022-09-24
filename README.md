# Arbitrage
Tools to test for possible crypto arbitrage trades
## How to use:
Youtube video coming soon!


## Developers

- [Lead: Mac Lawson](https://www.github.com/mac-lawson)



## Guide

#### Gaining API urls as vectors
Common tools such as Burp or OSWAP ZAP can be used to scan the different web servers you want to use this tool
to test.

For example, the Coinbase buy api can be used in the form of a curl request:

`https://api.coinbase.com/v2/prices/BTC-USD/buy`

Now you can run Arbitrage with the url:

##### Get price:
`python3 attack.py -g url`

##### Compare price price:
`python3 attack.py -c exName1 exName2 url1 url2 coinName priceMargin`





