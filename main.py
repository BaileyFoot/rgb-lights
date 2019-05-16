import lightLib
import display
#need ,lightControls in front of anything that belongs in other file...
pi = lightLib.Pi()
pi.setupGPIO()
#creating instance of Pi and setting up gpio lib.

lightOne = lightLib.Light(pi,[11,13,15]) #26,21,23
#creating instance of Light.

buttonOne = lightLib.Button(pi,12)
#creating instance of Button.

buttonOne.waitForPress()

#lightOne.testOutputs()
try:
    lightOne.cycleColours()
except:
    pi.cleanup()
    input()
