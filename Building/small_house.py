import random
from gdpc import Editor, Block, geometry

editor = Editor(buffering=True)




def foundation_s(x,y,z,m_id,e_id): #f=floor e-edge
    for xx in range(2):
        editor.placeBlock((x+1+xx,y,z+7),Block("grass_block"))
        editor.placeBlock((x+5+xx,y,z+7),Block("grass_block"))
        editor.placeBlock((x+1+xx,y,z+8),Block("spruce_trapdoor",{"facing":"south","half":"top","open":"true"}))
        editor.placeBlock((x+5+xx,y,z+8),Block("spruce_trapdoor",{"facing":"south","half":"top","open":"true"}))
        editor.placeBlock((x+1+xx,y+1,z+7),Block("oak_leaves",{"persistent":"true"}))
        editor.placeBlock((x+5+xx,y+1,z+7),Block("oak_leaves",{"persistent":"true"}))
    editor.placeBlock((x,y,z+7),Block("spruce_trapdoor",{"facing":"west","half":"top","open":"true"}))
    editor.placeBlock((x+7,y,z+7),Block("spruce_trapdoor",{"facing":"east","half":"top","open":"true"}))
    for zz in range(4):
        editor.placeBlock((x+1,y,z+2+zz),Block(e_id))
        editor.placeBlock((x+6,y,z+2+zz),Block(e_id))
    for xx in range(4):
        editor.placeBlock((x+2+xx,y,z+1),Block(e_id))
    for xx in range(4):
        for zz in range(5):
            editor.placeBlock((x+2+xx,y,z+2+zz),Block(m_id))
    for xx in range(2):
        editor.placeBlock((x+3+xx,y,z+7),Block("acacia_stairs",{"facing":"north","half":"bottom","shape":"straight"}))


def wall_s(x,y,z,m_id,p_id):
    for zz in range(4):
        for yy in range(4):
            editor.placeBlock((x+1,y+1+yy,z+2+zz),Block(m_id))
            editor.placeBlock((x+6,y+1+yy,z+2+zz),Block(m_id))
    for xx in range(4):
        for yy in range(4):
            editor.placeBlock((x+2+xx,y+1+yy,z+1),Block(m_id))
            editor.placeBlock((x+2+xx,y+1+yy,z+6),Block(m_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((x+3+xx,y+1+yy,z+6),Block("air"))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((x+1,y+2+yy,z+3+zz),Block("glass_pane"))
            editor.placeBlock((x+6,y+2+yy,z+3+zz),Block("glass_pane"))
    #piller
    for xx in range(2):
        for zz in range(2):
            for yy in range(6):
                    editor.placeBlock((x+1+xx*5,y+yy,z+1+zz*5),Block(p_id,{"axis":"y"}))
    for xx in range(4):
        editor.placeBlock((x+2+xx,y+5,z+1),Block(p_id,{"axis":"x"}))
        editor.placeBlock((x+2+xx,y+5,z+6),Block(p_id,{"axis":"x"}))
    for zz in range(4):
        editor.placeBlock((x+1,y+5,z+2+zz),Block(p_id,{"axis":"z"}))
        editor.placeBlock((x+6,y+5,z+2+zz),Block(p_id,{"axis":"z"}))

#roof
def roof_s(x,y,z,s_id,st_id,c_id):
    #ceiling
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x+2+xx,y+5,z+2+zz),Block(c_id))

    #edge
    for zz in range(2):
        editor.placeBlock((x,y+5,z+1+zz),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x,y+6,z+3+zz),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x,y+5,z+5+zz),Block(s_id,{"type":"top"}))

    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x+1+xx,y+5,z+zz*7),Block(s_id,{"type":"top"}))
            editor.placeBlock((x+3+xx,y+6,z+zz*7),Block(s_id,{"type":"bottom"}))
            editor.placeBlock((x+5+xx,y+5,z+zz*7),Block(s_id,{"type":"top"}))


    for zz in range(2):
        editor.placeBlock((x+7,y+5,z+1+zz),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x+7,y+6,z+3+zz),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x+7,y+5,z+5+zz),Block(s_id,{"type":"top"}))

#corner
    editor.placeBlock((x,y+6,z),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+7,y+6,z+7),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+7,y+6,z),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x,y+6,z+7),Block(s_id,{"type":"bottom"}))

