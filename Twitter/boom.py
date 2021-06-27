# import requests
# import json
# import config
# import preprocessor as p
# from langdetect import detect
# from ernie import SentenceClassifier
# import numpy as np
import csv
# import re

# sentimentList = []
# classifier = SentenceClassifier(model_path='./output')
#
# classes = ["bad", "ok", "good"]
# tweet = "buy bitcoin "
# tweet = p.clean(tweet)
# print("tweet" + tweet)

# probabilities = classifier.predict_one(tweet)
# polarity = classes[np.argmax(probabilities)]
# print(polarity)
# sentimentList.append(polarity)


with open('Book1.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)

    # Skip value
    next(reader)
    with open('new_dataSet.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile)

        for row in reader:
            # row = row[9]
            # row = p.clean(str(row))
            print(row)
            # print(polarity)

            # rowy = [row, polarity]
            # print(rowy)
            csv_writer.writerow(row)