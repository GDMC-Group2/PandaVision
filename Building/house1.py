from interfaceUtils import runCommand
from gdpc import Editor, Block, Transform, geometry
 
editor = Editor(buffering=True)


def check_coor(x,y,z):
    command = f"summon minecraft:shulker {x} {y} {z} {{Invulnerable:true,Glowing:true,Silent:true,Tags:[test],NoAI:true,PersistenceRequired:true}}"
    runCommand(command)


def light(x,y,z): #c=cobblestone_wall,l=lantern
    editor.placeBlock((x,y,z),Block("cobblestone_wall"))
    editor.placeBlock((x,y+1,z),Block("lantern"))

#west
def buildHouse_w(x, y, z, q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):    
    ##柱
    for yy in range(7):
        editor.placeBlock((x,y+yy,z),Block(q_ID))
        editor.placeBlock((x+8,y+yy,z),Block(q_ID))
        editor.placeBlock((x,y+yy,z+8),Block(q_ID))
        editor.placeBlock((x+8,y+yy,z+8),Block(q_ID))
    for xx in range(7):
        editor.placeBlock((x+1+xx,y+5,z),Block(q_ID))
        editor.placeBlock((x+1+xx,y+5,z+8),Block(q_ID))
    for zz in range(7):
        for yy in range(2):
            editor.placeBlock((x,y+4+yy,z+1+zz),Block(q_ID))
            editor.placeBlock((x+8,y+4+yy,z+1+zz),Block(q_ID))
     ##屋根
    for zz in range(5):
        editor.placeBlock((x-1,y+5,z+2*zz),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((x-2,y+4,z+2*zz),Block(w_ID,{"type": "top"}))
        editor.placeBlock((x+9,y+5,z+2*zz),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((x+10,y+4,z+2*zz),Block(w_ID,{"type": "top"}))
    for zz in range(9):
        editor.placeBlock((x+1,y+7,z+zz),Block(e_ID))
        editor.placeBlock((x+2,y+8,z+zz),Block(e_ID))
        editor.placeBlock((x+3,y+9,z+zz),Block(e_ID))
        editor.placeBlock((x+4,y+10,z+zz),Block(e_ID))

        editor.placeBlock((x+7,y+7,z+zz),Block(e_ID))
        editor.placeBlock((x+6,y+8,z+zz),Block(e_ID))
        editor.placeBlock((x+5,y+9,z+zz),Block(e_ID))
        editor.placeBlock((x+4,y+10,z+zz),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((x-1,y+6,z+2*zz),Block(e_ID))
        editor.placeBlock((x,y+7,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y+8,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+2,y+9,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+3,y+10,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+4,y+11,z+2*zz),Block(e_ID))

        editor.placeBlock((x+9,y+6,z+2*zz),Block(e_ID))
        editor.placeBlock((x+8,y+7,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+7,y+8,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+6,y+9,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+5,y+10,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+4,y+11,z+2*zz),Block(e_ID))

        editor.placeBlock((x-2,y+6,z+2*zz),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((x+10,y+6,z+2*zz),Block(r_ID,{"type": "bottom"}))
        for xx in range(2):
            editor.placeBlock((x-2-xx,y+5,z+2*zz),Block(e_ID))
            editor.placeBlock((x+10+xx,y+5,z+2*zz),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((x,y+6,z+1+2*zz),Block(e_ID))
        editor.placeBlock((x-1,y+5,z+1+2*zz),Block(e_ID))

        editor.placeBlock((x+8,y+6,z+1+2*zz),Block(e_ID))
        editor.placeBlock((x+9,y+5,z+1+2*zz),Block(e_ID))

        editor.placeBlock((x-2,y+5,z+1+2*zz),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((x+10,y+5,z+1+2*zz),Block(r_ID,{"type": "bottom"}))

    editor.placeBlock((x-3,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-2,y+5,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-1,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-1,y+6,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x,y+6,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x,y+7,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x+1,y+7,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+2,y+7,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+2,y+8,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+3,y+8,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+3,y+9,z-1),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x+4,y+9,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+4,y+10,z-1),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x+11,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+10,y+5,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+9,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+9,y+6,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x+8,y+6,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+8,y+7,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x+7,y+7,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+6,y+7,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+6,y+8,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+5,y+8,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+5,y+9,z-1),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x-3,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-2,y+5,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-1,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-1,y+6,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x,y+6,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x,y+7,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x+1,y+7,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+2,y+7,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+2,y+8,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+3,y+8,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+3,y+9,z+9),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x+4,y+9,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+4,y+10,z+9),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x+11,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+10,y+5,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+9,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+9,y+6,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x+8,y+6,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+8,y+7,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x+7,y+7,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+6,y+7,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+6,y+8,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+5,y+8,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+5,y+9,z+9),Block(y_ID,{"type": "double"}))
    #照明
    editor.placeBlock((x+4,y+12,z+4),Block("lantern"))
    editor.placeBlock((x+4,y+11,z-1),Block("lantern"))
    editor.placeBlock((x+4,y+11,z+9),Block("lantern"))
    editor.placeBlock((x+11,y+6,z+2),Block("lantern"))
    editor.placeBlock((x+11,y+6,z+6),Block("lantern"))
    editor.placeBlock((x-3,y+6,z+2),Block("lantern"))
    editor.placeBlock((x-3,y+6,z+6),Block("lantern"))





   
def Wall_w(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+6,z),Block(q_ID))
        editor.placeBlock((x+6+xx,y+6,z),Block(q_ID))
        editor.placeBlock((x+2+xx,y+7,z),Block(q_ID))
        editor.placeBlock((x+5+xx,y+7,z),Block(q_ID))

        editor.placeBlock((x+1+xx,y+6,z+8),Block(q_ID))
        editor.placeBlock((x+6+xx,y+6,z+8),Block(q_ID))
        editor.placeBlock((x+2+xx,y+7,z+8),Block(q_ID))
        editor.placeBlock((x+5+xx,y+7,z+8),Block(q_ID))

    for xx in range(3):
        editor.placeBlock((x+3+xx,y+8,z),Block(q_ID))
        editor.placeBlock((x+3+xx,y+8,z+8),Block(q_ID))
        
        editor.placeBlock((x+3+xx,y+6,z),Block(w_ID))
        editor.placeBlock((x+3+xx,y+6,z-1),Block("oak_trapdoor",{"facing": "north", "open": "true"}))
        editor.placeBlock((x+3+xx,y+6,z+8),Block(w_ID))
        editor.placeBlock((x+3+xx,y+6,z+9),Block("oak_trapdoor",{"facing": "south", "open": "true"}))
    editor.placeBlock((x+4,y+7,z),Block(w_ID))
    editor.placeBlock((x+4,y+7,z-1),Block("oak_trapdoor",{"facing": "north", "open": "true"}))
    editor.placeBlock((x+4,y+7,z+8),Block(w_ID))
    editor.placeBlock((x+4,y+7,z+9),Block("oak_trapdoor",{"facing": "south", "open": "true"}))

    for zz in range(5):
        editor.placeBlock((x-1,y+4,z+2*zz),Block(q_ID))
        editor.placeBlock((x+9,y+4,z+2*zz),Block(q_ID))
    for zz in range(4):
        editor.placeBlock((x-2,y+4,z+1+2*zz),Block(q_ID))
        editor.placeBlock((x+10,y+4,z+1+2*zz),Block(q_ID))

        editor.placeBlock((x-1,y+4,z+1+2*zz),Block(w_ID))
        editor.placeBlock((x+9,y+4,z+1+2*zz),Block(w_ID))

    def wall1(x,y,z):
        for yy in range(5):
            editor.placeBlock((x,y+yy,z),Block(e_ID))
            editor.placeBlock((x+6,y+yy,z),Block(e_ID))
        for xx in range(5):
            editor.placeBlock((x+1+xx,y+4,z),Block(e_ID))
            for yy in range(4):
                editor.placeBlock((x+1+xx,y+yy,z),Block(r_ID))
    def wall2(x,y,z):
        for zz in range(7):
            editor.placeBlock((x,y,z+1+zz),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((x,y+1+yy,z+2),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+6),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+1),Block(r_ID))
            editor.placeBlock((x,y+1+yy,z+7),Block(r_ID))

            editor.placeBlock((x+1,y+1+yy,z),Block(e_ID))
            editor.placeBlock((x+7,y+1+yy,z),Block(e_ID))
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((x,y+1+yy,z+3+zz),Block(r_ID))
        for xx in range(7):
            editor.placeBlock((x+1+xx,y+4,z),Block(e_ID))
    def wall3(x,y,z):
        for zz in range(2):
            editor.placeBlock((x,y,z+1+zz),Block(e_ID))
            editor.placeBlock((x,y,z+6+zz),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((x,y+1+yy,z+2),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+6),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+1),Block(r_ID))
            editor.placeBlock((x,y+1+yy,z+7),Block(r_ID))
        for zz in range(3):
            editor.placeBlock((x,y+3,z+3+zz),Block(e_ID))
    ##天井、床
    for xx in range(7):
        for zz in range(7):
            editor.placeBlock((x+1+xx,y+5,z+1+zz),Block(q_ID))
            editor.placeBlock((x+1+xx,y,z+1+zz),Block(q_ID))
    for zz in range(3):
        editor.placeBlock((x+8,y,z+3+zz),Block(q_ID))
    ##階段
    editor.placeBlock((x+9,y,z+3),Block(t_ID,{"facing": "north", "half": "bottom"}))
    editor.placeBlock((x+9,y,z+4),Block(t_ID,{"facing": "west", "half": "bottom"}))
    editor.placeBlock((x+9,y,z+5),Block(t_ID,{"facing": "south", "half": "bottom"}))
    editor.placeBlock((x+1,y,z),Block(t_ID,{"facing": "east", "half": "top"}))
    editor.placeBlock((x+7,y,z),Block(t_ID,{"facing": "west", "half": "top"}))
    editor.placeBlock((x+2,y,z),Block(t_ID,{"facing": "south", "half": "bottom"}))
    editor.placeBlock((x+6,y,z),Block(t_ID,{"facing": "south", "half": "bottom"}))
    for xx in range(3):
        editor.placeBlock((x+3+xx,y,z),Block(y_ID,{"type": "top"}))
    wall1(x+1,y,z+8)
    wall2(x,y,z)
    wall3(x+8,y,z)

    