#middle
    editor.placeBlock((x+1,y+6,z+1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+1,y+6,z+2),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+2,y+6,z+1),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+2,y+6,z+2),Block(st_id,{"facing":"south","half":"bottom","shape":"inner_left"}))

    editor.placeBlock((x+6,y+6,z+1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+5,y+6,z+1),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+5,y+6,z+2),Block(st_id,{"facing":"west","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x+6,y+6,z+2),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))

    editor.placeBlock((x+6,y+6,z+6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+5,y+6,z+5),Block(st_id,{"facing":"north","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x+5,y+6,z+6),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+6,y+6,z+5),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))

    editor.placeBlock((x+1,y+6,z+6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+1,y+6,z+5),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+2,y+6,z+5),Block(st_id,{"facing":"east","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x+2,y+6,z+6),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))
    #center
    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x+3+xx,y+7,z+3+zz),Block(s_id,{"type":"bottom"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+1+xx,y+6,z+3+zz),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+3+xx,y+6,z+1+zz),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+3+xx,y+6,z+5+zz),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+5+xx,y+6,z+3+zz),Block(s_id,{"type":"top"}))
    #light
    editor.placeBlock((x,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x,y+5,z+7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+7,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+7,y+5,z+7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+4,y+6,z+3),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+4,y+7,z+6),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+6,y+7,z+3),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+1,y+7,z+4),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+3,y+7,z+1),Block("lantern",{"hanging":"false"}))



##west

def foundation_w(x,y,z,m_id,e_id): #f=floor e-edge
    for xx in range(2):
        editor.placeBlock((x-7,y,z+1+xx),Block("grass_block"))
        editor.placeBlock((x-7,y,z+5+xx),Block("grass_block"))
        editor.placeBlock((x-8,y,z+1+xx),Block("spruce_trapdoor",{"facing":"west","half":"top","open":"true"}))
        editor.placeBlock((x-8,y,z+5+xx),Block("spruce_trapdoor",{"facing":"west","half":"top","open":"true"}))
        editor.placeBlock((x-7,y+1,z+1+xx),Block("oak_leaves",{"persistent":"true"}))
        editor.placeBlock((x-7,y+1,z+5+xx),Block("oak_leaves",{"persistent":"true"}))
    editor.placeBlock((x-7,y,z),Block("spruce_trapdoor",{"facing":"north","half":"top","open":"true"}))
    editor.placeBlock((x-7,y,z+7),Block("spruce_trapdoor",{"facing":"south","half":"top","open":"true"}))
    for zz in range(4):
        editor.placeBlock((x-2-zz,y,z+1),Block(e_id))
        editor.placeBlock((x-2-zz,y,z+6),Block(e_id))
    for xx in range(4):
        editor.placeBlock((x-1,y,z+2+xx),Block(e_id))
    for xx in range(4):
        for zz in range(5):
            editor.placeBlock((x-2-zz,y,z+2+xx),Block(m_id))
    for xx in range(2):
        editor.placeBlock((x-7,y,z+3+xx),Block("acacia_stairs",{"facing":"east","half":"bottom","shape":"straight"}))


def wall_w(x,y,z,m_id,p_id):
    for zz in range(4):
        for yy in range(4):
            editor.placeBlock((x-2-zz,y+1+yy,z+1),Block(m_id))
            editor.placeBlock((x-2-zz,y+1+yy,z+6),Block(m_id))
    for xx in range(4):
        for yy in range(4):
            editor.placeBlock((x-1,y+1+yy,z+2+xx),Block(m_id))
            editor.placeBlock((x-6,y+1+yy,z+2+xx),Block(m_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((x-6,y+1+yy,z+3+xx),Block("air"))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((x-3-zz,y+2+yy,z+1),Block("glass_pane"))
            editor.placeBlock((x-3-zz,y+2+yy,z+6),Block("glass_pane"))
    #piller
    for xx in range(2):
        for zz in range(2):
            for yy in range(6):
                    editor.placeBlock((x-1-zz*5,y+yy,z+1+xx*5),Block(p_id,{"axis":"y"}))
    for xx in range(4):
        editor.placeBlock((x-1,y+5,z+2+xx),Block(p_id,{"axis":"z"}))
        editor.placeBlock((x-6,y+5,z+2+xx),Block(p_id,{"axis":"z"}))
    for zz in range(4):
        editor.placeBlock((x-2-zz,y+5,z+1),Block(p_id,{"axis":"x"}))
        editor.placeBlock((x-2-zz,y+5,z+6),Block(p_id,{"axis":"x"}))

#roof
def roof_w(x,y,z,s_id,st_id,c_id):
    #ceiling
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x-2-zz,y+5,z+2+xx),Block(c_id))

    #edge
    for zz in range(2):
        editor.placeBlock((x-1-zz,y+5,z),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x-3-zz,y+6,z),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x-5-zz,y+5,z),Block(s_id,{"type":"top"}))

    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x-zz*7,y+5,z+1+xx),Block(s_id,{"type":"top"}))
            editor.placeBlock((x-zz*7,y+6,z+3+xx),Block(s_id,{"type":"bottom"}))
            editor.placeBlock((x-zz*7,y+5,z+5+xx),Block(s_id,{"type":"top"}))


    for zz in range(2):
        editor.placeBlock((x-1-zz,y+5,z+7),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x-3-zz,y+6,z+7),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x-5-zz,y+5,z+7),Block(s_id,{"type":"top"}))

