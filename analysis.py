#fabio bonini
#analysis iris.csv
import csv

#reading iris.csv
with open ('iris.csv', 'r') as table:
    read = csv.reader(table)
    for x in read:
        print(x)