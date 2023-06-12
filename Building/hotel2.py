__all__ = []
# __version__

import random
from interfaceUtils import runCommand
from gdpc import Editor, Block, Transform, geometry
 
editor = Editor(buffering=True)



#座標確認用関数
def check_coor(x,y,z):
    command = f"summon minecraft:shulker {x} {y} {z} {{Invulnerable:true,Glowing:true,Silent:true,Tags:[test],NoAI:true,PersistenceRequired:true}}"
    runCommand(command)



def foundation(x,y,z,q_id,w_id,e_id,i_id,r_id,t_id,y_id,u_id):
    for yy in range(3):
        for xx in range(27):
            for zz in range(47):
                editor.placeBlock((x-13+xx,y+yy,z-23+zz),Block(q_id))
        for xx in range(10):
            for zz in range(27):
                editor.placeBlock((x-14-xx,y+yy,z-13+zz),Block(q_id))
                editor.placeBlock((x+14+xx,y+yy,z-13+zz),Block(q_id))
    #z-
    editor.placeBlock((x+4,y+3,z-23),Block(w_id))
    editor.placeBlock((x+9,y+3,z-23),Block(w_id))
    editor.placeBlock((x+13,y+3,z-23),Block(w_id))

    editor.placeBlock((x-4,y+3,z-23),Block(w_id))
    editor.placeBlock((x-9,y+3,z-23),Block(w_id))
    editor.placeBlock((x-13,y+3,z-23),Block(w_id))

    editor.placeBlock((x+4,y+4,z-23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+9,y+4,z-23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+13,y+4,z-23),Block(i_id))
    editor.placeBlock((x+13,y+5,z-23),Block(u_id))

    editor.placeBlock((x-4,y+4,z-23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-9,y+4,z-23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+4,z-23),Block(i_id))
    editor.placeBlock((x-13,y+5,z-23),Block(u_id))
    #z+
    editor.placeBlock((x+4,y+3,z+23),Block(w_id))
    editor.placeBlock((x+9,y+3,z+23),Block(w_id))
    editor.placeBlock((x+13,y+3,z+23),Block(w_id))

    editor.placeBlock((x-4,y+3,z+23),Block(w_id))
    editor.placeBlock((x-9,y+3,z+23),Block(w_id))
    editor.placeBlock((x-13,y+3,z+23),Block(w_id))

    editor.placeBlock((x+4,y+4,z+23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+9,y+4,z+23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+13,y+4,z+23),Block(i_id))
    editor.placeBlock((x+13,y+5,z+23),Block(u_id))


    editor.placeBlock((x-4,y+4,z+23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-9,y+4,z+23),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+4,z+23),Block(i_id))
    editor.placeBlock((x-13,y+5,z+23),Block(u_id))

    for xx in range(4):
        editor.placeBlock((x+5+xx,y+3,z-23),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-5-xx,y+3,z-23),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+5+xx,y+3,z+23),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-5-xx,y+3,z+23),Block(r_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x+10+xx,y+3,z-23),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-10-xx,y+3,z-23),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+10+xx,y+3,z+23),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-10-xx,y+3,z+23),Block(r_id,{"type": "top"}))
    #x-
    editor.placeBlock((x-23,y+3,z+4),Block(w_id))
    editor.placeBlock((x-23,y+3,z+9),Block(w_id))
    editor.placeBlock((x-23,y+3,z+13),Block(w_id))

    editor.placeBlock((x-23,y+3,z-4),Block(w_id))
    editor.placeBlock((x-23,y+3,z-9),Block(w_id))
    editor.placeBlock((x-23,y+3,z-13),Block(w_id))

    editor.placeBlock((x-23,y+4,z+4),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-23,y+4,z+9),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-23,y+4,z+13),Block(i_id))
    editor.placeBlock((x-23,y+5,z+13),Block(u_id))

    editor.placeBlock((x-23,y+4,z-4),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-23,y+4,z-9),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-23,y+4,z-13),Block(i_id))
    editor.placeBlock((x-23,y+5,z-13),Block(u_id))

    #x+
    editor.placeBlock((x+23,y+3,z+4),Block(w_id))
    editor.placeBlock((x+23,y+3,z+9),Block(w_id))
    editor.placeBlock((x+23,y+3,z+13),Block(w_id))

    editor.placeBlock((x+23,y+3,z-4),Block(w_id))
    editor.placeBlock((x+23,y+3,z-9),Block(w_id))
    editor.placeBlock((x+23,y+3,z-13),Block(w_id))

    editor.placeBlock((x+23,y+4,z+4),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+23,y+4,z+9),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+23,y+4,z+13),Block(i_id))
    editor.placeBlock((x+23,y+5,z+13),Block(u_id))

    editor.placeBlock((x+23,y+4,z-4),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+23,y+4,z-9),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+23,y+4,z-13),Block(i_id))
    editor.placeBlock((x+23,y+5,z-13),Block(u_id))

    for zz in range(4):
        editor.placeBlock((x-23,y+3,z+5+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-23,y+3,z-5-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+23,y+3,z+5+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+23,y+3,z+-5-zz),Block(r_id,{"type": "top"}))
    for zz in range(3):
        editor.placeBlock((x+23,y+3,z+10+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+23,y+3,z-10-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-23,y+3,z+10+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-23,y+3,z-10-zz),Block(r_id,{"type": "top"}))

    editor.placeBlock((x-13,y+3,z-13),Block(w_id))
    editor.placeBlock((x-13,y+4,z-13),Block(i_id))
    editor.placeBlock((x-13,y+5,z-13),Block(u_id))
    editor.placeBlock((x-18,y+3,z-13),Block(w_id))
    editor.placeBlock((x-18,y+4,z-13),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+3,z-18),Block(w_id))
    editor.placeBlock((x-13,y+4,z-18),Block(e_id,{"type": "bottom"}))

    editor.placeBlock((x+13,y+3,z-13),Block(w_id))
    editor.placeBlock((x+13,y+4,z-13),Block(i_id))
    editor.placeBlock((x+13,y+5,z-13),Block(u_id))
    editor.placeBlock((x+18,y+3,z-13),Block(w_id))
    editor.placeBlock((x+18,y+4,z-13),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+13,y+3,z-18),Block(w_id))
    editor.placeBlock((x+13,y+4,z-18),Block(e_id,{"type": "bottom"}))

    editor.placeBlock((x-13,y+3,z+13),Block(w_id))
    editor.placeBlock((x-13,y+4,z+13),Block(i_id))
    editor.placeBlock((x-13,y+5,z+13),Block(u_id))
    editor.placeBlock((x-18,y+3,z+13),Block(w_id))
    editor.placeBlock((x-18,y+4,z+13),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+3,z+18),Block(w_id))
    editor.placeBlock((x-13,y+4,z+18),Block(e_id,{"type": "bottom"}))

    editor.placeBlock((x+13,y+3,z+13),Block(w_id))
    editor.placeBlock((x+13,y+4,z+13),Block(i_id))
    editor.placeBlock((x+13,y+5,z+13),Block(u_id))
    editor.placeBlock((x+18,y+3,z+13),Block(w_id))
    editor.placeBlock((x+18,y+4,z+13),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x+13,y+3,z+18),Block(w_id))
    editor.placeBlock((x+13,y+4,z+18),Block(e_id,{"type": "bottom"}))

    for xx in range(4):
        editor.placeBlock((x-14-xx,y+3,z-13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-19-xx,y+3,z-13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-14-xx,y+3,z+13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-19-xx,y+3,z+13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+14+xx,y+3,z-13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+19+xx,y+3,z-13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+14+xx,y+3,z+13),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+19+xx,y+3,z+13),Block(r_id,{"type": "top"}))

        editor.placeBlock((x-5-xx,y+2,z+19),Block(w_id))
        editor.placeBlock((x-5-xx,y+2,z-19),Block(w_id))
        editor.placeBlock((x+5+xx,y+2,z+19),Block(w_id))
        editor.placeBlock((x+5+xx,y+2,z-19),Block(w_id))
        editor.placeBlock((x+10+xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x+15+xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x-10-xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x-15-xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x+10+xx,y+2,z-9),Block(w_id))
        editor.placeBlock((x+15+xx,y+2,z-9),Block(w_id))
        editor.placeBlock((x-10-xx,y+2,z-9),Block(w_id))
        editor.placeBlock((x-15-xx,y+2,z-9),Block(w_id))
    for zz in range(4):
        editor.placeBlock((x-13,y+3,z-14-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-13,y+3,z-19-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-13,y+3,z+14+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x-13,y+3,z+19+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+13,y+3,z-14-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+13,y+3,z-19-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+13,y+3,z+14+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+13,y+3,z+19+zz),Block(r_id,{"type": "top"}))

        editor.placeBlock((x+19,y+2,z-5-zz),Block(w_id))
        editor.placeBlock((x-19,y+2,z-5-zz),Block(w_id))
        editor.placeBlock((x+19,y+2,z+5+zz),Block(w_id))
        editor.placeBlock((x-19,y+2,z+5+zz),Block(w_id))
        editor.placeBlock((x+9,y+2,z+10+zz),Block(w_id))
        editor.placeBlock((x+9,y+2,z+15+zz),Block(w_id))
        editor.placeBlock((x+9,y+2,z-10-zz),Block(w_id))
        editor.placeBlock((x+9,y+2,z-15-zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z+10+zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z+15+zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z-10-zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z-15-zz),Block(w_id))
    for xx in range(7):
        editor.placeBlock((x-3+xx,y+2,z-24),Block(y_id,{"facing": "south", "half": "bottom"}))
        editor.placeBlock((x-3+xx,y+1,z-25),Block(y_id,{"facing": "south", "half": "bottom"}))
        editor.placeBlock((x-3+xx,y,z-26),Block(y_id,{"facing": "south", "half": "bottom"}))

        for yy in range(2):
            editor.placeBlock((x-3+xx,y+yy,z-24),Block(t_id))
        editor.placeBlock((x-3+xx,y,z-25),Block(t_id))

    for xx in range(7):
        editor.placeBlock((x-3+xx,y+2,z+24),Block(y_id,{"facing": "north", "half": "bottom"}))
        editor.placeBlock((x-3+xx,y+1,z+25),Block(y_id,{"facing": "north", "half": "bottom"}))
        editor.placeBlock((x-3+xx,y,z+26),Block(y_id,{"facing": "north", "half": "bottom"}))

        editor.placeBlock((x-3+xx,y+2,z+19),Block(w_id))
        editor.placeBlock((x-3+xx,y+2,z-19),Block(w_id))
        for yy in range(2):
            editor.placeBlock((x-3+xx,y+yy,z+24),Block(t_id))
        editor.placeBlock((x-3+xx,y,z+25),Block(t_id))

    for zz in range(7):
        editor.placeBlock((x+24,y+2,z-3+zz),Block(y_id,{"facing": "west", "half": "bottom"}))
        editor.placeBlock((x+25,y+1,z-3+zz),Block(y_id,{"facing": "west", "half": "bottom"}))
        editor.placeBlock((x+26,y,z-3+zz),Block(y_id,{"facing": "west", "half": "bottom"}))

        editor.placeBlock((x+19,y+2,z-3+zz),Block(w_id))
        editor.placeBlock((x-19,y+2,z-3+zz),Block(w_id))
        for yy in range(2):
            editor.placeBlock((x+24,y+yy,z-3+zz),Block(t_id))
        editor.placeBlock((x+25,y,z-3+zz),Block(t_id))

    for zz in range(7):
        editor.placeBlock((x-24,y+2,z-3+zz),Block(y_id,{"facing": "east", "half": "bottom"}))
        editor.placeBlock((x-25,y+1,z-3+zz),Block(y_id,{"facing": "east", "half": "bottom"}))
        editor.placeBlock((x-26,y,z-3+zz),Block(y_id,{"facing": "east", "half": "bottom"}))
        for yy in range(2):
            editor.placeBlock((x-24,y+yy,z-3+zz),Block(t_id))
        editor.placeBlock((x-25,y,z-3+zz),Block(t_id))

    for yy in range(3):
        editor.placeBlock((x-4,y+yy,z-24),Block(t_id))
        editor.placeBlock((x+4,y+yy,z-24),Block(t_id))
        editor.placeBlock((x-4,y+yy,z+24),Block(t_id))
        editor.placeBlock((x+4,y+yy,z+24),Block(t_id))
        editor.placeBlock((x-24,y+yy,z-4),Block(t_id))
        editor.placeBlock((x-24,y+yy,z+4),Block(t_id))
        editor.placeBlock((x+24,y+yy,z-4),Block(t_id))
        editor.placeBlock((x+24,y+yy,z+4),Block(t_id))
    for yy in range(2):
        editor.placeBlock((x-4,y+yy,z-25),Block(t_id))
        editor.placeBlock((x+4,y+yy,z-25),Block(t_id))
        editor.placeBlock((x-4,y+yy,z+25),Block(t_id))
        editor.placeBlock((x+4,y+yy,z+25),Block(t_id))
        editor.placeBlock((x-25,y+yy,z-4),Block(t_id))
        editor.placeBlock((x-25,y+yy,z+4),Block(t_id))
        editor.placeBlock((x+25,y+yy,z-4),Block(t_id))
        editor.placeBlock((x+25,y+yy,z+4),Block(t_id))
    editor.placeBlock((x-4,y,z-26),Block(t_id))
    editor.placeBlock((x+4,y,z-26),Block(t_id))
    editor.placeBlock((x-4,y,z+26),Block(t_id))
    editor.placeBlock((x+4,y,z+26),Block(t_id))
    editor.placeBlock((x-26,y,z-4),Block(t_id))
    editor.placeBlock((x-26,y,z+4),Block(t_id))
    editor.placeBlock((x+26,y,z-4),Block(t_id))
    editor.placeBlock((x+26,y,z+4),Block(t_id))

    editor.placeBlock((x-4,y+1,z-26),Block(u_id))
    editor.placeBlock((x+4,y+1,z-26),Block(u_id))
    editor.placeBlock((x-4,y+1,z+26),Block(u_id))
    editor.placeBlock((x+4,y+1,z+26),Block(u_id))
    editor.placeBlock((x-26,y+1,z-4),Block(u_id))
    editor.placeBlock((x-26,y+1,z+4),Block(u_id))
    editor.placeBlock((x+26,y+1,z-4),Block(u_id))
    editor.placeBlock((x+26,y+1,z+4),Block(u_id))

    editor.placeBlock((x-4,y+2,z-25),Block(u_id))
    editor.placeBlock((x+4,y+2,z-25),Block(u_id))
    editor.placeBlock((x-4,y+2,z+25),Block(u_id))
    editor.placeBlock((x+4,y+2,z+25),Block(u_id))
    editor.placeBlock((x-25,y+2,z-4),Block(u_id))
    editor.placeBlock((x-25,y+2,z+4),Block(u_id))
    editor.placeBlock((x+25,y+2,z-4),Block(u_id))
    editor.placeBlock((x+25,y+2,z+4),Block(u_id))

    editor.placeBlock((x-4,y+3,z-24),Block(u_id))
    editor.placeBlock((x+4,y+3,z-24),Block(u_id))
    editor.placeBlock((x-4,y+3,z+24),Block(u_id))
    editor.placeBlock((x+4,y+3,z+24),Block(u_id))
    editor.placeBlock((x-24,y+3,z-4),Block(u_id))
    editor.placeBlock((x-24,y+3,z+4),Block(u_id))
    editor.placeBlock((x+24,y+3,z-4),Block(u_id))
    editor.placeBlock((x+24,y+3,z+4),Block(u_id))

    for xx in range(17):
        for zz in range(37):
            editor.placeBlock((x-8+xx,y+2,z-18+zz),Block(t_id))
    for xx in range(10):
        for zz in range(17):
            editor.placeBlock((x+9+xx,y+2,z-8+zz),Block(t_id))
            editor.placeBlock((x-9-xx,y+2,z-8+zz),Block(t_id))
    for xx in range(7):
        editor.placeBlock((x-3+xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x-3+xx,y+2,z-9),Block(w_id))
    for zz in range(7):
        editor.placeBlock((x+9,y+2,z-3+zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z-3+zz),Block(w_id))
    for xx in range(4):
        editor.placeBlock((x-5-xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x-5-xx,y+2,z-9),Block(w_id))
        editor.placeBlock((x+5+xx,y+2,z+9),Block(w_id))
        editor.placeBlock((x+5+xx,y+2,z-9),Block(w_id))
    for zz in range(4):
        editor.placeBlock((x+9,y+2,z+5+zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z+5+zz),Block(w_id))
        editor.placeBlock((x+9,y+2,z-5-zz),Block(w_id))
        editor.placeBlock((x-9,y+2,z-5-zz),Block(w_id))


# ��
def pillar(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for zz in range(3):
        editor.placeBlock((x+4,y,z-9-5*zz),Block(q_id))
        editor.placeBlock((x+9,y,z-9-5*zz),Block(q_id))
        editor.placeBlock((x-4,y,z-9-5*zz),Block(q_id))
        editor.placeBlock((x-9,y,z-9-5*zz),Block(q_id))
        editor.placeBlock((x+4,y,z+9+5*zz),Block(q_id))
        editor.placeBlock((x+9,y,z+9+5*zz),Block(q_id))
        editor.placeBlock((x-4,y,z+9+5*zz),Block(q_id))
        editor.placeBlock((x-9,y,z+9+5*zz),Block(q_id))
    for xx in range(3):
        editor.placeBlock((x-9-5*xx,y,z+4),Block(q_id))
        editor.placeBlock((x-9-5*xx,y,z+9),Block(q_id))
        editor.placeBlock((x-9-5*xx,y,z-4),Block(q_id))
        editor.placeBlock((x-9-5*xx,y,z-9),Block(q_id))
        editor.placeBlock((x+9+5*xx,y,z+4),Block(q_id))
        editor.placeBlock((x+9+5*xx,y,z+9),Block(q_id))
        editor.placeBlock((x+9+5*xx,y,z-4),Block(q_id))
        editor.placeBlock((x+9+5*xx,y,z-9),Block(q_id))

    

    for xx in range(17):
        for zz in range(2):
            editor.placeBlock((x-8+xx,y+7,z+14+5*zz),Block(w_id))
            editor.placeBlock((x-8+xx,y+7,z-14-5*zz),Block(w_id))
    for xx in range(37):
        for zz in range(2):
            editor.placeBlock((x-18+xx,y+7,z-4-5*zz),Block(w_id))
            editor.placeBlock((x-18+xx,y+7,z+4+5*zz),Block(w_id))
    for zz in range(17):
        for xx in range(2):
            editor.placeBlock((x+14+5*xx,y+7,z-8+zz),Block(w_id))
            editor.placeBlock((x-14-5*xx,y+7,z-8+zz),Block(w_id))
    for zz in range(37):
        for xx in range(2):
            editor.placeBlock((x-4-5*xx,y+7,z-18+zz),Block(w_id))
            editor.placeBlock((x+4+5*xx,y+7,z-18+zz),Block(w_id))

    for xx in range(17):
        for zz in range(2):
            editor.placeBlock((x-8+xx,y+8,z+14+5*zz),Block(e_id))
            editor.placeBlock((x-8+xx,y+8,z-14-5*zz),Block(e_id))
    for xx in range(37):
        for zz in range(2):
            editor.placeBlock((x-18+xx,y+8,z-4-5*zz),Block(e_id))
            editor.placeBlock((x-18+xx,y+8,z+4+5*zz),Block(e_id))
    for zz in range(17):
        for xx in range(2):
            editor.placeBlock((x+14+5*xx,y+8,z-8+zz),Block(e_id))
            editor.placeBlock((x-14-5*xx,y+8,z-8+zz),Block(e_id))
    for zz in range(37):
        for xx in range(2):
            editor.placeBlock((x-4-5*xx,y+8,z-18+zz),Block(e_id))
            editor.placeBlock((x+4+5*xx,y+8,z-18+zz),Block(e_id))
    
    for yy in range(8):
            for zz in range(3):
                editor.placeBlock((x+4,y+1+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x+9,y+1+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x-4,y+1+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x-9,y+1+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x+4,y+1+yy,z+9+5*zz),Block(w_id))
                editor.placeBlock((x+9,y+1+yy,z+9+5*zz),Block(w_id))
                editor.placeBlock((x-4,y+1+yy,z+9+5*zz),Block(w_id))
                editor.placeBlock((x-9,y+1+yy,z+9+5*zz),Block(w_id))
            for xx in range(3):
                editor.placeBlock((x-9-5*xx,y+1+yy,z+4),Block(w_id))
                editor.placeBlock((x-9-5*xx,y+1+yy,z+9),Block(w_id))
                editor.placeBlock((x-9-5*xx,y+1+yy,z-4),Block(w_id))
                editor.placeBlock((x-9-5*xx,y+1+yy,z-9),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+1+yy,z+4),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+1+yy,z+9),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+1+yy,z-4),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+1+yy,z-9),Block(w_id))

    for xx in range(21):
        for zz in range(2):
            editor.placeBlock((x-10+xx,y+9,z+14+5*zz),Block(w_id))
            editor.placeBlock((x-10+xx,y+9,z-14-5*zz),Block(w_id))
    for xx in range(41):
        for zz in range(2):
            editor.placeBlock((x-20+xx,y+9,z-4-5*zz),Block(w_id))
            editor.placeBlock((x-20+xx,y+9,z+4+5*zz),Block(w_id))
    for zz in range(21):
        for xx in range(2):
            editor.placeBlock((x+14+5*xx,y+9,z-10+zz),Block(w_id))
            editor.placeBlock((x-14-5*xx,y+9,z-10+zz),Block(w_id))
    for zz in range(41):
        for xx in range(2):
            editor.placeBlock((x-4-5*xx,y+9,z-20+zz),Block(w_id))
            editor.placeBlock((x+4+5*xx,y+9,z-20+zz),Block(w_id))

    for xx in range(7):
        for zz in range(4):
            for zzz in range(3):
                editor.placeBlock((x-3+xx,y+10,z-5-zz-5*zzz),Block(r_id))
                editor.placeBlock((x-3+xx,y+10,z+5+zz+5*zzz),Block(r_id))
    for zz in range(7):
        for xx in range(4):
            for xxx in range(2):
                editor.placeBlock((x-10-xx-5*xxx,y+10,z-3+zz),Block(r_id))
                editor.placeBlock((x+10+xx+5*xxx,y+10,z-3+zz),Block(r_id))

    for xx in range(4):
        for zz in range(4):
            for zzz in range(3):
                editor.placeBlock((x+5+xx,y+10,z-5-zz-5*zzz),Block(r_id))
                editor.placeBlock((x-5-xx,y+10,z-5-zz-5*zzz),Block(r_id))
                editor.placeBlock((x+5+xx,y+10,z+5+zz+5*zzz),Block(r_id))
                editor.placeBlock((x-5-xx,y+10,z+5+zz+5*zzz),Block(r_id))
    for zz in range(4):
        for xx in range(4):
            for xxx in range(2):
                editor.placeBlock((x+10+xx+5*xxx,y+10,z+5+zz),Block(r_id))
                editor.placeBlock((x+10+xx+5*xxx,y+10,z-5-zz),Block(r_id))
                editor.placeBlock((x-10-xx-5*xxx,y+10,z+5+zz),Block(r_id))
                editor.placeBlock((x-10-xx-5*xxx,y+10,z-5-zz),Block(r_id))

    for xx in range(7):
        for zz in range(7):
            editor.placeBlock((x-3+xx,y+10,z-3+zz),Block(r_id))
    for xx in range(3):
        editor.placeBlock((x-1+xx,y+10,z+2),Block(t_id))
        editor.placeBlock((x-1+xx,y+10,z-2),Block(t_id))
    for zz in range(3):
        editor.placeBlock((x+2,y+10,z-1+zz),Block(t_id))
        editor.placeBlock((x-2,y+10,z-1+zz),Block(t_id))

    editor.placeBlock((x+2,y+9,z+2),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x+3,y+9,z+3),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x-2,y+9,z-2),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x-3,y+9,z-3),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x+2,y+9,z-2),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x+3,y+9,z-3),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x-2,y+9,z+2),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x-3,y+9,z+3),Block(y_id,{"facing": "west", "half": "top", "open": "false"}))
    editor.placeBlock((x+2,y+11,z+2),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x+3,y+11,z+3),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x-2,y+11,z-2),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x-3,y+11,z-3),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x+2,y+11,z-2),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x+3,y+11,z-3),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x-2,y+11,z+2),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))
    editor.placeBlock((x-3,y+11,z+3),Block(y_id,{"facing": "west", "half": "bottom", "open": "false"}))

    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x+5+xx,y+10,z+5+zz),Block(u_id))
            editor.placeBlock((x-5-xx,y+10,z+5+zz),Block(u_id))

    for yy in range(4):
            for zz in range(3):
                editor.placeBlock((x+4,y+10+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x+9,y+10+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x-4,y+10+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x-9,y+10+yy,z-9-5*zz),Block(w_id))
                editor.placeBlock((x+4,y+10+yy,z+9+5*zz),Block(w_id))
                editor.placeBlock((x+9,y+10+yy,z+9+5*zz),Block(w_id))
                editor.placeBlock((x-4,y+10+yy,z+9+5*zz),Block(w_id))
                editor.placeBlock((x-9,y+10+yy,z+9+5*zz),Block(w_id))
            for xx in range(3):
                editor.placeBlock((x-9-5*xx,y+10+yy,z+4),Block(w_id))
                editor.placeBlock((x-9-5*xx,y+10+yy,z+9),Block(w_id))
                editor.placeBlock((x-9-5*xx,y+10+yy,z-4),Block(w_id))
                editor.placeBlock((x-9-5*xx,y+10+yy,z-9),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+10+yy,z+4),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+10+yy,z+9),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+10+yy,z-4),Block(w_id))
                editor.placeBlock((x+9+5*xx,y+10+yy,z-9),Block(w_id))