#corner
    editor.placeBlock((x,y+6,z),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-7,y+6,z+7),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x,y+6,z+7),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-7,y+6,z),Block(s_id,{"type":"bottom"}))

#middle
    editor.placeBlock((x-1,y+6,z+1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-2,y+6,z+1),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-1,y+6,z+2),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-2,y+6,z+2),Block(st_id,{"facing":"west","half":"bottom","shape":"inner_left"}))

    editor.placeBlock((x-1,y+6,z+6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-1,y+6,z+5),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-2,y+6,z+5),Block(st_id,{"facing":"north","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x-2,y+6,z+6),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))

    editor.placeBlock((x-6,y+6,z+6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-5,y+6,z+5),Block(st_id,{"facing":"east","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x-6,y+6,z+5),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-5,y+6,z+6),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))

    editor.placeBlock((x-6,y+6,z+1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-5,y+6,z+1),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-5,y+6,z+2),Block(st_id,{"facing":"south","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x-6,y+6,z+2),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))
    #center
    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x-3-zz,y+7,z+3+xx),Block(s_id,{"type":"bottom"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-3-zz,y+6,z+1+xx),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-1-zz,y+6,z+3+xx),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-5-zz,y+6,z+3+xx),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-3-zz,y+6,z+5+xx),Block(s_id,{"type":"top"}))
    #light
    editor.placeBlock((x,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-7,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x,y+5,z+7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-7,y+5,z+7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-3,y+6,z+4),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-6,y+7,z+4),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-3,y+7,z+6),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-4,y+7,z+1),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-1,y+7,z+3),Block("lantern",{"hanging":"false"}))

##north

def foundation_n(x,y,z,m_id,e_id): #f=floor e-edge
    for xx in range(2):
        editor.placeBlock((x-1-xx,y,z-7),Block("grass_block"))
        editor.placeBlock((x-5-xx,y,z-7),Block("grass_block"))
        editor.placeBlock((x-1-xx,y,z-8),Block("spruce_trapdoor",{"facing":"north","half":"top","open":"true"}))
        editor.placeBlock((x-5-xx,y,z-8),Block("spruce_trapdoor",{"facing":"north","half":"top","open":"true"}))
        editor.placeBlock((x-1-xx,y+1,z-7),Block("oak_leaves",{"persistent":"true"}))
        editor.placeBlock((x-5-xx,y+1,z-7),Block("oak_leaves",{"persistent":"true"}))
    editor.placeBlock((x,y,z-7),Block("spruce_trapdoor",{"facing":"east","half":"top","open":"true"}))
    editor.placeBlock((x-7,y,z-7),Block("spruce_trapdoor",{"facing":"west","half":"top","open":"true"}))
    for zz in range(4):
        editor.placeBlock((x-1,y,z-2-zz),Block(e_id))
        editor.placeBlock((x-6,y,z-2-zz),Block(e_id))
    for xx in range(4):
        editor.placeBlock((x-2-xx,y,z-1),Block(e_id))
    for xx in range(4):
        for zz in range(5):
            editor.placeBlock((x-2-xx,y,z-2-zz),Block(m_id))
    for xx in range(2):
        editor.placeBlock((x-3-xx,y,z-7),Block("acacia_stairs",{"facing":"south","half":"bottom","shape":"straight"}))


