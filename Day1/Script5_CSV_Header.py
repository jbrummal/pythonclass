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
    with open('./csv.csv','r') as CSVFILE: # This will auto close the file when the indentation is removed
        CSVDATA=csv.DictReader(CSVFILE, delimiter=",")

        for key in CSVDATA:
            print(key["Address"])

        with open('./users.txt','w') as outfile:
            for row in CSVDATA:
#                print("User is %s in %s" % (row[0], row[1]), file=outfile)
                outfile.write("User is %s in %s\n" % (row[0], row[1]))
    return

# --Main
main()