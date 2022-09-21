# Arbitrage
Tools to test for possible crypto arbitrage trades
## How to use:
Youtube video coming soon!


## Developers

- [Lead: Mac Lawson](https://www.github.com/mac-lawson)



## Guide

#### Gaining API urls as vectors
Common tools such as Burp or OSWAP ZAP can be used to scan the differant web servers you want to use this tool
to test.

For example, the Coinbase buy api can be used in the form of a curl request:

`curl https://api.coinbase.com/v2/prices/BTC-USD/buy \
  -H 'Authorization: Bearer abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c'`

With the new url, find the place in the script where you scan place
functions.

`def run():`





