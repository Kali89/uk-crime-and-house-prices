#!/usr/bin/python

import csv
import datetime

header_index_dictionary = {}
houseprice_dictionary = {}
filtered_houseprice_dictionary = {}
with open("/home/matt/Coding/Python/HouseandCrime/UKHousePriceData.csv", "rb") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header_list = [header.lower() for header in csv_reader.next() if header]
    for i in range(len(header_list)):
        header_index_dictionary[int(i)] = header_list[i]
    for line in csv_reader:
        if line[0]:
            houseprice_dictionary[line[0]] = [{header_index_dictionary[j/2 + 1] : line[i]} for j,i in enumerate(range(len(line))) if i % 2 == 1]

for item in houseprice_dictionary.keys():
    split_date = item.split(' ')
    if split_date[0] in ['Q3', 'Q4'] and int(split_date[1]) < 2013:
        new_date = "30-06-" + str(int(split_date[1]) + 1)
        print new_date
