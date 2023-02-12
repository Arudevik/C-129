

import csv

dataset_1 = []
dataset_2 = []

with open("Pro-129/convertedData.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("Pro-129/bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2

planet_data = []


for i in planet_data_1:
    planet_data.append(i)

for j in planet_data_2:
    planet_data.append(j)

with open("Pro-129/final.csv", "a+") as f:
    data = csv.writer(f)
    data.writerow(headers)
    data.writerows(planet_data)






