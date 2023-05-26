import random
from interfaceUtils import runCommand
import interfaceUtils
import lantern
from gdpc import Editor, Block, Transform, geometry
editor = Editor(buffering=True)


def River(x,y,z,l,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    for xx in range(l):
        for zz in range(9):
            editor.placeBlock((x+27+xx,y-4,z-4+zz),Block("grass_block"))
            editor.placeBlock((x-27-xx,y-4,z-4+zz),Block("grass_block"))
    for yy in range(4):
        for xx in range(l+2):
            editor.placeBlock((x+26+xx,y-4+yy,z-5),Block("grass_block"))
            editor.placeBlock((x-26-xx,y-4+yy,z-5),Block("grass_block"))
            editor.placeBlock((x+26+xx,y-4+yy,z+5),Block("grass_block"))
            editor.placeBlock((x-26-xx,y-4+yy,z+5),Block("grass_block"))
        for zz in range(11):
            editor.placeBlock((x+26,y-4+yy,z-5+zz),Block("grass_block"))
            editor.placeBlock((x-26,y-4+yy,z-5+zz),Block("grass_block"))
            editor.placeBlock((x+27+l,y-4+yy,z-5+zz),Block("grass_block"))
            editor.placeBlock((x-27-l,y-4+yy,z-5+zz),Block("grass_block"))
    for yy in range(3):
        for xx in range(l):
            for zz in range(9):
                editor.placeBlock((x+27+xx,y-1-yy,z-4+zz),Block(q_id))
                editor.placeBlock((x+27+xx,y-1-yy,z-4+zz),Block(q_id))
                editor.placeBlock((x+27+xx,y-1-yy,z-4+zz),Block(w_id))
                editor.placeBlock((x+27+xx,y-1-yy,z-4+zz),Block(w_id))

                editor.placeBlock((x-27-xx,y-1-yy,z-4+zz),Block(q_id))
                editor.placeBlock((x-27-xx,y-1-yy,z-4+zz),Block(q_id))
                editor.placeBlock((x-27-xx,y-1-yy,z-4+zz),Block(w_id))
                editor.placeBlock((x-27-xx,y-1-yy,z-4+zz),Block(w_id))

    ##   
    def kelp(x,y,z):
        editor.placeBlock((x,y,z),Block(u_id))
        editor.placeBlock((x,y+1,z),Block(o_id))

    def flower(x,y,z):
        for i in range(4):
            editor.placeBlock((x+random.randint(-2,2),y+1,z+random.randint(-2,2)),Block(t_id))
        editor.placeBlock((x+1,y,z),Block(t_id))
        editor.placeBlock((x,y,z),Block(e_id,{"facing":"east","half":"top","open":"false"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"waterlogged":"false"}))
        editor.placeBlock((x+1,y,z),Block(w_id))

 

    def grass(x,y,z):
        for i in range(6):
            editor.placeBlock((x+random.randint(-2,2),y,z+random.randint(-2,2)),Block(y_id))
        for i in range(3):           
            kelp(x+random.randint(-2,2),y,z+random.randint(-2,2))
        editor.placeBlock((x+random.randint(-1,1),y,z+random.randint(-1,1)),Block(i_id,{"pickles":"4"}))
 
    for i in range(int(l/3)):
        flower(x-30-random.randint(0,l-6),y-1,z-random.randint(-2,2))
        flower(x+30+random .randint(0,l-6),y-1,z+random.randint(-2,2))
    for i in range(int(2*l/5)):
        grass(x-30-random.randint(0,l-6),y-3,z-random.randint(-2,2))
        grass(x+30+random.randint(0,l-6),y-3,z+random.randint(-2,2))
    ##

def bridge(x,y,z,l,q_id,w_id,e_id,r_id,t_id,y_id):
    m=int(l/2)
    for xx in range(5):
        editor.placeBlock((x+47+m-2+xx,y-1,z+5),Block(w_id))
        editor.placeBlock((x+47+m-2+xx,y-1,z-5),Block(w_id))
        editor.placeBlock((x-47-m-2+xx,y-1,z+5),Block(w_id))
        editor.placeBlock((x-47-m-2+xx,y-1,z-5),Block(w_id))

        editor.placeBlock((x+47+m-2+xx,y,z+4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+47+m-2+xx,y,z-4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-47-m-2+xx,y,z+4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-47-m-2+xx,y,z-4),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x+47+m-2+xx,y,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+47+m-2+xx,y,z-3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-47-m-2+xx,y,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-47-m-2+xx,y,z-3),Block(e_id,{"type": "top"}))

        editor.placeBlock((x+47+m-2+xx,y+1,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+47+m-2+xx,y+1,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-47-m-2+xx,y+1,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-47-m-2+xx,y+1,z-2),Block(e_id,{"type": "bottom"}))

        for zz in range(3):
            editor.placeBlock((x+47+m-2+xx,y+1,z-1+zz),Block(e_id,{"type": "top"}))
            editor.placeBlock((x-47-m-2+xx,y+1,z-1+zz),Block(e_id,{"type": "top"}))
       
    for zz in range(3):
        editor.placeBlock((x+47+m+3,y,z+5-zz),Block(q_id))
        editor.placeBlock((x+47+m+3,y,z-5+zz),Block(q_id))
        editor.placeBlock((x+47+m-3,y,z+5-zz),Block(q_id))
        editor.placeBlock((x+47+m-3,y,z-5+zz),Block(q_id))

        editor.placeBlock((x-47-m+3,y,z+5-zz),Block(q_id))
        editor.placeBlock((x-47-m+3,y,z-5+zz),Block(q_id))
        editor.placeBlock((x-47-m-3,y,z+5-zz),Block(q_id))
        editor.placeBlock((x-47-m-3,y,z-5+zz),Block(q_id))


        editor.placeBlock((x+47+m+3,y+1,z+3-zz),Block(q_id))
        editor.placeBlock((x+47+m+3,y+1,z-3+zz),Block(q_id))
        editor.placeBlock((x+47+m-3,y+1,z+3-zz),Block(q_id))
        editor.placeBlock((x+47+m-3,y+1,z-3+zz),Block(q_id))

        editor.placeBlock((x-47-m+3,y+1,z+3-zz),Block(q_id))
        editor.placeBlock((x-47-m+3,y+1,z-3+zz),Block(q_id))
        editor.placeBlock((x-47-m-3,y+1,z+3-zz),Block(q_id))
        editor.placeBlock((x-47-m-3,y+1,z-3+zz),Block(q_id))

        editor.placeBlock((x+47+m+3,y+2,z-1+zz),Block(q_id))
        editor.placeBlock((x+47+m-3,y+2,z-1+zz),Block(q_id))
        editor.placeBlock((x-47-m+3,y+2,z-1+zz),Block(q_id))
        editor.placeBlock((x-47-m-3,y+2,z-1+zz),Block(q_id))

    editor.placeBlock((x+47+m+3,y,z+3),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+47+m+3,y,z-3),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+47+m-3,y,z+3),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+47+m-3,y,z-3),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))

    editor.placeBlock((x-47-m+3,y,z+3),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-47-m+3,y,z-3),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-47-m-3,y,z+3),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-47-m-3,y,z-3),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))

    for yy in range(3):
        editor.placeBlock((x+47+m+3,y-1-yy,z+4),Block(q_id))
        editor.placeBlock((x+47+m+3,y-1-yy,z-4),Block(q_id))
        editor.placeBlock((x+47+m-3,y-1-yy,z+4),Block(q_id))
        editor.placeBlock((x+47+m-3,y-1-yy,z-4),Block(q_id))

        editor.placeBlock((x-47-m+3,y-1-yy,z+4),Block(q_id))
        editor.placeBlock((x-47-m+3,y-1-yy,z-4),Block(q_id))
        editor.placeBlock((x-47-m-3,y-1-yy,z+4),Block(q_id))
        editor.placeBlock((x-47-m-3,y-1-yy,z-4),Block(q_id))

    for yy in range(4):
        editor.placeBlock((x+47+m+3,y-yy,z+2),Block(q_id))
        editor.placeBlock((x+47+m+3,y-yy,z-2),Block(q_id))
        editor.placeBlock((x+47+m-3,y-yy,z+2),Block(q_id))
        editor.placeBlock((x+47+m-3,y-yy,z-2),Block(q_id))

        editor.placeBlock((x-47-m+3,y-yy,z+2),Block(q_id))
        editor.placeBlock((x-47-m+3,y-yy,z-2),Block(q_id))
        editor.placeBlock((x-47-m-3,y-yy,z+2),Block(q_id))
        editor.placeBlock((x-47-m-3,y-yy,z-2),Block(q_id))

    editor.placeBlock((x+47+m+3,y+1,z+5),Block(t_id))
    editor.placeBlock((x+47+m+3,y+1,z-5),Block(t_id))
    editor.placeBlock((x+47+m-3,y+1,z+5),Block(t_id))
    editor.placeBlock((x+47+m-3,y+1,z-5),Block(t_id))

    editor.placeBlock((x-47-m+3,y+1,z+5),Block(t_id))
    editor.placeBlock((x-47-m+3,y+1,z-5),Block(t_id))
    editor.placeBlock((x-47-m-3,y+1,z+5),Block(t_id))
    editor.placeBlock((x-47-m-3,y+1,z-5),Block(t_id))

    editor.placeBlock((x+47+m+3,y+2,z+3),Block(t_id))
    editor.placeBlock((x+47+m+3,y+2,z-3),Block(t_id))
    editor.placeBlock((x+47+m-3,y+2,z+3),Block(t_id))
    editor.placeBlock((x+47+m-3,y+2,z-3),Block(t_id))

    editor.placeBlock((x-47-m+3,y+2,z+3),Block(t_id))
    editor.placeBlock((x-47-m+3,y+2,z-3),Block(t_id))
    editor.placeBlock((x-47-m-3,y+2,z+3),Block(t_id))
    editor.placeBlock((x-47-m-3,y+2,z-3),Block(t_id))

    editor.placeBlock((x+47+m+3,y+1,z+4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+47+m+3,y+1,z-4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+47+m-3,y+1,z+4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+47+m-3,y+1,z-4),Block(y_id,{"type": "bottom"}))

    editor.placeBlock((x-47-m+3,y+1,z+4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-47-m+3,y+1,z-4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-47-m-3,y+1,z+4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-47-m-3,y+1,z-4),Block(y_id,{"type": "bottom"}))

    editor.placeBlock((x+47+m+3,y+2,z+2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+47+m+3,y+2,z-2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+47+m-3,y+2,z+2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+47+m-3,y+2,z-2),Block(y_id,{"type": "bottom"}))

    editor.placeBlock((x-47-m+3,y+2,z+2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-47-m+3,y+2,z-2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-47-m-3,y+2,z+2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-47-m-3,y+2,z-2),Block(y_id,{"type": "bottom"}))

    lantern.Lantern(x+47+m-5,y,z-6)
    lantern.Lantern(x+47+m-5,y,z+6)
    lantern.Lantern(x+47+m+5,y,z-6)
    lantern.Lantern(x+47+m+5,y,z+6)

    lantern.Lantern(x-47-m-5,y,z-6)
    lantern.Lantern(x-47-m-5,y,z+6)
    lantern.Lantern(x-47-m+5,y,z-6)
    lantern.Lantern(x-47-m+5,y,z+6)


def river(x,y,z,L):   
    River(x,y,z,L-27,"air","water","warped_trapdoor","brain_coral_fan","lily_pad","seagrass","kelp_plant","sea_pickle","kelp")
    


river(-50,4,-380,40)

def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True

