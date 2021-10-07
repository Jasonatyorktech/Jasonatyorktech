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

GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#start an indinite loop
while True:
    #wait for one second
    time.sleep(1)
    #check the first buttion.
    if GPIO.input(6)==GPIO.LOW:
        print("Button 6 was pressed")
        mc.postToChat('hello')
    elif GPIO.input(13)==GPIO.LOW:
        print("Button 13 was pressed")
        mc.postToChat('HES BEHIND YOU RUN')
    elif GPIO.input(19)==GPIO.LOW:
        print("Button 19 was pressed")
    elif GPIO.input(26)==GPIO.LOW:
        print("Button 26 was pressed")