def wall_n(x,y,z,m_id,p_id):
    for zz in range(4):
        for yy in range(4):
            editor.placeBlock((x-1,y+1+yy,z-2-zz),Block(m_id))
            editor.placeBlock((x-6,y+1+yy,z-2-zz),Block(m_id))
    for xx in range(4):
        for yy in range(4):
            editor.placeBlock((x-2-xx,y+1+yy,z-1),Block(m_id))
            editor.placeBlock((x-2-xx,y+1+yy,z-6),Block(m_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((x-3-xx,y+1+yy,z-6),Block("air"))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((x-1,y+2+yy,z-3-zz),Block("glass_pane"))
            editor.placeBlock((x-6,y+2+yy,z-3-zz),Block("glass_pane"))
    #piller
    for xx in range(2):
        for zz in range(2):
            for yy in range(6):
                    editor.placeBlock((x-1-xx*5,y+yy,z-1-zz*5),Block(p_id,{"axis":"y"}))
    for xx in range(4):
        editor.placeBlock((x-2-xx,y+5,z-1),Block(p_id,{"axis":"x"}))
        editor.placeBlock((x-2-xx,y+5,z-6),Block(p_id,{"axis":"x"}))
    for zz in range(4):
        editor.placeBlock((x-1,y+5,z-2-zz),Block(p_id,{"axis":"z"}))
        editor.placeBlock((x-6,y+5,z-2-zz),Block(p_id,{"axis":"z"}))



#roof
def roof_n(x,y,z,s_id,st_id,c_id):
    #ceiling
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x-2-xx,y+5,z-2-zz),Block(c_id))

    #edge
    for zz in range(2):
        editor.placeBlock((x,y+5,z-1-zz),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x,y+6,z-3-zz),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x,y+5,z-5-zz),Block(s_id,{"type":"top"}))

    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x-1-xx,y+5,z-zz*7),Block(s_id,{"type":"top"}))
            editor.placeBlock((x-3-xx,y+6,z-zz*7),Block(s_id,{"type":"bottom"}))
            editor.placeBlock((x-5-xx,y+5,z-zz*7),Block(s_id,{"type":"top"}))


    for zz in range(2):
        editor.placeBlock((x-7,y+5,z-1-zz),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x-7,y+6,z-3-zz),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x-7,y+5,z-5-zz),Block(s_id,{"type":"top"}))

#corner
    editor.placeBlock((x,y+6,z),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-7,y+6,z-7),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-7,y+6,z),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x,y+6,z-7),Block(s_id,{"type":"bottom"}))

#middle
    editor.placeBlock((x-1,y+6,z-1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-1,y+6,z-2),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-2,y+6,z-1),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-2,y+6,z-2),Block(st_id,{"facing":"north","half":"bottom","shape":"inner_left"}))

    editor.placeBlock((x-6,y+6,z-1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-5,y+6,z-1),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-5,y+6,z-2),Block(st_id,{"facing":"east","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x-6,y+6,z-2),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))

    editor.placeBlock((x-6,y+6,z-6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-5,y+6,z-5),Block(st_id,{"facing":"south","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x-5,y+6,z-6),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-6,y+6,z-5),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))

    editor.placeBlock((x-1,y+6,z-6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x-1,y+6,z-5),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x-2,y+6,z-5),Block(st_id,{"facing":"west","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x-2,y+6,z-6),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))
    #center
    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x-3-xx,y+7,z-3-zz),Block(s_id,{"type":"bottom"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-1-xx,y+6,z-3-zz),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-3-xx,y+6,z-1-zz),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-3-xx,y+6,z-5-zz),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x-5-xx,y+6,z-3-zz),Block(s_id,{"type":"top"}))
    #light
    editor.placeBlock((x,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x,y+5,z-7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-7,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-7,y+5,z-7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x-4,y+6,z-3),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-4,y+7,z-6),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-6,y+7,z-3),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-1,y+7,z-4),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x-3,y+7,z-1),Block("lantern",{"hanging":"false"}))


#east

def foundation_e(x,y,z,m_id,e_id): #f=floor e-edge
    for xx in range(2):
        editor.placeBlock((x+7,y,z-1-xx),Block("grass_block"))
        editor.placeBlock((x+7,y,z-5-xx),Block("grass_block"))
        editor.placeBlock((x+8,y,z-1-xx),Block("spruce_trapdoor",{"facing":"east","half":"top","open":"true"}))
        editor.placeBlock((x+8,y,z-5-xx),Block("spruce_trapdoor",{"facing":"east","half":"top","open":"true"}))
        editor.placeBlock((x+7,y+1,z-1-xx),Block("oak_leaves",{"persistent":"true"}))
        editor.placeBlock((x+7,y+1,z-5-xx),Block("oak_leaves",{"persistent":"true"}))
    editor.placeBlock((x+7,y,z),Block("spruce_trapdoor",{"facing":"south","half":"top","open":"true"}))
    editor.placeBlock((x+7,y,z-7),Block("spruce_trapdoor",{"facing":"north","half":"top","open":"true"}))
    for zz in range(4):
        editor.placeBlock((x+2+zz,y,z-1),Block(e_id))
        editor.placeBlock((x+2+zz,y,z-6),Block(e_id))
    for xx in range(4):
        editor.placeBlock((x+1,y,z-2-xx),Block(e_id))
    for xx in range(4):
        for zz in range(5):
            editor.placeBlock((x+2+zz,y,z-2-xx),Block(m_id))
    for xx in range(2):
        editor.placeBlock((x+7,y,z-3-xx),Block("acacia_stairs",{"facing":"west","half":"bottom","shape":"straight"}))


