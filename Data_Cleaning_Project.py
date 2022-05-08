import csv
import pandas

reader = pandas.read_csv("Final_Project.csv")

del reader['Luminosity']
del reader['NAN values']

list = list(reader)
print(list)

header = reader[0]
data = reader[1: ]

with open('Final.csv') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)