#storey
def storey(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for xx in range(19):
        for zz in range(39):
            editor.placeBlock((x-9+xx,y,z-19+zz),Block(w_id))
    for xx in range(10):
        for zz in range(19):
            editor.placeBlock((x+10+xx,y,z-9+zz),Block(w_id))
            editor.placeBlock((x-10-xx,y,z-9+zz),Block(w_id))

    for xx in range(2):
        editor.placeBlock((x-19+38*xx,y+1,z-4),Block(e_id))
        editor.placeBlock((x-19+38*xx,y+1,z+4),Block(e_id))
        editor.placeBlock((x-19+38*xx,y+2,z-4),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x-19+38*xx,y+2,z+4),Block(r_id,{"type": "bottom"}))
    for zz in range(2):
        editor.placeBlock((x-4,y+1,z-19+38*zz),Block(e_id))
        editor.placeBlock((x+4,y+1,z-19+38*zz),Block(e_id))
        editor.placeBlock((x-4,y+2,z-19+38*zz),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+4,y+2,z-19+38*zz),Block(r_id,{"type": "bottom"}))
    for zz in range(3):
        for xx in range(2):
            editor.placeBlock((x-9+18*xx,y+1,z-9-5*zz),Block(e_id))
            editor.placeBlock((x-9+18*xx,y+1,z+9+5*zz),Block(e_id))
            editor.placeBlock((x-9+18*xx,y+2,z-9-5*zz),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-9+18*xx,y+2,z+9+5*zz),Block(r_id,{"type": "bottom"}))
    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x-14-5*xx,y+1,z-9+18*zz),Block(e_id))
            editor.placeBlock((x+14+5*xx,y+1,z-9+18*zz),Block(e_id))
            editor.placeBlock((x-14-5*xx,y+2,z-9+18*zz),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+14+5*xx,y+2,z-9+18*zz),Block(r_id,{"type": "bottom"}))

    for xx in range(2):
        for zz in range(7):
            editor.placeBlock((x-19+38*xx,y+1,z-3+zz),Block(t_id,{"type": "top"}))
        for zz in range(4):
            editor.placeBlock((x-19+38*xx,y+1,z-8+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-19+38*xx,y+1,z+5+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z-18+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z-13+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z+10+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z+15+zz),Block(t_id,{"type": "top"}))
    for zz in range(2):
        for xx in range(7):
            editor.placeBlock((x-3+xx,y+1,z-19+38*zz),Block(t_id,{"type": "top"}))
        for xx in range(4):
            editor.placeBlock((x-8+xx,y+1,z-19+38*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+5+xx,y+1,z-19+38*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-18+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-13+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+10+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+15+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
    editor.placeBlock((x-19,y+1,z),Block(t_id,{"type": "double"}))

    editor.placeBlock((x+19,y+1,z),Block(t_id,{"type": "double"}))
    editor.placeBlock((x,y+1,z+19),Block(t_id,{"type": "double"}))
    editor.placeBlock((x,y+1,z-19),Block(t_id,{"type": "double"}))

    for zz in range(2):
        for xx in range(2):
            editor.placeBlock((x+3+3*xx,y+1,z-11-5*zz),Block(q_id))
            editor.placeBlock((x-3-3*xx,y+1,z-11-5*zz),Block(q_id))
            editor.placeBlock((x+3+3*xx,y+1,z+11+5*zz),Block(q_id))
            editor.placeBlock((x-3-3*xx,y+1,z+11+5*zz),Block(q_id))
            editor.placeBlock((x-11-5*xx,y+1,z-3-3*zz),Block(q_id))
            editor.placeBlock((x+11+5*xx,y+1,z-3-3*zz),Block(q_id))
            editor.placeBlock((x-11-5*xx,y+1,z+3+3*zz),Block(q_id))
            editor.placeBlock((x+11+5*xx,y+1,z+3+3*zz),Block(q_id))
    editor.placeBlock((x-6,y+1,z-6),Block(q_id))
    editor.placeBlock((x-6,y+1,z+6),Block(q_id))
    editor.placeBlock((x+6,y+1,z+6),Block(q_id))
    editor.placeBlock((x+6,y+1,z-6),Block(q_id))
    

    for zz in range(2):
        for xx in range(13):
            editor.placeBlock((x-6+xx,y+6,z-11-5*zz),Block(w_id))
            editor.placeBlock((x-6+xx,y+6,z+11+5*zz),Block(w_id))
        for xx in range(11):
            editor.placeBlock((x-6-xx,y+6,z-3+6*zz),Block(w_id))
            editor.placeBlock((x+6+xx,y+6,z-3+6*zz),Block(w_id))
        for xx in range(33):
            editor.placeBlock((x-16+xx,y+6,z-6+12*zz),Block(w_id))
    for xx in range(2):
        for zz in range(13):
            editor.placeBlock((x-11-5*xx,y+6,z-6+zz),Block(w_id))
            editor.placeBlock((x+11+5*xx,y+6,z-6+zz),Block(w_id))
        for zz in range(11):
            editor.placeBlock((x-3+6*xx,y+6,z-6-zz),Block(w_id))
            editor.placeBlock((x-3+6*xx,y+6,z+6+zz),Block(w_id))
        for zz in range(33):
            editor.placeBlock((x-6+12*xx,y+6,z-16+zz),Block(w_id))

    for xx in range(2):
        for zz in range(13):
            editor.placeBlock((x-16+32*xx,y+7,z-6+zz),Block(y_id))
        for zz in range(11):
            editor.placeBlock((x-6+12*xx,y+7,z+6+zz),Block(y_id))
            editor.placeBlock((x-6+12*xx,y+7,z-6-zz),Block(y_id))
    for zz in range(2):
        for xx in range(13):
            editor.placeBlock((x-6+xx,y+7,z-16+32*zz),Block(y_id))
        for xx in range(11):
            editor.placeBlock((x-6-xx,y+7,z-6+12*zz),Block(y_id))
            editor.placeBlock((x+6+xx,y+7,z-6+12*zz),Block(y_id))

    for yy in range(6):
        for zz in range(2):
            for xx in range(2):
                editor.placeBlock((x+3+3*xx,y+2+yy,z-11-5*zz),Block(w_id))
                editor.placeBlock((x-3-3*xx,y+2+yy,z-11-5*zz),Block(w_id))
                editor.placeBlock((x+3+3*xx,y+2+yy,z+11+5*zz),Block(w_id))
                editor.placeBlock((x-3-3*xx,y+2+yy,z+11+5*zz),Block(w_id))
                editor.placeBlock((x-11-5*xx,y+2+yy,z-3-3*zz),Block(w_id))
                editor.placeBlock((x+11+5*xx,y+2+yy,z-3-3*zz),Block(w_id))
                editor.placeBlock((x-11-5*xx,y+2+yy,z+3+3*zz),Block(w_id))
                editor.placeBlock((x+11+5*xx,y+2+yy,z+3+3*zz),Block(w_id))
        editor.placeBlock((x-6,y+2+yy,z-6),Block(w_id))
        editor.placeBlock((x-6,y+2+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+2+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+2+yy,z-6),Block(w_id))

    for zz in range(2):
        for xx in range(15):
            editor.placeBlock((x-7+xx,y+8,z-11-5*zz),Block(w_id))
            editor.placeBlock((x-7+xx,y+8,z+11+5*zz),Block(w_id))
        for xx in range(12):
            editor.placeBlock((x-6-xx,y+8,z-3+6*zz),Block(w_id))
            editor.placeBlock((x+6+xx,y+8,z-3+6*zz),Block(w_id))
        for xx in range(35):
            editor.placeBlock((x-17+xx,y+8,z-6+12*zz),Block(w_id))
    for xx in range(2):
        for zz in range(15):
            editor.placeBlock((x-11-5*xx,y+8,z-7+zz),Block(w_id))
            editor.placeBlock((x+11+5*xx,y+8,z-7+zz),Block(w_id))
        for zz in range(12):
            editor.placeBlock((x-3+6*xx,y+8,z-6-zz),Block(w_id))
            editor.placeBlock((x-3+6*xx,y+8,z+6+zz),Block(w_id))
        for zz in range(35):
            editor.placeBlock((x-6+12*xx,y+8,z-17+zz),Block(w_id))
    for xx in range(11):
        for zz in range(2):
            editor.placeBlock((x-5+xx,y+8,z-3+6*zz),Block(w_id))
    for xx in range(2):
        for zz in range(11):
            editor.placeBlock((x-3+6*xx,y+8,z-5+zz),Block(w_id))

    for yy in range(6):
        for zz in range(2):
            for xx in range(2):
                editor.placeBlock((x+3+3*xx,y+9+yy,z-6-10*zz),Block(w_id))
                editor.placeBlock((x-3-3*xx,y+9+yy,z-6-10*zz),Block(w_id))
                editor.placeBlock((x+3+3*xx,y+9+yy,z+6+10*zz),Block(w_id))
                editor.placeBlock((x-3-3*xx,y+9+yy,z+6+10*zz),Block(w_id))
                editor.placeBlock((x-6-10*xx,y+9+yy,z-3-3*zz),Block(w_id))
                editor.placeBlock((x+6+10*xx,y+9+yy,z-3-3*zz),Block(w_id))
                editor.placeBlock((x-6-10*xx,y+9+yy,z+3+3*zz),Block(w_id))
                editor.placeBlock((x+6+10*xx,y+9+yy,z+3+3*zz),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z-6),Block(w_id))

    for xx in range(2):
        for zz in range(11):
            editor.placeBlock((x-16+32*xx,y+13,z-5+zz),Block(y_id))
            editor.placeBlock((x-16+32*xx,y+12,z-5+zz),Block(w_id))
        for zz in range(9):
            editor.placeBlock((x-6+12*xx,y+13,z+7+zz),Block(y_id))
            editor.placeBlock((x-6+12*xx,y+13,z-7-zz),Block(y_id))
            editor.placeBlock((x-6+12*xx,y+12,z+7+zz),Block(w_id))
            editor.placeBlock((x-6+12*xx,y+12,z-7-zz),Block(w_id))
    for zz in range(2):
        for xx in range(11):
            editor.placeBlock((x-5+xx,y+13,z-16+32*zz),Block(y_id))
            editor.placeBlock((x-5+xx,y+12,z-16+32*zz),Block(w_id))
        for xx in range(9):
            editor.placeBlock((x+7+xx,y+13,z-6+12*zz),Block(y_id))
            editor.placeBlock((x-7-xx,y+13,z-6+12*zz),Block(y_id))
            editor.placeBlock((x+7+xx,y+12,z-6+12*zz),Block(w_id))
            editor.placeBlock((x-7-xx,y+12,z-6+12*zz),Block(w_id))
    editor.placeBlock((x,y+13,z+16),Block(w_id))
    editor.placeBlock((x,y+13,z+17),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x,y+13,z-16),Block(w_id))
    editor.placeBlock((x,y+13,z-17),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x+16,y+13,z),Block(w_id))
    editor.placeBlock((x+17,y+13,z),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x-16,y+13,z),Block(w_id))
    editor.placeBlock((x-17,y+13,z),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x-11,y+13,z+6),Block(w_id))
    editor.placeBlock((x-11,y+13,z-6),Block(w_id))
    editor.placeBlock((x+11,y+13,z+6),Block(w_id))
    editor.placeBlock((x+11,y+13,z-6),Block(w_id))
    editor.placeBlock((x-6,y+13,z-11),Block(w_id))
    editor.placeBlock((x-6,y+13,z+11),Block(w_id))
    editor.placeBlock((x+6,y+13,z+11),Block(w_id))
    editor.placeBlock((x+6,y+13,z-11),Block(w_id))
    
    editor.placeBlock((x+3,y+9,z+11),Block(u_id))
    editor.placeBlock((x-3,y+9,z+11),Block(u_id))
    editor.placeBlock((x-3,y+9,z-11),Block(u_id))
    editor.placeBlock((x+3,y+9,z-11),Block(u_id))

    editor.placeBlock((x+3,y+9,z+3),Block(u_id))
    editor.placeBlock((x-3,y+9,z+3),Block(u_id))
    editor.placeBlock((x-3,y+9,z-3),Block(u_id))
    editor.placeBlock((x+3,y+9,z-3),Block(u_id))

    editor.placeBlock((x+11,y+9,z+3),Block(u_id))
    editor.placeBlock((x-11,y+9,z+3),Block(u_id))
    editor.placeBlock((x-11,y+9,z-3),Block(u_id))
    editor.placeBlock((x+11,y+9,z-3),Block(u_id))

    editor.placeBlock((x+6,y+9,z+11),Block(u_id))
    editor.placeBlock((x-6,y+9,z+11),Block(u_id))
    editor.placeBlock((x-6,y+9,z-11),Block(u_id))
    editor.placeBlock((x+6,y+9,z-11),Block(u_id))

    editor.placeBlock((x+11,y+9,z+6),Block(u_id))
    editor.placeBlock((x-11,y+9,z+6),Block(u_id))
    editor.placeBlock((x-11,y+9,z-6),Block(u_id))
    editor.placeBlock((x+11,y+9,z-6),Block(u_id))

    editor.placeBlock((x+3,y+7,z+6),Block(u_id))
    editor.placeBlock((x-3,y+7,z+6),Block(u_id))
    editor.placeBlock((x-3,y+7,z-6),Block(u_id))
    editor.placeBlock((x+3,y+7,z-6),Block(u_id))

    editor.placeBlock((x+6,y+7,z+3),Block(u_id))
    editor.placeBlock((x-6,y+7,z+3),Block(u_id))
    editor.placeBlock((x-6,y+7,z-3),Block(u_id))
    editor.placeBlock((x+6,y+7,z-3),Block(u_id))
