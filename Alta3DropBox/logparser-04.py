#!/usr/bin/python3
""" rzfeeser@alta3.com
parsing log file for match"""

# download the file here! goo.gl/uGeQ4n

def main():
    nonfail = 0
    counter = 0
    with open(r'C:\Users\Achimedes\Dropbox\2019-05-06 vzw pyans\keystone.txt', 'r') as logfile:
        for line in logfile:
            if "- - - - -] Authorization failed" in line:
                counter = counter + 1
            elif "-] Authorization failed" in line:
                nonfail = nonfail + 1
            
            
    print(counter)
    print(nonfail)
    input()
    
main()      