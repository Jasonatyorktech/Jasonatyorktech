#Jason Quinn
#Minecraft Code Example
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

mc.postToChat('hello')

playerPos=mc.player.getTilePos()
mc.postToChat(playerPos)