#storey4
def storey4(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for xx in range(19):
        for zz in range(39):
            editor.placeBlock((x-9+xx,y,z-19+zz),Block(w_id))
    for xx in range(10):
        for zz in range(19):
            editor.placeBlock((x+10+xx,y,z-9+zz),Block(w_id))
            editor.placeBlock((x-10-xx,y,z-9+zz),Block(w_id))

    for xx in range(2):
        editor.placeBlock((x-19+38*xx,y+1,z-4),Block(e_id))
        editor.placeBlock((x-19+38*xx,y+1,z+4),Block(e_id))
        editor.placeBlock((x-19+38*xx,y+2,z-4),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x-19+38*xx,y+2,z+4),Block(r_id,{"type": "bottom"}))
    for zz in range(2):
        editor.placeBlock((x-4,y+1,z-19+38*zz),Block(e_id))
        editor.placeBlock((x+4,y+1,z-19+38*zz),Block(e_id))
        editor.placeBlock((x-4,y+2,z-19+38*zz),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+4,y+2,z-19+38*zz),Block(r_id,{"type": "bottom"}))
    for zz in range(3):
        for xx in range(2):
            editor.placeBlock((x-9+18*xx,y+1,z-9-5*zz),Block(e_id))
            editor.placeBlock((x-9+18*xx,y+1,z+9+5*zz),Block(e_id))
            editor.placeBlock((x-9+18*xx,y+2,z-9-5*zz),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-9+18*xx,y+2,z+9+5*zz),Block(r_id,{"type": "bottom"}))
    for xx in range(2):
        for zz in range(2):
            editor.placeBlock((x-14-5*xx,y+1,z-9+18*zz),Block(e_id))
            editor.placeBlock((x+14+5*xx,y+1,z-9+18*zz),Block(e_id))
            editor.placeBlock((x-14-5*xx,y+2,z-9+18*zz),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+14+5*xx,y+2,z-9+18*zz),Block(r_id,{"type": "bottom"}))

    for xx in range(2):
        for zz in range(7):
            editor.placeBlock((x-19+38*xx,y+1,z-3+zz),Block(t_id,{"type": "top"}))
        for zz in range(4):
            editor.placeBlock((x-19+38*xx,y+1,z-8+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-19+38*xx,y+1,z+5+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z-18+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z-13+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z+10+zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-9+18*xx,y+1,z+15+zz),Block(t_id,{"type": "top"}))
    for zz in range(2):
        for xx in range(7):
            editor.placeBlock((x-3+xx,y+1,z-19+38*zz),Block(t_id,{"type": "top"}))
        for xx in range(4):
            editor.placeBlock((x-8+xx,y+1,z-19+38*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+5+xx,y+1,z-19+38*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-18+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-13+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+10+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+15+xx,y+1,z-9+18*zz),Block(t_id,{"type": "top"}))
    editor.placeBlock((x-19,y+1,z),Block(t_id,{"type": "double"}))
    editor.placeBlock((x+19,y+1,z),Block(t_id,{"type": "double"}))
    editor.placeBlock((x,y+1,z+19),Block(t_id,{"type": "double"}))
    editor.placeBlock((x,y+1,z-19),Block(t_id,{"type": "double"}))

    for zz in range(2):
        for xx in range(2):
            editor.placeBlock((x+3+3*xx,y+1,z-11-5*zz),Block(q_id))
            editor.placeBlock((x-3-3*xx,y+1,z-11-5*zz),Block(q_id))
            editor.placeBlock((x+3+3*xx,y+1,z+11+5*zz),Block(q_id))
            editor.placeBlock((x-3-3*xx,y+1,z+11+5*zz),Block(q_id))
            editor.placeBlock((x-11-5*xx,y+1,z-3-3*zz),Block(q_id))
            editor.placeBlock((x+11+5*xx,y+1,z-3-3*zz),Block(q_id))
            editor.placeBlock((x-11-5*xx,y+1,z+3+3*zz),Block(q_id))
            editor.placeBlock((x+11+5*xx,y+1,z+3+3*zz),Block(q_id))
    editor.placeBlock((x-6,y+1,z-6),Block(q_id))
    editor.placeBlock((x-6,y+1,z+6),Block(q_id))
    editor.placeBlock((x+6,y+1,z+6),Block(q_id))
    editor.placeBlock((x+6,y+1,z-6),Block(q_id))
    

    for zz in range(2):
        for xx in range(13):
            editor.placeBlock((x-6+xx,y+6,z-11-5*zz),Block(w_id))
            editor.placeBlock((x-6+xx,y+6,z+11+5*zz),Block(w_id))
        for xx in range(11):
            editor.placeBlock((x-6-xx,y+6,z-3+6*zz),Block(w_id))
            editor.placeBlock((x+6+xx,y+6,z-3+6*zz),Block(w_id))
        for xx in range(33):
            editor.placeBlock((x-16+xx,y+6,z-6+12*zz),Block(w_id))
    for xx in range(2):
        for zz in range(13):
            editor.placeBlock((x-11-5*xx,y+6,z-6+zz),Block(w_id))
            editor.placeBlock((x+11+5*xx,y+6,z-6+zz),Block(w_id))
        for zz in range(11):
            editor.placeBlock((x-3+6*xx,y+6,z-6-zz),Block(w_id))
            editor.placeBlock((x-3+6*xx,y+6,z+6+zz),Block(w_id))
        for zz in range(33):
            editor.placeBlock((x-6+12*xx,y+6,z-16+zz),Block(w_id))

    for xx in range(2):
        for zz in range(13):
            editor.placeBlock((x-16+32*xx,y+7,z-6+zz),Block(y_id))
        for zz in range(11):
            editor.placeBlock((x-6+12*xx,y+7,z+6+zz),Block(y_id))
            editor.placeBlock((x-6+12*xx,y+7,z-6-zz),Block(y_id))
    for zz in range(2):
        for xx in range(13):
            editor.placeBlock((x-6+xx,y+7,z-16+32*zz),Block(y_id))
        for xx in range(11):
            editor.placeBlock((x-6-xx,y+7,z-6+12*zz),Block(y_id))
            editor.placeBlock((x+6+xx,y+7,z-6+12*zz),Block(y_id))

    for yy in range(6):
        for zz in range(2):
            for xx in range(2):
                editor.placeBlock((x+3+3*xx,y+2+yy,z-11-5*zz),Block(w_id))
                editor.placeBlock((x-3-3*xx,y+2+yy,z-11-5*zz),Block(w_id))
                editor.placeBlock((x+3+3*xx,y+2+yy,z+11+5*zz),Block(w_id))
                editor.placeBlock((x-3-3*xx,y+2+yy,z+11+5*zz),Block(w_id))
                editor.placeBlock((x-11-5*xx,y+2+yy,z-3-3*zz),Block(w_id))
                editor.placeBlock((x+11+5*xx,y+2+yy,z-3-3*zz),Block(w_id))
                editor.placeBlock((x-11-5*xx,y+2+yy,z+3+3*zz),Block(w_id))
                editor.placeBlock((x+11+5*xx,y+2+yy,z+3+3*zz),Block(w_id))
        editor.placeBlock((x-6,y+2+yy,z-6),Block(w_id))
        editor.placeBlock((x-6,y+2+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+2+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+2+yy,z-6),Block(w_id))

    for zz in range(2):
        for xx in range(15):
            editor.placeBlock((x-7+xx,y+8,z-11-5*zz),Block(w_id))
            editor.placeBlock((x-7+xx,y+8,z+11+5*zz),Block(w_id))
        for xx in range(12):
            editor.placeBlock((x-6-xx,y+8,z-3+6*zz),Block(w_id))
            editor.placeBlock((x+6+xx,y+8,z-3+6*zz),Block(w_id))
        for xx in range(35):
            editor.placeBlock((x-17+xx,y+8,z-6+12*zz),Block(w_id))
    for xx in range(2):
        for zz in range(15):
            editor.placeBlock((x-11-5*xx,y+8,z-7+zz),Block(w_id))
            editor.placeBlock((x+11+5*xx,y+8,z-7+zz),Block(w_id))
        for zz in range(12):
            editor.placeBlock((x-3+6*xx,y+8,z-6-zz),Block(w_id))
            editor.placeBlock((x-3+6*xx,y+8,z+6+zz),Block(w_id))
        for zz in range(35):
            editor.placeBlock((x-6+12*xx,y+8,z-17+zz),Block(w_id))
    for xx in range(11):
        for zz in range(2):
            editor.placeBlock((x-5+xx,y+8,z-3+6*zz),Block(w_id))
    for xx in range(2):
        for zz in range(11):
            editor.placeBlock((x-3+6*xx,y+8,z-5+zz),Block(w_id))

    for yy in range(5):
        editor.placeBlock((x+3,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z+3),Block(w_id))
        editor.placeBlock((x+3,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z-3),Block(w_id))
        editor.placeBlock((x-3,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z+3),Block(w_id))
        editor.placeBlock((x-3,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z-3),Block(w_id))
    for yy in range(3):
        editor.placeBlock((x+6,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z+16),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z+16),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z-16),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z-16),Block(w_id))
        editor.placeBlock((x+16,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x-16,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x-16,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x+16,y+9+yy,z-6),Block(w_id))
    for yy in range(2):
        editor.placeBlock((x+3,y+9+yy,z+16),Block(w_id))
        editor.placeBlock((x+16,y+9+yy,z+3),Block(w_id))
        editor.placeBlock((x-3,y+9+yy,z+16),Block(w_id))
        editor.placeBlock((x-16,y+9+yy,z+3),Block(w_id))
        editor.placeBlock((x+3,y+9+yy,z-16),Block(w_id))
        editor.placeBlock((x+16,y+9+yy,z-3),Block(w_id))
        editor.placeBlock((x-3,y+9+yy,z-16),Block(w_id))
        editor.placeBlock((x-16,y+9+yy,z-3),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z+11),Block(w_id))
        editor.placeBlock((x+11,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z+11),Block(w_id))
        editor.placeBlock((x-11,y+9+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+9+yy,z-11),Block(w_id))
        editor.placeBlock((x+11,y+9+yy,z-6),Block(w_id))
        editor.placeBlock((x-6,y+9+yy,z-11),Block(w_id))
        editor.placeBlock((x-11,y+9+yy,z-6),Block(w_id))
    
    for zz in range(2):
        for yy in range(5):
            for xx in range(9-2*yy):
                editor.placeBlock((x-4+xx+yy,y+12+yy,z-15+30*zz),Block(w_id))
    for xx in range(2):
        for yy in range(5):
            for zz in range(9-2*yy):
                editor.placeBlock((x-15+30*xx,y+12+yy,z-4+zz+yy),Block(w_id))
    
    editor.placeBlock((x,y+13,z+16),Block(w_id))
    editor.placeBlock((x,y+13,z-16),Block(w_id))
    editor.placeBlock((x+16,y+13,z),Block(w_id))
    editor.placeBlock((x-16,y+13,z),Block(w_id))
    editor.placeBlock((x-11,y+13,z+6),Block(w_id))
    editor.placeBlock((x-11,y+13,z-6),Block(w_id))
    editor.placeBlock((x+11,y+13,z+6),Block(w_id))
    editor.placeBlock((x+11,y+13,z-6),Block(w_id))
    editor.placeBlock((x-6,y+13,z-11),Block(w_id))
    editor.placeBlock((x-6,y+13,z+11),Block(w_id))
    editor.placeBlock((x+6,y+13,z+11),Block(w_id))
    editor.placeBlock((x+6,y+13,z-11),Block(w_id))
    
    editor.placeBlock((x+3,y+9,z+11),Block(u_id))
    editor.placeBlock((x-3,y+9,z+11),Block(u_id))
    editor.placeBlock((x-3,y+9,z-11),Block(u_id))
    editor.placeBlock((x+3,y+9,z-11),Block(u_id))

    editor.placeBlock((x+3,y+9,z+3),Block(u_id))
    editor.placeBlock((x-3,y+9,z+3),Block(u_id))
    editor.placeBlock((x-3,y+9,z-3),Block(u_id))
    editor.placeBlock((x+3,y+9,z-3),Block(u_id))

    editor.placeBlock((x+11,y+9,z+3),Block(u_id))
    editor.placeBlock((x-11,y+9,z+3),Block(u_id))
    editor.placeBlock((x-11,y+9,z-3),Block(u_id))
    editor.placeBlock((x+11,y+9,z-3),Block(u_id))

    editor.placeBlock((x+6,y+9,z+11),Block(u_id))
    editor.placeBlock((x-6,y+9,z+11),Block(u_id))
    editor.placeBlock((x-6,y+9,z-11),Block(u_id))
    editor.placeBlock((x+6,y+9,z-11),Block(u_id))

    editor.placeBlock((x+11,y+9,z+6),Block(u_id))
    editor.placeBlock((x-11,y+9,z+6),Block(u_id))
    editor.placeBlock((x-11,y+9,z-6),Block(u_id))
    editor.placeBlock((x+11,y+9,z-6),Block(u_id))

    editor.placeBlock((x+3,y+7,z+6),Block(u_id))
    editor.placeBlock((x-3,y+7,z+6),Block(u_id))
    editor.placeBlock((x-3,y+7,z-6),Block(u_id))
    editor.placeBlock((x+3,y+7,z-6),Block(u_id))

    editor.placeBlock((x+6,y+7,z+3),Block(u_id))
    editor.placeBlock((x-6,y+7,z+3),Block(u_id))
    editor.placeBlock((x-6,y+7,z-3),Block(u_id))
    editor.placeBlock((x+6,y+7,z-3),Block(u_id))


def tiles1(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    def eaves_w(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z),Block(u_id,{"hanging": "true"}))
    def eaves_e(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z),Block(u_id,{"hanging": "true"}))
    def eaves_n(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+1),Block(u_id,{"hanging": "true"}))
    def eaves_s(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-1),Block(u_id,{"hanging": "true"}))
    def eaves_W(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+1),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z+1),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z+2),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z-1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x-2,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    def eaves_E(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "east", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "east", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-1),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z-1),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z-2),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z+1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x+2,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    def eaves_N(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z+1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x-2,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-1),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z-1),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z-2),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    def eaves_S(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z-1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x+2,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+1),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z+1),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z+2),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))

    eaves_w(x+20,y,z-4)
    eaves_w(x+20,y,z+4)
    eaves_w(x+10,y,z-14)
    eaves_w(x+10,y,z+14)   
    eaves_e(x-20,y,z-4)
    eaves_e(x-20,y,z+4)
    eaves_e(x-10,y,z-14)
    eaves_e(x-10,y,z+14)
    eaves_n(x+4,y,z+20)
    eaves_n(x-4,y,z+20)
    eaves_n(x+14,y,z+10)
    eaves_n(x-14,y,z+10)
    eaves_s(x+4,y,z-20)
    eaves_s(x-4,y,z-20)
    eaves_s(x+14,y,z-10)
    eaves_s(x-14,y,z-10)

    eaves_W(x+20,y,z-10)
    eaves_W(x+10,y,z-20)
    eaves_E(x-10,y,z+20)
    eaves_E(x-20,y,z+10)
    eaves_N(x+20,y,z+10)
    eaves_N(x+10,y,z+20)
    eaves_S(x-20,y,z-10)
    eaves_S(x-10,y,z-20)

    editor.placeBlock((x-10,y,z-10),Block(w_id))
    editor.placeBlock((x-10,y+1,z-10),Block(e_id))
    editor.placeBlock((x-10,y-1,z-10),Block(w_id))
    editor.placeBlock((x-11,y,z-10),Block(w_id))
    editor.placeBlock((x-11,y-1,z-10),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x-10,y,z-11),Block(w_id))
    editor.placeBlock((x-10,y-1,z-11),Block(u_id,{"hanging": "true"}))

    editor.placeBlock((x-10,y,z+10),Block(w_id))
    editor.placeBlock((x-10,y+1,z+10),Block(e_id))
    editor.placeBlock((x-10,y-1,z+10),Block(w_id))
    editor.placeBlock((x-11,y,z+10),Block(w_id))
    editor.placeBlock((x-11,y-1,z+10),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x-10,y,z+11),Block(w_id))
    editor.placeBlock((x-10,y-1,z+11),Block(u_id,{"hanging": "true"}))

    editor.placeBlock((x+10,y,z-10),Block(w_id))
    editor.placeBlock((x+10,y+1,z-10),Block(e_id))
    editor.placeBlock((x+10,y-1,z-10),Block(w_id))
    editor.placeBlock((x+11,y,z-10),Block(w_id))
    editor.placeBlock((x+11,y-1,z-10),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x+10,y,z-11),Block(w_id))
    editor.placeBlock((x+10,y-1,z-11),Block(u_id,{"hanging": "true"}))

    editor.placeBlock((x+10,y,z+10),Block(w_id))
    editor.placeBlock((x+10,y+1,z+10),Block(e_id))
    editor.placeBlock((x+10,y-1,z+10),Block(w_id))
    editor.placeBlock((x+11,y,z+10),Block(w_id))
    editor.placeBlock((x+11,y-1,z+10),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x+10,y,z+11),Block(w_id))
    editor.placeBlock((x+10,y-1,z+11),Block(u_id,{"hanging": "true"}))

    for xx in range(3):
        editor.placeBlock((x+11+xx,y+1,z+10),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+11+xx,y+1,z-10),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-13+xx,y+1,z-10),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-13+xx,y+1,z+10),Block(e_id,{"axis": "x"}))
    for xx in range(4):
        editor.placeBlock((x+15+xx,y+1,z+10),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+15+xx,y+1,z-10),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+5+xx,y+1,z-20),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-8+xx,y+1,z-20),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+5+xx,y+1,z+20),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-8+xx,y+1,z+20),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-18+xx,y+1,z+10),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-18+xx,y+1,z-10),Block(e_id,{"axis": "x"}))
    for xx in range(7):
        editor.placeBlock((x-3+xx,y+1,z+20),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-3+xx,y+1,z-20),Block(e_id,{"axis": "x"}))

    for zz in range(3):
        editor.placeBlock((x+10,y+1,z+11+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-10,y+1,z+11+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-10,y+1,z-13+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+10,y+1,z-13+zz),Block(e_id,{"axis": "z"}))
    for zz in range(4):
        editor.placeBlock((x+10,y+1,z+15+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-10,y+1,z+15+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-20,y+1,z+5+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-20,y+1,z-8+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+20,y+1,z+5+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+20,y+1,z-8+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+10,y+1,z-18+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-10,y+1,z-18+zz),Block(e_id,{"axis": "z"}))
    for zz in range(7):
        editor.placeBlock((x+20,y+1,z-3+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-20,y+1,z-3+zz),Block(e_id,{"axis": "z"}))

    #yane
    for zz in range(2):
        editor.placeBlock((x,y+1,z-21-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x,y+1,z+21+zz),Block(r_id,{"type": "top"}))
        for xx in range(10):
            editor.placeBlock((x+1+xx,y+1,z-21-zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-1-xx,y+1,z-21-zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+1+xx,y+1,z+21+zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-1-xx,y+1,z+21+zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))

            editor.placeBlock((x+11+xx,y+1,z-11-zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+11+xx,y+1,z+11+zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-11-xx,y+1,z-11-zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-11-xx,y+1,z+11+zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))

    for xx in range(2):
        editor.placeBlock((x-21-xx,y+1,z),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+21+xx,y+1,z),Block(r_id,{"type": "top"}))
        for zz in range(10):
            editor.placeBlock((x-21-xx,y+1,z-1-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-21-xx,y+1,z+1+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+21+xx,y+1,z-1-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+21+xx,y+1,z+1+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        for zz in range(8):
            editor.placeBlock((x-11-xx,y+1,z-13-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-11-xx,y+1,z+13+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+11+xx,y+1,z-13-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+11+xx,y+1,z+13+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
            
        def tiles_tt(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z+1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z+1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z+1),Block(r_id,{"type": "bottom"}))

            editor.placeBlock((x-1,y,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y,z-1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+1,z-1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x+xx,y+1,z+2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+xx,y+2,z+2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+1+xx,y+2,z+3),Block(y_id))
                editor.placeBlock((x+2+xx,y+3,z+3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x+2,y+1,z+zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+2,y+2,z+zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+3,y+2,z+1+zz),Block(y_id))
                editor.placeBlock((x+3,y+3,z+2+zz),Block(y_id))
            editor.placeBlock((x+2,y+1,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+2,z+2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x+3,y+4,z+3),Block(y_id))
            editor.placeBlock((x+2,y+3,z+2),Block(u_id,{"hanging": "true"}))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x-1,y+3,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z+1),Block(i_id))
            editor.placeBlock((x-1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+3,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z-1),Block(i_id))
            editor.placeBlock((x-1,y+1,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+2,z+1),Block(t_id,{"type": "bottom"}))

        def tiles_ff(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z-1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z-1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z-1),Block(r_id,{"type": "bottom"}))

            editor.placeBlock((x+1,y,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y,z+1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+1,z+1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x-xx,y+1,z-2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-xx,y+2,z-2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-1-xx,y+2,z-3),Block(y_id))
                editor.placeBlock((x-2-xx,y+3,z-3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x-2,y+1,z-zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-2,y+2,z-zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-3,y+2,z-1-zz),Block(y_id))
                editor.placeBlock((x-3,y+3,z-2-zz),Block(y_id))
            editor.placeBlock((x-2,y+1,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+2,z-2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x-3,y+4,z-3),Block(y_id))
            editor.placeBlock((x-2,y+3,z-2),Block(u_id,{"hanging": "true"}))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x+1,y+3,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z-1),Block(i_id))
            editor.placeBlock((x+1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+3,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z+1),Block(i_id))
            editor.placeBlock((x+1,y+1,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+2,z-1),Block(t_id,{"type": "bottom"}))

        def tiles_tf(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z-1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z-1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z-1),Block(r_id,{"type": "bottom"}))

            editor.placeBlock((x-1,y,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y,z+1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+1,z+1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x+xx,y+1,z-2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+xx,y+2,z-2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+1+xx,y+2,z-3),Block(y_id))
                editor.placeBlock((x+2+xx,y+3,z-3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x+2,y+1,z-zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+2,y+2,z-zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+3,y+2,z-1-zz),Block(y_id))
                editor.placeBlock((x+3,y+3,z-2-zz),Block(y_id))
            editor.placeBlock((x+2,y+1,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+2,z-2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x+3,y+4,z-3),Block(y_id))
            editor.placeBlock((x+2,y+3,z-2),Block(u_id,{"hanging": "true"}))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x-1,y+3,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z-1),Block(i_id))
            editor.placeBlock((x-1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+3,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z+1),Block(i_id))
            editor.placeBlock((x-1,y+1,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+2,z-1),Block(t_id,{"type": "bottom"}))
        def tiles_ft(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z+1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z+1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z+1),Block(r_id,{"type": "bottom"}))
            
            editor.placeBlock((x+1,y,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y,z-1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+1,z-1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x-xx,y+1,z+2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-xx,y+2,z+2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-1-xx,y+2,z+3),Block(y_id))
                editor.placeBlock((x-2-xx,y+3,z+3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x-2,y+1,z+zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-2,y+2,z+zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-3,y+2,z+1+zz),Block(y_id))
                editor.placeBlock((x-3,y+3,z+2+zz),Block(y_id))
            editor.placeBlock((x-2,y+1,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+2,z+2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x-3,y+4,z+3),Block(y_id))
            editor.placeBlock((x-2,y+3,z+2),Block(u_id,{"hanging": "true"}))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x+1,y+3,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z+1),Block(i_id))
            editor.placeBlock((x+1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+3,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z-1),Block(i_id))
            editor.placeBlock((x+1,y+1,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+2,z+1),Block(t_id,{"type": "bottom"}))

    tiles_tt(x+21,y+1,z+11)
    tiles_tt(x+11,y+1,z+21)
    tiles_ff(x-21,y+1,z-11)
    tiles_ff(x-11,y+1,z-21)
    tiles_tf(x+11,y+1,z-21)
    tiles_tf(x+21,y+1,z-11)
    tiles_ft(x-11,y+1,z+21)
    tiles_ft(x-21,y+1,z+11)

    for xx in range(9):
        editor.placeBlock((x-8+2*xx,y+1,z+23),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-8+2*xx,y+1,z-23),Block(t_id,{"type": "double"}))
    for xx in range(3):
        editor.placeBlock((x-14-2*xx,y+1,z+13),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-14-2*xx,y+1,z-13),Block(t_id,{"type": "double"}))
        editor.placeBlock((x+14+2*xx,y+1,z+13),Block(t_id,{"type": "double"}))
        editor.placeBlock((x+14+2*xx,y+1,z-13),Block(t_id,{"type": "double"}))
    for xx in range(10):
        editor.placeBlock((x-9+2*xx,y+1,z+23),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-9+2*xx,y+2,z+23),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-9+2*xx,y+1,z-23),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-9+2*xx,y+2,z-23),Block(t_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x-13-2*xx,y+1,z-13),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-13-2*xx,y+2,z-13),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+13+2*xx,y+1,z-13),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+13+2*xx,y+2,z-13),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-13-2*xx,y+1,z+13),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-13-2*xx,y+2,z+13),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+13+2*xx,y+1,z+13),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+13+2*xx,y+2,z+13),Block(t_id,{"type": "bottom"}))

    for zz in range(9):
        editor.placeBlock((x+23,y+1,z-8+2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-23,y+1,z-8+2*zz),Block(t_id,{"type": "double"}))
    for zz in range(3):
        editor.placeBlock((x+13,y+1,z-14-2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-13,y+1,z-14-2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x+13,y+1,z+14+2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-13,y+1,z+14+2*zz),Block(t_id,{"type": "double"}))
    for zz in range(10):
        editor.placeBlock((x+23,y+1,z-9+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+23,y+2,z-9+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-23,y+1,z-9+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-23,y+2,z-9+2*zz),Block(t_id,{"type": "bottom"}))
    for zz in range(4):
        editor.placeBlock((x-13,y+1,z-13-2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-13,y+2,z-13-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-13,y+1,z+13+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-13,y+2,z+13+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+13,y+1,z-13-2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+13,y+2,z-13-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+13,y+1,z+13+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+13,y+2,z+13+2*zz),Block(t_id,{"type": "bottom"}))

    for zz in range(19):
        editor.placeBlock((x-19,y+4,z-9+zz),Block(i_id))
        editor.placeBlock((x+19,y+4,z-9+zz),Block(i_id))
    for zz in range(10):
        editor.placeBlock((x-9,y+4,z-10-zz),Block(i_id))
        editor.placeBlock((x+9,y+4,z-10-zz),Block(i_id))
        editor.placeBlock((x-9,y+4,z+10+zz),Block(i_id))
        editor.placeBlock((x+9,y+4,z+10+zz),Block(i_id))
    for zz in range(10):
        editor.placeBlock((x-20,y+3,z-9+2*zz),Block(i_id))
        editor.placeBlock((x-21,y+3,z-9+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-22,y+2,z-9+2*zz),Block(i_id))

        editor.placeBlock((x+20,y+3,z-9+2*zz),Block(i_id))
        editor.placeBlock((x+21,y+3,z-9+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+22,y+2,z-9+2*zz),Block(i_id))

    for zz in range(4):
        editor.placeBlock((x-10,y+3,z+13+2*zz),Block(i_id))
        editor.placeBlock((x-11,y+3,z+13+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+2,z+13+2*zz),Block(i_id))

        editor.placeBlock((x-10,y+3,z-13-2*zz),Block(i_id))
        editor.placeBlock((x-11,y+3,z-13-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+2,z-13-2*zz),Block(i_id))

        editor.placeBlock((x+10,y+3,z-13-2*zz),Block(i_id))
        editor.placeBlock((x+11,y+3,z-13-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+12,y+2,z-13-2*zz),Block(i_id))

        editor.placeBlock((x+10,y+3,z+13+2*zz),Block(i_id))
        editor.placeBlock((x+11,y+3,z+13+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+12,y+2,z+13+2*zz),Block(i_id))
    for zz in range(9):
        editor.placeBlock((x-20,y+4,z-8+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-20,y+3,z-8+2*zz),Block(i_id))
        editor.placeBlock((x-21,y+2,z-8+2*zz),Block(i_id))
        editor.placeBlock((x-22,y+2,z-8+2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+20,y+4,z-8+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+20,y+3,z-8+2*zz),Block(i_id))
        editor.placeBlock((x+21,y+2,z-8+2*zz),Block(i_id))
        editor.placeBlock((x+22,y+2,z-8+2*zz),Block(t_id,{"type": "bottom"}))
    for zz in range(3):
        editor.placeBlock((x-10,y+4,z-14-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-10,y+3,z-14-2*zz),Block(i_id))
        editor.placeBlock((x-11,y+2,z-14-2*zz),Block(i_id))
        editor.placeBlock((x-12,y+2,z-14-2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+10,y+4,z-14-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10,y+3,z-14-2*zz),Block(i_id))
        editor.placeBlock((x+11,y+2,z-14-2*zz),Block(i_id))
        editor.placeBlock((x+12,y+2,z-14-2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x-10,y+4,z+14+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-10,y+3,z+14+2*zz),Block(i_id))
        editor.placeBlock((x-11,y+2,z+14+2*zz),Block(i_id))
        editor.placeBlock((x-12,y+2,z+14+2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+10,y+4,z+14+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10,y+3,z+14+2*zz),Block(i_id))
        editor.placeBlock((x+11,y+2,z+14+2*zz),Block(i_id))
        editor.placeBlock((x+12,y+2,z+14+2*zz),Block(t_id,{"type": "bottom"}))

    for xx in range(19):
        editor.placeBlock((x-9+xx,y+4,z-19),Block(i_id))
        editor.placeBlock((x-9+xx,y+4,z+19),Block(i_id))
    for xx in range(10):
        editor.placeBlock((x-10-xx,y+4,z-9),Block(i_id))
        editor.placeBlock((x-10-xx,y+4,z+9),Block(i_id))
        editor.placeBlock((x+10+xx,y+4,z-9),Block(i_id))
        editor.placeBlock((x+10+xx,y+4,z+9),Block(i_id))
    for xx in range(10):
        editor.placeBlock((x-9+2*xx,y+3,z-20),Block(i_id))
        editor.placeBlock((x-9+2*xx,y+3,z-21),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-9+2*xx,y+2,z-22),Block(i_id))

        editor.placeBlock((x-9+2*xx,y+3,z+20),Block(i_id))
        editor.placeBlock((x-9+2*xx,y+3,z+21),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-9+2*xx,y+2,z+22),Block(i_id))

    for xx in range(4):
        editor.placeBlock((x+13+2*xx,y+3,z-10),Block(i_id))
        editor.placeBlock((x+13+2*xx,y+3,z-11),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+13+2*xx,y+2,z-12),Block(i_id))

        editor.placeBlock((x-13-2*xx,y+3,z-10),Block(i_id))
        editor.placeBlock((x-13-2*xx,y+3,z-11),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-13-2*xx,y+2,z-12),Block(i_id))

        editor.placeBlock((x-13-2*xx,y+3,z+10),Block(i_id))
        editor.placeBlock((x-13-2*xx,y+3,z+11),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-13-2*xx,y+2,z+12),Block(i_id))

        editor.placeBlock((x+13+2*xx,y+3,z+10),Block(i_id))
        editor.placeBlock((x+13+2*xx,y+3,z+11),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+13+2*xx,y+2,z+12),Block(i_id))
    for xx in range(9):
        editor.placeBlock((x-8+2*xx,y+4,z-20),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-8+2*xx,y+3,z-20),Block(i_id))
        editor.placeBlock((x-8+2*xx,y+2,z-21),Block(i_id))
        editor.placeBlock((x-8+2*xx,y+2,z-22),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x-8+2*xx,y+4,z+20),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-8+2*xx,y+3,z+20),Block(i_id))
        editor.placeBlock((x-8+2*xx,y+2,z+21),Block(i_id))
        editor.placeBlock((x-8+2*xx,y+2,z+22),Block(t_id,{"type": "bottom"}))
    for xx in range(3):
        editor.placeBlock((x-14-2*xx,y+4,z-10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-14-2*xx,y+3,z-10),Block(i_id))
        editor.placeBlock((x-14-2*xx,y+2,z-11),Block(i_id))
        editor.placeBlock((x-14-2*xx,y+2,z-12),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x-14-2*xx,y+4,z+10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-14-2*xx,y+3,z+10),Block(i_id))
        editor.placeBlock((x-14-2*xx,y+2,z+11),Block(i_id))
        editor.placeBlock((x-14-2*xx,y+2,z+12),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+14+2*xx,y+4,z-10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+14+2*xx,y+3,z-10),Block(i_id))
        editor.placeBlock((x+14+2*xx,y+2,z-11),Block(i_id))
        editor.placeBlock((x+14+2*xx,y+2,z-12),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+14+2*xx,y+4,z+10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+14+2*xx,y+3,z+10),Block(i_id))
        editor.placeBlock((x+14+2*xx,y+2,z+11),Block(i_id))
        editor.placeBlock((x+14+2*xx,y+2,z+12),Block(t_id,{"type": "bottom"}))

        def corner_ff(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z-1),Block(i_id))
            editor.placeBlock((x-2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z-2),Block(i_id))
            editor.placeBlock((x-1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z-1),Block(i_id))
            editor.placeBlock((x-1,y+3,z-2),Block(i_id))
            editor.placeBlock((x-2,y+3,z-2),Block(t_id,{"type": "bottom"}))
        def corner_tt(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z+1),Block(i_id))
            editor.placeBlock((x+2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z+2),Block(i_id))
            editor.placeBlock((x+1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z+1),Block(i_id))
            editor.placeBlock((x+1,y+3,z+2),Block(i_id))
            editor.placeBlock((x+2,y+3,z+2),Block(t_id,{"type": "bottom"}))
        def corner_ft(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z+1),Block(i_id))
            editor.placeBlock((x-2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z+2),Block(i_id))
            editor.placeBlock((x-1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z+1),Block(i_id))
            editor.placeBlock((x-1,y+3,z+2),Block(i_id))
            editor.placeBlock((x-2,y+3,z+2),Block(t_id,{"type": "bottom"}))
        def corner_tf(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z-1),Block(i_id))
            editor.placeBlock((x+2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z-2),Block(i_id))
            editor.placeBlock((x+1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z-1),Block(i_id))
            editor.placeBlock((x+1,y+3,z-2),Block(i_id))
            editor.placeBlock((x+2,y+3,z-2),Block(t_id,{"type": "bottom"}))


        corner_ff(x-10,y,z-10)
        corner_tt(x+10,y,z+10)
        corner_tf(x+10,y,z-10)
        corner_ft(x-10,y,z+10)
    #light
    editor.placeBlock((x+23,y+2,z),Block(u_id))
    editor.placeBlock((x+21,y+3,z+6),Block(u_id))
    editor.placeBlock((x+21,y+3,z-6),Block(u_id))
    editor.placeBlock((x-23,y+2,z),Block(u_id))
    editor.placeBlock((x-21,y+3,z+6),Block(u_id))
    editor.placeBlock((x-21,y+3,z-6),Block(u_id))
    editor.placeBlock((x,y+2,z+23),Block(u_id))
    editor.placeBlock((x+6,y+3,z+21),Block(u_id))
    editor.placeBlock((x-6,y+3,z+21),Block(u_id))
    editor.placeBlock((x,y+2,z-23),Block(u_id))
    editor.placeBlock((x+6,y+3,z-21),Block(u_id))
    editor.placeBlock((x-6,y+3,z-21),Block(u_id))

    editor.placeBlock((x+11,y+3,z+16),Block(u_id))
    editor.placeBlock((x-11,y+3,z+16),Block(u_id))
    editor.placeBlock((x+11,y+3,z-16),Block(u_id))
    editor.placeBlock((x-11,y+3,z-16),Block(u_id))
    editor.placeBlock((x+16,y+3,z+11),Block(u_id))
    editor.placeBlock((x-16,y+3,z+11),Block(u_id))
    editor.placeBlock((x+16,y+3,z-11),Block(u_id))
    editor.placeBlock((x-16,y+3,z-11),Block(u_id))








