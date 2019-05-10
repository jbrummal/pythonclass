#!/usr/bin/python3

"""
Author: Jason Brummal
Create date: 05/06/2019
Purpose:
    Day 1: initial script
"""

# --Imports

# --Variables

# --Functions
def main():
    """This is our runtime code"""
    NETWORKLISTS = [['ios', '10.0.0.1'], ['ios', '10.0.0.2'],
                    ['ios-xr','192.168.3.1'], ['junos', '172.0.0.4'],
                    ['merkai','10.0.0.3']]
    print(NETWORKLISTS[0][1]) # print 10.0.0.1

    for DRIVERSANDIP in NETWORKLISTS:
        print("SSH to %s using %s" % (DRIVERSANDIP[1],DRIVERSANDIP[0])) # interate and print all elements in list

    input("Press enter to close again")

    return

# --Execute the runtime code
main()
