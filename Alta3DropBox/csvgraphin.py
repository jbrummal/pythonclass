#!/usr/bin/python3
"""learning how to manipulate csv data"""
# download from https://tinyurl.com/y3mpflqy

import csv

import matplotlib.pyplot as plt

def main():
    """runtime code"""
    xaxislist = []
    yaxislist = []

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
                yaxislist.append(totalrow)
                xaxislist.append(row[0])
                totalrow = 0
    print(xaxislist)
    print(yaxislist)

    plt.plot(yaxislist)
    plt.show()

main()