def tiles(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    def eaves_w(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z),Block(u_id,{"hanging": "true"}))
    def eaves_e(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z),Block(u_id,{"hanging": "true"}))
    def eaves_n(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+1),Block(u_id,{"hanging": "true"}))
    def eaves_s(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-1),Block(u_id,{"hanging": "true"}))
    def eaves_W(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+1),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z+1),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z+2),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z-1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x-2,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    def eaves_E(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "east", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "east", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-1),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z-1),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z-2),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z+1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x+2,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    def eaves_N(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "west", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x-1,y,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z+1),Block(q_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x-2,y,z),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-1),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-1),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z-1),Block(q_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z-2),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    def eaves_S(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "outer_left"}))
        editor.placeBlock((x+1,y,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z-1),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z-1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x+2,y,z),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+1),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z+1),Block(q_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-1,z+1),Block(u_id,{"hanging": "true"}))
        editor.placeBlock((x,y,z+2),Block(q_id,{"facing": "south", "half": "bottom", "shape": "straight"}))

    eaves_w(x+17,y,z-3)
    eaves_w(x+17,y,z+3)
    eaves_w(x+7,y,z-11)
    eaves_w(x+7,y,z+11)   
    eaves_e(x-17,y,z-3)
    eaves_e(x-17,y,z+3)
    eaves_e(x-7,y,z-11)
    eaves_e(x-7,y,z+11)
    eaves_n(x+3,y,z+17)
    eaves_n(x-3,y,z+17)
    eaves_n(x+11,y,z+7)
    eaves_n(x-11,y,z+7)
    eaves_s(x+3,y,z-17)
    eaves_s(x-3,y,z-17)
    eaves_s(x+11,y,z-7)
    eaves_s(x-11,y,z-7)

    eaves_W(x+17,y,z-7)
    eaves_W(x+7,y,z-17)
    eaves_E(x-7,y,z+17)
    eaves_E(x-17,y,z+7)
    eaves_N(x+17,y,z+7)
    eaves_N(x+7,y,z+17)
    eaves_S(x-17,y,z-7)
    eaves_S(x-7,y,z-17)

    editor.placeBlock((x-7,y,z-7),Block(w_id))
    editor.placeBlock((x-7,y+1,z-7),Block(e_id))
    editor.placeBlock((x-7,y-1,z-7),Block(w_id))
    editor.placeBlock((x-8,y,z-7),Block(w_id))
    editor.placeBlock((x-8,y-1,z-7),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x-7,y,z-8),Block(w_id))
    editor.placeBlock((x-7,y-1,z-8),Block(u_id,{"hanging": "true"}))

    editor.placeBlock((x-7,y,z+7),Block(w_id))
    editor.placeBlock((x-7,y+1,z+7),Block(e_id))
    editor.placeBlock((x-7,y-1,z+7),Block(w_id))
    editor.placeBlock((x-8,y,z+7),Block(w_id))
    editor.placeBlock((x-8,y-1,z+7),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x-7,y,z+8),Block(w_id))
    editor.placeBlock((x-7,y-1,z+8),Block(u_id,{"hanging": "true"}))

    editor.placeBlock((x+7,y,z-7),Block(w_id))
    editor.placeBlock((x+7,y+1,z-7),Block(e_id))
    editor.placeBlock((x+7,y-1,z-7),Block(w_id))
    editor.placeBlock((x+8,y,z-7),Block(w_id))
    editor.placeBlock((x+8,y-1,z-7),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x+7,y,z-8),Block(w_id))
    editor.placeBlock((x+7,y-1,z-8),Block(u_id,{"hanging": "true"}))

    editor.placeBlock((x+7,y,z+7),Block(w_id))
    editor.placeBlock((x+7,y+1,z+7),Block(e_id))
    editor.placeBlock((x+7,y-1,z+7),Block(w_id))
    editor.placeBlock((x+8,y,z+7),Block(w_id))
    editor.placeBlock((x+8,y-1,z+7),Block(u_id,{"hanging": "true"}))
    editor.placeBlock((x+7,y,z+8),Block(w_id))
    editor.placeBlock((x+7,y-1,z+8),Block(u_id,{"hanging": "true"}))

    for xx in range(3):
        editor.placeBlock((x+8+xx,y+1,z+7),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+8+xx,y+1,z-7),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-8-xx,y+1,z-7),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-8-xx,y+1,z+7),Block(e_id,{"axis": "x"}))
    for xx in range(4):
        editor.placeBlock((x+12+xx,y+1,z+7),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+12+xx,y+1,z-7),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-12-xx,y+1,z+7),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-12-xx,y+1,z-7),Block(e_id,{"axis": "x"}))
    for xx in range(2):
        editor.placeBlock((x+4+xx,y+1,z-17),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-4-xx,y+1,z-17),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x+4+xx,y+1,z+17),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-4-xx,y+1,z+17),Block(e_id,{"axis": "x"}))
    for xx in range(5):
        editor.placeBlock((x-2+xx,y+1,z+17),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-2+xx,y+1,z-17),Block(e_id,{"axis": "x"}))

    for zz in range(3):
        editor.placeBlock((x+7,y+1,z+8+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-7,y+1,z+8+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+7,y+1,z-8-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-7,y+1,z-8-zz),Block(e_id,{"axis": "z"}))
    for zz in range(4):
        editor.placeBlock((x+7,y+1,z+12+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-7,y+1,z+12+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+7,y+1,z-12-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-7,y+1,z-12-zz),Block(e_id,{"axis": "z"}))
    for zz in range(2):
        editor.placeBlock((x-17,y+1,z-4-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+17,y+1,z-4-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-17,y+1,z+4+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+17,y+1,z+4+zz),Block(e_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((x+17,y+1,z-2+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x-17,y+1,z-2+zz),Block(e_id,{"axis": "z"}))

    #yane
    for zz in range(2):
        editor.placeBlock((x,y+1,z-18-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x,y+1,z+18+zz),Block(r_id,{"type": "top"}))
        for xx in range(7):
            editor.placeBlock((x+1+xx,y+1,z-18-zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-1-xx,y+1,z-18-zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+1+xx,y+1,z+18+zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-1-xx,y+1,z+18+zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
        for xx in range(8):
            editor.placeBlock((x+10+xx,y+1,z-8-zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+10+xx,y+1,z+8+zz),Block(q_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-10-xx,y+1,z-8-zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-10-xx,y+1,z+8+zz),Block(q_id,{"facing": "east", "half": "top", "shape": "straight"}))

    for xx in range(2):
        editor.placeBlock((x-18-xx,y+1,z),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+18+xx,y+1,z),Block(r_id,{"type": "top"}))
        for zz in range(7):
            editor.placeBlock((x-18-xx,y+1,z-1-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-18-xx,y+1,z+1+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+18+xx,y+1,z-1-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+18+xx,y+1,z+1+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        for zz in range(8):
            editor.placeBlock((x-8-xx,y+1,z-10-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-8-xx,y+1,z+10+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+8+xx,y+1,z-10-zz),Block(q_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+8+xx,y+1,z+10+zz),Block(q_id,{"facing": "north", "half": "top", "shape": "straight"}))
        def tiles_tt(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z+1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z+1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z+1),Block(r_id,{"type": "bottom"}))

            editor.placeBlock((x-1,y,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y,z-1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+1,z-1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x+xx,y+1,z+2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+xx,y+2,z+2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+1+xx,y+2,z+3),Block(y_id))
                editor.placeBlock((x+2+xx,y+3,z+3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x+2,y+1,z+zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+2,y+2,z+zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+3,y+2,z+1+zz),Block(y_id))
                editor.placeBlock((x+3,y+3,z+2+zz),Block(y_id))
            editor.placeBlock((x+2,y+1,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+2,z+2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x+3,y+4,z+3),Block(y_id))
            editor.placeBlock((x+2,y+3,z+2),Block(u_id))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x-1,y+3,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z+1),Block(i_id))
            editor.placeBlock((x-1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+3,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z-1),Block(i_id))
            editor.placeBlock((x-1,y+1,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+2,z+1),Block(t_id,{"type": "bottom"}))

        def tiles_ff(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z-1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z-1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z-1),Block(r_id,{"type": "bottom"}))

            editor.placeBlock((x+1,y,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y,z+1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+1,z+1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x-xx,y+1,z-2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-xx,y+2,z-2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-1-xx,y+2,z-3),Block(y_id))
                editor.placeBlock((x-2-xx,y+3,z-3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x-2,y+1,z-zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-2,y+2,z-zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-3,y+2,z-1-zz),Block(y_id))
                editor.placeBlock((x-3,y+3,z-2-zz),Block(y_id))
            editor.placeBlock((x-2,y+1,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+2,z-2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x-3,y+4,z-3),Block(y_id))
            editor.placeBlock((x-2,y+3,z-2),Block(u_id))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x+1,y+3,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z-1),Block(i_id))
            editor.placeBlock((x+1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+3,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z+1),Block(i_id))
            editor.placeBlock((x+1,y+1,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+2,z-1),Block(t_id,{"type": "bottom"}))

        def tiles_tf(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z-1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z-1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z-1),Block(r_id,{"type": "bottom"}))

            editor.placeBlock((x-1,y,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y,z+1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+1,z+1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x+xx,y+1,z-2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+xx,y+2,z-2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+1+xx,y+2,z-3),Block(y_id))
                editor.placeBlock((x+2+xx,y+3,z-3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x+2,y+1,z-zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x+2,y+2,z-zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x+3,y+2,z-1-zz),Block(y_id))
                editor.placeBlock((x+3,y+3,z-2-zz),Block(y_id))
            editor.placeBlock((x+2,y+1,z-2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+2,y+2,z-2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x+3,y+4,z-3),Block(y_id))
            editor.placeBlock((x+2,y+3,z-2),Block(u_id))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x-1,y+3,z+1),Block(i_id))
            editor.placeBlock((x+1,y+2,z-1),Block(i_id))
            editor.placeBlock((x-1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+3,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+1,z+1),Block(i_id))
            editor.placeBlock((x-1,y+1,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+2,z-1),Block(t_id,{"type": "bottom"}))
        def tiles_ft(x,y,z):
            editor.placeBlock((x,y,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y,z),Block(r_id,{"type": "top"}))
            editor.placeBlock((x,y,z+1),Block(r_id,{"type": "top"}))
            editor.placeBlock((x-1,y+1,z),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x,y+1,z+1),Block(r_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z+1),Block(r_id,{"type": "bottom"}))
            
            editor.placeBlock((x+1,y,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x+1,y+1,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y,z-1),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+1,z-1),Block(t_id,{"type": "bottom"}))
            for xx in range(2):
                editor.placeBlock((x-xx,y+1,z+2),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-xx,y+2,z+2),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-1-xx,y+2,z+3),Block(y_id))
                editor.placeBlock((x-2-xx,y+3,z+3),Block(y_id))
            for zz in range(2):
                editor.placeBlock((x-2,y+1,z+zz),Block(t_id,{"type": "double"}))
                editor.placeBlock((x-2,y+2,z+zz),Block(t_id,{"type": "bottom"}))
                editor.placeBlock((x-3,y+2,z+1+zz),Block(y_id))
                editor.placeBlock((x-3,y+3,z+2+zz),Block(y_id))
            editor.placeBlock((x-2,y+1,z+2),Block(t_id,{"type": "top"}))
            editor.placeBlock((x-2,y+2,z+2),Block(t_id,{"type": "double"}))
            editor.placeBlock((x-3,y+4,z+3),Block(y_id))
            editor.placeBlock((x-2,y+3,z+2),Block(u_id))

            for yy in range(2):
                editor.placeBlock((x,y+2+yy,z),Block(i_id))
            editor.placeBlock((x,y+2,z-1),Block(i_id))
            editor.placeBlock((x+1,y+2,z),Block(i_id))
            editor.placeBlock((x,y+2,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z),Block(i_id))
            editor.placeBlock((x+1,y+3,z-1),Block(i_id))
            editor.placeBlock((x-1,y+2,z+1),Block(i_id))
            editor.placeBlock((x+1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+3,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-1,y+1,z-1),Block(i_id))
            editor.placeBlock((x+1,y+1,z+1),Block(i_id))
            editor.placeBlock((x-1,y+2,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+1,y+2,z+1),Block(t_id,{"type": "bottom"}))
    tiles_tt(x+18,y+1,z+8)
    tiles_tt(x+8,y+1,z+18)
    tiles_ff(x-18,y+1,z-8)
    tiles_ff(x-8,y+1,z-18)
    tiles_tf(x+8,y+1,z-18)
    tiles_tf(x+18,y+1,z-8)
    tiles_ft(x-8,y+1,z+18)
    tiles_ft(x-18,y+1,z+8)

    for xx in range(6):
        editor.placeBlock((x-5+2*xx,y+1,z+20),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-5+2*xx,y+1,z-20),Block(t_id,{"type": "double"}))
    for xx in range(3):
        editor.placeBlock((x-11-2*xx,y+1,z+10),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-11-2*xx,y+1,z-10),Block(t_id,{"type": "double"}))
        editor.placeBlock((x+11+2*xx,y+1,z+10),Block(t_id,{"type": "double"}))
        editor.placeBlock((x+11+2*xx,y+1,z-10),Block(t_id,{"type": "double"}))
    for xx in range(7):
        editor.placeBlock((x-6+2*xx,y+1,z+20),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-6+2*xx,y+2,z+20),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-6+2*xx,y+1,z-20),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-6+2*xx,y+2,z-20),Block(t_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x-10-2*xx,y+1,z-10),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-10-2*xx,y+2,z-10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10+2*xx,y+1,z-10),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+10+2*xx,y+2,z-10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-10-2*xx,y+1,z+10),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-10-2*xx,y+2,z+10),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10+2*xx,y+1,z+10),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+10+2*xx,y+2,z+10),Block(t_id,{"type": "bottom"}))

    for zz in range(6):
        editor.placeBlock((x+20,y+1,z-5+2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-20,y+1,z-5+2*zz),Block(t_id,{"type": "double"}))
    for zz in range(3):
        editor.placeBlock((x+10,y+1,z-11-2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-10,y+1,z-11-2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x+10,y+1,z+11+2*zz),Block(t_id,{"type": "double"}))
        editor.placeBlock((x-10,y+1,z+11+2*zz),Block(t_id,{"type": "double"}))
    for zz in range(7):
        editor.placeBlock((x+20,y+1,z-6+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+20,y+2,z-6+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-20,y+1,z-6+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-20,y+2,z-6+2*zz),Block(t_id,{"type": "bottom"}))
    for zz in range(4):
        editor.placeBlock((x-10,y+1,z-10-2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-10,y+2,z-10-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-10,y+1,z+10+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-10,y+2,z+10+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10,y+1,z-10-2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+10,y+2,z-10-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10,y+1,z+10+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+10,y+2,z+10+2*zz),Block(t_id,{"type": "bottom"}))
