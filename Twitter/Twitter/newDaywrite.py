import csv

import requests

# http://docs.python-requests.org/en/master/

# btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btc = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2019-09-01&end=2021-06-01')

with open('new_dataSet_withSentiment_withNewDateFormat_withBTCPrice.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    # Skip value
    next(reader)
    with open('new_day_write.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile)
        count = 0
        lastRowDate = '30-21-2014'
        for row in reader:
            # print(row)
            rowSentiment = row[0]
            rowDate = row[1]
            rowPrice = row[2]
            print(lastRowDate + ' :last')
            print(rowDate)
            if lastRowDate != rowDate:
                count += 1

            rowy = [rowSentiment,rowPrice, count, rowDate]
            # print(rowy)
            csv_writer.writerow(rowy)
