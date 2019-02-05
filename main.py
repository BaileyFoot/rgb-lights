import lightLib
#need ,lightControls in front of anything that belongs in other file...
pi = lightLib.Pi()
pi.setupGPIO()
#creating instance of Pi and setting up gpio lib.

lightOne = lightLib.Light(pi,[22,23,24])
#lightOne.setupPins()
#creating instance of Light and running pin setup.

red = int(input("red"))
green = int(input("green"))
blue = int(input("blue"))

lightOne.changeColour(red, green, blue)