def wall_e(x,y,z,m_id,p_id):
    for zz in range(4):
        for yy in range(4):
            editor.placeBlock((x+2+zz,y+1+yy,z-1),Block(m_id))
            editor.placeBlock((x+2+zz,y+1+yy,z-6),Block(m_id))
    for xx in range(4):
        for yy in range(4):
            editor.placeBlock((x+1,y+1+yy,z-2-xx),Block(m_id))
            editor.placeBlock((x+6,y+1+yy,z-2-xx),Block(m_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((x+6,y+1+yy,z-3-xx),Block("air"))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((x+3+zz,y+2+yy,z-1),Block("glass_pane"))
            editor.placeBlock((x+3+zz,y+2+yy,z-6),Block("glass_pane"))
    #piller
    for xx in range(2):
        for zz in range(2):
            for yy in range(6):
                    editor.placeBlock((x+1+zz*5,y+yy,z-1-xx*5),Block(p_id,{"axis":"y"}))
    for xx in range(4):
        editor.placeBlock((x+1,y+5,z-2-xx),Block(p_id,{"axis":"z"}))
        editor.placeBlock((x+6,y+5,z-2-xx),Block(p_id,{"axis":"z"}))
    for zz in range(4):
        editor.placeBlock((x+2+zz,y+5,z-1),Block(p_id,{"axis":"x"}))
        editor.placeBlock((x+2+zz,y+5,z-6),Block(p_id,{"axis":"x"}))




#roof
def roof_e(x,y,z,s_id,st_id,c_id):
    #ceiling
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x+2+zz,y+5,z-2-xx),Block(c_id))

    #edge
    for zz in range(2):
        editor.placeBlock((x+1+zz,y+5,z),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x+3+zz,y+6,z),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x+5+zz,y+5,z),Block(s_id,{"type":"top"}))

    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x+zz*7,y+5,z-1-xx),Block(s_id,{"type":"top"}))
            editor.placeBlock((x+zz*7,y+6,z-3-xx),Block(s_id,{"type":"bottom"}))
            editor.placeBlock((x+zz*7,y+5,z-5-xx),Block(s_id,{"type":"top"}))


    for zz in range(2):
        editor.placeBlock((x+1+zz,y+5,z-7),Block(s_id,{"type":"top"}))
    for zz in range(2):
        editor.placeBlock((x+3+zz,y+6,z-7),Block(s_id,{"type":"bottom"}))
    for zz in range(2):
        editor.placeBlock((x+5+zz,y+5,z-7),Block(s_id,{"type":"top"}))

#corner
    editor.placeBlock((x,y+6,z),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+7,y+6,z-7),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x,y+6,z-7),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+7,y+6,z),Block(s_id,{"type":"bottom"}))

#middle
    editor.placeBlock((x+1,y+6,z-1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+2,y+6,z-1),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+1,y+6,z-2),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+2,y+6,z-2),Block(st_id,{"facing":"east","half":"bottom","shape":"inner_left"}))

    editor.placeBlock((x+1,y+6,z-6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+1,y+6,z-5),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+2,y+6,z-5),Block(st_id,{"facing":"south","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x+2,y+6,z-6),Block(st_id,{"facing":"east","half":"bottom","shape":"straight"}))

    editor.placeBlock((x+6,y+6,z-6),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+5,y+6,z-5),Block(st_id,{"facing":"west","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x+6,y+6,z-5),Block(st_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+5,y+6,z-6),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))

    editor.placeBlock((x+6,y+6,z-1),Block(s_id,{"type":"bottom"}))
    editor.placeBlock((x+5,y+6,z-1),Block(st_id,{"facing":"west","half":"bottom","shape":"straight"}))
    editor.placeBlock((x+5,y+6,z-2),Block(st_id,{"facing":"north","half":"bottom","shape":"inner_left"}))
    editor.placeBlock((x+6,y+6,z-2),Block(st_id,{"facing":"north","half":"bottom","shape":"straight"}))
    #center
    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x+3+zz,y+7,z-3-xx),Block(s_id,{"type":"bottom"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+3+zz,y+6,z-1-xx),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+1+zz,y+6,z-3-xx),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+5+zz,y+6,z-3-xx),Block(s_id,{"type":"top"}))
    for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+3+zz,y+6,z-5-xx),Block(s_id,{"type":"top"}))
    #light
    editor.placeBlock((x,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+7,y+5,z),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x,y+5,z-7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+7,y+5,z-7),Block("lantern",{"hanging":"true"}))
    editor.placeBlock((x+3,y+6,z-4),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+6,y+7,z-4),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+3,y+7,z-6),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+4,y+7,z-1),Block("lantern",{"hanging":"false"}))
    editor.placeBlock((x+1,y+7,z-3),Block("lantern",{"hanging":"false"}))

