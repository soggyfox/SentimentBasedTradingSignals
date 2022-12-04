# Get the current price of Bitcoin in USD using the coindesk.com API with Python and the Requests HTTP library

import requests
# http://docs.python-requests.org/en/master/

# btc = requests.get('https://api.coindesk.com'
#                    '/v1/bpi/currentprice.json')
btc = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2018-09-01')

date = "2013-09-01"
day = '01'
month = "09"
year = "2013"
correctDate = year+'-'+month+'-'+day
stable = ((btc.json()['bpi'][correctDate]))
print((correctDate))

