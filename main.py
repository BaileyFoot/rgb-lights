import lightLib
import display
#need ,lightControls in front of anything that belongs in other file...
pi = lightLib.Pi()
pi.setupGPIO()
#creating instance of Pi and setting up gpio lib.

lightOne = lightLib.Light(pi,[11,13,15]) #26,21,23
#lightOne.setupPins()
#creating instance of Light and running pin setup.

lightOne.test()

#display.output("Hello there!")

#red = int(input("red"))
#green = int(input("green"))
#blue = int(input("blue"))

#lightOne.changeColour(red, green, blue)

input()