def rand_flower():
    flower=["dandelion","poppy","blue_orchid","allium","azure_bluet","red_tulip","orange_tulip","white_tulip","pink_tulip","oxeye_daisy","cornflower","lily_of_the_valley"]
    r=random.randint(0,11)
    return flower[r]

def rand_color():
    rand_c=["white","orange","magenta","light_blue","yellow","lime","pink","gray","light_gray","cyan","purple","blue","brown","green","red","black"]
    c=random.randint(0,15)
    return rand_c[c]


def rand_tool():
    rand_t=["ender_chest","furnace","anvil","loom","smoker","blast_furnace","stonecutter","grindstone"]
    t=random.randint(0,len(rand_t)-1)
    return rand_t[t]


def rand_tool_nof():
    rand_tn=["enchanting_table","jukebox","crafting_table","fletching_table","cartography_table","smithing_table"]
    tn=random.randint(0,len(rand_tn)-1)
    return rand_tn[tn]

#(-53,4,0)

def furniture_s(x,y,z):
    #door
    editor.placeBlock((x+3,y+1,z+6),Block("acacia_door",{"facing":"north","open":"true","hinge":"left"}))
    editor.placeBlock((x+4,y+1,z+6),Block("acacia_door",{"facing":"north","open":"true","hinge":"right"}))

    #bed
    bed_c=rand_color()
    editor.placeBlock((x+2,y+1,z+3),Block(bed_c+"_bed",{"facing":"north"}))
    editor.placeBlock((x+3,y+1,z+3),Block(bed_c+"_bed",{"facing":"north"}))
    #light 
    editor.placeBlock((x+4,y+1,z+2),Block("redstone_lamp"))
    editor.placeBlock((x+4,y+2,z+2),Block("lever",{"face":"floor","facing":"north","powered":"true"}))
    #cartain
    ban_c=rand_color()
    editor.placeBlock((x+5,y+3,z+2),Block(ban_c+"_wall_banner",{"facing":"west"}))
    editor.placeBlock((x+5,y+3,z+5),Block(ban_c+"_wall_banner",{"facing":"west"}))
    editor.placeBlock((x+2,y+3,z+2),Block(ban_c+"_wall_banner",{"facing":"east"}))
    editor.placeBlock((x+2,y+3,z+5),Block(ban_c+"_wall_banner",{"facing":"east"}))

    r=random.randint(0,4)    
    if(r==0):
        editor.placeBlock((x+4,y+1,z+3),Block("bookshelf"))
    elif(r==1):
        editor.placeBlock((x+4,y+1,z+3),Block("oak_stairs",{"facing":"south","half":"top"}))
        editor.placeBlock((x+4,y+2,z+3),Block("potted_"+rand_flower()))
    elif(r==2):
        editor.placeBlock((x+5,y+1,z+2),Block(rand_tool(),{"facing":"south"}))
    elif(r==3):
        editor.placeBlock((x+5,y+1,z+2),Block(rand_tool_nof()))
    else:
        editor.placeBlock((x+5,y+1,z+3),Block("oak_stairs",{"facing":"north","half":"top"}))
        editor.placeBlock((x+5,y+1,z+4),Block("oak_stairs",{"facing":"south","half":"top"}))
        editor.placeBlock((x+5,y+2,z+4),Block("potted_"+rand_flower()))

