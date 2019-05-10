#!/usr/bin/python3
"""grab json of ISS location"""

import urllib.request
import json

def main():
    issurl = "http://api.open-notify.org/iss-now.json"
    result = urllib.request.urlopen(issurl)
    
    readresult = (result.read()).decode('utf-8')
    input()
    issloc = json.load(readresult)
    print(type(issloc))
    input()
    
main()
    