#z
    for zz in range(13):
        editor.placeBlock((x-16,y+4,z-6+zz),Block(i_id))
        editor.placeBlock((x+16,y+4,z-6+zz),Block(i_id))
    for zz in range(10):
        editor.placeBlock((x-6,y+4,z-7-zz),Block(i_id))
        editor.placeBlock((x+6,y+4,z-7-zz),Block(i_id))
        editor.placeBlock((x-6,y+4,z+7+zz),Block(i_id))
        editor.placeBlock((x+6,y+4,z+7+zz),Block(i_id))
    for zz in range(7):
        editor.placeBlock((x-17,y+3,z-6+2*zz),Block(i_id))
        editor.placeBlock((x-18,y+3,z-6+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-19,y+2,z-6+2*zz),Block(i_id))

        editor.placeBlock((x+17,y+3,z-6+2*zz),Block(i_id))
        editor.placeBlock((x+18,y+3,z-6+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+19,y+2,z-6+2*zz),Block(i_id))

    for zz in range(4):
        editor.placeBlock((x-7,y+3,z+10+2*zz),Block(i_id))
        editor.placeBlock((x-8,y+3,z+10+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-9,y+2,z+10+2*zz),Block(i_id))

        editor.placeBlock((x-7,y+3,z-10-2*zz),Block(i_id))
        editor.placeBlock((x-8,y+3,z-10-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-9,y+2,z-10-2*zz),Block(i_id))

        editor.placeBlock((x+7,y+3,z-10-2*zz),Block(i_id))
        editor.placeBlock((x+8,y+3,z-10-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+9,y+2,z-10-2*zz),Block(i_id))

        editor.placeBlock((x+7,y+3,z+10+2*zz),Block(i_id))
        editor.placeBlock((x+8,y+3,z+10+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+9,y+2,z+10+2*zz),Block(i_id))
    for zz in range(6):
        editor.placeBlock((x-17,y+4,z-5+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-17,y+3,z-5+2*zz),Block(i_id))
        editor.placeBlock((x-18,y+2,z-5+2*zz),Block(i_id))
        editor.placeBlock((x-19,y+2,z-5+2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+17,y+4,z-5+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+17,y+3,z-5+2*zz),Block(i_id))
        editor.placeBlock((x+18,y+2,z-5+2*zz),Block(i_id))
        editor.placeBlock((x+19,y+2,z-5+2*zz),Block(t_id,{"type": "bottom"}))
    for zz in range(3):
        editor.placeBlock((x-7,y+4,z-11-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-7,y+3,z-11-2*zz),Block(i_id))
        editor.placeBlock((x-8,y+2,z-11-2*zz),Block(i_id))
        editor.placeBlock((x-9,y+2,z-11-2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+7,y+4,z-11-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+7,y+3,z-11-2*zz),Block(i_id))
        editor.placeBlock((x+8,y+2,z-11-2*zz),Block(i_id))
        editor.placeBlock((x+9,y+2,z-11-2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x-7,y+4,z+11+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-7,y+3,z+11+2*zz),Block(i_id))
        editor.placeBlock((x-8,y+2,z+11+2*zz),Block(i_id))
        editor.placeBlock((x-9,y+2,z+11+2*zz),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+7,y+4,z+11+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+7,y+3,z+11+2*zz),Block(i_id))
        editor.placeBlock((x+8,y+2,z+11+2*zz),Block(i_id))
        editor.placeBlock((x+9,y+2,z+11+2*zz),Block(t_id,{"type": "bottom"}))
#x
    for xx in range(13):
        editor.placeBlock((x-6+xx,y+4,z-16),Block(i_id))
        editor.placeBlock((x-6+xx,y+4,z+16),Block(i_id))
    for xx in range(10):
        editor.placeBlock((x-7-xx,y+4,z-6),Block(i_id))
        editor.placeBlock((x-7-xx,y+4,z+6),Block(i_id))
        editor.placeBlock((x+7+xx,y+4,z-6),Block(i_id))
        editor.placeBlock((x+7+xx,y+4,z+6),Block(i_id))
    for xx in range(7):
        editor.placeBlock((x-6+2*xx,y+3,z-17),Block(i_id))
        editor.placeBlock((x-6+2*xx,y+3,z-18),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-6+2*xx,y+2,z-19),Block(i_id))

        editor.placeBlock((x-6+2*xx,y+3,z+17),Block(i_id))
        editor.placeBlock((x-6+2*xx,y+3,z+18),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-6+2*xx,y+2,z+19),Block(i_id))

    for xx in range(4):
        editor.placeBlock((x+10+2*xx,y+3,z-7),Block(i_id))
        editor.placeBlock((x+10+2*xx,y+3,z-8),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10+2*xx,y+2,z-9),Block(i_id))

        editor.placeBlock((x-10-2*xx,y+3,z-7),Block(i_id))
        editor.placeBlock((x-10-2*xx,y+3,z-8),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-10-2*xx,y+2,z-9),Block(i_id))

        editor.placeBlock((x-10-2*xx,y+3,z+7),Block(i_id))
        editor.placeBlock((x-10-2*xx,y+3,z+8),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-10-2*xx,y+2,z+9),Block(i_id))

        editor.placeBlock((x+10+2*xx,y+3,z+7),Block(i_id))
        editor.placeBlock((x+10+2*xx,y+3,z+8),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+10+2*xx,y+2,z+9),Block(i_id))
    for xx in range(6):
        editor.placeBlock((x-5+2*xx,y+4,z-17),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-5+2*xx,y+3,z-17),Block(i_id))
        editor.placeBlock((x-5+2*xx,y+2,z-18),Block(i_id))
        editor.placeBlock((x-5+2*xx,y+2,z-19),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x-5+2*xx,y+4,z+17),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-5+2*xx,y+3,z+17),Block(i_id))
        editor.placeBlock((x-5+2*xx,y+2,z+18),Block(i_id))
        editor.placeBlock((x-5+2*xx,y+2,z+19),Block(t_id,{"type": "bottom"}))
    for xx in range(3):
        editor.placeBlock((x-11-2*xx,y+4,z-7),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-11-2*xx,y+3,z-7),Block(i_id))
        editor.placeBlock((x-11-2*xx,y+2,z-8),Block(i_id))
        editor.placeBlock((x-11-2*xx,y+2,z-9),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x-11-2*xx,y+4,z+7),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-11-2*xx,y+3,z+7),Block(i_id))
        editor.placeBlock((x-11-2*xx,y+2,z+8),Block(i_id))
        editor.placeBlock((x-11-2*xx,y+2,z+9),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+11+2*xx,y+4,z-7),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+11+2*xx,y+3,z-7),Block(i_id))
        editor.placeBlock((x+11+2*xx,y+2,z-8),Block(i_id))
        editor.placeBlock((x+11+2*xx,y+2,z-9),Block(t_id,{"type": "bottom"}))

        editor.placeBlock((x+11+2*xx,y+4,z+7),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+11+2*xx,y+3,z+7),Block(i_id))
        editor.placeBlock((x+11+2*xx,y+2,z+8),Block(i_id))
        editor.placeBlock((x+11+2*xx,y+2,z+9),Block(t_id,{"type": "bottom"}))

        def corner_ff(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+6,z),Block(u_id,{"hanging": "true"}))
            editor.placeBlock((x-1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z-1),Block(i_id))
            editor.placeBlock((x-2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z-2),Block(i_id))
            editor.placeBlock((x-1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z-1),Block(i_id))
            editor.placeBlock((x-1,y+3,z-2),Block(i_id))
            editor.placeBlock((x-2,y+3,z-2),Block(t_id,{"type": "bottom"}))
        def corner_tt(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+6,z),Block(u_id,{"hanging": "true"}))
            editor.placeBlock((x+1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z+1),Block(i_id))
            editor.placeBlock((x+2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z+2),Block(i_id))
            editor.placeBlock((x+1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z+1),Block(i_id))
            editor.placeBlock((x+1,y+3,z+2),Block(i_id))
            editor.placeBlock((x+2,y+3,z+2),Block(t_id,{"type": "bottom"}))
        def corner_ft(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+6,z),Block(u_id,{"hanging": "true"}))
            editor.placeBlock((x-1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z+1),Block(i_id))
            editor.placeBlock((x-2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z+2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z+2),Block(i_id))
            editor.placeBlock((x-1,y+4,z+1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y+3,z+1),Block(i_id))
            editor.placeBlock((x-1,y+3,z+2),Block(i_id))
            editor.placeBlock((x-2,y+3,z+2),Block(t_id,{"type": "bottom"}))
        def corner_tf(x,y,z):
            editor.placeBlock((x,y+4,z),Block(i_id))
            editor.placeBlock((x,y+5,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+6,z),Block(u_id,{"hanging": "true"}))
            editor.placeBlock((x+1,y+4,z),Block(i_id))
            editor.placeBlock((x,y+4,z-1),Block(i_id))
            editor.placeBlock((x+2,y+4,z),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x,y+4,z-2),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z),Block(i_id))
            editor.placeBlock((x,y+3,z-2),Block(i_id))
            editor.placeBlock((x+1,y+4,z-1),Block(t_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y+3,z-1),Block(i_id))
            editor.placeBlock((x+1,y+3,z-2),Block(i_id))
            editor.placeBlock((x+2,y+3,z-2),Block(t_id,{"type": "bottom"}))

        corner_ff(x-7,y,z-7)
        corner_tt(x+7,y,z+7)
        corner_tf(x+7,y,z-7)
        corner_ft(x-7,y,z+7)
    #light    
        editor.placeBlock((x+3,y+2,z+20),Block(u_id))
        editor.placeBlock((x-3,y+2,z+20),Block(u_id))
        editor.placeBlock((x+3,y+2,z-20),Block(u_id))
        editor.placeBlock((x-3,y+2,z-20),Block(u_id))
        editor.placeBlock((x+20,y+2,z+3),Block(u_id))
        editor.placeBlock((x-20,y+2,z+3),Block(u_id))
        editor.placeBlock((x+20,y+2,z-3),Block(u_id))
        editor.placeBlock((x-20,y+2,z-3),Block(u_id))
        editor.placeBlock((x+15,y+2,z+10),Block(u_id))
        editor.placeBlock((x+15,y+2,z-10),Block(u_id))
        editor.placeBlock((x-15,y+2,z+10),Block(u_id))
        editor.placeBlock((x-15,y+2,z-10),Block(u_id))
        editor.placeBlock((x+10,y+2,z+15),Block(u_id))
        editor.placeBlock((x+10,y+2,z-15),Block(u_id))
        editor.placeBlock((x-10,y+2,z+15),Block(u_id))
        editor.placeBlock((x-10,y+2,z-15),Block(u_id))



