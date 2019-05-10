#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

# --Imports

# --Functions
def main():
    """Run time function"""
    COUNTER=0
    with open('./keystone.common.wsgi', 'r') as LOGFILE:
        for line in LOGFILE:
            if "- - - - -] Authorization" in line:
                COUNTER+= 1
                print(line)
    print(COUNTER)
# --Run
main()
