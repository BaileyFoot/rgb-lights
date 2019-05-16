import lightLib
import display
import time
#need ,lightControls in front of anything that belongs in other file...
pi = lightLib.Pi()
pi.setupGPIO()
#creating instance of Pi and setting up gpio lib.

lightOne = lightLib.Light(pi,[11,13,15]) #26,21,23
#creating instance of Light.

rightButton = lightLib.Button(pi,12)
leftButton = lightLib.Button(pi,16)
#creating instance of Button.


display.output("left Button: change basic colour.")
time.sleep(6)
display.output("right Button: cycle colours")
time.sleep(6)
display.output("")

presses=0

while True:
    if rightButton.isPressed():
        lightOne.cycleColours()

    if leftButton.isPressed():
        presses+=1
        if presses % 3 == 0:
            lightOne.basicChangeColour("red")
        elif presses % 3 == 1:
            lightOne.basicChangeColour("green")
        elif presses % 3 == 2:
            lightOne.basicChangeColour("blue")

    time.sleep(.01)



#lightOne.testOutputs()
