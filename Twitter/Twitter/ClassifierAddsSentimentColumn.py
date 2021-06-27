import preprocessor as p
from ernie import SentenceClassifier
import numpy as np
import csv

# sentimentList = []
classifier = SentenceClassifier(model_path='./output')

classes = [-1, 0, 1]
tweet = "buy bitcoin "
tweet = p.clean(tweet)
print("tweet" + tweet)

# probabilities = classifier.predict_one(tweet)
# polarity = classes[np.argmax(probabilities)]
# print(polarity)
# sentimentList.append(polarity)


with open('new_dataSet.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)

    # Skip value
    next(reader)
    with open('new_dataSet_withSentiment.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile)

        for row in reader:
            rowTime = row[3]
            rowTExt = row[4]
            rowTExt = p.clean(str(rowTExt))
            # print(row)
            probabilities = classifier.predict_one(rowTExt)
            polarity = classes[np.argmax(probabilities)]
            # print(polarity)

            rowy = [rowTExt, polarity, rowTime]
            # print(rowy)
            csv_writer.writerow(rowy)
