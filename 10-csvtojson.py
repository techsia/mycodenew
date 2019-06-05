#!usr/bin/python3

import csv
import json

def main():
    #open a file to dump json to
    jsonf = open('csvfile.json', 'w') #open a file for writing to

    #open our csv file to read in csv to python format
    with open('csvfile.csv') as csvf:
        reader = csv.DictReader(csvf)
        #for row in reader:
        json.dump(list(reader), jsonf)

    jsonf.close() #close the csvfile.json file we opened

if __name__ == "__main__":
    main()
