#!/usr/bin/python3
"""
Author: Jason Brummal
Create date: 
Purpose:
"""

import urllib.request
import json
import turtle
import time

# --Vars
issurl='http://api.open-notify.org/iss-now.json'

# --Functions
# noinspection PyUnreachableCode
def main():
    """Run time code"""

# --Second part of the lesson, print first, then graph it
    screen = turtle.Screen() # Creates the actual GUI screen
    screen.setup(720, 360)

    screen.setworldcoordinates(-180, -90, 180, 90) # Need to set the cartesian coordinate syste
    screen.bgpic('iss_map.gif') # Create a background picture to overlay coordinate system on

    screen.register_shape('spriteiss.gif') # Register a shapde

    iss = turtle.Turtle() # Creates the ability to move around on the screen
    iss.shape('spriteiss.gif') # Change the shape of the turtle to spriteiss.gif

    iss.setheading(90) # Set an initial heading

    # --Loop updates
    while True:
        result = urllib.request.urlopen(issurl)
    #    readresult=(result.read()).decode('utf-8') # Decode as utf-8 and then load the string (json.loads vs json.load)
    #    issloc_decode=json.loads(readresult)
        issloc_decode=json.load(result)

    # --Print the information for giggles
#        print(type(issloc_decode))
        print(issloc_decode['iss_position'])
#        print(issloc_decode['iss_position']['longitude'])
#        print(issloc_decode['iss_position']['latitude'])
        # --Dynamically grab the value from the json
        lon = round(float(issloc_decode['iss_position']['longitude']), ndigits=4)
        lat = round(float(issloc_decode['iss_position']['latitude']), ndigits=4)

    # --Set the direction and the location then loop to hold open
#        iss.penup() # Stop moving
        iss.goto(lon,lat) # Go to this location
        time.sleep(10)
    turtle.mainloop() #

# --Main
main()

