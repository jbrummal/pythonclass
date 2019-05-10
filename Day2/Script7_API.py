#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

import urllib.request
import json

# --Vars
majortom='http://api.open-notify.org/astros.json'

# --Functions
def main():
    """Run time code"""
    groundctrl = urllib.request.urlopen(majortom)
    helmet=groundctrl.read()
    helmetson=json.loads(helmet.decode('utf-8'))
    print("\n\nConverted python data")
    print(helmetson)
    print("\n\nPeople in Space: ", helmetson['number'])
    people=helmetson['people']
    print(people)

# --Main
main()

