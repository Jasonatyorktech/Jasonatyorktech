#Jason Quinn
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

woolLine=[13,23,8,7,1]
woolGrid=[[12,12,12,12,12,12,12,12,12,12,12,0,0,0],
          [0,12,12,12,12,12,12,12,12,],
          [0,0,0,12,12,12,12,12,],
          [0,0,0,0,12,12,12],
          [1,1,1,1,0,0,0,],
          [1,1,1,0,0,0,0,],
          [1,1,0,0,15,0,0,]]

pos=mc.player.getTilePos()

pos= mc.player.getTilePos()
'''
for i, wool in enumerate(woolLine):
    
    print(str(i)+" is the color "+ str(wool))
    mc.setBlock(pos.x+i,pos.y,pos.z,35,wool)
'''   
for i,row in enumerate(woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock(pos.x+j,pos.y+i,pos.z,35,col)