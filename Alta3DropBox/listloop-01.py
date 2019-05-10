#!/usr/bin/python3
"""
Python script 01
learning about lists and loops
"""

def main():
    """this is our runtime code"""
    networklists = [['ios', '10.0.0.1'], ['ios', '10.0.0.2'], ['ios-xr', '192.168.3.1'], ['junos', '172.0.0.4'], ['merkai', '10.0.0.3']]
    
    print(networklists[0][1]) # print 10.0.0.1
    
    for driversandip in networklists:
        print('SSH to', driversandip[1], 'using', driversandip[0])
        
    input("Press Enter to close")

main()
        
    
    