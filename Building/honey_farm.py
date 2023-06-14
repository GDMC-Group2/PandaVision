__all__ = []
# __version__

import random
from gdpc import Editor, Block, geometry
from interfaceUtils import getBlock
from interfaceUtils import runCommand

editor = Editor(buffering=True)

def flower_garden(x,y,z,pro,facing):
    editor.buffering = False
    flower=random.sample(("dandelion","poppy","blue_orchid","allium","azure_bluet","red_tulip","orange_tulip","white_tulip","pink_tulip","oxeye_daisy","cornflower","lily_of_the_valley"),3)
    if(facing=='n'):
        for xx in range(13):
            for zz in range(9):
                if("air" in getBlock(x+1+xx,y,z+1+zz) and pro>random.random()): #そこに何も置かれていない,かつ確率を通ったら
                    editor.placeBlock((x+1+xx,y,z+1+zz),Block(random.choice(flower)))
    elif(facing=='e'):
        for xx in range(13):
            for zz in range(9):
                if("air" in getBlock(x-1-zz,y,z+1+xx) and pro>random.random()):
                    editor.placeBlock((x-1-zz,y,z+1+xx),Block(random.choice(flower)))



def honey_farm(x,y,z,facing): #east or north
        
    if(facing=='n'):
        for xx in range(15):
            for zz in range(10):
                editor.placeBlock((x+xx,y-1,z+zz),Block("grass_block"))
        for zz in [2,5,8]:
            for xx in [2,5]:
                editor.placeBlock((x+xx,y-1,z+zz),Block("campfire",{"facing":"west","lit":"false"}))
                editor.placeBlock((x+xx,y,z+zz),Block("beehive",{"facing":"east"}))
            for xx in [9,12]:
                editor.placeBlock((x+xx,y-1,z+zz),Block("campfire",{"facing":"west","lit":"false"}))
                editor.placeBlock((x+xx,y,z+zz),Block("beehive",{"facing":"west"}))        
        editor.placeBlock((x+7,y-1,z+5),Block("glowstone"))
        editor.placeBlock((x+7,y,z+5),Block("green_carpet"))
        for xx in range(15):
            editor.placeBlock((x+xx,y,z),Block("oak_fence"))
            editor.placeBlock((x+xx,y,z+10),Block("oak_fence"))
        for zz in range(10):
            editor.placeBlock((x,y,z+zz),Block("oak_fence"))
            editor.placeBlock((x+14,y,z+zz),Block("oak_fence"))
        for xx in range(3):
            editor.placeBlock((x+6+xx,y,z),Block("oak_fence_gate",{"facing":"north"}))
            editor.placeBlock((x+6+xx,y,z+10),Block("oak_fence_gate",{"facing":"north"}))
        editor.placeBlock((x,y+1,z),Block("lantern"))
        editor.placeBlock((x,y+1,z+10),Block("lantern"))
        editor.placeBlock((x+14,y+1,z),Block("lantern"))
        editor.placeBlock((x+14,y+1,z+10),Block("lantern"))

        flower_garden(x,y,z,0.6,facing)
        command=command = f"summon minecraft:bee {x+7} {y+4} {z+5}"
        for i in range(3):
            runCommand(command)
    
    elif(facing=='e'):
        for xx in range(15):
            for zz in range(10):
                editor.placeBlock((x-zz,y-1,z+xx),Block("grass_block"))
        for zz in [2,5,8]:
            for xx in [2,5]:
                editor.placeBlock((x-zz,y-1,z+xx),Block("campfire",{"facing":"north","lit":"false"}))
                editor.placeBlock((x-zz,y,z+xx),Block("beehive",{"facing":"south"}))
            for xx in [9,12]:
                editor.placeBlock((x-zz,y-1,z+xx),Block("campfire",{"facing":"north","lit":"false"}))
                editor.placeBlock((x-zz,y,z+xx),Block("beehive",{"facing":"north"}))        
        editor.placeBlock((x-5,y-1,z+7),Block("glowstone"))
        editor.placeBlock((x-5,y,z+7),Block("green_carpet"))
        for xx in range(15):
            editor.placeBlock((x,y,z+xx),Block("oak_fence"))
            editor.placeBlock((x-10,y,z+xx),Block("oak_fence"))
        for zz in range(10):
            editor.placeBlock((x-zz,y,z),Block("oak_fence"))
            editor.placeBlock((x-zz,y,z+14),Block("oak_fence"))
        for xx in range(3):
            editor.placeBlock((x,y,z+6+xx),Block("oak_fence_gate",{"facing":"west"}))
            editor.placeBlock((x-10,y,z+6+xx),Block("oak_fence_gate",{"facing":"west"}))
        editor.placeBlock((x,y+1,z),Block("lantern"))
        editor.placeBlock((x-10,y+1,z),Block("lantern"))
        editor.placeBlock((x,y+1,z+14),Block("lantern"))
        editor.placeBlock((x-10,y+1,z+14),Block("lantern"))

        flower_garden(x,y,z,0.6,facing)
        command=command = f"summon minecraft:bee {x-5} {y+4} {z+7}"
        for i in range(3):
            runCommand(command)


honey_farm(-170,4,45,'e')
honey_farm(-200,4,45,'n')

