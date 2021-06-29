import csv

with open("Evaluation.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    print(header)

