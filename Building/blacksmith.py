__all__ = []
# __version__

import random
from gdpc import Editor, Block, geometry

editor = Editor(buffering=True)


def floor_s(x,y,z,f_id,e_id): #f=floorblock e=edge
    #floor
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x+5+xx,y-1,z+3+zz),Block(f_id))
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x+xx,y,z+zz),Block(f_id))
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x+5+xx,y,z+3+zz),Block("air"))

    for zz in range(4):
        editor.placeBlock((x+4,y,z+3+zz),Block(e_id,{"facing":"west"}))
        editor.placeBlock((x+8,y,z+3+zz),Block(e_id,{"facing":"east"}))
    for xx in range(3):
        editor.placeBlock((x+5+xx,y,z+6),Block(e_id,{"facing":"south"}))
    for zz in range(7):
        editor.placeBlock((x,y,z+1+zz),Block(e_id,{"facing":"east"}))
    for xx in range(8):
        editor.placeBlock((x+1+xx,y,z+7),Block(e_id,{"facing":"north"}))



#roof
def roof_s(x,y,z,r_id): #r=roofblock
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x+xx,y+6,z+zz),Block(r_id,{"type":"bottom"}))


#wall
def wall_s(x,y,z,w_id): #w=wallblock
    for xx in range(10):
        editor.placeBlock((x+xx,y+1,z),Block(w_id))
        editor.placeBlock((x+xx,y+2,z),Block(w_id))
    for zz in range(8):
        editor.placeBlock((x+9,y+1,z+zz),Block(w_id))
        editor.placeBlock((x+9,y+2,z+zz),Block(w_id))
    for yy in range(3):
        editor.placeBlock((x,y+3+yy,z),Block(w_id))
        editor.placeBlock((x+9,y+3+yy,z),Block(w_id))
        editor.placeBlock((x+9,y+3+yy,z+7),Block(w_id))

#furnace
def furnace_s(x,y,z,fc_id,fe_id): #fc=furnace_casing fe=fuenace_edge
    for xx in range(3):
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((x+5+xx,y+yy,z+zz),Block(fc_id))
    editor.placeBlock((x+6,y+1,z+1),Block("blast_furnace",{"facing":"south","lit":"true"}))
    editor.placeBlock((x+6,y+1,z+2),Block("iron_bars"))

    editor.placeBlock((x+6,y,z+2),Block(fe_id,{"facing":"north","half":"bottom"}))
    editor.placeBlock((x+6,y+2,z+2),Block(fe_id,{"facing":"north","half":"top"}))
    for xx in range(3):
        editor.placeBlock((x+5+xx,y+3,z),Block(fe_id,{"facing":"south"}))
        editor.placeBlock((x+5+xx,y+3,z+2),Block(fe_id,{"facing":"north"}))
    editor.placeBlock((x+5,y+3,z+1),Block(fe_id,{"facing":"east"}))
    editor.placeBlock((x+7,y+3,z+1),Block(fe_id,{"facing":"west"}))
    for yy in range(4):
        editor.placeBlock((x+6,y+4+yy,z+1),Block(fc_id))

#decorate
def decorate_s(x,y,z):
    editor.placeBlock((x+7,y,z+3),Block("water_cauldron",{"level":"2"}))
    editor.placeBlock((x+7,y,z+5),Block("anvil",{"facing":"south"}))
    editor.placeBlock((x+1,y+1,z+4),Block("grindstone",{"face":"floor","facing":"west"}))
    editor.placeBlock((x+1,y+1,z+5),Block("stonecutter",{"facing":"east"}))

    editor.placeBlock((x+2,y+1,z+2),Block("polished_andesite"))
    editor.placeBlock((x+3,y+1,z+2),Block("polished_andesite"))
    editor.placeBlock((x+3,y+2,z+2),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x,y+5,z+7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+1,y+5,z+1),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+4,y+5,z+7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+8,y+5,z+1),Block("lantern",{"hanging":"true"}))



