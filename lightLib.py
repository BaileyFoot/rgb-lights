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
            print("Mode BCM")
        elif self.mode == 'board':
            GPIO.setmode(GPIO.BOARD)
            print("Mode BOARD")
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
        print(pins)
        self.pi = pi
        #runs through array of pins, creating them as properties of component.
        self.pins = []
        for i in range(len(pins)-1):
            self.pins.append(pins[i])


    def testOutputs(self, pins):
        #able to input array of power pins to test each individually.
        for i in range(len(pins)):
            GPIO.setup(pins[i-1], GPIO.OUT)
            GPIO.output(pins[i-1], True)
            input("pin number", i, " set to high.")
        print("Test finished.")

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
            GPIO.setup(self.pins[i-1], GPIO.OUT)
            GPIO.output(self.pins[i-1], True)
            #input("pin number", i , " set to high.")
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

#encapsulation used as nothing is defined globally/returned to main program.
#inheritance used when instance of pi is made a property of light.
#still need an example of polymorphism.
