from itertools import count
import os
import csv

csvpath = os.path.join("Resources1", "election_data.csv")

count = 0

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    counter_Khan = 0

    for row in csv_reader:
        # print(row[0], row[1], row[2])
        if row[2] == str("Khan"):
            counter_Khan = counter_Khan + 1


        count = count + 1
    print(count)
    print(counter_Khan)