def floor_e(x,y,z,f_id,e_id): #f=floorblock e=edge
    #floor
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x-3-zz,y-1,z+5+xx),Block(f_id))
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x-zz,y,z+xx),Block(f_id))
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x-3-zz,y,z+5+xx),Block("air"))

    for zz in range(4):
        editor.placeBlock((x-3-zz,y,z+4),Block(e_id,{"facing":"north"}))
        editor.placeBlock((x-3-zz,y,z+8),Block(e_id,{"facing":"south"}))
    for xx in range(3):
        editor.placeBlock((x-6,y,z+5+xx),Block(e_id,{"facing":"west"}))
    for zz in range(7):
        editor.placeBlock((x-1-zz,y,z),Block(e_id,{"facing":"south"}))
    for xx in range(8):
        editor.placeBlock((x-7,y,z+1+xx),Block(e_id,{"facing":"east"}))



#roof
def roof_e(x,y,z,r_id): #r=roofblock
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x-zz,y+6,z+xx),Block(r_id,{"type":"bottom"}))


#wall
def wall_e(x,y,z,w_id): #w=wallblock
    for xx in range(10):
        editor.placeBlock((x,y+1,z+xx),Block(w_id))
        editor.placeBlock((x,y+2,z+xx),Block(w_id))
    for zz in range(8):
        editor.placeBlock((x-zz,y+1,z+9),Block(w_id))
        editor.placeBlock((x-zz,y+2,z+9),Block(w_id))
    for yy in range(3):
        editor.placeBlock((x,y+3+yy,z),Block(w_id))
        editor.placeBlock((x,y+3+yy,z+9),Block(w_id))
        editor.placeBlock((x-7,y+3+yy,z+9),Block(w_id))

#furnace
def furnace_e(x,y,z,fc_id,fe_id): #fc=furnace_casing fe=fuenace_edge
    for xx in range(3):
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((x-zz,y+yy,z+5+xx),Block(fc_id))
    editor.placeBlock((x-1,y+1,z+6),Block("blast_furnace",{"facing":"west","lit":"true"}))
    editor.placeBlock((x-2,y+1,z+6),Block("iron_bars"))

    editor.placeBlock((x-2,y,z+6),Block(fe_id,{"facing":"east","half":"bottom"}))
    editor.placeBlock((x-2,y+2,z+6),Block(fe_id,{"facing":"east","half":"top"}))
    for xx in range(3):
        editor.placeBlock((x,y+3,z+5+xx),Block(fe_id,{"facing":"west"}))
        editor.placeBlock((x-2,y+3,z+5+xx),Block(fe_id,{"facing":"east"}))
    editor.placeBlock((x-1,y+3,z+5),Block(fe_id,{"facing":"south"}))
    editor.placeBlock((x-1,y+3,z+7),Block(fe_id,{"facing":"north"}))
    for yy in range(4):
        editor.placeBlock((x-1,y+4+yy,z+6),Block(fc_id))



#decorate
def decorate_e(x,y,z):
    editor.placeBlock((x-3,y,z+7),Block("water_cauldron",{"level":"2"}))
    editor.placeBlock((x-5,y,z+7),Block("anvil",{"facing":"west"}))
    editor.placeBlock((x-4,y+1,z+1),Block("grindstone",{"face":"floor","facing":"north"}))
    editor.placeBlock((x-5,y+1,z+1),Block("stonecutter",{"facing":"south"}))

    editor.placeBlock((x-2,y+1,z+2),Block("polished_andesite"))
    editor.placeBlock((x-2,y+1,z+3),Block("polished_andesite"))
    editor.placeBlock((x-2,y+2,z+3),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-7,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-1,y+5,z+1),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-7,y+5,z+4),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-1,y+5,z+8),Block("lantern",{"hanging":"true"}))


def floor_n(x,y,z,f_id,e_id): #f=floorblock e=edge
    #floor
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x-5-xx,y-1,z-3-zz),Block(f_id))
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x-xx,y,z-zz),Block(f_id))
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x-5-xx,y,z-3-zz),Block("air"))

    for zz in range(4):
        editor.placeBlock((x-4,y,z-3-zz),Block(e_id,{"facing":"east"}))
        editor.placeBlock((x-8,y,z-3-zz),Block(e_id,{"facing":"west"}))
    for xx in range(3):
        editor.placeBlock((x-5-xx,y,z-6),Block(e_id,{"facing":"north"}))
    for zz in range(7):
        editor.placeBlock((x,y,z-1-zz),Block(e_id,{"facing":"west"}))
    for xx in range(8):
        editor.placeBlock((x-1-xx,y,z-7),Block(e_id,{"facing":"south"}))



