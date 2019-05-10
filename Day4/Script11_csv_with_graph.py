#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

# --Imports
import csv
import matplotlib.pyplot as plt

# --Constants
SRC_FILE='./source.csv'
DATECOL=0
COL_SUM=0
START_COL = 1

# --Functions
def sumcol(row):
    """Sum the current row by column
    - iterate all columns across the row
    - return the sum"""

    col_sum=0
    for col in range(START_COL, len(row)):
        # --Handle dirty data
        if not row[col]: row[col] = 0
        # --Sum the col
        col_sum += float(row[col])
    return(col_sum)

def graphit(xaxis, yaxis):
    plt.plot(yaxis)
    plt.show()
    return

def main():
    """Run time code that controls the source function
    Open the file with csv.reader and store in variable;
    - Iterate across every row of the csv file and sum rows
    - Compare the sum against the largest
    - If larger than largest, replace value and store date"""

    # --Setup variables
    max_total=0.0
    max_date=""
    xaxis =[]
    yaxis =[]

    with open(SRC_FILE, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if "Time" not in row[0]:
                currentmax = sumcol(row)

                # --Create the graphing information
                xaxis.append(row[0])
                yaxis.append(currentmax)

                # --Find out if there is a new max
                if currentmax > max_total:
                    max_total = currentmax
                    max_date = row[DATECOL]
    print("The max occurred on %s with a value of %s" % (max_date, round(max_total)))
    graphit(xaxis,yaxis)
    return()

# --Execute the script
main()