import csv

with open("letter_frequency.csv","r") as fle:
    lst = csv.reader(fle)
    for i in lst:
        print(i)