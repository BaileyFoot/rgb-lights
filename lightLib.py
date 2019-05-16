import RPi.GPIO as GPIO
import time
import sys


class Pi:

    def __init__(self, mode='board'):
        #makes the gpio mode a property of the pi class.
        self.mode = mode

    def setupGPIO(self):
        #sets board GPIO numbering to BCM or BOARD based on input (bcm by default).
        #ends program if input is invalid.
        if self.mode == 'bcm':
            GPIO.setmode(GPIO.BCM)
            #print("Mode BCM")
        elif self.mode == 'board':
            GPIO.setmode(GPIO.BOARD)
            #print("Mode BOARD")
        else:
            print(
            '''
            This is not a vaild option...
            *exiting*
            '''
            )
            sys.exit()


    def cleanup(self):
        #cleans up and gpio pins etc.
        print(
        '''
        *GPIOcleanup*
        Pins will be set to Low...
        '''
        )
        GPIO.cleanup()

class Component:

    def __init__(self, pi, pins):
        self.pi = pi
        #runs through array of pins, creating them as properties of component.
        self.pins = []
        for i in range(len(pins)):
            self.pins.append(pins[i])


    def testOutputs(self):
        #able to input array of power pins to test each individually.
        for i in range(len(self.pins)):
            #GPIO.setup(self.pins[i], GPIO.OUT)
            GPIO.output(self.pins[i], True)

            print(self.pins[i], "Set to high.")
            input()

        print("Test finished.")

        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], False)


class Light(Component):

    def __init__(self, pi, pins):
        #init function of superclass
        Component.__init__(self, pi, pins)
        #creates red, green and blue pin properties.
        self.redPin = pins[0]
        self.greenPin = pins[1]
        self.bluePin = pins[2]

        #sets up red, geen and blue pins as outputs using gpio.
        GPIO.setup(self.redPin, GPIO.OUT)
        GPIO.setup(self.greenPin, GPIO.OUT)
        GPIO.setup(self.bluePin, GPIO.OUT)

        #sets up red, green and blue pins as pwm outputs using gpio.
        self.redPwm = GPIO.PWM(self.redPin, 50)
        self.greenPwm = GPIO.PWM(self.greenPin, 50)
        self.bluePwm = GPIO.PWM(self.bluePin, 50)

    def testOutputs(self):
        #able to input array of power pins to test each individually.
        for i in range(len(self.pins)):
            #GPIO.setup(self.pins[i], GPIO.OUT)
            GPIO.output(self.pins[i], True)
            print(self.pins[i], "Set to high.")
            input()

            GPIO.output(self.pins[i], False)
            print(self.pins[i], "Set to low.")
            input()

        print("Test finished.")

    def changeColour(self, redVal, greenVal, blueVal):
        #changes the colour of the light using % of red, green and blue.

        #sets % power for each pin to 0.
        self.redPwm.start(0)
        self.greenPwm.start(0)
        self.bluePwm.start(0)

        #applies % power to corresponding pin.
        self.redPwm.ChangeDutyCycle(redVal)
        self.greenPwm.ChangeDutyCycle(greenVal)
        self.bluePwm.ChangeDutyCycle(blueVal)

    def basicChangeColour(self, colour):
        if colour == "red":
            self.changeColour(100,0,0)
        if colour == "green":
            self.changeColour(0,100,0)
        if colour == "blue":
            self.changeColour(0,0,100)

    def cycleColours(self):
        while True:
            for i in range(100):
                self.changeColour(100,i,0)
                time.sleep(.01)
                #print("green", i)

            for i in range(100):
                self.changeColour(100,100,i)
                time.sleep(.01)
                #print("blue", i)

            for i in range(100):
                self.changeColour(100-i,100,100)
                time.sleep(.01)
                #print("red", 100-i)

            for i in range(100):
                self.changeColour(0,100-i,100)
                time.sleep(.01)
                #print("green", 100-i)

            for i in range(100):
                self.changeColour(i,0,100-i)
                time.sleep(.01)
                #print("blue", 100-i)
                #print("red", i)


class Button(Component):
    def __init__(self, pi, inputPin):

        self.inputPin = inputPin
        #GPIO.setup(self.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        #init function of superclass
        #Component.__init__(self, pi, self.inputPin)

        #need to make functions to test if button is pushed...

    def isPressed(self):
        if GPIO.input(self.inputPin)) == 1:
            return True
        else:
            return False

    def waitForPress(self):
        while GPIO.input(self.inputPin) == 0:
            time.sleep(0.05)

#encapsulation used as nothing is defined globally/returned to main program.
#inheritance used when instance of pi is made a property of light.
#still need an example of polymorphism.
