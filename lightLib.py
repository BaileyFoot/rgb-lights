#Import stuff
import RPi.GPIO as GPIO
import time
import sys


class Pi:

    def __init__(self, mode='bcm'):

        self.mode = mode
        #self.setupGPIO(mode)


    def setupGPIO(self):

        #sets board GPIO numbering to BCM or BOARD based on input.
        if self.mode == 'bcm':
            GPIO.setmode(GPIO.BCM)
        elif self.mode == 'board':
            GPIO.setmode(GPIO.BOARD)
        else:
            print(
            '''
            This is not a vaild option...
            *exiting*
            '''
            )
            sys.exit()


    def cleanup(self):
        print(
        '''
        *GPIOcleanup*
        Pins will be set to Low...
        '''
        )
        GPIO.cleanup()


class Light:

    def __init__(self, pi, pins):
        #creates red, green and blue pins properties.
        self.pi = pi
        self.pins = []
        self.redPin = pins[0]
        self.greenPin = pins[1]
        self.bluePin = pins[2]

        #creates desired red, green and blue colour val properties.
        #dont't think I need this.
        #self.redVal = redVal
        #self.greenVal = greenVal
        #self.blueVal = blueVal

    def setupPins(self):
        #sets up red, green and blue pins for output.
        GPIO.setup(self.redPin, GPIO.OUT)
        GPIO.setup(self.greenPin, GPIO.OUT)
        GPIO.setup(self.bluePin, GPIO.OUT)



    def changeColour(self, redVal, greenVal, blueVal):
        red = GPIO.PWM(self.redPin, 50)
        green = GPIO.PWM(self.greenPin, 50)
        blue = GPIO.PWM(self.bluePin, 50)

        red.start(0)
        green.start(0)
        blue.start(0)

        red.ChangeDutyCycle(int(redVal))
        green.ChangeDutyCycle(int(greenVal))
        blue.ChangeDutyCycle(int(blueVal))
        print(self.redPin)
        print(self.greenPin)
        print(self.bluePin)
        print("changed colour: redVal", redVal, "greenVal", greenVal, "blueVal", blueVal)
        #https://raspi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control
        #https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/


        #Could just take one value as input. format: rrr,ggg,bbb.
        #this would be readable from text file

        #red = GPIO.PWM() #need to put GPIO pin num in brackets. SCOPE!
        #green = GPIO.PWM()
        #blue = GPIO.PWM()
        #red.start(0)
        #green.start(0)
        #blue.start(0)

#will all be in main.py...
#This is only for testing.