def housetop(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id):
    for xx in range(33):
        editor.placeBlock((x-16+xx,y+5,z),Block(q_id))
    for zz in range(33):
        editor.placeBlock((x,y+5,z-16+zz),Block(q_id))
    def top1(x,y,z):
        editor.placeBlock((x,y,z),Block(t_id))
        editor.placeBlock((x-1,y+4,z),Block(q_id))
        editor.placeBlock((x+1,y+4,z),Block(q_id))
        editor.placeBlock((x-2,y+3,z),Block(q_id))
        editor.placeBlock((x+2,y+3,z),Block(q_id))
        editor.placeBlock((x-3,y+2,z),Block(q_id))
        editor.placeBlock((x+3,y+2,z),Block(q_id))
        editor.placeBlock((x-4,y+1,z),Block(q_id))
        editor.placeBlock((x+4,y+1,z),Block(q_id))
        editor.placeBlock((x-5,y,z),Block(q_id))
        editor.placeBlock((x+5,y,z),Block(q_id))
        
        editor.placeBlock((x,y+4,z),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y+3,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y+3,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-2,y+2,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+2,y+2,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-3,y+1,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+3,y+1,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-4,y,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+4,y,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))

        editor.placeBlock((x,y+2,z+1),Block(y_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y+1,z),Block(r_id,{"facing": "west", "half": "bottom", "shape": "inner_right"}))
        editor.placeBlock((x+1,y+1,z),Block(r_id,{"facing": "east", "half": "bottom", "shape": "inner_left"}))
        editor.placeBlock((x,y+2,z),Block(u_id))
        
        editor.placeBlock((x-1,y+2,z),Block(r_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y+2,z),Block(r_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+3,z),Block(r_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-2,y,z),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+2,y,z),Block(e_id,{"type": "top"}))



    def top2(x,y,z):
        editor.placeBlock((x,y,z),Block(t_id))
        editor.placeBlock((x-1,y+4,z),Block(q_id))
        editor.placeBlock((x+1,y+4,z),Block(q_id))
        editor.placeBlock((x-2,y+3,z),Block(q_id))
        editor.placeBlock((x+2,y+3,z),Block(q_id))
        editor.placeBlock((x-3,y+2,z),Block(q_id))
        editor.placeBlock((x+3,y+2,z),Block(q_id))
        editor.placeBlock((x-4,y+1,z),Block(q_id))
        editor.placeBlock((x+4,y+1,z),Block(q_id))
        editor.placeBlock((x-5,y,z),Block(q_id))
        editor.placeBlock((x+5,y,z),Block(q_id))
        
        editor.placeBlock((x,y+4,z),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y+3,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y+3,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-2,y+2,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+2,y+2,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-3,y+1,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+3,y+1,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-4,y,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+4,y,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))

        editor.placeBlock((x,y+2,z-1),Block(y_id,{"facing": "north", "half": "bottom", "open": "true"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y+1,z),Block(r_id,{"facing": "west", "half": "bottom", "shape": "inner_right"}))
        editor.placeBlock((x+1,y+1,z),Block(r_id,{"facing": "east", "half": "bottom", "shape": "inner_left"}))
        editor.placeBlock((x,y+2,z),Block(u_id))
        
        editor.placeBlock((x-1,y+2,z),Block(r_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y+2,z),Block(r_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+3,z),Block(r_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-2,y,z),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+2,y,z),Block(e_id,{"type": "top"}))
    def top3(x,y,z):
        editor.placeBlock((x,y,z),Block(t_id))
        editor.placeBlock((x,y+4,z-1),Block(q_id))
        editor.placeBlock((x,y+4,z+1),Block(q_id))
        editor.placeBlock((x,y+3,z-2),Block(q_id))
        editor.placeBlock((x,y+3,z+2),Block(q_id))
        editor.placeBlock((x,y+2,z-3),Block(q_id))
        editor.placeBlock((x,y+2,z+3),Block(q_id))
        editor.placeBlock((x,y+1,z-4),Block(q_id))
        editor.placeBlock((x,y+1,z+4),Block(q_id))
        editor.placeBlock((x,y,z-5),Block(q_id))
        editor.placeBlock((x,y,z+5),Block(q_id))
        
        editor.placeBlock((x,y+4,z),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+3,z-1),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+3,z+1),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+2,z-2),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+2,z+2),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+1,z-3),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+1,z+3),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z-4),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z+4),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))

        editor.placeBlock((x+1,y+2,z),Block(y_id,{"facing": "east", "half": "bottom", "open": "true"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z-1),Block(r_id,{"facing": "south", "half": "bottom", "shape": "inner_right"}))
        editor.placeBlock((x,y+1,z+1),Block(r_id,{"facing": "north", "half": "bottom", "shape": "inner_left"}))
        editor.placeBlock((x,y+2,z),Block(u_id))
        
        editor.placeBlock((x,y+2,z-1),Block(r_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+2,z+1),Block(r_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+3,z),Block(r_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x,y,z+2),Block(e_id,{"type": "top"}))
    def top4(x,y,z):
        editor.placeBlock((x,y,z),Block(t_id))
        editor.placeBlock((x,y+4,z-1),Block(q_id))
        editor.placeBlock((x,y+4,z+1),Block(q_id))
        editor.placeBlock((x,y+3,z-2),Block(q_id))
        editor.placeBlock((x,y+3,z+2),Block(q_id))
        editor.placeBlock((x,y+2,z-3),Block(q_id))
        editor.placeBlock((x,y+2,z+3),Block(q_id))
        editor.placeBlock((x,y+1,z-4),Block(q_id))
        editor.placeBlock((x,y+1,z+4),Block(q_id))
        editor.placeBlock((x,y,z-5),Block(q_id))
        editor.placeBlock((x,y,z+5),Block(q_id))
        
        editor.placeBlock((x,y+4,z),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+3,z-1),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+3,z+1),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+2,z-2),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+2,z+2),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+1,z-3),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+1,z+3),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z-4),Block(r_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z+4),Block(r_id,{"facing": "north", "half": "top", "shape": "straight"}))

        editor.placeBlock((x-1,y+2,z),Block(y_id,{"facing": "west", "half": "bottom", "open": "true"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z-1),Block(r_id,{"facing": "south", "half": "bottom", "shape": "inner_right"}))
        editor.placeBlock((x,y+1,z+1),Block(r_id,{"facing": "north", "half": "bottom", "shape": "inner_left"}))
        editor.placeBlock((x,y+2,z),Block(u_id))
        
        editor.placeBlock((x,y+2,z-1),Block(r_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+2,z+1),Block(r_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+3,z),Block(r_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x,y,z+2),Block(e_id,{"type": "top"}))
    top1(x,y,z+16)
    top2(x,y,z-16)
    top3(x+16,y,z)
    top4(x-16,y,z)

    for xx in range(11):
        editor.placeBlock((x+15-xx,y,z+5),Block(w_id))
        editor.placeBlock((x-15+xx,y,z+5),Block(w_id))
        editor.placeBlock((x+15-xx,y,z-5),Block(w_id))
        editor.placeBlock((x-15+xx,y,z-5),Block(w_id))
    for zz in range(11):
        editor.placeBlock((x+5,y,z+15-zz),Block(w_id))
        editor.placeBlock((x+5,y,z-15+zz),Block(w_id))
        editor.placeBlock((x-5,y,z+15-zz),Block(w_id))
        editor.placeBlock((x-5,y,z-15+zz),Block(w_id))
    for xx in range(12):
        editor.placeBlock((x+15-xx,y+1,z+4),Block(w_id))
        editor.placeBlock((x-15+xx,y+1,z+4),Block(w_id))
        editor.placeBlock((x+15-xx,y+1,z-4),Block(w_id))
        editor.placeBlock((x-15+xx,y+1,z-4),Block(w_id))
    for zz in range(12):
        editor.placeBlock((x+4,y+1,z+15-zz),Block(w_id))
        editor.placeBlock((x+4,y+1,z-15+zz),Block(w_id))
        editor.placeBlock((x-4,y+1,z+15-zz),Block(w_id))
        editor.placeBlock((x-4,y+1,z-15+zz),Block(w_id))
    for xx in range(13):
        editor.placeBlock((x+15-xx,y+2,z+3),Block(w_id))
        editor.placeBlock((x-15+xx,y+2,z+3),Block(w_id))
        editor.placeBlock((x+15-xx,y+2,z-3),Block(w_id))
        editor.placeBlock((x-15+xx,y+2,z-3),Block(w_id))
    for zz in range(13):
        editor.placeBlock((x+3,y+2,z+15-zz),Block(w_id))
        editor.placeBlock((x+3,y+2,z-15+zz),Block(w_id))
        editor.placeBlock((x-3,y+2,z+15-zz),Block(w_id))
        editor.placeBlock((x-3,y+2,z-15+zz),Block(w_id))
    for xx in range(14):
        editor.placeBlock((x+15-xx,y+3,z+2),Block(w_id))
        editor.placeBlock((x-15+xx,y+3,z+2),Block(w_id))
        editor.placeBlock((x+15-xx,y+3,z-2),Block(w_id))
        editor.placeBlock((x-15+xx,y+3,z-2),Block(w_id))
    for zz in range(14):
        editor.placeBlock((x+2,y+3,z+15-zz),Block(w_id))
        editor.placeBlock((x+2,y+3,z-15+zz),Block(w_id))
        editor.placeBlock((x-2,y+3,z+15-zz),Block(w_id))
        editor.placeBlock((x-2,y+3,z-15+zz),Block(w_id))
    for xx in range(15):
        editor.placeBlock((x+15-xx,y+4,z+1),Block(w_id))
        editor.placeBlock((x-15+xx,y+4,z+1),Block(w_id))
        editor.placeBlock((x+15-xx,y+4,z-1),Block(w_id))
        editor.placeBlock((x-15+xx,y+4,z-1),Block(w_id))
    for zz in range(15):
        editor.placeBlock((x+1,y+4,z+15-zz),Block(w_id))
        editor.placeBlock((x+1,y+4,z-15+zz),Block(w_id))
        editor.placeBlock((x-1,y+4,z+15-zz),Block(w_id))
        editor.placeBlock((x-1,y+4,z-15+zz),Block(w_id))

    for xx in range(6):
        editor.placeBlock((x+6+2*xx,y,z-6),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-6-2*xx,y,z-6),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+6+2*xx,y,z+6),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-6-2*xx,y,z+6),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x+5+2*xx,y+1,z-5),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-5-2*xx,y+1,z-5),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+5+2*xx,y+1,z+5),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-5-2*xx,y+1,z+5),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x+4+2*xx,y+2,z-4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-4-2*xx,y+2,z-4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+4+2*xx,y+2,z+4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-4-2*xx,y+2,z+4),Block(e_id,{"type": "bottom"}))
    for zz in range(6):
        editor.placeBlock((x-6,y,z+6+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-6,y,z-6-2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+6,y,z+6+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+6,y,z-6-2*zz),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x-5,y+1,z+5+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-5,y+1,z-5-2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+5,y+1,z+5+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+5,y+1,z-5-2*zz),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x-4,y+2,z+4+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-4,y+2,z-4-2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+4,y+2,z+4+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+4,y+2,z-4-2*zz),Block(e_id,{"type": "bottom"}))
    for xx in range(7):
        editor.placeBlock((x+3+2*xx,y+3,z-3),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-3-2*xx,y+3,z-3),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+3+2*xx,y+3,z+3),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-3-2*xx,y+3,z+3),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x+2+2*xx,y+4,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2-2*xx,y+4,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+4,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2-2*xx,y+4,z+2),Block(e_id,{"type": "bottom"}))
    for zz in range(7):
        editor.placeBlock((x-3,y+3,z+3+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-3,y+3,z-3-2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+3,y+3,z+3+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+3,y+3,z-3-2*zz),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x-2,y+4,z+2+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y+4,z-2-2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y+4,z+2+2*zz),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y+4,z-2-2*zz),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x,y+6,z),Block(p_id))

        editor.placeBlock((x,y+6,z+1),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+2),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+6,z+3),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+4),Block(o_id,{"type": "top"}))
        editor.placeBlock((x,y+7,z+5),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+6),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+5),Block(u_id))
        editor.placeBlock((x-1,y+6,z+5),Block(y_id,{"facing": "west", "half": "top", "open": "true"}))
        editor.placeBlock((x+1,y+6,z+5),Block(y_id,{"facing": "east", "half": "top", "open": "true"}))

        editor.placeBlock((x,y+6,z-1),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-2),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+6,z-3),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-4),Block(o_id,{"type": "top"}))
        editor.placeBlock((x,y+7,z-5),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-6),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-5),Block(u_id))
        editor.placeBlock((x-1,y+6,z-5),Block(y_id,{"facing": "west", "half": "top", "open": "true"}))
        editor.placeBlock((x+1,y+6,z-5),Block(y_id,{"facing": "east", "half": "top", "open": "true"}))

        editor.placeBlock((x-1,y+6,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-2,y+6,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x-3,y+6,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-4,y+6,z),Block(o_id,{"type": "top"}))
        editor.placeBlock((x-5,y+7,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-6,y+6,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-5,y+6,z),Block(u_id))
        editor.placeBlock((x-5,y+6,z-1),Block(y_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x-5,y+6,z+1),Block(y_id,{"facing": "south", "half": "top", "open": "true"}))

        editor.placeBlock((x+1,y+6,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+2,y+6,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x+3,y+6,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+4,y+6,z),Block(o_id,{"type": "top"}))
        editor.placeBlock((x+5,y+7,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+6,y+6,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+5,y+6,z),Block(u_id))
        editor.placeBlock((x+5,y+6,z-1),Block(y_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x+5,y+6,z+1),Block(y_id,{"facing": "south", "half": "top", "open": "true"}))


        editor.placeBlock((x+17,y+5,z),Block(i_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+17,y+6,z),Block(q_id))
        editor.placeBlock((x+17,y+7,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+16,y+6,z),Block(i_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+16,y+7,z),Block(q_id))
        editor.placeBlock((x+16,y+8,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+15,y+6,z),Block(i_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+13,y+6,z),Block(i_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+14,y+8,z),Block(i_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+15,y+7,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+14,y+6,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+13,y+8,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+12,y+6,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+12,y+8,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x+11,y+6,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x+10,y+6,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x+15,y+8,z),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x+15,y+9,z),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x+14,y+9,z),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x+12,y+7,z),Block(u_id))

        editor.placeBlock((x-17,y+5,z),Block(i_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-17,y+6,z),Block(q_id))
        editor.placeBlock((x-17,y+7,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-16,y+6,z),Block(i_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-16,y+7,z),Block(q_id))
        editor.placeBlock((x-16,y+8,z),Block(i_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-15,y+6,z),Block(i_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-13,y+6,z),Block(i_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-14,y+8,z),Block(i_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-15,y+7,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-14,y+6,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-13,y+8,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-12,y+6,z),Block(i_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-12,y+8,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x-11,y+6,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x-10,y+6,z),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x-15,y+8,z),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x-15,y+9,z),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+9,z),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+7,z),Block(u_id))

        editor.placeBlock((x,y+5,z-17),Block(i_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-17),Block(q_id))
        editor.placeBlock((x,y+7,z-17),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-16),Block(i_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+7,z-16),Block(q_id))
        editor.placeBlock((x,y+8,z-16),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-15),Block(i_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-13),Block(i_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+8,z-14),Block(i_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+7,z-15),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-14),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+8,z-13),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z-12),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+8,z-12),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+6,z-11),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+6,z-10),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+8,z-15),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x,y+9,z-15),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x,y+9,z-14),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x,y+7,z-12),Block(u_id))

        editor.placeBlock((x,y+5,z+17),Block(i_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+17),Block(q_id))
        editor.placeBlock((x,y+7,z+17),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+16),Block(i_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+7,z+16),Block(q_id))
        editor.placeBlock((x,y+8,z+16),Block(i_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+15),Block(i_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+13),Block(i_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+8,z+14),Block(i_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+7,z+15),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+14),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+8,z+13),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+6,z+12),Block(i_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+8,z+12),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+6,z+11),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+6,z+10),Block(o_id,{"type": "bottom"}))
        editor.placeBlock((x,y+8,z+15),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x,y+9,z+15),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x,y+9,z+14),Block(a_id,{"type": "bottom"}))
        editor.placeBlock((x,y+7,z+12),Block(u_id))






def floor(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    def floor_Z(x,y,z):
        for xx in range(2):
            for zz in range(9):
                editor.placeBlock((x-4+8*xx,y,z-4+zz),Block(q_id))
                editor.placeBlock((x-2+4*xx,y,z-4+zz),Block(e_id))
                editor.placeBlock((x-3+6*xx,y,z-4+zz),Block(w_id))
            editor.placeBlock((x-2+4*xx,y,z),Block(r_id))
        for xx in range(3):
            for zz in range(9):
                editor.placeBlock((x-1+xx,y,z-4+zz),Block(w_id))
    def floor_X(x,y,z):
        for zz in range(2):
            for xx in range(9):
                editor.placeBlock((x-4+xx,y,z-4+8*zz),Block(q_id))
                editor.placeBlock((x-4+xx,y,z-2+4*zz),Block(e_id))
                editor.placeBlock((x-4+xx,y,z-3+6*zz),Block(w_id))
            editor.placeBlock((x,y,z-2+4*zz),Block(r_id))
        for zz in range(3):
            for xx in range(9):
                editor.placeBlock((x-4+xx,y,z-1+zz),Block(w_id))
    def floor_z(x,y,z):
        for xx in range(9):
            for zz in range(9):
                editor.placeBlock((x-4+xx,y,z-4+zz),Block(w_id))
        editor.placeBlock((x,y,z),Block(t_id))
        editor.placeBlock((x+4,y,z+4),Block(q_id))
        editor.placeBlock((x-4,y,z-4),Block(q_id))
        editor.placeBlock((x+4,y,z-4),Block(q_id))
        editor.placeBlock((x-4,y,z+4),Block(q_id))
        editor.placeBlock((x+1,y,z+1),Block(q_id))
        editor.placeBlock((x-1,y,z+1),Block(q_id))
        editor.placeBlock((x-1,y,z-1),Block(q_id))
        editor.placeBlock((x+1,y,z-1),Block(q_id))
        for t in range(2):
            editor.placeBlock((x+2+t,y,z+2+t),Block(e_id))
            editor.placeBlock((x-2-t,y,z+2+t),Block(e_id))
            editor.placeBlock((x+2+t,y,z-2-t),Block(e_id))
            editor.placeBlock((x-2-t,y,z-2-t),Block(e_id))

    for zz in range(2):
        floor_Z(x,y,z-31-9*zz)       
        floor_z(x-9,y,z-31-9*zz)
        floor_z(x+9,y,z-31-9*zz)
        floor_Z(x,y,z+31+9*zz)       
        floor_z(x-9,y,z+31+9*zz)
        floor_z(x+9,y,z+31+9*zz)
    
    
    for zz in range(5):
        editor.placeBlock((x-13,y+1,z-24-5*zz),Block(q_id))
        editor.placeBlock((x-13,y+2,z-24-5*zz),Block(y_id,{"type": "bottom"}))
        editor.placeBlock((x+13,y+1,z-24-5*zz),Block(q_id))
        editor.placeBlock((x+13,y+2,z-24-5*zz),Block(y_id,{"type": "bottom"}))
        editor.placeBlock((x-13,y+1,z+24+5*zz),Block(q_id))
        editor.placeBlock((x-13,y+2,z+24+5*zz),Block(y_id,{"type": "bottom"}))
        editor.placeBlock((x+13,y+1,z+24+5*zz),Block(q_id))
        editor.placeBlock((x+13,y+2,z+24+5*zz),Block(y_id,{"type": "bottom"}))
    for zz in range(4):
        for zzz in range(4):
            editor.placeBlock((x-13,y+1,z-25-zz-5*zzz),Block(u_id,{"type": "top"}))
            editor.placeBlock((x+13,y+1,z-25-zz-5*zzz),Block(u_id,{"type": "top"}))
            editor.placeBlock((x-13,y+1,z+25+zz+5*zzz),Block(u_id,{"type": "top"}))
            editor.placeBlock((x+13,y+1,z+25+zz+5*zzz),Block(u_id,{"type": "top"}))
    for zz in range(3):
        for xx in range(9):
            editor.placeBlock((x-5-xx,y,z-24-zz),Block(w_id))
            editor.placeBlock((x+5+xx,y,z-24-zz),Block(w_id))
            editor.placeBlock((x-5-xx,y,z+24+zz),Block(w_id))
            editor.placeBlock((x+5+xx,y,z+24+zz),Block(w_id))

    
    

def stairs(x,y,z,q_id,w_id,e_id,r_id,t_id):
    def stairs1(x,y,z):
        for xx in range(2):
            for zz in range(3):
                editor.placeBlock((x-6-xx,y+13,z-3-zz),Block(q_id))
        for yy in range(2):
            for xx in range(2):
                editor.placeBlock((x-6-xx,y+yy,z+9-yy),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-6-xx,y+yy,z+8-yy),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x-9+yy,y+yy,z+6+zz),Block(w_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-8+yy,y+yy,z+6+zz),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x-4-yy,y+yy,z+6+zz),Block(w_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-5-yy,y+yy,z+6+zz),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
        for yy in range(11):
            for xx in range(2):
                editor.placeBlock((x-6-xx,y+2+yy,z+5-yy),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-6-xx,y+2+yy,z+4-yy),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-7,y+13,z-6),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))

        for xx in range(2):
            editor.placeBlock((x-7+xx,y+14,z-2),Block(r_id))
            for zz in range(4):
                editor.placeBlock((x-8+3*xx,y+14,z-2-zz),Block(r_id))

        editor.placeBlock((x-8,y+15,z-2),Block(t_id))
        editor.placeBlock((x-5,y+15,z-2),Block(t_id))
        editor.placeBlock((x-8,y+15,z-5),Block(t_id))
        editor.placeBlock((x-5,y+15,z-5),Block(t_id))

        editor.placeBlock((x-7,y-1,z+7),Block("glowstone"))
        editor.placeBlock((x-7,y,z+7),Block("acacia_trapdoor",{"facing": "north", "half": "bottom"}))
        


    def stairs12(x,y,z):
        for xx in range(2):
            for zz in range(3):
                editor.placeBlock((x-6-xx,y+13,z-3-zz),Block(q_id))
        for yy in range(2):
            for xx in range(2):
                editor.placeBlock((x-6-xx,y+yy,z+9-yy),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-6-xx,y+yy,z+8-yy),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x-9+yy,y+yy,z+6+zz),Block(w_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-8+yy,y+yy,z+6+zz),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x-4-yy,y+yy,z+6+zz),Block(w_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-5-yy,y+yy,z+6+zz),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
        for yy in range(11):
            for xx in range(2):
                editor.placeBlock((x-6-xx,y+2+yy,z+5-yy),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-6-xx,y+2+yy,z+4-yy),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-6,y+13,z-6),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))

        for xx in range(2):
            editor.placeBlock((x-7+xx,y+14,z-2),Block(r_id))
            for zz in range(4):
                editor.placeBlock((x-8+3*xx,y+14,z-2-zz),Block(r_id))

        editor.placeBlock((x-8,y+15,z-2),Block(t_id))
        editor.placeBlock((x-5,y+15,z-2),Block(t_id))
        editor.placeBlock((x-8,y+15,z-5),Block(t_id))
        editor.placeBlock((x-5,y+15,z-5),Block(t_id))

        editor.placeBlock((x-6,y-1,z+7),Block("glowstone"))
        editor.placeBlock((x-6,y,z+7),Block("acacia_trapdoor",{"facing": "north", "half": "bottom"}))

    stairs1(x,y,z)
    stairs12(x+13,y,z)
    for xx in range(4):
            editor.placeBlock((x-12-xx,y+21,z-3),Block(q_id))
            editor.placeBlock((x+12+xx,y+21,z-3),Block(q_id))
    