def niwa_w(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(3):
        editor.placeBlock((x+9+xx,y-1,z),Block(e_ID))
    for xx in range(11):
        editor.placeBlock((x+xx,y-1,z-5),Block(e_ID))
        editor.placeBlock((x+xx,y-1,z+13),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((x,y-1,z-1-zz),Block(e_ID))
        editor.placeBlock((x,y-1,z+9+zz),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((x+11,y-1,z-1-zz),Block(e_ID))
        editor.placeBlock((x+11,y-1,z+9+zz),Block(e_ID))

    for yy in range(2):
        for xx in range(3):
            editor.placeBlock((x+9+xx,y+yy,z),Block(q_ID))
        for xx in range(11):
            editor.placeBlock((x+xx,y+yy,z-5),Block(q_ID))
            editor.placeBlock((x+xx,y+yy,z+13),Block(q_ID))
        for zz in range(4):
            editor.placeBlock((x,y+yy,z-1-zz),Block(q_ID))
            editor.placeBlock((x,y+yy,z+9+zz),Block(q_ID))
        for zz in range(5):
            editor.placeBlock((x+11,y+yy,z-1-zz),Block(q_ID))
            editor.placeBlock((x+11,y+yy,z+9+zz),Block(q_ID))

    editor.placeBlock((x+9,y,z+9),Block(w_ID,{"facing": "south", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+9,y+1,z+9),Block(w_ID,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+10,y,z+9),Block(w_ID,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+10,y+1,z+9),Block(w_ID,{"facing": "south", "half": "upper", "hinge": "left"}))



    for yy in range(4):
        editor.placeBlock((x+9,y+yy,z+2),Block(r_ID))
        editor.placeBlock((x+9,y+yy,z+6),Block(r_ID))
    for xx in range(3):
        for zz in range(8):
            editor.placeBlock((x+9+xx,y-1,z+1+zz),Block(t_ID))
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x+2+xx,y-1,z-1-zz),Block(t_ID))
    ##ドア
    editor.placeBlock((x+8,y+1,z+3),Block(y_ID,{"facing": "west", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+8,y+2,z+3),Block(y_ID,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+8,y+1,z+4),Block(y_ID,{"facing": "west", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+8,y+2,z+4),Block(y_ID,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+8,y+1,z+5),Block(y_ID,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+8,y+2,z+5),Block(y_ID,{"facing": "west", "half": "upper", "hinge": "left"}))

def farm_w(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID):
    for xx in range(5):
        for zz in range(4):
            editor.placeBlock((x+1+xx,y-1,z+9+zz),Block(q_ID))
            editor.placeBlock((x+1+xx,y,z+9+zz),Block(w_ID,{"age": "7"}))
    editor.placeBlock((x+4,y-1,z+10),Block(e_ID))
    editor.placeBlock((x+9,y,z+12),Block(r_ID))
    editor.placeBlock((x+10,y,z+11),Block(r_ID))
    for yy in range(2):
        editor.placeBlock((x+10,y+yy,z+12),Block(r_ID))
    editor.placeBlock((x+9,y,z+11),Block(y_ID))
    editor.placeBlock((x+9,y+1,z+12),Block(t_ID))
    editor.placeBlock((x+8,y,z+12),Block(u_ID,{"level": "3"}))
    editor.placeBlock((x+6,y,z+12),Block(i_ID))
    editor.placeBlock((x+6,y+1,z+12),Block(o_ID))
    editor.placeBlock((x+6,y+3,z),Block(o_ID,{"hanging": "true"}))
    editor.placeBlock((x+2,y+3,z),Block(o_ID,{"hanging": "true"}))
def pool_w(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x+6+xx,y-1,z-1-zz),Block(q_ID))
    for zz in range(2):
        editor.placeBlock((x+10,y-1,z-2-zz),Block(q_ID))
    editor.placeBlock((x+10,y-1,z-1),Block("grass_block"))
    editor.placeBlock((x+10,y,z-1),Block(w_ID,{"half": "lower"}))
    editor.placeBlock((x+10,y+1,z-1),Block(w_ID,{"half": "upper"}))
    editor.placeBlock((x+10,y-1,z-4),Block("grass_block"))
    editor.placeBlock((x+10,y,z-4),Block(e_ID,{"half": "lower"}))
    editor.placeBlock((x+10,y+1,z-4),Block(e_ID,{"half": "upper"}))
    editor.placeBlock((x+9,y-2,z-3),Block("glowstone"))
    editor.placeBlock((x+8,y,z-3),Block(r_ID))
    editor.placeBlock((x+7,y,z-2),Block(r_ID))
    editor.placeBlock((x+1,y,z-1),Block(t_ID,{"facing": "east"}))
    editor.placeBlock((x+1,y,z-2),Block(y_ID))
    editor.placeBlock((x+1,y,z-3),Block(u_ID))
    editor.placeBlock((x+1,y,z-4),Block(i_ID))
    editor.placeBlock((x+2,y,z-4),Block(o_ID))
    editor.placeBlock((x+3,y,z-4),Block(p_ID))
    editor.placeBlock((x+1,y+1,z-4),Block(s_ID))
    editor.placeBlock((x+2,y,z-3),Block(a_ID,{"facing": "west"}))

def heya_w(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(5):
        editor.placeBlock((x+2+xx,y+4,z-1),Block(q_ID))
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+1,z+7),Block(w_ID))
        editor.placeBlock((x+1+xx,y+3,z+7),Block(t_ID,{"type": "top"}))
        editor.placeBlock((x+1+xx,y+1,z+4),Block(y_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
    for yy in range(3):
        editor.placeBlock((x+3,y+1+yy,z+7),Block(e_ID))
    editor.placeBlock((x+1,y+1,z+5),Block(r_ID,{"facing": "south", "part": "foot"}))
    editor.placeBlock((x+2,y+1,z+5),Block(r_ID,{"facing": "south", "part": "foot"}))
    command = f"summon panda {x+1} {y+2} {z+6}"
    runCommand(command)
    command = f"summon panda {x+2} {y+2} {z+5}"
    runCommand(command)
    editor.placeBlock((x+3,y+1,z+4),Block(u_ID,{"facing": "east", "half": "top", "open": "true"}))
    editor.placeBlock((x+2,y+2,z+7),Block(i_ID))
    editor.placeBlock((x+3,y+4,z+7),Block(i_ID))
    editor.placeBlock((x+5,y+2,z+7),Block(i_ID))
    editor.placeBlock((x+1,y+4,z+7),Block(o_ID,{"facing": "north"}))
    editor.placeBlock((x+1,y+5,z+7),Block("oak_slab",{"type": "bottom"}))
    editor.placeBlock((x+1,y+2,z+7),Block(p_ID))
    editor.placeBlock((x+2,y+4,z+7),Block(a_ID))

    editor.placeBlock((x+1,y+2,z+1),Block(o_ID,{"facing": "east", "type": "left"}))
    editor.placeBlock((x+1,y+2,z+2),Block(o_ID,{"facing": "east", "type": "right"}))
    for zz in range(2):
        editor.placeBlock((x+3,y+1,z+5+zz),Block(s_ID))
        editor.placeBlock((x+1,y+1,z+1+zz),Block(e_ID,{"facing": "east"}))
        editor.placeBlock((x+1,y+3,z+1+zz),Block(y_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
      


def kagu_w(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID):
    editor.placeBlock((x+4,y+1,z+8),Block(q_ID))
    editor.placeBlock((x+4,y+2,z+8),Block(q_ID))
    editor.placeBlock((x+1,y+4,z+1),Block(w_ID,{"facing": "east"}))
    editor.placeBlock((x+1,y+4,z+2),Block(e_ID,{"facing": "east"}))
    for yy in range(3):
        editor.placeBlock((x+4,y+1+yy,z+7),Block(r_ID))
    for xx in range(3):
        editor.placeBlock((x+5+xx,y+3,z+7),Block(r_ID))
    editor.placeBlock((x+5,y+1,z+7),Block(t_ID))
    editor.placeBlock((x+6,y+1,z+7),Block(y_ID))
    editor.placeBlock((x+7,y+1,z+7),Block(u_ID))
    editor.placeBlock((x+7,y+2,z+7),Block(i_ID))
def road_w(x,y,z,q_id):
    for xx in range(18):
        for zz in range(25):
            editor.placeBlock((x-3+xx,y-1,z-8+zz),Block(q_id))
    light(x+13,y,z-7)
    light(x-2,y,z-7)
    light(x+13,y,z+15)
    light(x-2,y,z+15)
    light(x+13,y,z)
    light(x+13,y,z+8)
    light(x+5,y,z+15)
    light(x+5,y,z-7)
    light(x-2,y,z)
    light(x-2,y,z+8)

  

#east
def buildHouse_e(x, y, z, q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):    
    ##柱
    for yy in range(7):
        editor.placeBlock((x,y+yy,z),Block(q_ID))
        editor.placeBlock((x-8,y+yy,z),Block(q_ID))
        editor.placeBlock((x,y+yy,z+8),Block(q_ID))
        editor.placeBlock((x-8,y+yy,z+8),Block(q_ID))
    for xx in range(7):
        editor.placeBlock((x-1-xx,y+5,z),Block(q_ID))
        editor.placeBlock((x-1-xx,y+5,z+8),Block(q_ID))
    for zz in range(7):
        for yy in range(2):
            editor.placeBlock((x,y+4+yy,z+1+zz),Block(q_ID))
            editor.placeBlock((x-8,y+4+yy,z+1+zz),Block(q_ID))
     ##屋根
    for zz in range(5):
        editor.placeBlock((x+1,y+5,z+2*zz),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((x+2,y+4,z+2*zz),Block(w_ID,{"type": "top"}))
        editor.placeBlock((x-9,y+5,z+2*zz),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((x-10,y+4,z+2*zz),Block(w_ID,{"type": "top"}))
    for zz in range(9):
        editor.placeBlock((x-1,y+7,z+zz),Block(e_ID))
        editor.placeBlock((x-2,y+8,z+zz),Block(e_ID))
        editor.placeBlock((x-3,y+9,z+zz),Block(e_ID))
        editor.placeBlock((x-4,y+10,z+zz),Block(e_ID))

        editor.placeBlock((x-7,y+7,z+zz),Block(e_ID))
        editor.placeBlock((x-6,y+8,z+zz),Block(e_ID))
        editor.placeBlock((x-5,y+9,z+zz),Block(e_ID))
        editor.placeBlock((x-4,y+10,z+zz),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((x+1,y+6,z+2*zz),Block(e_ID))
        editor.placeBlock((x,y+7,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y+8,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-2,y+9,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-3,y+10,z+2*zz),Block(t_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-4,y+11,z+2*zz),Block(e_ID))

        editor.placeBlock((x-9,y+6,z+2*zz),Block(e_ID))
        editor.placeBlock((x-8,y+7,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-7,y+8,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-6,y+9,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-5,y+10,z+2*zz),Block(t_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-4,y+11,z+2*zz),Block(e_ID))

        editor.placeBlock((x+2,y+6,z+2*zz),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((x-10,y+6,z+2*zz),Block(r_ID,{"type": "bottom"}))
        for xx in range(2):
            editor.placeBlock((x+2+xx,y+5,z+2*zz),Block(e_ID))
            editor.placeBlock((x-10-xx,y+5,z+2*zz),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((x,y+6,z+1+2*zz),Block(e_ID))
        editor.placeBlock((x+1,y+5,z+1+2*zz),Block(e_ID))

        editor.placeBlock((x-8,y+6,z+1+2*zz),Block(e_ID))
        editor.placeBlock((x-9,y+5,z+1+2*zz),Block(e_ID))

        editor.placeBlock((x+2,y+5,z+1+2*zz),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((x-10,y+5,z+1+2*zz),Block(r_ID,{"type": "bottom"}))

    editor.placeBlock((x+3,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+2,y+5,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+1,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+1,y+6,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x,y+6,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x,y+7,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-2,y+7,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-2,y+8,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-3,y+8,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-3,y+9,z-1),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x-4,y+9,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-4,y+10,z-1),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x-11,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-10,y+5,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-9,y+5,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-9,y+6,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x-8,y+6,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-8,y+7,z-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x-7,y+7,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-6,y+7,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-6,y+8,z-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-5,y+8,z-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-5,y+9,z-1),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x+3,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+2,y+5,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x+1,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x+1,y+6,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x,y+6,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x,y+7,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-2,y+7,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-2,y+8,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-3,y+8,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-3,y+9,z+9),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x-4,y+9,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-4,y+10,z+9),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x-11,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-10,y+5,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-9,y+5,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-9,y+6,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x-8,y+6,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-8,y+7,z+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((x-7,y+7,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-6,y+7,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-6,y+8,z+9),Block(y_ID,{"type": "double"}))
    editor.placeBlock((x-5,y+8,z+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((x-5,y+9,z+9),Block(y_ID,{"type": "double"}))

    editor.placeBlock((x-4,y+12,z+4),Block("lantern"))
    editor.placeBlock((x-4,y+11,z-1),Block("lantern"))
    editor.placeBlock((x-4,y+11,z+9),Block("lantern"))

    editor.placeBlock((x+3,y+6,z+2),Block("lantern"))
    editor.placeBlock((x+3,y+6,z+6),Block("lantern"))
    editor.placeBlock((x-11,y+6,z+2),Block("lantern"))
    editor.placeBlock((x-11,y+6,z+6),Block("lantern"))


   
def Wall_e(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(2):
        editor.placeBlock((x-1-xx,y+6,z),Block(q_ID))
        editor.placeBlock((x-6-xx,y+6,z),Block(q_ID))
        editor.placeBlock((x-2-xx,y+7,z),Block(q_ID))
        editor.placeBlock((x-5-xx,y+7,z),Block(q_ID))

        editor.placeBlock((x-1-xx,y+6,z+8),Block(q_ID))
        editor.placeBlock((x-6-xx,y+6,z+8),Block(q_ID))
        editor.placeBlock((x-2-xx,y+7,z+8),Block(q_ID))
        editor.placeBlock((x-5-xx,y+7,z+8),Block(q_ID))

    for xx in range(3):
        editor.placeBlock((x-3-xx,y+8,z),Block(q_ID))
        editor.placeBlock((x-3-xx,y+8,z+8),Block(q_ID))
        
        editor.placeBlock((x-3-xx,y+6,z),Block(w_ID))
        editor.placeBlock((x-3-xx,y+6,z-1),Block("oak_trapdoor",{"facing": "north", "open": "true"}))
        editor.placeBlock((x-3-xx,y+6,z+8),Block(w_ID))
        editor.placeBlock((x-3-xx,y+6,z+9),Block("oak_trapdoor",{"facing": "south", "open": "true"}))
    editor.placeBlock((x-4,y+7,z),Block(w_ID))
    editor.placeBlock((x-4,y+7,z-1),Block("oak_trapdoor",{"facing": "north", "open": "true"}))
    editor.placeBlock((x-4,y+7,z+8),Block(w_ID))
    editor.placeBlock((x-4,y+7,z+9),Block("oak_trapdoor",{"facing": "south", "open": "true"}))

    for zz in range(5):
        editor.placeBlock((x+1,y+4,z+2*zz),Block(q_ID))
        editor.placeBlock((x-9,y+4,z+2*zz),Block(q_ID))
    for zz in range(4):
        editor.placeBlock((x+2,y+4,z+1+2*zz),Block(q_ID))
        editor.placeBlock((x-10,y+4,z+1+2*zz),Block(q_ID))

        editor.placeBlock((x+1,y+4,z+1+2*zz),Block(w_ID))
        editor.placeBlock((x-9,y+4,z+1+2*zz),Block(w_ID))

    def wall1(x,y,z):
        for yy in range(5):
            editor.placeBlock((x,y+yy,z),Block(e_ID))
            editor.placeBlock((x-6,y+yy,z),Block(e_ID))
        for xx in range(5):
            editor.placeBlock((x-1-xx,y+4,z),Block(e_ID))
            for yy in range(4):
                editor.placeBlock((x-1-xx,y+yy,z),Block(r_ID))
    def wall2(x,y,z):
        for zz in range(7):
            editor.placeBlock((x,y,z+1+zz),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((x,y+1+yy,z+2),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+6),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+1),Block(r_ID))
            editor.placeBlock((x,y+1+yy,z+7),Block(r_ID))

            editor.placeBlock((x-1,y+1+yy,z),Block(e_ID))
            editor.placeBlock((x-7,y+1+yy,z),Block(e_ID))
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((x,y+1+yy,z+3+zz),Block(r_ID))
        for xx in range(7):
            editor.placeBlock((x-1-xx,y+4,z),Block(e_ID))
    def wall3(x,y,z):
        for zz in range(2):
            editor.placeBlock((x,y,z+1+zz),Block(e_ID))
            editor.placeBlock((x,y,z+6+zz),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((x,y+1+yy,z+2),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+6),Block(e_ID))
            editor.placeBlock((x,y+1+yy,z+1),Block(r_ID))
            editor.placeBlock((x,y+1+yy,z+7),Block(r_ID))
        for zz in range(3):
            editor.placeBlock((x,y+3,z+3+zz),Block(e_ID))
    ##天井,床
    for xx in range(7):
        for zz in range(7):
            editor.placeBlock((x-1-xx,y+5,z+1+zz),Block(q_ID))
            editor.placeBlock((x-1-xx,y,z+1+zz),Block(q_ID))
    for zz in range(3):
        editor.placeBlock((x-8,y,z+3+zz),Block(q_ID))
    ##階段 
    editor.placeBlock((x-9,y,z+3),Block(t_ID,{"facing": "north", "half": "bottom"}))
    editor.placeBlock((x-9,y,z+4),Block(t_ID,{"facing": "east", "half": "bottom"}))
    editor.placeBlock((x-9,y,z+5),Block(t_ID,{"facing": "south", "half": "bottom"}))
    editor.placeBlock((x-1,y,z),Block(t_ID,{"facing": "west", "half": "top"}))
    editor.placeBlock((x-7,y,z),Block(t_ID,{"facing": "east", "half": "top"}))
    editor.placeBlock((x-2,y,z),Block(t_ID,{"facing": "south", "half": "bottom"}))
    editor.placeBlock((x-6,y,z),Block(t_ID,{"facing": "south", "half": "bottom"}))
    for xx in range(3):
        editor.placeBlock((x-3-xx,y,z),Block(y_ID,{"type": "top"}))
    wall1(x-1,y,z+8)
    wall2(x,y,z)
    wall3(x-8,y,z)

    

def niwa_e(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(3):
        editor.placeBlock((x-9+xx,y-1,z),Block(e_ID))
    for xx in range(11):
        editor.placeBlock((x-xx,y-1,z-5),Block(e_ID))
        editor.placeBlock((x-xx,y-1,z+13),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((x,y-1,z-1-zz),Block(e_ID))
        editor.placeBlock((x,y-1,z+9+zz),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((x-11,y-1,z-1-zz),Block(e_ID))
        editor.placeBlock((x-11,y-1,z+9+zz),Block(e_ID))

    for yy in range(2):
        for xx in range(3):
            editor.placeBlock((x-9-xx,y+yy,z),Block(q_ID))
        for xx in range(11):
            editor.placeBlock((x-xx,y+yy,z-5),Block(q_ID))
            editor.placeBlock((x-xx,y+yy,z+13),Block(q_ID))
        for zz in range(4):
            editor.placeBlock((x,y+yy,z-1-zz),Block(q_ID))
            editor.placeBlock((x,y+yy,z+9+zz),Block(q_ID))
        for zz in range(5):
            editor.placeBlock((x-11,y+yy,z-1-zz),Block(q_ID))
            editor.placeBlock((x-11,y+yy,z+9+zz),Block(q_ID))

    editor.placeBlock((x-9,y,z+9),Block(w_ID,{"facing": "south", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x-9,y+1,z+9),Block(w_ID,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x-10,y,z+9),Block(w_ID,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x-10,y+1,z+9),Block(w_ID,{"facing": "south", "half": "upper", "hinge": "left"}))



    for yy in range(4):
        editor.placeBlock((x-9,y+yy,z+2),Block(r_ID))
        editor.placeBlock((x-9,y+yy,z+6),Block(r_ID))
    for xx in range(3):
        for zz in range(8):
            editor.placeBlock((x-9-xx,y-1,z+1+zz),Block(t_ID))
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x-5+xx,y-1,z-1-zz),Block(t_ID))
    ##ドア
    editor.placeBlock((x-8,y+1,z+3),Block(y_ID,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x-8,y+2,z+3),Block(y_ID,{"facing": "east", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x-8,y+1,z+4),Block(y_ID,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x-8,y+2,z+4),Block(y_ID,{"facing": "east", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x-8,y+1,z+5),Block(y_ID,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x-8,y+2,z+5),Block(y_ID,{"facing": "east", "half": "upper", "hinge": "left"}))

def farm_e(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID):
    for xx in range(5):
        for zz in range(4):
            editor.placeBlock((x-1-xx,y-1,z+9+zz),Block(q_ID))
            editor.placeBlock((x-1-xx,y,z+9+zz),Block(w_ID,{"age": "7"}))
    editor.placeBlock((x-4,y-1,z+10),Block(e_ID))
    editor.placeBlock((x-9,y,z+12),Block(r_ID))
    editor.placeBlock((x-10,y,z+11),Block(r_ID))
    for yy in range(2):
        editor.placeBlock((x-10,y+yy,z+12),Block(r_ID))
    editor.placeBlock((x-9,y,z+11),Block(y_ID))
    editor.placeBlock((x-9,y+1,z+12),Block(t_ID))
    editor.placeBlock((x-8,y,z+12),Block(u_ID,{"level": "3"}))
    editor.placeBlock((x-6,y,z+12),Block(i_ID))
    editor.placeBlock((x-6,y+1,z+12),Block(o_ID))
    editor.placeBlock((x-6,y+3,z),Block(o_ID,{"hanging": "true"}))
    editor.placeBlock((x-2,y+3,z),Block(o_ID,{"hanging": "true"}))
def pool_e(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((x-6-xx,y-1,z-1-zz),Block(q_ID))
    for zz in range(2):
        editor.placeBlock((x-10,y-1,z-2-zz),Block(q_ID))
    editor.placeBlock((x-10,y-1,z-1),Block("grass_block"))
    editor.placeBlock((x-10,y,z-1),Block(w_ID,{"half": "lower"}))
    editor.placeBlock((x-10,y+1,z-1),Block(w_ID,{"half": "upper"}))
    editor.placeBlock((x-10,y-1,z-4),Block("grass_block"))
    editor.placeBlock((x-10,y,z-4),Block(e_ID,{"half": "lower"}))
    editor.placeBlock((x-10,y+1,z-4),Block(e_ID,{"half": "upper"}))
    editor.placeBlock((x-9,y-2,z-3),Block("glowstone"))
    editor.placeBlock((x-8,y,z-3),Block(r_ID))
    editor.placeBlock((x-7,y,z-2),Block(r_ID))
    editor.placeBlock((x-1,y,z-1),Block(t_ID,{"facing": "west"}))
    editor.placeBlock((x-1,y,z-2),Block(y_ID))
    editor.placeBlock((x-1,y,z-3),Block(u_ID))
    editor.placeBlock((x-1,y,z-4),Block(i_ID))
    editor.placeBlock((x-2,y,z-4),Block(o_ID))
    editor.placeBlock((x-3,y,z-4),Block(p_ID))
    editor.placeBlock((x-1,y+1,z-4),Block(s_ID))
    editor.placeBlock((x-2,y,z-3),Block(a_ID,{"facing": "west"}))

def heya_e(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(5):
        editor.placeBlock((x-2-xx,y+4,z-1),Block(q_ID))
    for xx in range(2):
        editor.placeBlock((x-1-xx,y+1,z+7),Block(w_ID))
        editor.placeBlock((x-1-xx,y+3,z+7),Block(t_ID,{"type": "top"}))
        editor.placeBlock((x-1-xx,y+1,z+4),Block(y_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
    for yy in range(3):
        editor.placeBlock((x-3,y+1+yy,z+7),Block(e_ID))
    editor.placeBlock((x-1,y+1,z+5),Block(r_ID,{"facing": "south", "part": "foot"}))
    editor.placeBlock((x-2,y+1,z+5),Block(r_ID,{"facing": "south", "part": "foot"}))
    command = f"summon panda {x-1} {y+2} {z+6}"
    runCommand(command)
    command = f"summon panda {x-2} {y+2} {z+5}"
    runCommand(command)
    editor.placeBlock((x-3,y+1,z+4),Block(u_ID,{"facing": "west", "half": "top", "open": "true"}))
    editor.placeBlock((x-2,y+2,z+7),Block(i_ID))
    editor.placeBlock((x-3,y+4,z+7),Block(i_ID))
    editor.placeBlock((x-5,y+2,z+7),Block(i_ID))
    editor.placeBlock((x-1,y+4,z+7),Block(o_ID))
    editor.placeBlock((x-1,y+5,z+7),Block("oak_slab",{"type": "bottom"}))
    editor.placeBlock((x-1,y+2,z+7),Block(p_ID))
    editor.placeBlock((x-2,y+4,z+7),Block(a_ID))

    editor.placeBlock((x-1,y+2,z+1),Block(o_ID,{"facing": "west", "type": "left"}))
    editor.placeBlock((x-1,y+2,z+2),Block(o_ID,{"facing": "west", "type": "right"}))
    for zz in range(2):
        editor.placeBlock((x-3,y+1,z+5+zz),Block(s_ID))
        editor.placeBlock((x-1,y+1,z+1+zz),Block(e_ID,{"facing": "west"}))
        editor.placeBlock((x-1,y+3,z+1+zz),Block(y_ID,{"facing": "east", "half": "bottom", "shape": "straight"}))
      


def kagu_e(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID):   
    editor.placeBlock((x-4,y+1,z+8),Block(q_ID))
    editor.placeBlock((x-4,y+2,z+8),Block(q_ID))
    editor.placeBlock((x-1,y+4,z+1),Block(w_ID,{"facing": "west"}))
    editor.placeBlock((x-1,y+4,z+2),Block(e_ID,{"facing": "west"}))
    for yy in range(3):
        editor.placeBlock((x-4,y+1+yy,z+7),Block(r_ID))
    for xx in range(3):
        editor.placeBlock((x-5-xx,y+3,z+7),Block(r_ID))
    editor.placeBlock((x-5,y+1,z+7),Block(t_ID))
    editor.placeBlock((x-6,y+1,z+7),Block(y_ID))
    editor.placeBlock((x-7,y+1,z+7),Block(u_ID))
    editor.placeBlock((x-7,y+2,z+7),Block(i_ID))
def road_e(x,y,z,q_id):
    for xx in range(18):
        for zz in range(25):
            editor.placeBlock((x+3-xx,y-1,z-8+zz),Block(q_id))
    light(x-13,y,z-7)
    light(x+2,y,z-7)
    light(x-13,y,z+15)
    light(x+2,y,z+15)
    light(x-13,y,z)
    light(x-13,y,z+8)
    light(x-5,y,z+15)
    light(x-5,y,z-7)
    light(x+2,y,z)
    light(x+2,y,z+8)






#north
def buildHouse_n(x, y, z, q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):    
    ##柱
    for yy in range(7):
        editor.placeBlock((z,y+yy,x),Block(q_ID))
        editor.placeBlock((z,y+yy,x+8),Block(q_ID))
        editor.placeBlock((z+8,y+yy,x),Block(q_ID))
        editor.placeBlock((z+8,y+yy,x+8),Block(q_ID))
    for xx in range(7):
        editor.placeBlock((z,y+5,x+1+xx),Block(q_ID))
        editor.placeBlock((z+8,y+5,x+1+xx),Block(q_ID))
    for zz in range(7):
        for yy in range(2):
            editor.placeBlock((z+1+zz,y+4+yy,x),Block(q_ID))
            editor.placeBlock((z+1+zz,y+4+yy,x+8),Block(q_ID))
     ##屋根
    for zz in range(5):
        editor.placeBlock((z+2*zz,y+5,x-1),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x-2),Block(w_ID,{"type": "top"}))
        editor.placeBlock((z+2*zz,y+5,x+9),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x+10),Block(w_ID,{"type": "top"}))
    for zz in range(9):
        editor.placeBlock((z+zz,y+7,x+1),Block(e_ID))
        editor.placeBlock((z+zz,y+8,x+2),Block(e_ID))
        editor.placeBlock((z+zz,y+9,x+3),Block(e_ID))
        editor.placeBlock((z+zz,y+10,x+4),Block(e_ID))

        editor.placeBlock((z+zz,y+7,x+7),Block(e_ID))
        editor.placeBlock((z+zz,y+8,x+6),Block(e_ID))
        editor.placeBlock((z+zz,y+9,x+5),Block(e_ID))
        editor.placeBlock((z+zz,y+10,x+4),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((z+2*zz,y+6,x-1),Block(e_ID))
        editor.placeBlock((z+2*zz,y+7,x),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+8,x+1),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+9,x+2),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+10,x+3),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+11,x+4),Block(e_ID))

        editor.placeBlock((z+2*zz,y+6,x+9),Block(e_ID))
        editor.placeBlock((z+2*zz,y+7,x+8),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+8,x+7),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+9,x+6),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+10,x+5),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+11,x+4),Block(e_ID))

        editor.placeBlock((z+2*zz,y+6,x-2),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+6,x+10),Block(r_ID,{"type": "bottom"}))
        for xx in range(2):
            editor.placeBlock((z+2*zz,y+5,x-2-xx),Block(e_ID))
            editor.placeBlock((z+2*zz,y+5,x+10+xx),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((z+1+2*zz,y+6,x),Block(e_ID))
        editor.placeBlock((z+1+2*zz,y+5,x-1),Block(e_ID))

        editor.placeBlock((z+1+2*zz,y+6,x+8),Block(e_ID))
        editor.placeBlock((z+1+2*zz,y+5,x+9),Block(e_ID))

        editor.placeBlock((z+1+2*zz,y+5,x-2),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((z+1+2*zz,y+5,x+10),Block(r_ID,{"type": "bottom"}))

    editor.placeBlock((z-1,y+5,x-3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+5,x-2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+5,x-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+6,x-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+6,x),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+7,x+1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x+2),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+8,x+2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+8,x+3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+9,x+3),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z-1,y+9,x+4),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+10,x+4),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z-1,y+5,x+11),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+5,x+10),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+5,x+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+6,x+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+6,x+8),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x+8),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+7,x+7),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x+6),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+8,x+6),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+8,x+5),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+9,x+5),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+9,y+5,x-3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+5,x-2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+5,x-1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+6,x-1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+6,x),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+7,x+1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x+2),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+8,x+2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+8,x+3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+9,x+3),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+9,y+9,x+4),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+10,x+4),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+9,y+5,x+11),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+5,x+10),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+5,x+9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+6,x+9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+6,x+8),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x+8),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+7,x+7),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x+6),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+8,x+6),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+8,x+5),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+9,x+5),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+4,y+12,x+4),Block("lantern"))
    editor.placeBlock((z-1,y+11,x+4),Block("lantern"))
    editor.placeBlock((z+9,y+11,x+4),Block("lantern"))
    editor.placeBlock((z+2,y+6,x-3),Block("lantern"))
    editor.placeBlock((z+6,y+6,x-3),Block("lantern"))
    editor.placeBlock((z+2,y+6,x+11),Block("lantern"))
    editor.placeBlock((z+6,y+6,x+11),Block("lantern"))



