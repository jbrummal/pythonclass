#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

# --Imports
import csv

# --Variables

# --Functions
def main():
    """Run time code"""
    with open('./csvheader.csv','r') as CSVFILE: # This will auto close the file when the indentation is removed
        CSVDATA=csv.DictReader(CSVFILE, delimiter=",") # This uses DictReader to imply that there is a header

        for key in CSVDATA:
            print("User is %s in %s" % (key.get('Address'), key.get('HSS')))
    return

# --Main
main()