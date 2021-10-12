

import requests

#use a module to control time
import time

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

#srtup for buttons and leds
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Set up each pin number
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#start an indinite loop
while True:
    #wait for one second
    time.sleep(0)
    #check the first buttion.
    if GPIO.input(6)==GPIO.LOW:
        print("Button 6 was pressed")
        mc.postToChat('hello')
   