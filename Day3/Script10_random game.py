#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

# --Imports
import requests

# --Variables
MYAPI = 'https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new'

def main():
    """Run time code"""
    value = requests.get(MYAPI)
    if "1" in value.text.strip('\n'):
        print("You are a stud")
    else:
        print("You are a loser")
    return

# --Run the actual code
main()
