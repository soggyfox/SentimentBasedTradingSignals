import csv

with open('new_dataSet_withSentiment.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)

    # Skip value
    next(reader)
    with open('new_dataSet_withSentiment_withNewDateFormat.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile)

        for row in reader:
            # print(row)
            rowSentiment= row[1]
            rowTime = row[2].split('/')
            day = (rowTime[0])
            month = rowTime[1]
            yearAndShit = rowTime[2]

            yearAndShit = yearAndShit.split(" ", 1)
            year = yearAndShit[0]
            # '2013-09-01':
            correctDate = year+'-'+month+'-'+day
            print(correctDate)
            rowy = [rowSentiment, correctDate]
            # print(rowy)
            csv_writer.writerow(rowy)
