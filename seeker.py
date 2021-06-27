import csv
import codecs
count = 0
with open('Bitcoin_tweets.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)

    # Skip value
    next(reader)
    with open('new_dataSet.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile)

        for row in reader:
            # print(row)
            count += 1
            if count == 50:
                csv_writer.writerow(row)
                count = 0