#!/usr/bin/python3
"""learning how to manipulate csv data"""
# download from https://tinyurl.com/y3mpflqy

import csv

def main():
    """runtime code"""
    totalrow = 0  # this is the total value of a single line (row)
    totaldict = {"date": " ", "total": 0} # this tracks the current highest line (row)

    ## get the file open file
    with open("2019-01-PGWU.csv", "r") as csvfile:
        ## read the file
        csvdata = csv.reader(csvfile) ## returns the data is a list format []
        ## loop across our data
        for row in csvdata:
        ## ignore first row
            if "Time" not in row[0]:  # we want to ignore headers
                for entry in range(1, len(row)):  # skip first column (time)
                    if row[entry] is "":   # if nothing in cell
                        row[entry] = 0     # assign a value (to prev. errors)
                    totalrow = float(row[entry]) + totalrow  # add up all row values
                if totaldict["total"] < totalrow: # comparison of current row to alltimerecordholder
                    totaldict["total"] = totalrow  # if new row is larger, rewrite totaldict
                    totaldict["date"] = row[0]   # if new row is lager, rewrite totaldict
                totalrow = 0
        print(totaldict)

        ## in a row... ignore row[0] add all other values in row place that total in a dict with date

        ## move to next line... IF next line is larger than previous line, rewrite dict with that total and date

        ## move to the next

    ## return the result
    ## write out to file where the file is YY-MO-DAY-johnresults.txt

main()