def Wall_n(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(2):
        editor.placeBlock((z,y+6,x+1+xx),Block(q_ID))
        editor.placeBlock((z,y+6,x+6+xx),Block(q_ID))
        editor.placeBlock((z,y+7,x+2+xx),Block(q_ID))
        editor.placeBlock((z,y+7,x+5+xx),Block(q_ID))

        editor.placeBlock((z+8,y+6,x+1+xx),Block(q_ID))
        editor.placeBlock((z+8,y+6,x+6+xx),Block(q_ID))
        editor.placeBlock((z+8,y+7,x+2+xx),Block(q_ID))
        editor.placeBlock((z+8,y+7,x+5+xx),Block(q_ID))

    for xx in range(3):
        editor.placeBlock((z,y+8,x+3+xx),Block(q_ID))
        editor.placeBlock((z+8,y+8,x+3+xx),Block(q_ID))
        
        editor.placeBlock((z,y+6,x+3+xx),Block(w_ID))
        editor.placeBlock((z-1,y+6,x+3+xx),Block("oak_trapdoor",{"facing": "west", "open": "true"}))
        editor.placeBlock((z+8,y+6,x+3+xx),Block(w_ID))
        editor.placeBlock((z+9,y+6,x+3+xx),Block("oak_trapdoor",{"facing": "east", "open": "true"}))
    editor.placeBlock((z,y+7,x+4),Block(w_ID))
    editor.placeBlock((z-1,y+7,x+4),Block("oak_trapdoor",{"facing": "west", "open": "true"}))
    editor.placeBlock((z+8,y+7,x+4),Block(w_ID))
    editor.placeBlock((z+9,y+7,x+4),Block("oak_trapdoor",{"facing": "east", "open": "true"}))

    for zz in range(5):
        editor.placeBlock((z+2*zz,y+4,x-1),Block(q_ID))
        editor.placeBlock((z+2*zz,y+4,x+9),Block(q_ID))
    for zz in range(4):
        editor.placeBlock((z+1+2*zz,y+4,x-2),Block(q_ID))
        editor.placeBlock((z+1+2*zz,y+4,x+10),Block(q_ID))

        editor.placeBlock((z+1+2*zz,y+4,x-1),Block(w_ID))
        editor.placeBlock((z+1+2*zz,y+4,x+9),Block(w_ID))

    def wall1(x,y,z):
        for yy in range(5):
            editor.placeBlock((z,y+yy,x),Block(e_ID))
            editor.placeBlock((z,y+yy,x+6),Block(e_ID))
        for xx in range(5):
            editor.placeBlock((z,y+4,x+1+xx),Block(e_ID))
            for yy in range(4):
                editor.placeBlock((z,y+yy,x+1+xx),Block(r_ID))
    def wall2(x,y,z):
        for zz in range(7):
            editor.placeBlock((z+1+zz,y,x),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((z+2,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+6,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+1,y+1+yy,x),Block(r_ID))
            editor.placeBlock((z+7,y+1+yy,x),Block(r_ID))

            editor.placeBlock((z,y+1+yy,x+1),Block(e_ID))
            editor.placeBlock((z,y+1+yy,x+7),Block(e_ID))
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((z+3+zz,y+1+yy,x),Block(r_ID))
        for xx in range(7):
            editor.placeBlock((z,y+4,x+1+xx),Block(e_ID))
    def wall3(x,y,z):
        for zz in range(2):
            editor.placeBlock((z+1+zz,y,x),Block(e_ID))
            editor.placeBlock((z+6+zz,y,x),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((z+2,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+6,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+1,y+1+yy,x),Block(r_ID))
            editor.placeBlock((z+7,y+1+yy,x),Block(r_ID))
        for zz in range(3):
            editor.placeBlock((z+3+zz,y+3,x),Block(e_ID))
    ##天井,床   
    for xx in range(7):
        for zz in range(7):
            editor.placeBlock((z+1+zz,y+5,x+1+xx),Block(q_ID))
            editor.placeBlock((z+1+zz,y,x+1+xx),Block(q_ID))
    for zz in range(3):
        editor.placeBlock((z+3+zz,y,x+8),Block(q_ID))
    ##階段
    editor.placeBlock((z+3,y,x+9),Block(t_ID,{"facing": "west", "half": "bottom"}))
    editor.placeBlock((z+4,y,x+9),Block(t_ID,{"facing": "north", "half": "bottom"}))
    editor.placeBlock((z+5,y,x+9),Block(t_ID,{"facing": "east", "half": "bottom"}))
    editor.placeBlock((z,y,x+1),Block(t_ID,{"facing": "south", "half": "top"}))
    editor.placeBlock((z,y,x+7),Block(t_ID,{"facing": "north", "half": "top"}))
    editor.placeBlock((z,y,x+2),Block(t_ID,{"facing": "east", "half": "bottom"}))
    editor.placeBlock((z,y,x+6),Block(t_ID,{"facing": "east", "half": "bottom"}))
    for xx in range(3):
        editor.placeBlock((z,y,x+3+xx),Block(y_ID,{"type": "top"}))
    wall1(x+1,y,z+8)
    wall2(x,y,z)
    wall3(x+8,y,z)

    

def niwa_n(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(3):
        editor.placeBlock((z,y-1,x+9+xx),Block(e_ID))
    for xx in range(11):
        editor.placeBlock((z-5,y-1,x+xx),Block(e_ID))
        editor.placeBlock((z+13,y-1,x+xx),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((z-1-zz,y-1,x),Block(e_ID))
        editor.placeBlock((z+9+zz,y-1,x),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((z-1-zz,y-1,x+11),Block(e_ID))
        editor.placeBlock((z+9+zz,y-1,x+11),Block(e_ID))

    for yy in range(2):
        for xx in range(3):
            editor.placeBlock((z,y+yy,x+9+xx),Block(q_ID))
        for xx in range(11):
            editor.placeBlock((z-5,y+yy,x+xx),Block(q_ID))
            editor.placeBlock((z+13,y+yy,x+xx),Block(q_ID))
        for zz in range(4):
            editor.placeBlock((z-1-zz,y+yy,x),Block(q_ID))
            editor.placeBlock((z+9+zz,y+yy,x),Block(q_ID))
        for zz in range(5):
            editor.placeBlock((z-1-zz,y+yy,x+11),Block(q_ID))
            editor.placeBlock((z+9+zz,y+yy,x+11),Block(q_ID))

    editor.placeBlock((z+9,y,x+9),Block(w_ID,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+9,y+1,x+9),Block(w_ID,{"facing": "east", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+9,y,x+10),Block(w_ID,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+9,y+1,x+10),Block(w_ID,{"facing": "east", "half": "upper", "hinge": "right"}))



    for yy in range(4):
        editor.placeBlock((z+2,y+yy,x+9),Block(r_ID))
        editor.placeBlock((z+6,y+yy,x+9),Block(r_ID))
    for xx in range(3):
        for zz in range(8):
            editor.placeBlock((z+1+zz,y-1,x+9+xx),Block(t_ID))
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((z-1-zz,y-1,x+2+xx),Block(t_ID))
    ##ドア
    editor.placeBlock((z+3,y+1,x+8),Block(y_ID,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+3,y+2,x+8),Block(y_ID,{"facing": "north", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+4,y+1,x+8),Block(y_ID,{"facing": "north", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+4,y+2,x+8),Block(y_ID,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z+5,y+1,x+8),Block(y_ID,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+5,y+2,x+8),Block(y_ID,{"facing": "north", "half": "upper", "hinge": "left"}))

def farm_n(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID):
    for xx in range(5):
        for zz in range(4):
            editor.placeBlock((z+9+zz,y-1,x+1+xx),Block(q_ID))
            editor.placeBlock((z+9+zz,y,x+1+xx),Block(w_ID,{"age": "7"}))
    editor.placeBlock((z+10,y-1,x+4),Block(e_ID))
    editor.placeBlock((z+12,y,x+9),Block(r_ID))
    editor.placeBlock((z+11,y,x+10),Block(r_ID))
    for yy in range(2):
        editor.placeBlock((z+12,y+yy,x+10),Block(r_ID))
    editor.placeBlock((z+11,y,x+9),Block(y_ID))
    editor.placeBlock((z+12,y+1,x+9),Block(t_ID))
    editor.placeBlock((z+12,y,x+8),Block(u_ID,{"level": "3"}))
    editor.placeBlock((z+12,y,x+6),Block(i_ID))
    editor.placeBlock((z+12,y+1,x+6),Block(o_ID))
    editor.placeBlock((z,y+3,x+6),Block(o_ID,{"hanging": "true"}))
    editor.placeBlock((z,y+3,x+2),Block(o_ID,{"hanging": "true"}))
def pool_n(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((z-1-zz,y-1,x+6+xx),Block(q_ID))
    for zz in range(2):
        editor.placeBlock((z-2-zz,y-1,x+10),Block(q_ID))
    editor.placeBlock((z-1,y-1,x+10),Block("grass_block"))
    editor.placeBlock((z-1,y,x+10),Block(w_ID,{"half": "lower"}))
    editor.placeBlock((z-1,y+1,x+10),Block(w_ID,{"half": "upper"}))
    editor.placeBlock((z-4,y-1,x+10),Block("grass_block"))
    editor.placeBlock((z-4,y,x+10),Block(e_ID,{"half": "lower"}))
    editor.placeBlock((z-4,y+1,x+10),Block(e_ID,{"half": "upper"}))
    editor.placeBlock((z-3,y-2,x+9),Block("glowstone"))
    editor.placeBlock((z-3,y,x+8),Block(r_ID))
    editor.placeBlock((z-2,y,x+7),Block(r_ID))
    editor.placeBlock((z-1,y,x+1),Block(t_ID))
    editor.placeBlock((z-2,y,x+1),Block(y_ID))
    editor.placeBlock((z-3,y,x+1),Block(u_ID))
    editor.placeBlock((z-4,y,x+1),Block(i_ID))
    editor.placeBlock((z-4,y,x+2),Block(o_ID))
    editor.placeBlock((z-4,y,x+3),Block(p_ID))
    editor.placeBlock((z-4,y+1,x+1),Block(s_ID))
    editor.placeBlock((z-3,y,x+2),Block(a_ID,{"facing": "south"}))

def heya_n(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(5):
        editor.placeBlock((z-1,y+4,x+2+xx),Block(q_ID))
    for xx in range(2):
        editor.placeBlock((z+7,y+1,x+1+xx),Block(w_ID))
        editor.placeBlock((z+7,y+3,x+1+xx),Block(t_ID,{"type": "top"}))
        editor.placeBlock((z+4,y+1,x+1+xx),Block(y_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
    for yy in range(3):
        editor.placeBlock((z+7,y+1+yy,x+3),Block(e_ID))
    editor.placeBlock((z+5,y+1,x+1),Block(r_ID,{"facing": "east", "part": "foot"}))
    editor.placeBlock((z+5,y+1,x+2),Block(r_ID,{"facing": "east", "part": "foot"}))
    command = f"summon panda {z+5} {y+2} {x+2}"
    runCommand(command)
    command = f"summon panda {z+4} {y+2} {x+2}"
    runCommand(command)
    editor.placeBlock((z+4,y+1,x+3),Block(u_ID,{"facing": "south", "half": "top", "open": "true"}))
    editor.placeBlock((z+7,y+2,x+2),Block(i_ID))
    editor.placeBlock((z+7,y+4,x+3),Block(i_ID))
    editor.placeBlock((z+7,y+2,x+5),Block(i_ID))
    editor.placeBlock((z+7,y+4,x+1),Block(o_ID,{"facing": "west"}))
    editor.placeBlock((z+7,y+5,x+1),Block("oak_slab",{"type": "bottom"}))
    editor.placeBlock((z+7,y+2,x+1),Block(p_ID))
    editor.placeBlock((z+7,y+4,x+2),Block(a_ID))

    editor.placeBlock((z+1,y+2,x+1),Block(o_ID,{"facing": "south", "type": "left"}))
    editor.placeBlock((z+2,y+2,x+1),Block(o_ID,{"facing": "south", "type": "right"}))
    for zz in range(2):
        editor.placeBlock((z+5+zz,y+1,x+3),Block(s_ID))
        editor.placeBlock((z+1+zz,y+1,x+1),Block(e_ID,{"facing": "south"}))
        editor.placeBlock((z+1+zz,y+3,x+1),Block(y_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
      


def kagu_n(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID):
    editor.placeBlock((z+8,y+1,x+4),Block(q_ID))
    editor.placeBlock((z+8,y+2,x+4),Block(q_ID))
    editor.placeBlock((z+1,y+4,x+1),Block(w_ID,{"facing": "south"}))
    editor.placeBlock((z+2,y+4,x+1),Block(e_ID,{"facing": "south"}))
    for yy in range(3):
        editor.placeBlock((z+7,y+1+yy,x+4),Block(r_ID))
    for xx in range(3):
        editor.placeBlock((z+7,y+3,x+5+xx),Block(r_ID))
    editor.placeBlock((z+7,y+1,x+5),Block(t_ID))
    editor.placeBlock((z+7,y+1,x+6),Block(y_ID))
    editor.placeBlock((z+7,y+1,x+7),Block(u_ID))
    editor.placeBlock((z+7,y+2,x+7),Block(i_ID))
def road_n(x,y,z,q_id):   
    for xx in range(18):
        for zz in range(25):
            editor.placeBlock((z-8+zz,y-1,x-3+xx),Block(q_id))
    light(z-7,y,x-2)
    light(z-7,y,x+13)
    light(z+15,y,x-2)
    light(z+15,y,x+13)
    light(z,y,x+13)
    light(z+8,y,x+13)
    light(z-7,y,x+6)
    light(z,y,x-2)
    light(z+8,y,x-2)

#south
def buildHouse_s(x, y, z, q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):    
    ##柱
    for yy in range(7):
        editor.placeBlock((z,y+yy,x),Block(q_ID))
        editor.placeBlock((z,y+yy,x-8),Block(q_ID))
        editor.placeBlock((z+8,y+yy,x),Block(q_ID))
        editor.placeBlock((z+8,y+yy,x-8),Block(q_ID))
    for xx in range(7):
        editor.placeBlock((z,y+5,x-1-xx),Block(q_ID))
        editor.placeBlock((z+8,y+5,x-1-xx),Block(q_ID))
    for zz in range(7):
        for yy in range(2):
            editor.placeBlock((z+1+zz,y+4+yy,x),Block(q_ID))
            editor.placeBlock((z+1+zz,y+4+yy,x-8),Block(q_ID))
     ##屋根
    for zz in range(5):
        editor.placeBlock((z+2*zz,y+5,x+1),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x+2),Block(w_ID,{"type": "top"}))
        editor.placeBlock((z+2*zz,y+5,x-9),Block(w_ID,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x-10),Block(w_ID,{"type": "top"}))
    for zz in range(9):
        editor.placeBlock((z+zz,y+7,x-1),Block(e_ID))
        editor.placeBlock((z+zz,y+8,x-2),Block(e_ID))
        editor.placeBlock((z+zz,y+9,x-3),Block(e_ID))
        editor.placeBlock((z+zz,y+10,x-4),Block(e_ID))

        editor.placeBlock((z+zz,y+7,x-7),Block(e_ID))
        editor.placeBlock((z+zz,y+8,x-6),Block(e_ID))
        editor.placeBlock((z+zz,y+9,x-5),Block(e_ID))
        editor.placeBlock((z+zz,y+10,x-4),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((z+2*zz,y+6,x+1),Block(e_ID))
        editor.placeBlock((z+2*zz,y+7,x),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+8,x-1),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+9,x-2),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+10,x-3),Block(t_ID,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+11,x-4),Block(e_ID))

        editor.placeBlock((z+2*zz,y+6,x-9),Block(e_ID))
        editor.placeBlock((z+2*zz,y+7,x-8),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+8,x-7),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+9,x-6),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+10,x-5),Block(t_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+2*zz,y+11,x-4),Block(e_ID))

        editor.placeBlock((z+2*zz,y+6,x+2),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+6,x-10),Block(r_ID,{"type": "bottom"}))
        for xx in range(2):
            editor.placeBlock((z+2*zz,y+5,x+2+xx),Block(e_ID))
            editor.placeBlock((z+2*zz,y+5,x-10-xx),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((z+1+2*zz,y+6,x),Block(e_ID))
        editor.placeBlock((z+1+2*zz,y+5,x+1),Block(e_ID))

        editor.placeBlock((z+1+2*zz,y+6,x-8),Block(e_ID))
        editor.placeBlock((z+1+2*zz,y+5,x-9),Block(e_ID))

        editor.placeBlock((z+1+2*zz,y+5,x+2),Block(r_ID,{"type": "bottom"}))
        editor.placeBlock((z+1+2*zz,y+5,x-10),Block(r_ID,{"type": "bottom"}))

    editor.placeBlock((z-1,y+5,x+3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+5,x+2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+5,x+1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+6,x+1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+6,x),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+7,x-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x-2),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+8,x-2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+8,x-3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+9,x-3),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z-1,y+9,x-4),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+10,x-4),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z-1,y+5,x-11),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+5,x-10),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+5,x-9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+6,x-9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+6,x-8),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x-8),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z-1,y+7,x-7),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x-6),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+8,x-6),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z-1,y+8,x-5),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z-1,y+9,x-5),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+9,y+5,x+3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+5,x+2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+5,x+1),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+6,x+1),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+6,x),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+7,x-1),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x-2),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+8,x-2),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+8,x-3),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+9,x-3),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+9,y+9,x-4),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+10,x-4),Block(y_ID,{"type": "double"}))

    editor.placeBlock((z+9,y+5,x-11),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+5,x-10),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+5,x-9),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+6,x-9),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+6,x-8),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x-8),Block(y_ID,{"type": "bottom"}))
    editor.placeBlock((z+9,y+7,x-7),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+7,x-6),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+8,x-6),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+9,y+8,x-5),Block(y_ID,{"type": "top"}))
    editor.placeBlock((z+9,y+9,x-5),Block(y_ID,{"type": "double"}))
    editor.placeBlock((z+4,y+12,x-4),Block("lantern"))
    editor.placeBlock((z-1,y+11,x-4),Block("lantern"))
    editor.placeBlock((z+9,y+11,x-4),Block("lantern"))
    editor.placeBlock((z+2,y+6,x-11),Block("lantern"))
    editor.placeBlock((z+6,y+6,x-11),Block("lantern"))
    editor.placeBlock((z+2,y+6,x+3),Block("lantern"))
    editor.placeBlock((z+6,y+6,x+3),Block("lantern"))



   
