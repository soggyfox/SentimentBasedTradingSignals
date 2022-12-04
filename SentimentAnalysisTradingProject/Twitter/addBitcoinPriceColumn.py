import csv

import requests
# http://docs.python-requests.org/en/master/

# btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btc = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2019-09-01&end=2021-06-01')

with open('dataSetWithSentimentWithNewDateFormat.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)

    # Skip value
    next(reader)
    with open('dataSetWithSentimentWithNewDateFormatWithBTCPrice.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile)

        for row in reader:
            # print(row)
            rowSentiment= row[0]

            rowTime = row[1].split('/')
            day = (rowTime[0])
            month = rowTime[1]
            yearAndShit = rowTime[2]

            yearAndShit = yearAndShit.split(" ", 1)
            year = yearAndShit[0]
            # '2013-09-01':
            correctDate = year+'-'+month+'-'+day
            print(correctDate)
            # get btc price to add to column
            dateTouse = year+month+day
            print(correctDate + 'year')
            btcPrice = ((btc.json()['bpi'][correctDate]))
            print((btcPrice))

            rowy = [rowSentiment, correctDate, dateTouse, btcPrice]
            print(rowy)
            csv_writer.writerow(rowy)
