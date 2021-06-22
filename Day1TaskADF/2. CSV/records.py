import csv
f=open('files.csv','r')
reader=csv.reader(f)

people={}

for row in reader:
    people[row[0]]={row[1],row[2]}

print(people)