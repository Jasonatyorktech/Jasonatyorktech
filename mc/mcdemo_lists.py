#Jason Quinn
#Places a randomy colored wool block

''''
Set up programing for MC and two buttons
Create a 'counter' variable that starts at 0
Create a list of blockdata numbers for different color wool
Define a function called placeNext
    - it takes one argument called direction
    -it changes the counter by adding the dirextion argument
    -place a wool block of color from the list where
     the index matches the counter variable
    -If the counter is out of bounds of the index, reset it
In a forever loop:
    -if the first button was pressed, placeNext(1)
    -if the second button was pressed, placeNext(-1)
'''
from mcpi.minecraft import Minecraft
mc=Minecraft.create()


import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)


counter= 0
woolColor =[6,5,10]

def placeNext(direction):
    global counter
    counter += direction
    if counter > 2:
        counter=0
    if counter< 0:
        counter=2
    mc.setBlock(-21, 14,-17,35,woolColor[counter])

        

while True:
    if GPIO.input(6)==GPIO.LOW:
        placeNext(1)
    elif GPIO.input(13)==GPIO.LOW:
        placeNext(-1)
        