def furniture_w(x,y,z):
    #door
    editor.placeBlock((x-6,y+1,z+3),Block("acacia_door",{"facing":"east","open":"true","hinge":"left"}))
    editor.placeBlock((x-6,y+1,z+4),Block("acacia_door",{"facing":"east","open":"true","hinge":"right"}))
    #bed
    bed_c=rand_color()
    editor.placeBlock((x-3,y+1,z+2),Block(bed_c+"_bed",{"facing":"east"}))
    editor.placeBlock((x-3,y+1,z+3),Block(bed_c+"_bed",{"facing":"east"}))
    #light 
    editor.placeBlock((x-2,y+1,z+4),Block("redstone_lamp"))
    editor.placeBlock((x-2,y+2,z+4),Block("lever",{"face":"floor","facing":"east","powered":"true"}))
    #cartain
    ban_c=rand_color()
    editor.placeBlock((x-2,y+3,z+5),Block(ban_c+"_wall_banner",{"facing":"north"}))
    editor.placeBlock((x-5,y+3,z+5),Block(ban_c+"_wall_banner",{"facing":"north"}))
    editor.placeBlock((x-2,y+3,z+2),Block(ban_c+"_wall_banner",{"facing":"south"}))
    editor.placeBlock((x-5,y+3,z+2),Block(ban_c+"_wall_banner",{"facing":"south"}))

    r=random.randint(0,4)    
    if(r==0):
        editor.placeBlock((x-3,y+1,z+4),Block("bookshelf"))
    elif(r==1):
        editor.placeBlock((x-3,y+1,z+4),Block("oak_stairs",{"facing":"west","half":"top"}))
        editor.placeBlock((x-3,y+2,z+4),Block("potted_"+rand_flower()))
    elif(r==2):
        editor.placeBlock((x-2,y+1,z+5),Block(rand_tool(),{"facing":"west"}))
    elif(r==3):
        editor.placeBlock((x-2,y+1,z+5),Block(rand_tool_nof()))
    else:
        editor.placeBlock((x-3,y+1,z+5),Block("oak_stairs",{"facing":"east","half":"top"}))
        editor.placeBlock((x-4,y+1,z+5),Block("oak_stairs",{"facing":"west","half":"top"}))
        editor.placeBlock((x-4,y+2,z+5),Block("potted_"+rand_flower()))

def furniture_n(x,y,z):
    #door
    editor.placeBlock((x-3,y+1,z-6),Block("acacia_door",{"facing":"south","open":"true","hinge":"left"}))
    editor.placeBlock((x-4,y+1,z-6),Block("acacia_door",{"facing":"south","open":"true","hinge":"right"}))
    #bed
    bed_c=rand_color()
    editor.placeBlock((x-2,y+1,z-3),Block(bed_c+"_bed",{"facing":"south"}))
    editor.placeBlock((x-3,y+1,z-3),Block(bed_c+"_bed",{"facing":"south"}))
    #light 
    editor.placeBlock((x-4,y+1,z-2),Block("redstone_lamp"))
    editor.placeBlock((x-4,y+2,z-2),Block("lever",{"face":"floor","facing":"south","powered":"true"}))
    #cartain
    ban_c=rand_color()
    editor.placeBlock((x-5,y+3,z-2),Block(ban_c+"_wall_banner",{"facing":"east"}))
    editor.placeBlock((x-5,y+3,z-5),Block(ban_c+"_wall_banner",{"facing":"east"}))
    editor.placeBlock((x-2,y+3,z-2),Block(ban_c+"_wall_banner",{"facing":"west"}))
    editor.placeBlock((x-2,y+3,z-5),Block(ban_c+"_wall_banner",{"facing":"west"}))

    r=random.randint(0,4)    
    if(r==0):
        editor.placeBlock((x-4,y+1,z-3),Block("bookshelf"))
    elif(r==1):
        editor.placeBlock((x-4,y+1,z-3),Block("oak_stairs",{"facing":"north","half":"top"}))
        editor.placeBlock((x-4,y+2,z-3),Block("potted_"+rand_flower()))
    elif(r==2):
        editor.placeBlock((x-5,y+1,z-2),Block(rand_tool(),{"facing":"north"}))
    elif(r==3):
        editor.placeBlock((x-5,y+1,z-2),Block(rand_tool_nof()))
    else:
        editor.placeBlock((x-5,y+1,z-3),Block("oak_stairs",{"facing":"south","half":"top"}))
        editor.placeBlock((x-5,y+1,z-4),Block("oak_stairs",{"facing":"north","half":"top"}))
        editor.placeBlock((x-5,y+2,z-4),Block("potted_"+rand_flower()))