#roof
def roof_n(x,y,z,r_id): #r=roofblock
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x-xx,y+6,z-zz),Block(r_id,{"type":"bottom"}))


#wall
def wall_n(x,y,z,w_id): #w=wallblock
    for xx in range(10):
        editor.placeBlock((x-xx,y+1,z),Block(w_id))
        editor.placeBlock((x-xx,y+2,z),Block(w_id))
    for zz in range(8):
        editor.placeBlock((x-9,y+1,z-zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z-zz),Block(w_id))
    for yy in range(3):
        editor.placeBlock((x,y+3+yy,z),Block(w_id))
        editor.placeBlock((x-9,y+3+yy,z),Block(w_id))
        editor.placeBlock((x-9,y+3+yy,z-7),Block(w_id))

#furnace
def furnace_n(x,y,z,fc_id,fe_id): #fc=furnace_casing fe=fuenace_edge
    for xx in range(3):
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((x-5-xx,y+yy,z-zz),Block(fc_id))
    editor.placeBlock((x-6,y+1,z-1),Block("blast_furnace",{"facing":"north","lit":"true"}))
    editor.placeBlock((x-6,y+1,z-2),Block("iron_bars"))

    editor.placeBlock((x-6,y,z-2),Block(fe_id,{"facing":"south","half":"bottom"}))
    editor.placeBlock((x-6,y+2,z-2),Block(fe_id,{"facing":"south","half":"top"}))
    for xx in range(3):
        editor.placeBlock((x-5-xx,y+3,z),Block(fe_id,{"facing":"north"}))
        editor.placeBlock((x-5-xx,y+3,z-2),Block(fe_id,{"facing":"south"}))
    editor.placeBlock((x-5,y+3,z-1),Block(fe_id,{"facing":"west"}))
    editor.placeBlock((x-7,y+3,z-1),Block(fe_id,{"facing":"east"}))
    for yy in range(4):
        editor.placeBlock((x-6,y+4+yy,z-1),Block(fc_id))



#decorate
def decorate_n(x,y,z):
    editor.placeBlock((x-7,y,z-3),Block("water_cauldron",{"level":"2"}))
    editor.placeBlock((x-7,y,z-5),Block("anvil",{"facing":"north"}))
    editor.placeBlock((x-1,y+1,z-4),Block("grindstone",{"face":"floor","facing":"east"}))
    editor.placeBlock((x-1,y+1,z-5),Block("stonecutter",{"facing":"west"}))

    editor.placeBlock((x-2,y+1,z-2),Block("polished_andesite"))
    editor.placeBlock((x-3,y+1,z-2),Block("polished_andesite"))
    editor.placeBlock((x-3,y+2,z-2),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x,y+5,z-7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-1,y+5,z-1),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-4,y+5,z-7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-8,y+5,z-1),Block("lantern",{"hanging":"true"}))







def floor_w(x,y,z,f_id,e_id): #f=floorblock e=edge
    #floor
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x+3+zz,y-1,z-5-xx),Block(f_id))
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x+zz,y,z-xx),Block(f_id))
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x+3+zz,y,z-5-xx),Block("air"))

    for zz in range(4):
        editor.placeBlock((x+3+zz,y,z-4),Block(e_id,{"facing":"south"}))
        editor.placeBlock((x+3+zz,y,z-8),Block(e_id,{"facing":"north"}))
    for xx in range(3):
        editor.placeBlock((x+6,y,z-5-xx),Block(e_id,{"facing":"east"}))
    for zz in range(7):
        editor.placeBlock((x+1+zz,y,z),Block(e_id,{"facing":"north"}))
    for xx in range(8):
        editor.placeBlock((x+7,y,z-1-xx),Block(e_id,{"facing":"west"}))


#roof
def roof_w(x,y,z,r_id): #r=roofblock
    for xx in range(10):
        for zz in range(8):
            editor.placeBlock((x+zz,y+6,z-xx),Block(r_id,{"type":"bottom"}))