def stairs2(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for xx in range(4):
            editor.placeBlock((x-12-xx,y+21,z-3),Block(q_id))
            editor.placeBlock((x+12+xx,y+21,z-3),Block(q_id))
    for yy in range(5):
        editor.placeBlock((x-11,y+14+yy,z+3),Block(q_id))
        editor.placeBlock((x+11,y+14+yy,z+3),Block(q_id))
    def staris21(x,y,z):
        for yy in range(2):
            for xx in range(2):
                editor.placeBlock((x-xx,y+yy,z-yy),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-xx,y+yy,z-1-yy),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x-3+yy,y+yy,z-3+zz),Block(w_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-2+yy,y+yy,z-3+zz),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x+2-yy,y+yy,z-3+zz),Block(w_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x+1-yy,y+yy,z-3+zz),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
        for yy in range(5):
            for xx in range(2):
                editor.placeBlock((x-xx,y+2+yy,z-4-yy),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-xx,y+2+yy,z-5-yy),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))

    staris21(x-13,y+14,z+6)
    staris21(x+14,y+14,z+6)
    for zz in range(2):
        for xx in range(5):
            editor.placeBlock((x-5-xx,y+27,z-2-zz),Block(q_id))
            editor.placeBlock((x+5+xx,y+27,z-2-zz),Block(q_id))
    def staris22(x,y,z):
        for yy in range(7):
            for zz in range(2):
                editor.placeBlock((x+yy,y+yy,z+zz),Block(w_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x+1+yy,y+yy,z+zz),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
    def staris23(x,y,z):
        for yy in range(7):
            for zz in range(2):
                editor.placeBlock((x-yy,y+yy,z+zz),Block(w_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
                editor.placeBlock((x-1-yy,y+yy,z+zz),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
    staris22(x-12,y+21,z-3) 
    staris23(x+12,y+21,z-3) 
    for xx in range(5):
        editor.placeBlock((x+6+xx,y+28,z-4),Block(r_id))
        editor.placeBlock((x+6+xx,y+28,z-1),Block(r_id))
        editor.placeBlock((x-6-xx,y+28,z-4),Block(r_id))
        editor.placeBlock((x-6-xx,y+28,z-1),Block(r_id))
    for zz in range(2):
        editor.placeBlock((x+10,y+28,z-2-zz),Block(r_id))
        editor.placeBlock((x-10,y+28,z-2-zz),Block(r_id))
    editor.placeBlock((x+10,y+29,z-4),Block(t_id))
    editor.placeBlock((x+10,y+29,z-1),Block(t_id))
    editor.placeBlock((x+6,y+29,z-4),Block(t_id))
    editor.placeBlock((x+6,y+29,z-1),Block(t_id))

    editor.placeBlock((x-10,y+29,z-4),Block(t_id))
    editor.placeBlock((x-10,y+29,z-1),Block(t_id))
    editor.placeBlock((x-6,y+29,z-4),Block(t_id))
    editor.placeBlock((x-6,y+29,z-1),Block(t_id))

def pool(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id):
    for yy in range(3):
        for zz in range(39):
            for xx in range(20):
                editor.placeBlock((x-24-xx,y-yy,z+5+zz),Block(q_id))
                editor.placeBlock((x+24+xx,y-yy,z+5+zz),Block(q_id))
                editor.placeBlock((x+24+xx,y-yy,z-5-zz),Block(q_id))
                editor.placeBlock((x-24-xx,y-yy,z-5-zz),Block(q_id))
        for zz in range(30):
            for xx in range(11):
                editor.placeBlock((x-14-xx,y-yy,z+14+zz),Block(q_id))
                editor.placeBlock((x+14+xx,y-yy,z+14+zz),Block(q_id))
                editor.placeBlock((x+14+xx,y-yy,z-14-zz),Block(q_id))
                editor.placeBlock((x-14-xx,y-yy,z-14-zz),Block(q_id))

        for zz in range(19):
            for xx in range(20):
                editor.placeBlock((x-24-xx,y-yy,z+5+2*zz),Block(w_id))
                editor.placeBlock((x+24+xx,y-yy,z+5+2*zz),Block(w_id))
                editor.placeBlock((x+24+xx,y-yy,z-5-2*zz),Block(w_id))
                editor.placeBlock((x-24-xx,y-yy,z-5-2*zz),Block(w_id))
        for zz in range(15):
            for xx in range(11):
                editor.placeBlock((x-14-xx,y-yy,z+14+2*zz),Block(w_id))
                editor.placeBlock((x+14+xx,y-yy,z+14+2*zz),Block(w_id))
                editor.placeBlock((x+14+xx,y-yy,z-14-2*zz),Block(w_id))
                editor.placeBlock((x-14-xx,y-yy,z-14-2*zz),Block(w_id))
    def flower(x,y,z):
        for i in range(4):
            editor.placeBlock((x+random.randint(-2,2),y+1,z+random.randint(-2,2)),Block(t_id))
        editor.placeBlock((x+1,y,z),Block(t_id))
        editor.placeBlock((x,y,z),Block(e_id,{"facing":"east","half":"top","open":"false"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"waterlogged":"false"}))
        editor.placeBlock((x+1,y,z),Block(w_id))
    
    def kelp(x,y,z):
        editor.placeBlock((x,y,z),Block(i_id))
        editor.placeBlock((x,y+1,z),Block(p_id))
    def grass(x,y,z):
        for i in range(6):
            editor.placeBlock((x+random.randint(-2,2),y,z+random.randint(-2,2)),Block(u_id))
        for i in range(3):           
            kelp(x+random.randint(-2,2),y,z+random.randint(-2,2))
        editor.placeBlock((x+random.randint(-1,1),y,z+random.randint(-1,1)),Block(o_id,{"pickles":"4"}))

    for i in range(8):
        flower(x-33-random.randint(0,7),y,z-8-random.randint(0,25))
        flower(x+33+random.randint(0,7),y,z-8-random.randint(0,25))
        flower(x+33+random.randint(0,7),y,z+8+random.randint(0,25))
        flower(x-33-random.randint(0,7),y,z+8+random.randint(0,25))

        grass(x-33-random.randint(0,7),y-2,z-8-random.randint(0,25))
        grass(x+33+random.randint(0,7),y-2,z-8-random.randint(0,25))
        grass(x+33+random.randint(0,7),y-2,z+8+random.randint(0,25))
        grass(x-33-random.randint(0,7),y-2,z+8+random.randint(0,25))
    for i in range(6):
        flower(x-26-random.randint(0,5),y,z-7-random.randint(0,21))
        flower(x+26+random.randint(0,5),y,z-7-random.randint(0,21))
        flower(x+26+random.randint(0,5),y,z+7+random.randint(0,21))
        flower(x-26-random.randint(0,5),y,z+7+random.randint(0,21))

        grass(x-26-random.randint(0,5),y-2,z-7-random.randint(0,21))
        grass(x+26+random.randint(0,5),y-2,z-7-random.randint(0,21))
        grass(x+26+random.randint(0,5),y-2,z+7+random.randint(0,21))
        grass(x-26-random.randint(0,5),y-2,z+7+random.randint(0,21))
    for i in range(3):
        flower(x-23-random.randint(0,4),y,z-18-random.randint(0,14))
        flower(x+23+random.randint(0,4),y,z-18-random.randint(0,14))
        flower(x+23+random.randint(0,4),y,z+18+random.randint(0,14))
        flower(x-23-random.randint(0,4),y,z+18+random.randint(0,14))

        grass(x-23-random.randint(0,4),y-2,z-18-random.randint(0,14))
        grass(x+23+random.randint(0,4),y-2,z-18-random.randint(0,14))
        grass(x+23+random.randint(0,4),y-2,z+18+random.randint(0,14))
        grass(x-23-random.randint(0,4),y-2,z+18+random.randint(0,14))
    for i in range(4):
        flower(x-16-random.randint(0,3),y,z-22-random.randint(0,18))
        flower(x+16+random.randint(0,3),y,z-22-random.randint(0,18))
        flower(x+16+random.randint(0,3),y,z+22+random.randint(0,18))
        flower(x-16-random.randint(0,3),y,z+22+random.randint(0,18))

        grass(x-16-random.randint(0,3),y-2,z-22-random.randint(0,18))
        grass(x+16+random.randint(0,3),y-2,z-22-random.randint(0,18))
        grass(x+16+random.randint(0,3),y-2,z+22+random.randint(0,18))
        grass(x-16-random.randint(0,3),y-2,z+22+random.randint(0,18))



def furnitur1(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    #q_idをe_idに
    editor.placeBlock((x,y,z),Block(e_id))
    editor.placeBlock((x+5,y,z-3),Block(e_id))
    editor.placeBlock((x-5,y,z-3),Block(e_id))
    editor.placeBlock((x+5,y,z+4),Block(e_id))
    editor.placeBlock((x-5,y,z+4),Block(e_id))
    for xx in range(13):
        editor.placeBlock((x-6+xx,y,z-6),Block(e_id))
        for zz in range(10):
            editor.placeBlock((x-6+xx,y,z-4+zz),Block(q_id))
            editor.placeBlock((x-6+xx,y+1,z-4+zz),Block(w_id))


    editor.placeBlock((x,y,z-5),Block(e_id))
    for xx in range(7):
        editor.placeBlock((x-3+xx,y,z-7),Block(e_id))
        editor.placeBlock((x-3+xx,y+1,z-6),Block(o_id,{"facing": "north", "half": "top", "shape": "straight"}))
    for xx in range(3):
        editor.placeBlock((x-5-xx,y,z-5),Block(r_id))
        editor.placeBlock((x+5+xx,y,z-5),Block(r_id))
    for xx in range(4):
        editor.placeBlock((x-4-xx,y,z-7),Block(r_id))
        editor.placeBlock((x+4+xx,y,z-7),Block(r_id))
        editor.placeBlock((x+5+xx,y,z-8),Block(y_id,{"type": "top"}))
        editor.placeBlock((x-5-xx,y,z-8),Block(y_id,{"type": "top"}))
    editor.placeBlock((x+7,y,z-6),Block(r_id))
    editor.placeBlock((x-7,y,z-6),Block(r_id))
    for xx in range(2):
        editor.placeBlock((x-1-xx,y,z-5),Block(t_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1+xx,y,z-5),Block(t_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+7+xx,y,z-4),Block(y_id,{"type": "top"}))
        editor.placeBlock((x-7-xx,y,z-4),Block(y_id,{"type": "top"}))
        editor.placeBlock((x-5-xx,y+1,z-6),Block(i_id))
        editor.placeBlock((x+5+xx,y+1,z-6),Block(i_id))
    editor.placeBlock((x-4,y,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "inner_right"}))
    editor.placeBlock((x-1,y,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "inner_left"}))
    editor.placeBlock((x+4,y,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "inner_right"}))
    editor.placeBlock((x+1,y,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "inner_left"}))
    for zz in range(3):
        editor.placeBlock((x+8,y,z-5-zz),Block(y_id,{"type": "top"}))
        editor.placeBlock((x-8,y,z-5-zz),Block(y_id,{"type": "top"}))
    for zz in range(7):
        editor.placeBlock((x-3+xx,y,z-8),Block(u_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-4,y,z-8),Block(u_id,{"facing": "west", "half": "bottom", "shape": "inner_left"}))
    editor.placeBlock((x+4,y,z-8),Block(u_id,{"facing": "east", "half": "bottom", "shape": "inner_right"}))

    for yy in range(3):
        for xx in range(13):
            editor.placeBlock((x-6+xx,y+2+yy,z-6),Block(i_id))
    editor.placeBlock((x-4,y+1,z-6),Block(o_id,{"facing": "west", "half": "top", "shape": "inner_right"}))
    editor.placeBlock((x+4,y+1,z-6),Block(o_id,{"facing": "east", "half": "top", "shape": "inner_left"}))

    # right
    editor.placeBlock((x+6,y+1,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+6,y+1,z-7),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+6,y+4,z-5),Block(t_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+6,y+4,z-7),Block(t_id,{"facing": "east", "half": "top", "shape": "straight"}))
    for zz in range(3):
        editor.placeBlock((x+7,y+1,z-5-zz),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+7,y+2,z-5-zz),Block(t_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+7,y+4,z-5-zz),Block(t_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+5,y+1,z-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+5,y+1,z-7),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+4,y+1,z-7),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+4,y+1,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+4,y+2,z-5),Block(a_id,{"facing": "up"}))
    editor.placeBlock((x+3,y+1,z-7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+3,y+2,z-7),Block(a_id,{"facing": "up"}))
    editor.placeBlock((x+6,y+2,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+6,y+2,z-7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+7,y+3,z-6),Block(s_id))
    editor.placeBlock((x+7,y+5,z-6),Block(s_id))
    editor.placeBlock((x+7,y+5,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+7,y+5,z-7),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+6,y+5,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+6,y+5,z-7),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+5,y+4,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+5,y+4,z-7),Block(p_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x+5-xx,y+5,z-5),Block(p_id,{"type": "bottom"}))
        editor.placeBlock((x+5-xx,y+5,z-7),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+6,y+6,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+5,y+6,z-5),Block(t_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+4,y+6,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+6,y+6,z-7),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+5,y+6,z-7),Block(t_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+4,y+6,z-7),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+3,y+6,z-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+3,y+6,z-7),Block(p_id,{"type": "bottom"}))
    # left
    editor.placeBlock((x-6,y+1,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-6,y+1,z-7),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-6,y+4,z-5),Block(t_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-6,y+4,z-7),Block(t_id,{"facing": "west", "half": "top", "shape": "straight"}))
    for zz in range(3):
        editor.placeBlock((x-7,y+1,z-5-zz),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-7,y+2,z-5-zz),Block(t_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-7,y+4,z-5-zz),Block(t_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-5,y+1,z-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+1,z-7),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-4,y+1,z-7),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-4,y+1,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-4,y+2,z-5),Block(a_id,{"facing": "up"}))
    editor.placeBlock((x-3,y+1,z-7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-3,y+2,z-7),Block(a_id,{"facing": "up"}))
    editor.placeBlock((x-6,y+2,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-6,y+2,z-7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-7,y+3,z-6),Block(s_id))
    editor.placeBlock((x-7,y+5,z-6),Block(s_id))
    editor.placeBlock((x-7,y+5,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-7,y+5,z-7),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-6,y+5,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-6,y+5,z-7),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-5,y+4,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-5,y+4,z-7),Block(p_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x-5+xx,y+5,z-5),Block(p_id,{"type": "bottom"}))
        editor.placeBlock((x-5+xx,y+5,z-7),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-6,y+6,z-5),Block(t_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-5,y+6,z-5),Block(t_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-4,y+6,z-5),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-6,y+6,z-7),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-5,y+6,z-7),Block(t_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-4,y+6,z-7),Block(t_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-3,y+6,z-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+6,z-7),Block(p_id,{"type": "bottom"}))

def lantern(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    def lantern1(x,y,z):
        for xx in range(3):
            editor.placeBlock((x-1+xx,y,z),Block(q_id))
        for zz in range(3):
            editor.placeBlock((x,y,z-1+zz),Block(q_id))
        editor.placeBlock((x+1,y-1,z),Block(w_id))
        editor.placeBlock((x-1,y-1,z),Block(w_id))
        editor.placeBlock((x,y-1,z+1),Block(w_id))
        editor.placeBlock((x,y-1,z-1),Block(w_id))
        editor.placeBlock((x,y-1,z),Block(e_id))
        editor.placeBlock((x,y-2,z),Block(r_id))
        editor.placeBlock((x+1,y-2,z),Block(t_id,{"facing": "east"}))
        editor.placeBlock((x-1,y-2,z),Block(t_id,{"facing": "west"}))
        editor.placeBlock((x,y-2,z+1),Block(t_id,{"facing": "south"}))
        editor.placeBlock((x,y-2,z-1),Block(t_id,{"facing": "north"}))

    def lantern2_x(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        lantern1(x-2,y,z)
        lantern1(x+2,y,z)
    def lantern2_z(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        lantern1(x,y,z-2)
        lantern1(x,y,z+2)
    def lantern3_x(x,y,z):
        editor.placeBlock((x,y,z),Block(r_id))
        editor.placeBlock((x-1,y,z),Block(y_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(y_id,{"facing": "east", "half": "top", "shape": "straight"}))
        for yy in range(2):
            editor.placeBlock((x-2,y-yy,z),Block(y_id,{"facing": "west", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+2,y-yy,z),Block(y_id,{"facing": "east", "half": "top", "shape": "straight"}))
    def lantern3_z(x,y,z):
        editor.placeBlock((x,y,z),Block(r_id))
        editor.placeBlock((x,y,z-1),Block(y_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y,z+1),Block(y_id,{"facing": "south", "half": "top", "shape": "straight"}))
        for yy in range(2):
            editor.placeBlock((x,y-yy,z-2),Block(y_id,{"facing": "north", "half": "top", "shape": "straight"}))
            editor.placeBlock((x,y-yy,z+2),Block(y_id,{"facing": "south", "half": "top", "shape": "straight"}))

    #�^��
    def lantern1_c(x,y,z):
        lantern1(x,y,z)
        for zz in range(5):
            editor.placeBlock((x,y+1,z+2-zz),Block(q_id))
        for xx in range(5):
            editor.placeBlock((x+2-xx,y+1,z),Block(q_id))

    lantern2_x(x,y+10,z+9)
    lantern2_x(x,y+10,z+14)
    lantern2_x(x,y+10,z-14)
    lantern2_z(x-14,y+10,z)
    lantern2_z(x+14,y+10,z)

    lantern1(x+3,y+23,z+3)
    lantern1(x-3,y+23,z+3)
    lantern1(x-3,y+23,z-3)
    lantern1(x+3,y+23,z-3)
    lantern1(x+3,y+37,z+3)
    lantern1(x-3,y+37,z+3)
    lantern1(x-3,y+37,z-3)
    lantern1(x+3,y+37,z-3)
    lantern1_c(x,y+37,z)
    lantern1(x+3,y+51,z+3)
    lantern1(x-3,y+51,z+3)
    lantern1(x-3,y+51,z-3)
    lantern1(x+3,y+51,z-3)
    lantern1_c(x,y+51,z)



    for yy in range(3):
        lantern3_x(x,y+21+14*yy,z-11)
        lantern3_x(x,y+21+14*yy,z-16)
        lantern3_x(x,y+21+14*yy,z+11)
        lantern3_x(x,y+21+14*yy,z+16)
        lantern3_z(x-11,y+21+14*yy,z)
        lantern3_z(x-16,y+21+14*yy,z)
        lantern3_z(x+11,y+21+14*yy,z)
        lantern3_z(x+16,y+21+14*yy,z)
    

def table2(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for zz in range(8):
        editor.placeBlock((x-2,y,z-6+2*zz),Block(q_id))
        editor.placeBlock((x+2,y,z-6+2*zz),Block(q_id))
    editor.placeBlock((x,y,z-6),Block(q_id))
    editor.placeBlock((x,y,z+8),Block(q_id))
    for zz in range(7):
        editor.placeBlock((x-2,y,z-5+2*zz),Block(w_id,{"facing": "east"}))
        editor.placeBlock((x+2,y,z-5+2*zz),Block(w_id,{"facing": "east"}))
    for xx in range(5):
        for zz in range(15):
            editor.placeBlock((x-2+xx,y+1,z-6+zz),Block(e_id,{"facing": "east", "half": "bottom"}))
  
    for xx in range(2):
        editor.placeBlock((x-1+2*xx,y,z-8),Block(r_id))
        editor.placeBlock((x-1+2*xx,y+1,z-8),Block(t_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((x-1+2*xx,y,z+10),Block(r_id))
        editor.placeBlock((x-1+2*xx,y+1,z+10),Block(t_id,{"facing": "north", "half": "bottom", "open": "true"}))
    for zz in range(8):
        editor.placeBlock((x-4,y,z-6+2*zz),Block(r_id))
        editor.placeBlock((x-4,y+1,z-6+2*zz),Block(t_id,{"facing": "east", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+4,y,z-6+2*zz),Block(r_id))
        editor.placeBlock((x+4,y+1,z-6+2*zz),Block(t_id,{"facing": "west", "half": "bottom", "open": "true"}))
    editor.placeBlock((x,y-1,z),Block("glowstone"))
    editor.placeBlock((x,y-1,z-4),Block("glowstone"))
    editor.placeBlock((x,y-1,z+4),Block("glowstone"))




def pot(x,y,z,q_id,w_id,e_id):
    def pot2(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        editor.placeBlock((x+1,y,z),Block(w_id,{"facing": "east", "half": "top", "open": "true"}))
        editor.placeBlock((x-1,y,z),Block(w_id,{"facing": "west", "half": "top", "open": "true"}))
        editor.placeBlock((x,y,z+1),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
        editor.placeBlock((x,y,z-1),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x,y+1,z),Block(e_id))
        editor.placeBlock((x,y-1,z),Block("glowstone"))
    pot2(x-3,y+17,z+13)
    pot2(x+3,y+17,z+13)
    pot2(x-3,y+17,z-13)
    pot2(x+3,y+17,z-13)
    pot2(x+13,y+17,z-3)
    pot2(x-13,y+17,z-3)
    pot2(x+13,y+31,z-3)
    pot2(x-13,y+31,z-3)



def table3(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id):
    for xx in range(9):
        editor.placeBlock((x-4+xx,y,z-9),Block(q_id,{"facing": "south"}))
        editor.placeBlock((x-4+xx,y,z-10),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x-4+xx,y,z-8),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
    editor.placeBlock((x-1,y+1,z-9),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-1,y+2,z-9),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-1,y+3,z-9),Block(r_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+3,z-9),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-3,y+1,z-9),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-4,y+1,z-9),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-4,y+3,z-9),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-4,y+2,z-9),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-4,y+4,z-9),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-2,y+1,z-9),Block(w_id,{"facing": "east", "half": "top"}))
    editor.placeBlock((x-3,y+3,z-9),Block(w_id,{"facing": "east", "half": "bottom"}))

    editor.placeBlock((x+1,y+1,z-9),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+1,y+2,z-9),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+1,y+3,z-9),Block(r_id,{"type": "bottom"}))
    editor.placeBlock((x+2,y+3,z-9),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+3,y+1,z-9),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+4,y+1,z-9),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+4,y+3,z-9),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+4,y+2,z-9),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+4,y+4,z-9),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+2,y+1,z-9),Block(w_id,{"facing": "west", "half": "top"}))
    editor.placeBlock((x+3,y+3,z-9),Block(w_id,{"facing": "west", "half": "bottom"}))
    for xx in range(7):
        editor.placeBlock((x-3+xx,y+4,z-9),Block(r_id,{"type": "bottom"}))
    editor.placeBlock((x+3,y+4,z+6),Block(t_id))
    editor.placeBlock((x-3,y+4,z+6),Block(t_id))
    editor.placeBlock((x-3,y+4,z-6),Block(t_id))
    editor.placeBlock((x+3,y+4,z-6),Block(t_id))
    editor.placeBlock((x-3,y+2,z-9),Block(t_id))
    editor.placeBlock((x-2,y+2,z-9),Block(y_id))
    editor.placeBlock((x+3,y+2,z-9),Block(t_id))
    editor.placeBlock((x+2,y+2,z-9),Block(y_id))

    def table_t(x,y,z):
        editor.placeBlock((x,y,z),Block(u_id))
        for xx in range(2):
            editor.placeBlock((x-xx,y,z+1),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x-xx,y,z-1),Block(e_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y,z),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-1,y+1,z),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x,y+1,z+1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y+1,z-1),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y+1,z+1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z+1),Block(o_id))
        editor.placeBlock((x+1,y,z),Block(i_id))
    def table_f(x,y,z):
        editor.placeBlock((x,y,z),Block(u_id))
        for xx in range(2):
            editor.placeBlock((x+xx,y,z+1),Block(e_id,{"facing": "south", "half": "top", "shape": "straight"}))
            editor.placeBlock((x+xx,y,z-1),Block(e_id,{"facing": "north", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y,z),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x+1,y+1,z),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x,y+1,z+1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y+1,z-1),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y+1,z+1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z+1),Block(o_id))
        editor.placeBlock((x-1,y,z),Block(i_id))
    for zz in range(2):
        table_t(x-4,y,z+1+4*zz)
        table_f(x+4,y,z+1+4*zz)

    for zz in range(3):
        editor.placeBlock((x+3,y,z+8+zz),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x-3,y,z+8+zz),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
    for xx in range(5):
        editor.placeBlock((x-2+xx,y,z+10),Block(r_id,{"type": "top"}))
    for zz in range(2):
        editor.placeBlock((x+2,y,z+8+zz),Block(u_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y,z+8+zz),Block(u_id,{"type": "bottom"}))
    for xx in range(3):
        editor.placeBlock((x-1+xx,y,z+9),Block(p_id,{"facing": "south", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+1,y,z+8),Block(p_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-1,y,z+8),Block(p_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x,y,z+8),Block(a_id,{"type": "top"}))
    editor.placeBlock((x+2,y+1,z+10),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+3,y+1,z+10),Block(e_id,{"facing": "east", "half": "bottom", "shape": "inner_right"}))
    editor.placeBlock((x-2,y+1,z+10),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-3,y+1,z+10),Block(e_id,{"facing": "west", "half": "bottom", "shape": "inner_left"}))
    for xx in range(3):
        editor.placeBlock((x-1+xx,y+1,z+10),Block(r_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+1,z+9),Block(r_id,{"type": "bottom"}))
    editor.placeBlock((x+3,y+1,z+9),Block(r_id,{"type": "bottom"}))





