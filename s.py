import csv


with open('test.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    for line in csv_reader:
        print(line)