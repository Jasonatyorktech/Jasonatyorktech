#mcdemo_placeblock.py
#jason quinn

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_UP)
           
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def buildHouse():
    pos=mc.player.getTilePos()
    mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x+6, pos.y+5, pos.z+6, 5)
    mc.setBlock(pos.x+3,pos.y,pos.z,5)
    mc.setBlock(pos.x+2,pos.y,pos.z,53)
    mc.setBlocks(pos.x+2, pos.y+1, pos.z+2, pos.x+5, pos.y +4, pos.z + 5, 0)
    mc.setBlocks(pos.x+3, pos.y+1, pos.z+1,pos.x+3, pos.y +2, pos.z+1, 64)

while True:
    if GPIO.input(6)==GPIO.LOW:
        buildHouse()
        