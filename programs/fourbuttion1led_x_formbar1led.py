import requests

#use a module to control time
import time

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
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13)==GPIO.LOW:
        print("Button 13 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=wiggle")
    elif GPIO.input(19)==GPIO.LOW:
        print("Button 19 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    elif GPIO.input(26)==GPIO.LOW:
        print("Button 26 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")