def Firework_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for zz in range(4):
        for xx in range(19):
            editor.placeBlock((x-9+xx,y-1,z-zz),Block(i_id))
    for xx in range(7):
        for zz in range(2):
            editor.placeBlock((x-9+3*xx,y,z-zz),Block(q_id,{"facing": "up"}))
    
    for xx in range(7):
        editor.placeBlock((x-9+3*xx,y,z-2),Block(w_id))
    for xx in range(19):
        editor.placeBlock((x-9+xx,y,z-3),Block(w_id))
    editor.placeBlock((x,y,z-5),Block(e_id))
    editor.placeBlock((x,y,z-7),Block(e_id))
    for yy in range(2):
        editor.placeBlock((x,y+yy,z-6),Block(r_id))
    editor.placeBlock((x,y+1,z-7),Block(t_id,{"facing": "south"}))
    editor.placeBlock((x,y+2,z-7),Block(y_id,{"inverted": "false"}))
    for xx in range(3):
        for zz in range(4):
            editor.placeBlock((x-1+xx,y-1,z-4-zz),Block(u_id))
    for yy in range(3):
        for zz in range(5):
            editor.placeBlock((x-2,y-1+yy,z-4-zz),Block(i_id))
            editor.placeBlock((x+2,y-1+yy,z-4-zz),Block(i_id))
        for xx in range(3):
            editor.placeBlock((x-1+xx,y-1+yy,z-8),Block(i_id))
def fire(x,y,z):
    for xx in range(7):
        for zz in range(2):
            fire="firework_rocket{Fireworks:{Flight:9,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.0 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:7,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.1 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:8,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.2 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:10,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.3 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:8,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.4 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:9,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.5 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:10,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.6 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:8,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.7 {fire} 64"
            runCommand(command)
            fire="firework_rocket{Fireworks:{Flight:9,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;1017855,1370367,3590655,8567039,15531845,16733376,8912655,12876031]}]}}"
            command = f"replaceitem block {x-9+3*xx} {y} {z-zz} container.8 {fire} 64"
            runCommand(command)


def floor_light(x,y,z,u_id,g_id,c_id,r_id): #u_id=glowtone,g_id=glass,c_id=carpet r_id=red_carpet ���Ɩ�
    def light1(x,y,z):
        editor.placeBlock((x,y,z),Block(u_id))
        editor.placeBlock((x,y+1,z),Block(g_id))
        editor.placeBlock((x,y+2,z),Block(c_id))
    light1(x+11,y,z)
    light1(x+17,y,z)
    light1(x-11,y,z)
    light1(x-17,y,z)
    light1(x,y,z+11)
    light1(x,y,z+17)
    light1(x,y,z-11)
    light1(x,y,z-17)

    light1(x+14,y,z+8)
    light1(x+14,y,z-8)
    light1(x-14,y,z+8)
    light1(x-14,y,z-8)
    light1(x+8,y,z+14)
    light1(x+8,y,z-14)
    light1(x-8,y,z+14)
    light1(x-8,y,z-14)

    light1(x+20,y,z+10)
    light1(x+20,y,z-10)
    light1(x-20,y,z+10)
    light1(x-20,y,z-10)
    light1(x+10,y,z+20)
    light1(x+10,y,z-20)
    light1(x-10,y,z+20)
    light1(x-10,y,z-20)

    light1(x+11,y,z+11)
    light1(x+11,y,z-11)
    light1(x-11,y,z+11)
    light1(x-11,y,z-11)

    def light2(x,y,z):
        editor.placeBlock((x,y,z),Block(u_id))
        editor.placeBlock((x,y+1,z),Block(g_id))
        editor.placeBlock((x,y+2,z),Block(r_id))

    light2(x+13,y+14,z+4)
    light2(x+14,y+14,z+4)
    light2(x-13,y+14,z+4)
    light2(x-14,y+14,z+4)
    
    light2(x+8,y+14,z+8)
    light2(x+8,y+14,z-8)
    light2(x-8,y+14,z+8)
    light2(x-8,y+14,z-8)

    for yy in range(2):
        light2(x+13,y+28+yy*14,z+4)
        light2(x+14,y+28+yy*14,z+4)
        light2(x-13,y+28+yy*14,z+4)
        light2(x-14,y+28+yy*14,z+4)
        light2(x+15,y+28+yy*14,z-5)
        light2(x-15,y+28+yy*14,z-5)
        light2(x+5,y+28+yy*14,z+15)
        light2(x+5,y+28+yy*14,z-15)
        light2(x-5,y+28+yy*14,z+15)
        light2(x-5,y+28+yy*14,z-15)
        light2(x+7,y+28+yy*14,z+5)
        light2(x-7,y+28+yy*14,z+5)
        light2(x+5,y+28+yy*14,z+10)
        light2(x-5,y+28+yy*14,z+10)
        light2(x,y+28+yy*14,z+7)
        light2(x,y+28+yy*14,z-6)
    

def panda(x,y,z):
    X=x
    Z=z+35    
    command = f"summon panda {X} {y} {Z}"
    for i in range(4):
        runCommand(command)
    Z=z-35
    command = f"summon panda {X} {y} {Z}"
    for i in range(4):
        runCommand(command)
    
    X=x
    Y=y+6
    Z=z
    command = f"summon panda {X} {Y} {Z}"
    for i in range(4):
        runCommand(command)
    X=x+8
    Y=y+22
    command = f"summon panda {X} {Y} {Z}"
    for i in range(4):
        runCommand(command)
    X=x
    Y=y+35
    Z=z
    command = f"summon panda {X} {Y} {Z}"
    for i in range(4):
        runCommand(command)
    Y=y+47
    command = f"summon panda {X} {Y} {Z}"
    for i in range(4):
        runCommand(command)

def dragon_x1(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    #z+1
    for xx in range(4):
        for yy in range(3):
            editor.placeBlock((x-xx,y+yy,z+1),Block(q_id))
    editor.placeBlock((x-3,y-1,z+1),Block(q_id))
    editor.placeBlock((x-4,y+2,z+1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+1,z+1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-6,y+1,z+1),Block(q_id))
    editor.placeBlock((x-6,y,z+1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-7,y+1,z+1),Block(w_id,{"type": "bottom"}))
    for xx in range(2):
        editor.placeBlock((x-4-xx,y,z+1),Block(w_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x-4-xx,y-1,z+1),Block(w_id,{"type": "top"}))
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+2,z+1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-xx,y+3,z+1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+3+xx,y+4,z+1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+2,y+3,z+1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+3,z+1),Block(q_id))
    editor.placeBlock((x,y+4,z+1),Block(q_id))
    editor.placeBlock((x+1,y+4,z+1),Block(w_id,{"type": "bottom"}))
    for yy in range(2):
        editor.placeBlock((x+2,y+4+yy,z+1),Block(q_id))
    editor.placeBlock((x-3,y+1,z+1),Block(e_id))
    #z-1
    for xx in range(4):
        for yy in range(3):
            editor.placeBlock((x-xx,y+yy,z-1),Block(q_id))
    editor.placeBlock((x-3,y-1,z-1),Block(q_id))
    editor.placeBlock((x-4,y+2,z-1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+1,z-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-6,y+1,z-1),Block(q_id))
    editor.placeBlock((x-6,y,z-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-7,y+1,z-1),Block(w_id,{"type": "bottom"}))
    for xx in range(2):
        editor.placeBlock((x-4-xx,y,z-1),Block(w_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x-4-xx,y-1,z-1),Block(w_id,{"type": "top"}))
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+2,z-1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-xx,y+3,z-1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+3+xx,y+4,z-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+2,y+3,z-1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+3,z-1),Block(q_id))
    editor.placeBlock((x,y+4,z-1),Block(q_id))
    editor.placeBlock((x+1,y+4,z-1),Block(w_id,{"type": "bottom"}))
    for yy in range(2):
        editor.placeBlock((x+2,y+4+yy,z-1),Block(q_id))
    editor.placeBlock((x-3,y+1,z-1),Block(e_id))
    #z
    for xx in range(6):
        for yy in range(3):
            editor.placeBlock((x-xx,y+yy,z),Block(q_id))
    editor.placeBlock((x+1,y+2,z),Block(q_id))
    editor.placeBlock((x+2,y+3,z),Block(q_id))
    editor.placeBlock((x-2,y+4,z),Block(q_id))
    editor.placeBlock((x-8,y+2,z),Block(q_id))
    editor.placeBlock((x-7,y-1,z),Block(q_id))
    editor.placeBlock((x-3,y-1,z),Block(q_id))
    editor.placeBlock((x+1,y+3,z),Block(w_id,{"type": "bottom"}))
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+3,z),Block(w_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x-6-xx,y+1,z),Block(q_id))
        editor.placeBlock((x-1-xx,y+3,z),Block(q_id))
        editor.placeBlock((x+1+xx,y,z),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-4-xx,y-1,z),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-4,y+3,z),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-6,y+2,z),Block(w_id,{"type": "bottom"}))

    #z+2
    editor.placeBlock((x-5,y+1,z+2),Block(t_id,{"type": "bottom"}))
    editor.placeBlock((x-4,y+1,z+2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x-4,y,z+2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x-3,y,z+2),Block(r_id))
    editor.placeBlock((x-2,y+1,z+2),Block(r_id))
    for xx in range(4):
        editor.placeBlock((x-xx,y+2,z+2),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+1-xx,y,z+2),Block(t_id,{"type": "top"}))
    #z-2
    editor.placeBlock((x-5,y+1,z-2),Block(t_id,{"type": "bottom"}))
    editor.placeBlock((x-4,y+1,z-2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x-4,y,z-2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x-3,y,z-2),Block(r_id))
    editor.placeBlock((x-2,y+1,z-2),Block(r_id))
    for xx in range(4):
        editor.placeBlock((x-xx,y+2,z-2),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+1-xx,y,z-2),Block(t_id,{"type": "top"}))
    #z+3
    for xx in range(4):
        editor.placeBlock((x+1-xx,y+1,z+3),Block(t_id,{"type": "top"}))
    #z-3
    for xx in range(4):
        editor.placeBlock((x+1-xx,y+1,z-3),Block(t_id,{"type": "top"}))
    for xx in range(2):
        editor.placeBlock((x-7-xx,y,z),Block(y_id))

def dragon_x2(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    #z+1
    for xx in range(4):
        for yy in range(3):
            editor.placeBlock((x+xx,y+yy,z+1),Block(q_id))
    editor.placeBlock((x+3,y-1,z+1),Block(q_id))
    editor.placeBlock((x+4,y+2,z+1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+5,y+1,z+1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+6,y+1,z+1),Block(q_id))
    editor.placeBlock((x+6,y,z+1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+7,y+1,z+1),Block(w_id,{"type": "bottom"}))
    for xx in range(2):
        editor.placeBlock((x+4+xx,y,z+1),Block(w_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x+4+xx,y-1,z+1),Block(w_id,{"type": "top"}))
    for xx in range(2):
        editor.placeBlock((x-1-xx,y+2,z+1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+xx,y+3,z+1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-3-xx,y+4,z+1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-2,y+3,z+1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+2,y+3,z+1),Block(q_id))
    editor.placeBlock((x,y+4,z+1),Block(q_id))
    editor.placeBlock((x-1,y+4,z+1),Block(w_id,{"type": "bottom"}))
    for yy in range(2):
        editor.placeBlock((x-2,y+4+yy,z+1),Block(q_id))
    editor.placeBlock((x+3,y+1,z+1),Block(e_id))
    #z-1
    for xx in range(4):
        for yy in range(3):
            editor.placeBlock((x+xx,y+yy,z-1),Block(q_id))
    editor.placeBlock((x+3,y-1,z-1),Block(q_id))
    editor.placeBlock((x+4,y+2,z-1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+5,y+1,z-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+6,y+1,z-1),Block(q_id))
    editor.placeBlock((x+6,y,z-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+7,y+1,z-1),Block(w_id,{"type": "bottom"}))
    for xx in range(2):
        editor.placeBlock((x+4+xx,y,z-1),Block(w_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x+4+xx,y-1,z-1),Block(w_id,{"type": "top"}))
    for xx in range(2):
        editor.placeBlock((x-1-xx,y+2,z-1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+xx,y+3,z-1),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-3-xx,y+4,z-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-2,y+3,z-1),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+2,y+3,z-1),Block(q_id))
    editor.placeBlock((x,y+4,z-1),Block(q_id))
    editor.placeBlock((x-1,y+4,z-1),Block(w_id,{"type": "bottom"}))
    for yy in range(2):
        editor.placeBlock((x-2,y+4+yy,z-1),Block(q_id))
    editor.placeBlock((x+3,y+1,z-1),Block(e_id))
    #z
    for xx in range(6):
        for yy in range(3):
            editor.placeBlock((x+xx,y+yy,z),Block(q_id))
    editor.placeBlock((x-1,y+2,z),Block(q_id))
    editor.placeBlock((x-2,y+3,z),Block(q_id))
    editor.placeBlock((x+2,y+4,z),Block(q_id))
    editor.placeBlock((x+8,y+2,z),Block(q_id))
    editor.placeBlock((x+7,y-1,z),Block(q_id))
    editor.placeBlock((x+3,y-1,z),Block(q_id))
    editor.placeBlock((x-1,y+3,z),Block(w_id,{"type": "bottom"}))
    for xx in range(2):
        editor.placeBlock((x-1-xx,y+3,z),Block(w_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x+6+xx,y+1,z),Block(q_id))
        editor.placeBlock((x+1+xx,y+3,z),Block(q_id))
        editor.placeBlock((x-1-xx,y,z),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+4+xx,y-1,z),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+4,y+3,z),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+6,y+2,z),Block(w_id,{"type": "bottom"}))

    #z+2
    editor.placeBlock((x+5,y+1,z+2),Block(t_id,{"type": "bottom"}))
    editor.placeBlock((x+4,y+1,z+2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x+4,y,z+2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x+3,y,z+2),Block(r_id))
    editor.placeBlock((x+2,y+1,z+2),Block(r_id))
    for xx in range(4):
        editor.placeBlock((x+xx,y+2,z+2),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-1+xx,y,z+2),Block(t_id,{"type": "top"}))
    #z-2
    editor.placeBlock((x+5,y+1,z-2),Block(t_id,{"type": "bottom"}))
    editor.placeBlock((x+4,y+1,z-2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x+4,y,z-2),Block(t_id,{"type": "top"}))
    editor.placeBlock((x+3,y,z-2),Block(r_id))
    editor.placeBlock((x+2,y+1,z-2),Block(r_id))
    for xx in range(4):
        editor.placeBlock((x+xx,y+2,z-2),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-1+xx,y,z-2),Block(t_id,{"type": "top"}))
    #z+3
    for xx in range(4):
        editor.placeBlock((x-1+xx,y+1,z+3),Block(t_id,{"type": "top"}))
    #z-3
    for xx in range(4):
        editor.placeBlock((x-1+xx,y+1,z-3),Block(t_id,{"type": "top"}))
    for xx in range(2):
        editor.placeBlock((x+7+xx,y,z),Block(y_id))

def hosoku(x,y,z,q_id):
    for xx in range(87):
        for zz in range(87):
            editor.placeBlock((x-43+xx,y,z-43+zz),Block(q_id))
    for yy in range(4):
        for xx in range(89):
            editor.placeBlock((x-44+xx,y+yy,z-44),Block(q_id))
            editor.placeBlock((x-44+xx,y+yy,z+44),Block(q_id))
        for zz in range(89):
            editor.placeBlock((x+44,y+yy,z-44+zz),Block(q_id))
            editor.placeBlock((x-44,y+yy,z-44+zz),Block(q_id))

def hotel(x,y,z):
    for xx in range(90):
        for zz in range(90):
            for yy in range(30):
                editor.placeBlock((x-44+xx,y+yy,z-44+zz),Block("air"))
    foundation(x,y,z,"stone_bricks","chiseled_stone_bricks","stone_brick_slab","stone_brick_wall","stone_slab","polished_andesite","polished_andesite_stairs","lantern")
    hosoku(x,y-4,z,"grass_block")
    pillar(x,y+3,z,"black_concrete","red_concrete","white_concrete","glowstone","gilded_blackstone","oak_trapdoor","air")
    storey(x,y+16,z,"black_concrete","red_concrete","stripped_dark_oak_wood","dark_oak_slab","spruce_slab","white_concrete","lantern")
    storey(x,y+30,z,"black_concrete","red_concrete","stripped_dark_oak_wood","dark_oak_slab","spruce_slab","white_concrete","lantern")
    storey4(x,y+44,z,"black_concrete","red_concrete","stripped_dark_oak_wood","dark_oak_slab","spruce_slab","white_concrete","lantern")
    tiles1(x,y+11,z,"spruce_stairs","oak_fence","oak_log","spruce_slab","stone_brick_slab","stone_brick_wall","lantern","stone_bricks")
    tiles(x,y+23,z,"spruce_stairs","oak_fence","oak_log","spruce_slab","stone_brick_slab","stone_brick_wall","lantern","stone_bricks")
    tiles(x,y+37,z,"spruce_stairs","oak_fence","oak_log","spruce_slab","stone_brick_slab","stone_brick_wall","lantern","stone_bricks")
    tiles(x,y+51,z,"spruce_stairs","oak_fence","oak_log","spruce_slab","stone_brick_slab","stone_brick_wall","lantern","stone_bricks")
    housetop(x,y+56,z,"smooth_stone","stone_bricks","stone_brick_slab","stone_brick_stairs","stone_brick_wall","oak_trapdoor","glowstone","polished_andesite_stairs","polished_andesite_slab","sea_lantern","smooth_stone_slab")
    floor(x,y-1,z,"chiseled_stone_bricks","polished_andesite","smooth_stone","glowstone","sea_lantern","stone_brick_slab","stone_slab")
    stairs(x,y+3,z,"air","acacia_stairs","oak_stairs","oak_fence","lantern")
    stairs2(x,y+3,z,"air","acacia_stairs","oak_stairs","oak_fence","lantern")
    stairs2(x,y+17,z,"air","acacia_stairs","oak_stairs","oak_fence","lantern")
    furnitur1(x,y+3,z,"red_concrete","red_carpet","glowstone","polished_andesite","oak_stairs","polished_andesite_slab","polished_andesite_stairs","birch_planks","birch_stairs","oak_slab","end_rod","lantern")
    lantern(x,y,z,"oak_fence","chain","red_glazed_terracotta","shroomlight","orange_wall_banner","acacia_stairs")
    table2(x,y+17,z,"dark_oak_fence","dark_oak_fence_gate","spruce_trapdoor","scaffolding","jungle_trapdoor")
    pot(x,y,z,"scaffolding","acacia_trapdoor","potted_oak_sapling")
    table3(x,y+31,z,"barrel","dark_oak_trapdoor","dark_oak_stairs","dark_oak_slab","lantern","potted_oak_sapling","oak_slab","spruce_pressure_plate","potted_cactus","spruce_stairs","spruce_slab")
    table3(x,y+45,z,"barrel","dark_oak_trapdoor","dark_oak_stairs","dark_oak_slab","lantern","potted_oak_sapling","oak_slab","spruce_pressure_plate","potted_cactus","spruce_stairs","spruce_slab")
    floor_light(x,y+1,z,"glowstone","glass","light_gray_carpet","red_carpet")
    dragon_x1(x-14,y+13,z-17,"chiseled_red_sandstone","red_sandstone_slab","glowstone","dark_prismarine","dark_prismarine_slab","water")
    dragon_x1(x-14,y+13,z+17,"chiseled_red_sandstone","red_sandstone_slab","glowstone","dark_prismarine","dark_prismarine_slab","water")
    dragon_x2(x+14,y+13,z-17,"chiseled_red_sandstone","red_sandstone_slab","glowstone","dark_prismarine","dark_prismarine_slab","water")
    dragon_x2(x+14,y+13,z+17,"chiseled_red_sandstone","red_sandstone_slab","glowstone","dark_prismarine","dark_prismarine_slab","water")
    pool(x,y-1,z,"air","water","warped_trapdoor","brain_coral_fan","lily_pad","stone","seagrass","kelp_plant","sea_pickle","kelp")    
  
    panda(x,y,z)
#light+hosoku
    editor.placeBlock((x+11,y+57,z+6),Block("glowstone"))
    editor.placeBlock((x-11,y+57,z+6),Block("glowstone"))
    editor.placeBlock((x+11,y+57,z-6),Block("glowstone"))
    editor.placeBlock((x-11,y+57,z-6),Block("glowstone"))
    editor.placeBlock((x+6,y+57,z+11),Block("glowstone"))
    editor.placeBlock((x-6,y+57,z+11),Block("glowstone"))
    editor.placeBlock((x+6,y+57,z-11),Block("glowstone"))
    editor.placeBlock((x-6,y+57,z-11),Block("glowstone"))
    editor.placeBlock((x+4,y+59,z+4),Block("glowstone"))
    editor.placeBlock((x+4,y+59,z-4),Block("glowstone"))
    editor.placeBlock((x-4,y+59,z+4),Block("glowstone"))
    editor.placeBlock((x-4,y+59,z-4),Block("glowstone"))
    editor.placeBlock((x+7,y+57,z+7),Block("air"))
    editor.placeBlock((x+7,y+57,z-7),Block("air"))
    editor.placeBlock((x-7,y+57,z+7),Block("air"))
    editor.placeBlock((x-7,y+57,z-7),Block("air"))
    


def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True


