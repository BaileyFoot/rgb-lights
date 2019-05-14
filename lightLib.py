import RPi.GPIO as GPIO
import time
import sys


class Pi:

    def __init__(self, mode='bcm'):
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


    def testPower(self, pins):
        #able to input array of power pins to test each individually.
        for i in range(len(pins)):
            GPIO.setup(pins[i], GPIO.OUT)
            GPIO.output(pins[i], True)
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

    def test(self):
        #tests that the red, green and blue pins are all working.
        #turns each light on individually.
        GPIO.output(self.redPin, True)
        input("Red pin set to high")
        GPIO.output(self.redPin, False)
        GPIO.output(self.greenPin, True)
        input("Green pin set to high")
        GPIO.output(self.greenPin, False)
        GPIO.output(self.bluePin, True)
        input("Blue pin set to high")
        GPIO.output(self.bluePin, False)
        input("Test finished")

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
