#!/usr/bin/python3

import csv

def main():
    with open(r'C:\Users\Achimedes\Dropbox\2019-05-06 vzw pyans\mockcsvheader.csv', 'r') as csvfile:
        mycsvdat = csv.DictReader(csvfile)
        for entry in mycsvdat:
            print(entry['aor'], entry['hss'])
    input()
      
main()