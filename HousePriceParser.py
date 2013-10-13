#!/usr/bin/python

import csv
import datetime
import locale

header_index_dictionary = {}
houseprice_dictionary = {}
with open("/home/matt/Coding/Python/HouseandCrime/UKHousePriceData.csv", "rb") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header_list = [header.lower() for header in csv_reader.next() if header]
    for i in range(len(header_list)):
        header_index_dictionary[header_list[i]] = int(i)
    print header_index_dictionary