#wall
def wall_w(x,y,z,w_id): #w=wallblock
    for xx in range(10):
        editor.placeBlock((x,y+1,z-xx),Block(w_id))
        editor.placeBlock((x,y+2,z-xx),Block(w_id))
    for zz in range(8):
        editor.placeBlock((x+zz,y+1,z-9),Block(w_id))
        editor.placeBlock((x+zz,y+2,z-9),Block(w_id))
    for yy in range(3):
        editor.placeBlock((x,y+3+yy,z),Block(w_id))
        editor.placeBlock((x,y+3+yy,z-9),Block(w_id))
        editor.placeBlock((x+7,y+3+yy,z-9),Block(w_id))

#furnace
def furnace_w(x,y,z,fc_id,fe_id): #fc=furnace_casing fe=fuenace_edge
    for xx in range(3):
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((x+zz,y+yy,z-5-xx),Block(fc_id))
    editor.placeBlock((x+1,y+1,z-6),Block("blast_furnace",{"facing":"east","lit":"true"}))
    editor.placeBlock((x+2,y+1,z-6),Block("iron_bars"))

    editor.placeBlock((x+2,y,z-6),Block(fe_id,{"facing":"west","half":"bottom"}))
    editor.placeBlock((x+2,y+2,z-6),Block(fe_id,{"facing":"west","half":"top"}))
    for xx in range(3):
        editor.placeBlock((x,y+3,z-5-xx),Block(fe_id,{"facing":"east"}))
        editor.placeBlock((x+2,y+3,z-5-xx),Block(fe_id,{"facing":"west"}))
    editor.placeBlock((x+1,y+3,z-5),Block(fe_id,{"facing":"north"}))
    editor.placeBlock((x+1,y+3,z-7),Block(fe_id,{"facing":"south"}))
    for yy in range(4):
        editor.placeBlock((x+1,y+4+yy,z-6),Block(fc_id))



#decorate
def decorate_w(x,y,z):
    editor.placeBlock((x+3,y,z-7),Block("water_cauldron",{"level":"2"}))
    editor.placeBlock((x+5,y,z-7),Block("anvil",{"facing":"east"}))
    editor.placeBlock((x+4,y+1,z-1),Block("grindstone",{"face":"floor","facing":"south"}))
    editor.placeBlock((x+5,y+1,z-1),Block("stonecutter",{"facing":"north"}))

    editor.placeBlock((x+2,y+1,z-2),Block("polished_andesite"))
    editor.placeBlock((x+2,y+1,z-3),Block("polished_andesite"))
    editor.placeBlock((x+2,y+2,z-3),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+7,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+1,y+5,z-1),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+7,y+5,z-4),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+1,y+5,z-8),Block("lantern",{"hanging":"true"}))










def blacksmith_main(x,y,z,facing):
    if(facing=='e'):
        blacksmith_e(x,y,z)
    elif(facing=='s'):
        blacksmith_s(x,y,z)
    elif(facing=='w'):
        blacksmith_w(x,y,z)
    elif(facing=='n'):
        blacksmith_n(x,y,z)

def blacksmith_e(x,y,z):
    floor_e(x,y,z,"cobblestone","cobblestone_stairs")
    roof_e(x,y,z,"dark_prismarine_slab")
    wall_e(x,y,z,"cobblestone_wall")
    furnace_e(x,y,z,"polished_blackstone_bricks","polished_blackstone_stairs")
    decorate_e(x,y,z)

def blacksmith_s(x,y,z):
    floor_s(x,y,z,"cobblestone","cobblestone_stairs")
    roof_s(x,y,z,"dark_prismarine_slab")
    wall_s(x,y,z,"cobblestone_wall")
    furnace_s(x,y,z,"polished_blackstone_bricks","polished_blackstone_stairs")
    decorate_s(x,y,z)

def blacksmith_w(x,y,z):
    floor_w(x,y,z,"cobblestone","cobblestone_stairs")
    roof_w(x,y,z,"dark_prismarine_slab")
    wall_w(x,y,z,"cobblestone_wall")
    furnace_w(x,y,z,"polished_blackstone_bricks","polished_blackstone_stairs")
    decorate_w(x,y,z)


def blacksmith_n(x,y,z):
    floor_n(x,y,z,"cobblestone","cobblestone_stairs")
    roof_n(x,y,z,"dark_prismarine_slab")
    wall_n(x,y,z,"cobblestone_wall")
    furnace_n(x,y,z,"polished_blackstone_bricks","polished_blackstone_stairs")
    decorate_n(x,y,z)