def Wall_s(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(2):
        editor.placeBlock((z,y+6,x-1-xx),Block(q_ID))
        editor.placeBlock((z,y+6,x-6-xx),Block(q_ID))
        editor.placeBlock((z,y+7,x-2-xx),Block(q_ID))
        editor.placeBlock((z,y+7,x-5-xx),Block(q_ID))

        editor.placeBlock((z+8,y+6,x-1-xx),Block(q_ID))
        editor.placeBlock((z+8,y+6,x-6-xx),Block(q_ID))
        editor.placeBlock((z+8,y+7,x-2-xx),Block(q_ID))
        editor.placeBlock((z+8,y+7,x-5-xx),Block(q_ID))

    for xx in range(3):
        editor.placeBlock((z,y+8,x-3-xx),Block(q_ID))
        editor.placeBlock((z+8,y+8,x-3-xx),Block(q_ID))
        
        editor.placeBlock((z,y+6,x-3-xx),Block(w_ID))
        editor.placeBlock((z-1,y+6,x-3-xx),Block("oak_trapdoor",{"facing": "west", "open": "true"}))
        editor.placeBlock((z+8,y+6,x-3-xx),Block(w_ID))
        editor.placeBlock((z+9,y+6,x-3-xx),Block("oak_trapdoor",{"facing": "east", "open": "true"}))
    editor.placeBlock((z,y+7,x-4),Block(w_ID))
    editor.placeBlock((z-1,y+7,x-4),Block("oak_trapdoor",{"facing": "west", "open": "true"}))
    editor.placeBlock((z+8,y+7,x-4),Block(w_ID))
    editor.placeBlock((z+9,y+7,x-4),Block("oak_trapdoor",{"facing": "east", "open": "true"}))

    for zz in range(5):
        editor.placeBlock((z+2*zz,y+4,x+1),Block(q_ID))
        editor.placeBlock((z+2*zz,y+4,x-9),Block(q_ID))
    for zz in range(4):
        editor.placeBlock((z+1+2*zz,y+4,x+2),Block(q_ID))
        editor.placeBlock((z+1+2*zz,y+4,x-10),Block(q_ID))

        editor.placeBlock((z+1+2*zz,y+4,x+1),Block(w_ID))
        editor.placeBlock((z+1+2*zz,y+4,x-9),Block(w_ID))

    def wall1(x,y,z):
        for yy in range(5):
            editor.placeBlock((z,y+yy,x),Block(e_ID))
            editor.placeBlock((z,y+yy,x-6),Block(e_ID))
        for xx in range(5):
            editor.placeBlock((z,y+4,x-1-xx),Block(e_ID))
            for yy in range(4):
                editor.placeBlock((z,y+yy,x-1-xx),Block(r_ID))
    def wall2(x,y,z):
        for zz in range(7):
            editor.placeBlock((z+1+zz,y,x),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((z+2,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+6,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+1,y+1+yy,x),Block(r_ID))
            editor.placeBlock((z+7,y+1+yy,x),Block(r_ID))

            editor.placeBlock((z,y+1+yy,x-1),Block(e_ID))
            editor.placeBlock((z,y+1+yy,x-7),Block(e_ID))
        for zz in range(3):
            for yy in range(3):
                editor.placeBlock((z+3+zz,y+1+yy,x),Block(r_ID))
        for xx in range(7):
            editor.placeBlock((z,y+4,x-1-xx),Block(e_ID))
    def wall3(x,y,z):
        for zz in range(2):
            editor.placeBlock((z+1+zz,y,x),Block(e_ID))
            editor.placeBlock((z+6+zz,y,x),Block(e_ID))
        for yy in range(3):
            editor.placeBlock((z+2,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+6,y+1+yy,x),Block(e_ID))
            editor.placeBlock((z+1,y+1+yy,x),Block(r_ID))
            editor.placeBlock((z+7,y+1+yy,x),Block(r_ID))
        for zz in range(3):
            editor.placeBlock((z+3+zz,y+3,x),Block(e_ID))
    ##天井,床
    for xx in range(7):
        for zz in range(7):
            editor.placeBlock((z+1+zz,y+5,x-1-xx),Block(q_ID))
            editor.placeBlock((z+1+zz,y,x-1-xx),Block(q_ID))
    for zz in range(3):
        editor.placeBlock((z+3+zz,y,x-8),Block(q_ID))
    ##階段
    editor.placeBlock((z+3,y,x-9),Block(t_ID,{"facing": "west", "half": "bottom"}))
    editor.placeBlock((z+4,y,x-9),Block(t_ID,{"facing": "south", "half": "bottom"}))
    editor.placeBlock((z+5,y,x-9),Block(t_ID,{"facing": "east", "half": "bottom"}))
    editor.placeBlock((z,y,x-1),Block(t_ID,{"facing": "north", "half": "top"}))
    editor.placeBlock((z,y,x-7),Block(t_ID,{"facing": "south", "half": "top"}))
    editor.placeBlock((z,y,x-2),Block(t_ID,{"facing": "east", "half": "bottom"}))
    editor.placeBlock((z,y,x-6),Block(t_ID,{"facing": "east", "half": "bottom"}))
    for xx in range(3):
        editor.placeBlock((z,y,x-3-xx),Block(y_ID,{"type": "top"}))
    wall1(x-1,y,z+8)
    wall2(x,y,z)
    wall3(x-8,y,z)

    

def niwa_s(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID):
    for xx in range(3):
        editor.placeBlock((z,y-1,x-9-xx),Block(e_ID))
    for xx in range(11):
        editor.placeBlock((z-5,y-1,x-xx),Block(e_ID))
        editor.placeBlock((z+13,y-1,x-xx),Block(e_ID))
    for zz in range(4):
        editor.placeBlock((z-1-zz,y-1,x),Block(e_ID))
        editor.placeBlock((z+9+zz,y-1,x),Block(e_ID))
    for zz in range(5):
        editor.placeBlock((z-1-zz,y-1,x-11),Block(e_ID))
        editor.placeBlock((z+9+zz,y-1,x-11),Block(e_ID))

    for yy in range(2):
        for xx in range(3):
            editor.placeBlock((z,y+yy,x-9-xx),Block(q_ID))
        for xx in range(11):
            editor.placeBlock((z-5,y+yy,x-xx),Block(q_ID))
            editor.placeBlock((z+13,y+yy,x-xx),Block(q_ID))
        for zz in range(4):
            editor.placeBlock((z-1-zz,y+yy,x),Block(q_ID))
            editor.placeBlock((z+9+zz,y+yy,x),Block(q_ID))
        for zz in range(5):
            editor.placeBlock((z-1-zz,y+yy,x-11),Block(q_ID))
            editor.placeBlock((z+9+zz,y+yy,x-11),Block(q_ID))

    editor.placeBlock((z+9,y,x-9),Block(w_ID,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+9,y+1,x-9),Block(w_ID,{"facing": "east", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+9,y,x-10),Block(w_ID,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+9,y+1,x-10),Block(w_ID,{"facing": "east", "half": "upper", "hinge": "right"}))



    for yy in range(4):
        editor.placeBlock((z+2,y+yy,x-9),Block(r_ID))
        editor.placeBlock((z+6,y+yy,x-9),Block(r_ID))
    for xx in range(3):
        for zz in range(8):
            editor.placeBlock((z+1+zz,y-1,x-9-xx),Block(t_ID))
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((z-1-zz,y-1,x-2-xx),Block(t_ID))
    ##ドア
    editor.placeBlock((z+3,y+1,x-8),Block(y_ID,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+3,y+2,x-8),Block(y_ID,{"facing": "south", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+4,y+1,x-8),Block(y_ID,{"facing": "south", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+4,y+2,x-8),Block(y_ID,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z+5,y+1,x-8),Block(y_ID,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+5,y+2,x-8),Block(y_ID,{"facing": "south", "half": "upper", "hinge": "left"}))

def farm_s(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID):
    for xx in range(5):
        for zz in range(4):
            editor.placeBlock((z+9+zz,y-1,x-1-xx),Block(q_ID))
            editor.placeBlock((z+9+zz,y,x-1-xx),Block(w_ID,{"age": "7"}))
    editor.placeBlock((z+10,y-1,x-4),Block(e_ID))
    editor.placeBlock((z+12,y,x-9),Block(r_ID))
    editor.placeBlock((z+11,y,x-10),Block(r_ID))
    for yy in range(2):
        editor.placeBlock((z+12,y+yy,x-10),Block(r_ID))
    editor.placeBlock((z+11,y,x-9),Block(y_ID))
    editor.placeBlock((z+12,y+1,x-9),Block(t_ID))
    editor.placeBlock((z+12,y,x-8),Block(u_ID,{"level": "3"}))
    editor.placeBlock((z+12,y,x-6),Block(i_ID))
    editor.placeBlock((z+12,y+1,x-6),Block(o_ID))
    editor.placeBlock((z,y+3,x-6),Block(o_ID,{"hanging": "true"}))
    editor.placeBlock((z,y+3,x-2),Block(o_ID,{"hanging": "true"}))
def pool_s(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(4):
        for zz in range(4):
            editor.placeBlock((z-1-zz,y-1,x-6-xx),Block(q_ID))
    for zz in range(2):
        editor.placeBlock((z-2-zz,y-1,x-10),Block(q_ID))
    editor.placeBlock((z-1,y-1,x-10),Block("grass_block"))
    editor.placeBlock((z-1,y,x-10),Block(w_ID,{"half": "lower"}))
    editor.placeBlock((z-1,y+1,x-10),Block(w_ID,{"half": "upper"}))
    editor.placeBlock((z-4,y-1,x-10),Block("grass_block"))
    editor.placeBlock((z-4,y,x-10),Block(e_ID,{"half": "lower"}))
    editor.placeBlock((z-4,y+1,x-10),Block(e_ID,{"half": "upper"}))
    editor.placeBlock((z-3,y-2,x-9),Block("glowstone"))
    editor.placeBlock((z-3,y,x-8),Block(r_ID))
    editor.placeBlock((z-2,y,x-7),Block(r_ID))
    editor.placeBlock((z-1,y,x-1),Block(t_ID))
    editor.placeBlock((z-2,y,x-1),Block(y_ID))
    editor.placeBlock((z-3,y,x-1),Block(u_ID))
    editor.placeBlock((z-4,y,x-1),Block(i_ID))
    editor.placeBlock((z-4,y,x-2),Block(o_ID))
    editor.placeBlock((z-4,y,x-3),Block(p_ID))
    editor.placeBlock((z-4,y+1,x-1),Block(s_ID))
    editor.placeBlock((z-3,y,x-2),Block(a_ID,{"facing": "south"}))

def heya_s(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID,o_ID,p_ID,a_ID,s_ID):
    for xx in range(5):
        editor.placeBlock((z-1,y+4,x-2-xx),Block(q_ID))
    for xx in range(2):
        editor.placeBlock((z+7,y+1,x-1-xx),Block(w_ID))
        editor.placeBlock((z+7,y+3,x-1-xx),Block(t_ID,{"type": "top"}))
        editor.placeBlock((z+4,y+1,x-1-xx),Block(y_ID,{"facing": "west", "half": "bottom", "shape": "straight"}))
    for yy in range(3):
        editor.placeBlock((z+7,y+1+yy,x-3),Block(e_ID))
    editor.placeBlock((z+5,y+1,x-1),Block(r_ID,{"facing": "east", "part": "foot"}))
    editor.placeBlock((z+5,y+1,x-2),Block(r_ID,{"facing": "east", "part": "foot"}))
    command = f"summon panda {z+5} {y+2} {x-2}"
    runCommand(command)
    command = f"summon panda {z+6} {y+2} {x-2}"
    runCommand(command)
    editor.placeBlock((z+4,y+1,x-3),Block(u_ID,{"facing": "north", "half": "top", "open": "true"}))
    editor.placeBlock((z+7,y+2,x-2),Block(i_ID))
    editor.placeBlock((z+7,y+4,x-3),Block(i_ID))
    editor.placeBlock((z+7,y+2,x-5),Block(i_ID))
    editor.placeBlock((z+7,y+4,x-1),Block(o_ID,{"facing": "west"}))
    editor.placeBlock((z+7,y+5,x-1),Block("oak_slab",{"type": "bottom"}))
    editor.placeBlock((z+7,y+2,x-1),Block(p_ID))
    editor.placeBlock((z+7,y+4,x-2),Block(a_ID))

    editor.placeBlock((z+1,y+2,x-1),Block(o_ID,{"facing": "north", "type": "left"}))
    editor.placeBlock((z+2,y+2,x-1),Block(o_ID,{"facing": "north", "type": "right"}))
    for zz in range(2):
        editor.placeBlock((z+5+zz,y+1,x-3),Block(s_ID))
        editor.placeBlock((z+1+zz,y+1,x-1),Block(e_ID,{"facing": "north"}))
        editor.placeBlock((z+1+zz,y+3,x-1),Block(y_ID,{"facing": "south", "half": "bottom", "shape": "straight"}))
      


def kagu_s(x,y,z,q_ID,w_ID,e_ID,r_ID,t_ID,y_ID,u_ID,i_ID):
    editor.placeBlock((z+8,y+1,x-4),Block(q_ID))
    editor.placeBlock((z+8,y+2,x-4),Block(q_ID))
    editor.placeBlock((z+1,y+4,x-1),Block(w_ID,{"facing": "north"}))
    editor.placeBlock((z+2,y+4,x-1),Block(e_ID,{"facing": "north"}))
    for yy in range(3):
        editor.placeBlock((z+7,y+1+yy,x-4),Block(r_ID))
    for xx in range(3):
        editor.placeBlock((z+7,y+3,x-5-xx),Block(r_ID))
    editor.placeBlock((z+7,y+1,x-5),Block(t_ID))
    editor.placeBlock((z+7,y+1,x-6),Block(y_ID))
    editor.placeBlock((z+7,y+1,x-7),Block(u_ID))
    editor.placeBlock((z+7,y+2,x-7),Block(i_ID))
def road_s(x,y,z,q_id):
    for xx in range(18):
        for zz in range(25):
            editor.placeBlock((z-8+zz,y-1,x+3-xx),Block(q_id))
    light(z-7,y,x-13)
    light(z-7,y,x+2)
    light(z+15,y,x-13)
    light(z+15,y,x+2)
    light(z,y,x-13)
    light(z+8,y,x-13)
    light(z-7,y,x-5)    
    light(z,y,x+2)
    light(z+8,y,x+2)



def house1_w(x,y,z):
    road_w(x,y,z,"smooth_stone")
    buildHouse_w(x,y,z, "stripped_spruce_log","spruce_slab","cobblestone","cobblestone_slab","cobblestone_stairs","smooth_stone_slab")
    Wall_w(x,y,z, "oak_planks","sea_lantern","stripped_oak_log","smooth_sandstone","oak_stairs","oak_slab")
    niwa_w(x,y,z,"jungle_leaves","acacia_door","jungle_log","diorite_wall","polished_andesite","oak_door")
    farm_w(x,y,z,"farmland","wheat","water","hay_block","potted_poppy","chest","water_cauldron","mossy_cobblestone_wall","lantern")
    pool_w(x,y,z,"water","rose_bush","lilac","lily_pad","furnace","crafting_table","smoker","blast_furnace","smithing_table","stonecutter","campfire","potted_oxeye_daisy")
    heya_w(x,y,z,"jungle_slab","stripped_spruce_log","barrel","light_blue_bed","spruce_slab","spruce_stairs","oak_trapdoor","lantern","chest","potted_jungle_sapling","potted_pink_tulip","light_gray_carpet")
    kagu_w(x,y,z,"smooth_sandstone","zombie_wall_head","creeper_wall_head","bookshelf","cartography_table","enchanting_table","fletching_table","potted_oxeye_daisy")

def house1_e(x,y,z):
    road_e(x,y,z,"smooth_stone")
    buildHouse_e(x,y,z, "stripped_spruce_log","spruce_slab","cobblestone","cobblestone_slab","cobblestone_stairs","smooth_stone_slab")
    Wall_e(x,y,z, "oak_planks","sea_lantern","stripped_oak_log","smooth_sandstone","oak_stairs","oak_slab")
    niwa_e(x,y,z,"jungle_leaves","acacia_door","jungle_log","diorite_wall","polished_andesite","oak_door")
    farm_e(x,y,z,"farmland","wheat","water","hay_block","potted_poppy","chest","water_cauldron","mossy_cobblestone_wall","lantern")
    pool_e(x,y,z,"water","rose_bush","lilac","lily_pad","furnace","crafting_table","smoker","blast_furnace","smithing_table","stonecutter","campfire","potted_oxeye_daisy")
    heya_e(x,y,z,"jungle_slab","stripped_spruce_log","barrel","light_blue_bed","spruce_slab","spruce_stairs","oak_trapdoor","lantern","chest","potted_jungle_sapling","potted_pink_tulip","light_gray_carpet")
    kagu_e(x,y,z,"smooth_sandstone","zombie_wall_head","creeper_wall_head","bookshelf","cartography_table","enchanting_table","fletching_table","potted_oxeye_daisy")


def house1_n(z,y,x):
    road_n(x,y,z,"smooth_stone")
    buildHouse_n(x,y,z, "stripped_spruce_log","spruce_slab","cobblestone","cobblestone_slab","cobblestone_stairs","smooth_stone_slab")
    Wall_n(x,y,z, "oak_planks","sea_lantern","stripped_oak_log","smooth_sandstone","oak_stairs","oak_slab")
    niwa_n(x,y,z,"jungle_leaves","acacia_door","jungle_log","diorite_wall","polished_andesite","oak_door")
    farm_n(x,y,z,"farmland","wheat","water","hay_block","potted_poppy","chest","water_cauldron","mossy_cobblestone_wall","lantern")
    pool_n(x,y,z,"water","rose_bush","lilac","lily_pad","furnace","crafting_table","smoker","blast_furnace","smithing_table","stonecutter","campfire","potted_oxeye_daisy")
    heya_n(x,y,z,"jungle_slab","stripped_spruce_log","barrel","light_blue_bed","spruce_slab","spruce_stairs","oak_trapdoor","lantern","chest","potted_jungle_sapling","potted_pink_tulip","light_gray_carpet")
    kagu_n(x,y,z,"smooth_sandstone","zombie_wall_head","creeper_wall_head","bookshelf","cartography_table","enchanting_table","fletching_table","potted_oxeye_daisy")


def house1_s(z,y,x):
    road_s(x,y,z,"smooth_stone")
    buildHouse_s(x,y,z, "stripped_spruce_log","spruce_slab","cobblestone","cobblestone_slab","cobblestone_stairs","smooth_stone_slab")
    Wall_s(x,y,z, "oak_planks","sea_lantern","stripped_oak_log","smooth_sandstone","oak_stairs","oak_slab")
    niwa_s(x,y,z,"jungle_leaves","acacia_door","jungle_log","diorite_wall","polished_andesite","oak_door")
    farm_s(x,y,z,"farmland","wheat","water","hay_block","potted_poppy","chest","water_cauldron","mossy_cobblestone_wall","lantern")
    pool_s(x,y,z,"water","rose_bush","lilac","lily_pad","furnace","crafting_table","smoker","blast_furnace","smithing_table","stonecutter","campfire","potted_oxeye_daisy")
    heya_s(x,y,z,"jungle_slab","stripped_spruce_log","barrel","light_blue_bed","spruce_slab","spruce_stairs","oak_trapdoor","lantern","chest","potted_jungle_sapling","potted_pink_tulip","light_gray_carpet")
    kagu_s(x,y,z,"smooth_sandstone","zombie_wall_head","creeper_wall_head","bookshelf","cartography_table","enchanting_table","fletching_table","potted_oxeye_daisy")

def house1(x,y,z,f):
    if f=="n":
        house1_n(x,y,z)
    elif f=="s":
        house1_s(x,y,z)
    elif f=="e":
        house1_e(x,y,z)
    elif f=="w":
        house1_w(x,y,z)

house1(-50,4,-200,"n")
house1(-50,4,-240,"s")
house1(-50,4,-280,"e")
house1(-50,4,-320,"w")


def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True


