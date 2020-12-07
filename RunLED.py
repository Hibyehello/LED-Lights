import time
#import RPi.GPIO as GPIO
import random

class LED():
    led = 0
    def Yellow_LED(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
    
    #Defining which LED
        led = 10
    
        #GPIO.setup(led, GPIO.OUT)
    
    #Turn on LED
        print("Yellow Light On")
        #GPIO.output(led, GPIO.HIGH)
    
    #Turn off LED after set amount of time
        time.sleep(1)
        print("Yellow Light off")
        #GPIO.output(led, GPIO.LOW)
    
    #Resets GPIO outputs
        #GPIO.cleanup()

    def Red_LED(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
    
    #Defining which LED
        led = 9
    
        #GPIO.setup(led, GPIO.OUT)
    
    #Turn on LED
        print("Red Light On")
        #GPIO.output(led, GPIO.HIGH)
    
    #Turn off LED after set amount of time
        time.sleep(1)
        print("Red Light off")
        #GPIO.output(led, GPIO.LOW)
    
    #Resets GPIO outputs
        #GPIO.cleanup()

    def Green_LED(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
    
    #Defining which LED
        led = 11
    
        #GPIO.setup(led, GPIO.OUT)
    
    #Turn on LED
        print("Green Light On")
        #GPIO.output(led, GPIO.HIGH)
    
    #Turn off LED after set amount of time
        time.sleep(1)
        print("Green Light off")
        #GPIO.output(led, GPIO.LOW)
    
    #Resets GPIO outputs
        #GPIO.cleanup()

    def Rand_LED(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
    
    #Defining which LED
        led = random.randint(9,11)
    
        #GPIO.setup(led, GPIO.OUT)
    
    #Turn on LED
        if led == 11:
            print("Green Light on")
        elif led == 10:
            print ("Yellow Light on")
        else:
            print ("Red Light on")
        #GPIO.output(led, GPIO.HIGH)
    
    #Turn off LED after set amount of time
        time.sleep(1)
        if led == 11:
            print("Green Light off")
        elif led == 10:
            print ("Yellow Light off")
        else:
            print ("Red Light off")
        #GPIO.output(led, GPIO.LOW)
    
    #Resets GPIO outputs
        #GPIO.cleanup()