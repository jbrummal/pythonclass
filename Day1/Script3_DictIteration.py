#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

# --Imports
import json

# --Functions
def main():
    """Run time function for parsing json"""
    MYJSONFILE=open('./ciscoAPIC.json', 'r')
    MYJSONDECODEDASSTRING=MYJSONFILE.read()
    print(type(MYJSONDECODEDASSTRING)) # just shows that the read is a text...and no use to us


    # Use old school way of opening and print full json
    with open('./ciscoAPIC.json','r') as MYJSONFILE:
        MYJSONFILEASJSON=json.load(MYJSONFILE)
        print(type(MYJSONFILEASJSON))

    # Print full json
    print(MYJSONFILEASJSON)

    # Print the first dictionary value
    print(MYJSONFILEASJSON.get('imdata'))

    # Dictionary contains a list, print the first list
    print(MYJSONFILEASJSON.get('imdata')[0])

    # First list contains 2 embedded dictionaries
    print(MYJSONFILEASJSON.get('imdata')[0].get('firmwareCtrlrRunning').get('attributes').get('applId'))

    # Loop through the list in the dictionary and grabbing applId
    for app in MYJSONFILEASJSON.get('imdata'):
        print(app.get('firmwareCtrlrRunning').get('attributes').get('applId'))

    MYJSONFILE.close()
    return

# --Run the main file
main()