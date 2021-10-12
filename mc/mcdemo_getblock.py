#jason Quinn
#Gets mincraft block by Position

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(6)==GPIO.LOW:
        pos= mc.player.getTilePos()
        blockData = mc.getBlock(pos.x, pos.y-1,pos.z)
        print(blockData)
#IF 57 then YEET
        if blockData==57:
            mc.player.setPos(pos.x,pos.y+20,pos.z)
