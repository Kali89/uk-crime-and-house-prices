#!/usr/bin/python

import csv
import datetime
import locale

crime_dictionary = {}
with open("/home/matt/Coding/Python/HouseandCrime/UKCrimeData.csv", "rb") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter="\t")
    # Skip the headers
    csv_reader.next()
    for row in csv_reader:
        ### Row[0] date
        ### Row[1] county
        ### Row[2] wider region
        ### Row[3] offence
        ### Row[4] number of incidences
        row[0] = datetime.datetime.strptime(row[0], "%d-%b-%y")
        if row[2] not in crime_dictionary:
            crime_dictionary[row[2]] = {row[0] : {row[3] : int(row[4])}}
        else:
            if row[0] not in crime_dictionary[row[2]]:
                crime_dictionary[row[2]][row[0]] = {row[3] : int(row[4])}
            else:
                if row[3] not in crime_dictionary[row[2]][row[0]]:
                    crime_dictionary[row[2]][row[0]][row[3]] = int(row[4])
                else:
                    crime_dictionary[row[2]][row[0]][row[3]] += int(row[4])



