#!/usr/bin/python3
"""using csv data"""

import csv

def main():
    # subscriberdat = open('mockcsv.csv', 'r')
    with open(r'C:\Users\Achimedes\Dropbox\2019-05-06 vzw pyans\mockcsv.csv', 'r') as subscriberdat:
        subscriberlist = csv.reader(subscriberdat, delimiter=",")
        print(subscriberlist)
    
        with open(r'C:\Users\Achimedes\Dropbox\2019-05-06 vzw pyans\users.txt', 'w') as usershss:            
            for row in subscriberlist:
                #print(row[0], row[3], file=usershss)
                usershss.write(row[0] + row[3] + "\n")

                
    input()
    
main()