def furniture_e(x,y,z):
    #door
    editor.placeBlock((x+6,y+1,z-3),Block("acacia_door",{"facing":"west","open":"true","hinge":"left"}))
    editor.placeBlock((x+6,y+1,z-4),Block("acacia_door",{"facing":"west","open":"true","hinge":"right"}))
    #bed
    bed_c=rand_color()
    editor.placeBlock((x+3,y+1,z-2),Block(bed_c+"_bed",{"facing":"west"}))
    editor.placeBlock((x+3,y+1,z-3),Block(bed_c+"_bed",{"facing":"west"}))
    #light 
    editor.placeBlock((x+2,y+1,z-4),Block("redstone_lamp"))
    editor.placeBlock((x+2,y+2,z-4),Block("lever",{"face":"floor","facing":"west","powered":"true"}))
    #cartain
    ban_c=rand_color()
    editor.placeBlock((x+2,y+3,z-5),Block(ban_c+"_wall_banner",{"facing":"south"}))
    editor.placeBlock((x+5,y+3,z-5),Block(ban_c+"_wall_banner",{"facing":"south"}))
    editor.placeBlock((x+2,y+3,z-2),Block(ban_c+"_wall_banner",{"facing":"north"}))
    editor.placeBlock((x+5,y+3,z-2),Block(ban_c+"_wall_banner",{"facing":"north"}))

    r=random.randint(0,4)    
    if(r==0):
        editor.placeBlock((x+3,y+1,z-4),Block("bookshelf"))
    elif(r==1):
        editor.placeBlock((x+3,y+1,z-4),Block("oak_stairs",{"facing":"east","half":"top"}))
        editor.placeBlock((x+3,y+2,z-4),Block("potted_"+rand_flower()))
    elif(r==2):
        editor.placeBlock((x+2,y+1,z-5),Block(rand_tool(),{"facing":"east"}))
    elif(r==3):
        editor.placeBlock((x+2,y+1,z-5),Block(rand_tool_nof()))
    else:
        editor.placeBlock((x+3,y+1,z-5),Block("oak_stairs",{"facing":"west","half":"top"}))
        editor.placeBlock((x+4,y+1,z-5),Block("oak_stairs",{"facing":"east","half":"top"}))
        editor.placeBlock((x+4,y+2,z-5),Block("potted_"+rand_flower()))

def rand_build():
    #定義文 ここを替えることで建築の様相を変化できる

    #メイン建材候補(床と壁と天井は同じになるだろう)
    m=["smooth_quartz","birch_planks","jungle_planks","acacia_planks"]
    #柱候補(向き情報を持つブロック)
    p=["stripped_mangrove_log","acacia_log","stripped_spruce_log","stripped_jungle_log","stripped_acacia_log"]
    #屋根1,2(同タイプの建材になる)
    r=["warped","stone_brick","prismarine_brick","dark_prismarine",
    "waxed_weathered_cut_copper","waxed_oxidized_cut_copper"]
    m_id=m[random.randint(0,len(m)-1)]
    p_id=p[random.randint(0,len(p)-1)]
    r_id=r[random.randint(0,len(r)-1)]

    return m_id,p_id,r_id


def smallhouse(x,y,z,facing):
    m_id,p_id,r_id = rand_build()
    s_id=r_id+"_slab"
    st_id=r_id+"_stairs"

    if(facing=="s"):
        small_house_s(x,y,z,m_id,p_id,s_id,st_id)
    elif(facing=="w"):
        small_house_w(x,y,z,m_id,p_id,s_id,st_id)
    elif(facing=="n"):
        small_house_n(x,y,z,m_id,p_id,s_id,st_id)
    elif(facing=="e"):
        small_house_e(x,y,z,m_id,p_id,s_id,st_id)


e_id="cobblestone" #土台

def small_house_s(x,y,z,m_id,p_id,s_id,st_id):
    foundation_s(x,y,z,m_id,e_id)
    wall_s(x,y,z,m_id,p_id)
    roof_s(x,y,z,s_id,st_id,m_id)
    furniture_s(x,y,z)

def small_house_w(x,y,z,m_id,p_id,s_id,st_id):
    foundation_w(x,y,z,m_id,e_id)
    wall_w(x,y,z,m_id,p_id)
    roof_w(x,y,z,s_id,st_id,m_id)
    furniture_w(x,y,z)

def small_house_n(x,y,z,m_id,p_id,s_id,st_id):
    foundation_n(x,y,z,m_id,e_id)
    wall_n(x,y,z,m_id,p_id)
    roof_n(x,y,z,s_id,st_id,m_id)
    furniture_n(x,y,z)

def small_house_e(x,y,z,m_id,p_id,s_id,st_id):
    foundation_e(x,y,z,m_id,e_id)
    wall_e(x,y,z,m_id,p_id)
    roof_e(x,y,z,s_id,st_id,m_id)
    furniture_e(x,y,z)



for i in range(30):
    smallhouse(-48-10*i,4,80,"n")









