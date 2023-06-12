from interfaceUtils import runCommand

from gdpc import Editor, Block, Transform, geometry
 
editor = Editor(buffering=True)

def light(x,y,z): #c=cobblestone_wall,l=lantern
    editor.placeBlock((x,y,z),Block("stone_brick_wall"))
    editor.placeBlock((x,y+1,z),Block("lantern"))



#south
def buildHouse_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((x+1+xx,y,z+1+zz),Block(w_id))
    for yy in range(2):       
        editor.placeBlock((x+15,y+yy,z),Block(q_id))
        for xx in range(10):
            editor.placeBlock((x+1+xx,y+yy,z),Block(q_id))
        for zz in range(13):
            editor.placeBlock((x,y+yy,z+zz),Block(q_id))
            editor.placeBlock((x+16,y+yy,z+zz),Block(q_id))
        for xx in range(15):            
            editor.placeBlock((x+1+xx,y+yy,z+12),Block(q_id))
    for yy in range(6):
        editor.placeBlock((x+15,y+2+yy,z),Block(e_id))
        for xx in range(10):
            editor.placeBlock((x+1+xx,y+2+yy,z),Block(e_id))
        for zz in range(13):
            editor.placeBlock((x,y+2+yy,z+zz),Block(e_id))
            editor.placeBlock((x+16,y+2+yy,z+zz),Block(e_id))
        for xx in range(15):            
            editor.placeBlock((x+1+xx,y+2+yy,z+12),Block(e_id))
    for yy in range(7):
        editor.placeBlock((x+17,y+yy,z-1),Block(r_id))
        editor.placeBlock((x+6,y+yy,z-1),Block(r_id))
        editor.placeBlock((x-1,y+yy,z-1),Block(r_id))
        editor.placeBlock((x-1,y+yy,z+13),Block(r_id))
        editor.placeBlock((x+17,y+yy,z+13),Block(r_id))
    for yy in range(3):
        for xx in range(4):
            editor.placeBlock((x+11+xx,y+5+yy,z),Block(e_id))

    for xx in range(9):
        editor.placeBlock((x+2*xx,y+7,z-1),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z-2),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+2*xx,y+8,z-1),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z-2),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z-3),Block(u_id))
        editor.placeBlock((x+2*xx,y+8,z-2),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z-1),Block(y_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y+7,z-1),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z-2),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z-1),Block(o_id))
        editor.placeBlock((x+1+2*xx,y+13,z+6),Block(i_id,{"type": "bottom"}))
    for xx in range(15):
        editor.placeBlock((x+1+xx,y+8,z+1),Block(y_id))
        editor.placeBlock((x+1+xx,y+10,z+4),Block(y_id))
        editor.placeBlock((x+1+xx,y+11,z+5),Block(y_id))
        editor.placeBlock((x+1+xx,y+12,z+6),Block(y_id))
        for zz in range(2):
            editor.placeBlock((x+1+xx,y+9,z+2+zz),Block(y_id))
    for xx in range(7):
        editor.placeBlock((x+2+2*xx,y+12,z+5),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+11,z+4),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z+3),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+9,z+1),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z+2),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+9,z),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+13,z+6),Block(y_id))
    for xx in range(6):
        editor.placeBlock((x+xx,y+3,z-1),Block(r_id))

    for yy in range(5):
        editor.placeBlock((x,y+8+yy,z+6),Block(e_id))
    for yy in range(4):
        editor.placeBlock((x,y+8+yy,z+5),Block(e_id))
        editor.placeBlock((x,y+8+yy,z+7),Block(e_id))
    for yy in range(3):
        editor.placeBlock((x,y+8+yy,z+4),Block(e_id))
        editor.placeBlock((x,y+8+yy,z+8),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((x,y+8+yy,z+9+zz),Block(e_id))
            editor.placeBlock((x,y+8+yy,z+2+zz),Block(e_id))
    editor.placeBlock((x,y+8,z+1),Block(e_id))
    editor.placeBlock((x,y+8,z+11),Block(e_id))

    editor.placeBlock((x,y+13,z+6),Block(y_id))
    editor.placeBlock((x,y+12,z+5),Block(y_id))
    editor.placeBlock((x,y+12,z+7),Block(y_id))
    editor.placeBlock((x,y+11,z+4),Block(y_id))
    editor.placeBlock((x,y+11,z+8),Block(y_id))
    for zz in range(2):
        editor.placeBlock((x,y+10,z+2+zz),Block(y_id))
        editor.placeBlock((x,y+10,z+9+zz),Block(y_id))
        editor.placeBlock((x,y+9,z+zz),Block(y_id))
        editor.placeBlock((x,y+9,z+11+zz),Block(y_id))
    for yy in range(2):
        editor.placeBlock((x-1,y+11+yy,z+6),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+11,z+5),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+10,z+5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+10,z+4),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z+3),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z+2),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z+2),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+8,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+7,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+7,z-2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z-3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+6,z-2),Block(p_id,{"type": "top"}))

    editor.placeBlock((x-1,y+11,z+7),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+10,z+7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+10,z+8),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z+9),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z+10),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z+10),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+8,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z+12),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z+12),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+7,z+13),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+7,z+14),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z+15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+6,z+14),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((x-1,y+5,z+zz),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((x-1,y+6,z+1+2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((x-1,y+7,z+1+zz),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((x-1,y+8,z+4+2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((x-1,y+9,z+4+zz),Block(r_id,{"axis": "z"}))
    editor.placeBlock((x-1,y+10,z+6),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((x-1,y+yy,z+3),Block(r_id,{"axis": "z"}))
        editor.placeBlock((x-1,y+yy,z+9),Block(r_id,{"axis": "z"}))
    for yy in range(3):
        for zz in range(5):
            editor.placeBlock((x,y+2+yy,z+4+zz),Block(a_id))
    for zz in range(5):
        for xx in range(2):
            editor.placeBlock((x-1-xx,y+1,z+4+zz),Block(q_id))


    for yy in range(5):
        editor.placeBlock((x+16,y+8+yy,z+6),Block(e_id))
    for yy in range(4):
        editor.placeBlock((x+16,y+8+yy,z+5),Block(e_id))
        editor.placeBlock((x+16,y+8+yy,z+7),Block(e_id))
    for yy in range(3):
        editor.placeBlock((x+16,y+8+yy,z+4),Block(e_id))
        editor.placeBlock((x+16,y+8+yy,z+8),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((x+16,y+8+yy,z+9+zz),Block(e_id))
            editor.placeBlock((x+16,y+8+yy,z+2+zz),Block(e_id))
    editor.placeBlock((x+16,y+8,z+1),Block(e_id))
    editor.placeBlock((x+16,y+8,z+11),Block(e_id))

    editor.placeBlock((x+16,y+13,z+6),Block(y_id))
    editor.placeBlock((x+16,y+12,z+5),Block(y_id))
    editor.placeBlock((x+16,y+12,z+7),Block(y_id))
    editor.placeBlock((x+16,y+11,z+4),Block(y_id))
    editor.placeBlock((x+16,y+11,z+8),Block(y_id))
    for zz in range(2):
        editor.placeBlock((x+16,y+10,z+2+zz),Block(y_id))
        editor.placeBlock((x+16,y+10,z+9+zz),Block(y_id))
        editor.placeBlock((x+16,y+9,z+zz),Block(y_id))
        editor.placeBlock((x+16,y+9,z+11+zz),Block(y_id))

    for xx in range(17):
        editor.placeBlock((x+xx,y+8,z),Block(y_id))
        editor.placeBlock((x+xx,y+8,z+12),Block(y_id))
    for yy in range(2):
        editor.placeBlock((x+17,y+11+yy,z+6),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+11,z+5),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+10,z+5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+10,z+4),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z+3),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z+2),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z+2),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+8,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+7,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+7,z-2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z-3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+6,z-2),Block(p_id,{"type": "top"}))

    editor.placeBlock((x+17,y+11,z+7),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+10,z+7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+10,z+8),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z+9),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z+10),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z+10),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+8,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z+12),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z+12),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+7,z+13),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+7,z+14),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z+15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+6,z+14),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((x+17,y+5,z+zz),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((x+17,y+6,z+1+2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((x+17,y+7,z+1+zz),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((x+17,y+8,z+4+2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((x+17,y+9,z+4+zz),Block(r_id,{"axis": "z"}))
    editor.placeBlock((x+17,y+10,z+6),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((x+17,y+yy,z+3),Block(r_id,{"axis": "z"}))
        editor.placeBlock((x+17,y+yy,z+9),Block(r_id,{"axis": "z"}))

    for xx in range(9):
        editor.placeBlock((x+2*xx,y+7,z+13),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z+14),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+2*xx,y+8,z+13),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z+14),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z+15),Block(u_id))
        editor.placeBlock((x+2*xx,y+8,z+14),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z+13),Block(y_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y+7,z+13),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z+14),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z+13),Block(o_id))
    for xx in range(15):
        editor.placeBlock((x+1+xx,y+8,z+11),Block(y_id))
        editor.placeBlock((x+1+xx,y+10,z+8),Block(y_id))
        editor.placeBlock((x+1+xx,y+11,z+7),Block(y_id))
        for zz in range(2):
            editor.placeBlock((x+1+xx,y+9,z+9+zz),Block(y_id))
    for xx in range(7):
        editor.placeBlock((x+2+2*xx,y+12,z+7),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+11,z+8),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z+9),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+9,z+11),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z+10),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+9,z+12),Block(i_id,{"type": "bottom"}))
    #light
    editor.placeBlock((x-1,y+9,z+1),Block("lantern"))
    editor.placeBlock((x-1,y+13,z+6),Block("lantern"))
    editor.placeBlock((x-1,y+9,z+11),Block("lantern"))
    editor.placeBlock((x+8,y+8,z-3),Block("lantern"))
    editor.placeBlock((x+8,y+10,z+1),Block("lantern"))
    editor.placeBlock((x+8,y+14,z+6),Block("lantern"))
    editor.placeBlock((x+8,y+10,z+11),Block("lantern"))
    editor.placeBlock((x+8,y+8,z+15),Block("lantern"))
    editor.placeBlock((x+17,y+9,z+1),Block("lantern"))
    editor.placeBlock((x+17,y+13,z+6),Block("lantern"))
    editor.placeBlock((x+17,y+9,z+11),Block("lantern"))



def window_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for zz in range(5):
        editor.placeBlock((x,y,z+zz),Block(q_id,{"facing": "east", "half": "top"}))
        editor.placeBlock((x-1,y,z+zz),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-1,y-2,z),Block(e_id))
    editor.placeBlock((x-1,y-2,z+1),Block(r_id))
    editor.placeBlock((x-1,y-2,z+2),Block(t_id))
    editor.placeBlock((x-1,y-2,z+3),Block(t_id))
    editor.placeBlock((x-1,y-2,z+4),Block(y_id))
def garden_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for xx in range(7):
        for zz in range(5):
            editor.placeBlock((x+xx,y+6,z-3-zz),Block(q_id,{"type": "bottom"}))
    for yy in range(6):
        editor.placeBlock((x,y+yy,z-6),Block(w_id))
        editor.placeBlock((x+6,y+yy,z-6),Block(w_id))
    for xx in range(6):
        for zz in range(5):
            editor.placeBlock((x+xx,y-1,z-1-zz),Block("grass_block"))
    for zz in range(8):
        editor.placeBlock((x-1,y,z-2-zz),Block(w_id))
        editor.placeBlock((x+17,y,z-2-zz),Block(w_id))
    for xx in range(10):
        editor.placeBlock((x-1+xx,y,z-9),Block(w_id))
    for xx in range(5):
        editor.placeBlock((x+1+xx,y,z-2),Block(e_id))
        editor.placeBlock((x+1+xx,y,z-3),Block(r_id))
        editor.placeBlock((x+1+xx,y,z-4),Block(t_id))
    for xx in range(4):
        editor.placeBlock((x+11+xx,y,z),Block(y_id,{"facing": "south", "half": "bottom"}))
    #light
    editor.placeBlock((x-1,y+1,z-2),Block("lantern"))
    editor.placeBlock((x-1,y+1,z-9),Block("lantern"))
    editor.placeBlock((x+8,y+1,z-9),Block("lantern"))
    editor.placeBlock((x+17,y+1,z-9),Block("lantern"))
    editor.placeBlock((x+17,y+1,z-3),Block("lantern"))
    light(x+3,y,z-6)
    light(x+6,y,z-3)
    light(x-3,y,z+2)
    light(x-3,y,z+10)
    light(x-3,y,z+15)
    light(x+8,y,z+15)
    light(x+19,y,z+15)
    light(x+19,y,z+6)
    light(x+10,y,z-6)
    light(x+15,y,z-6)


def indoor_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(15):
        for zz in range(12):
            editor.placeBlock((x+1+xx,y+7,z+1+zz),Block(q_id))
    for xx in range(3):
        editor.placeBlock((x+8+xx,y+3,z+11),Block(w_id))
    for yy in range(4):
        editor.placeBlock((x+7,y+1+yy,z+11),Block(w_id))
        editor.placeBlock((x+11,y+1+yy,z+11),Block(w_id))
        editor.placeBlock((x+12,y+1+yy,z+11),Block(y_id,{"facing": "north", "type": "left"}))
        editor.placeBlock((x+13,y+1+yy,z+11),Block(y_id,{"facing": "north", "type": "right"}))
        editor.placeBlock((x+14,y+1+yy,z+11),Block(u_id))
    editor.placeBlock((x+8,y+1,z+11),Block(e_id))
    editor.placeBlock((x+9,y+1,z+11),Block(r_id))
    editor.placeBlock((x+10,y+1,z+11),Block(t_id))
    for zz in range(5):
        editor.placeBlock((x+6,y+2,z+10-zz),Block(i_id,{"facing": "west", "half": "lower", "hinge": "left"}))
        editor.placeBlock((x+6,y+3,z+10-zz),Block(i_id,{"facing": "west", "half": "upper", "hinge": "left"}))
def bed_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(3):
        editor.placeBlock((x+xx,y,z),Block(q_id))
        editor.placeBlock((x+xx,y,z-2),Block(w_id,{"facing": "south", "part": "foot"}))
        editor.placeBlock((x+xx,y,z-3),Block(e_id,{"facing": "west", "lit": "false"}))
        command = f"summon panda {x+xx} {y+2} {z-2}"
        runCommand(command)
        editor.placeBlock((x+xx,y,z-4),Block(t_id,{"facing": "north", "half": "bottom", "open": "true"}))
    for xx in range(5):
        editor.placeBlock((x+xx,y+3,z),Block(r_id,{"axis": "x"}))
    for yy in range(6):
        editor.placeBlock((x+5,y+yy,z),Block(r_id,{"axis": "y"}))
        editor.placeBlock((x+5,y+yy,z-6),Block(r_id,{"axis": "y"}))
    for zz in range(5):
        editor.placeBlock((x+5,y,z-1-zz),Block(r_id,{"axis": "z"}))
        editor.placeBlock((x+5,y+3,z-1-zz),Block(r_id,{"axis": "z"}))
    editor.placeBlock((x,y+1,z),Block(y_id))
    editor.placeBlock((x+1,y+1,z),Block(i_id))
    editor.placeBlock((x+2,y+1,z),Block(u_id))
    editor.placeBlock((x,y+5,z),Block(i_id))
    editor.placeBlock((x,y+5,z-10),Block(i_id))
    editor.placeBlock((x+14,y+5,z),Block(i_id))
    editor.placeBlock((x+14,y+5,z-10),Block(i_id))
    editor.placeBlock((x+5,y+4,z-2),Block(i_id))
    editor.placeBlock((x+5,y+4,z-4),Block(i_id))
    editor.placeBlock((x+8,y+3,z),Block(i_id))

def kagu_s(x,y,z,r_id,o_id,g_id,l_id,t_id,a_id): #("red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((x+11+xx,y+1,z+1+zz),Block(r_id))

    c1=[[8,4],[12,4],[10,6],[8,8],[12,8]] #coor
    for i in range(5):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+c1[i][0]+xx,y+1,z+c1[i][1]+zz),Block(o_id))
    c2=[[10,4],[8,6],[12,6],[10,8]]
    for i in range(4):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+c2[i][0]+xx,y+1,z+c2[i][1]+zz),Block(g_id))
    editor.placeBlock((x+8,y,z+4),Block(l_id))
    editor.placeBlock((x+8,y,z+9),Block(l_id))
    editor.placeBlock((x+13,y,z+4),Block(l_id))
    editor.placeBlock((x+13,y,z+9),Block(l_id))
    editor.placeBlock((x+2,y,z+2),Block(l_id))

    for zz in range(2):
        editor.placeBlock((x+1,y+1,z+1+zz),Block(t_id,{"facing":"west","half":"top"}))
        editor.placeBlock((x+2,y+1,z+1+zz),Block(a_id,{"type":"top"}))
        editor.placeBlock((x+3,y+1,z+1+zz),Block(t_id,{"facing":"east","half":"top"}))
    editor.placeBlock((x+2,y+1,z+4),Block(t_id,{"facing":"south","half":"bottom"}))

#north
def buildHouse_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((x+1+xx,y,z-1-zz),Block(w_id))
    for yy in range(2):       
        editor.placeBlock((x+15,y+yy,z),Block(q_id))
        for xx in range(10):
            editor.placeBlock((x+1+xx,y+yy,z),Block(q_id))
        for zz in range(13):
            editor.placeBlock((x,y+yy,z-zz),Block(q_id))
            editor.placeBlock((x+16,y+yy,z-zz),Block(q_id))
        for xx in range(15):            
            editor.placeBlock((x+1+xx,y+yy,z-12),Block(q_id))
    for yy in range(6):
        editor.placeBlock((x+15,y+2+yy,z),Block(e_id))
        for xx in range(10):
            editor.placeBlock((x+1+xx,y+2+yy,z),Block(e_id))
        for zz in range(13):
            editor.placeBlock((x,y+2+yy,z-zz),Block(e_id))
            editor.placeBlock((x+16,y+2+yy,z-zz),Block(e_id))
        for xx in range(15):            
            editor.placeBlock((x+1+xx,y+2+yy,z-12),Block(e_id))
    for yy in range(7):
        editor.placeBlock((x+17,y+yy,z+1),Block(r_id))
        editor.placeBlock((x+6,y+yy,z+1),Block(r_id))
        editor.placeBlock((x-1,y+yy,z+1),Block(r_id))
        editor.placeBlock((x-1,y+yy,z-13),Block(r_id))
        editor.placeBlock((x+17,y+yy,z-13),Block(r_id))
    for yy in range(3):
        for xx in range(4):
            editor.placeBlock((x+11+xx,y+5+yy,z),Block(e_id))

    for xx in range(9):
        editor.placeBlock((x+2*xx,y+7,z+1),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z+2),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+2*xx,y+8,z+1),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z+2),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z+3),Block(u_id))
        editor.placeBlock((x+2*xx,y+8,z+2),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z+1),Block(y_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y+7,z+1),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z+2),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z+1),Block(o_id))
        editor.placeBlock((x+1+2*xx,y+13,z-6),Block(i_id,{"type": "bottom"}))
    for xx in range(15):
        editor.placeBlock((x+1+xx,y+8,z-1),Block(y_id))
        editor.placeBlock((x+1+xx,y+10,z-4),Block(y_id))
        editor.placeBlock((x+1+xx,y+11,z-5),Block(y_id))
        editor.placeBlock((x+1+xx,y+12,z-6),Block(y_id))
        for zz in range(2):
            editor.placeBlock((x+1+xx,y+9,z-2-zz),Block(y_id))
    for xx in range(7):
        editor.placeBlock((x+2+2*xx,y+12,z-5),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+11,z-4),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z-3),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+9,z-1),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z-2),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+9,z),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+13,z-6),Block(y_id))
    for xx in range(6):
        editor.placeBlock((x+xx,y+3,z+1),Block(r_id))

    for yy in range(5):
        editor.placeBlock((x,y+8+yy,z-6),Block(e_id))
    for yy in range(4):
        editor.placeBlock((x,y+8+yy,z-5),Block(e_id))
        editor.placeBlock((x,y+8+yy,z-7),Block(e_id))
    for yy in range(3):
        editor.placeBlock((x,y+8+yy,z-4),Block(e_id))
        editor.placeBlock((x,y+8+yy,z-8),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((x,y+8+yy,z-9-zz),Block(e_id))
            editor.placeBlock((x,y+8+yy,z-2-zz),Block(e_id))
    editor.placeBlock((x,y+8,z-1),Block(e_id))
    editor.placeBlock((x,y+8,z-11),Block(e_id))

    editor.placeBlock((x,y+13,z-6),Block(y_id))
    editor.placeBlock((x,y+12,z-5),Block(y_id))
    editor.placeBlock((x,y+12,z-7),Block(y_id))
    editor.placeBlock((x,y+11,z-4),Block(y_id))
    editor.placeBlock((x,y+11,z-8),Block(y_id))
    for zz in range(2):
        editor.placeBlock((x,y+10,z-2-zz),Block(y_id))
        editor.placeBlock((x,y+10,z-9-zz),Block(y_id))
        editor.placeBlock((x,y+9,z-zz),Block(y_id))
        editor.placeBlock((x,y+9,z-11-zz),Block(y_id))
    for yy in range(2):
        editor.placeBlock((x-1,y+11+yy,z-6),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+11,z-5),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+10,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+10,z-4),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z-3),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z-2),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z-2),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+8,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+7,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+7,z+2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z+3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+6,z+2),Block(p_id,{"type": "top"}))

    editor.placeBlock((x-1,y+11,z-7),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+10,z-7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+10,z-8),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z-9),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+9,z-10),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z-10),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+8,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+8,z-12),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z-12),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-1,y+7,z-13),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-1,y+7,z-14),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+7,z-15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+6,z-14),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((x-1,y+5,z-zz),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((x-1,y+6,z-1-2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((x-1,y+7,z-1-zz),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((x-1,y+8,z-4-2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((x-1,y+9,z-4-zz),Block(r_id,{"axis": "z"}))
    editor.placeBlock((x-1,y+10,z-6),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((x-1,y+yy,z-3),Block(r_id,{"axis": "z"}))
        editor.placeBlock((x-1,y+yy,z-9),Block(r_id,{"axis": "z"}))
    for yy in range(3):
        for zz in range(5):
            editor.placeBlock((x,y+2+yy,z-4-zz),Block(a_id))
    for zz in range(5):
        for xx in range(2):
            editor.placeBlock((x-1-xx,y+1,z-4-zz),Block(q_id))


    for yy in range(5):
        editor.placeBlock((x+16,y+8+yy,z-6),Block(e_id))
    for yy in range(4):
        editor.placeBlock((x+16,y+8+yy,z-5),Block(e_id))
        editor.placeBlock((x+16,y+8+yy,z-7),Block(e_id))
    for yy in range(3):
        editor.placeBlock((x+16,y+8+yy,z-4),Block(e_id))
        editor.placeBlock((x+16,y+8+yy,z-8),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((x+16,y+8+yy,z-9-zz),Block(e_id))
            editor.placeBlock((x+16,y+8+yy,z-2-zz),Block(e_id))
    editor.placeBlock((x+16,y+8,z-1),Block(e_id))
    editor.placeBlock((x+16,y+8,z-11),Block(e_id))

    editor.placeBlock((x+16,y+13,z-6),Block(y_id))
    editor.placeBlock((x+16,y+12,z-5),Block(y_id))
    editor.placeBlock((x+16,y+12,z-7),Block(y_id))
    editor.placeBlock((x+16,y+11,z-4),Block(y_id))
    editor.placeBlock((x+16,y+11,z-8),Block(y_id))
    for zz in range(2):
        editor.placeBlock((x+16,y+10,z-2-zz),Block(y_id))
        editor.placeBlock((x+16,y+10,z-9-zz),Block(y_id))
        editor.placeBlock((x+16,y+9,z-zz),Block(y_id))
        editor.placeBlock((x+16,y+9,z-11-zz),Block(y_id))

    for xx in range(17):
        editor.placeBlock((x+xx,y+8,z),Block(y_id))
        editor.placeBlock((x+xx,y+8,z-12),Block(y_id))
    for yy in range(2):
        editor.placeBlock((x+17,y+11+yy,z-6),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+11,z-5),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+10,z-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+10,z-4),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z-3),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z-2),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z-2),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+8,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+7,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+7,z+2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z+3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+6,z+2),Block(p_id,{"type": "top"}))

    editor.placeBlock((x+17,y+11,z-7),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+10,z-7),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+10,z-8),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z-9),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+9,z-10),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z-10),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+8,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+8,z-12),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z-12),Block(p_id,{"type": "top"}))
    editor.placeBlock((x+17,y+7,z-13),Block(p_id,{"type": "double"}))
    editor.placeBlock((x+17,y+7,z-14),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+7,z-15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x+17,y+6,z-14),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((x+17,y+5,z-zz),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((x+17,y+6,z-1-2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((x+17,y+7,z-1-zz),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((x+17,y+8,z-4-2*zz),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((x+17,y+9,z-4-zz),Block(r_id,{"axis": "z"}))
    editor.placeBlock((x+17,y+10,z-6),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((x+17,y+yy,z-3),Block(r_id,{"axis": "z"}))
        editor.placeBlock((x+17,y+yy,z-9),Block(r_id,{"axis": "z"}))

    for xx in range(9):
        editor.placeBlock((x+2*xx,y+7,z-13),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z-14),Block(t_id,{"type": "top"}))
        editor.placeBlock((x+2*xx,y+8,z-13),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z-14),Block(y_id))
        editor.placeBlock((x+2*xx,y+7,z-15),Block(u_id))
        editor.placeBlock((x+2*xx,y+8,z-14),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y+6,z-13),Block(y_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y+7,z-13),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z-14),Block(y_id))
        editor.placeBlock((x+1+2*xx,y+6,z-13),Block(o_id))
    for xx in range(15):
        editor.placeBlock((x+1+xx,y+8,z-11),Block(y_id))
        editor.placeBlock((x+1+xx,y+10,z-8),Block(y_id))
        editor.placeBlock((x+1+xx,y+11,z-7),Block(y_id))
        for zz in range(2):
            editor.placeBlock((x+1+xx,y+9,z-9-zz),Block(y_id))
    for xx in range(7):
        editor.placeBlock((x+2+2*xx,y+12,z-7),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+11,z-8),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z-9),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+9,z-11),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z-10),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+9,z-12),Block(i_id,{"type": "bottom"}))

    #light
    editor.placeBlock((x-1,y+9,z-1),Block("lantern"))
    editor.placeBlock((x-1,y+13,z-6),Block("lantern"))
    editor.placeBlock((x-1,y+9,z-11),Block("lantern"))
    editor.placeBlock((x+8,y+8,z+3),Block("lantern"))
    editor.placeBlock((x+8,y+10,z-1),Block("lantern"))
    editor.placeBlock((x+8,y+14,z-6),Block("lantern"))
    editor.placeBlock((x+8,y+10,z-11),Block("lantern"))
    editor.placeBlock((x+8,y+8,z-15),Block("lantern"))
    editor.placeBlock((x+17,y+9,z-1),Block("lantern"))
    editor.placeBlock((x+17,y+13,z-6),Block("lantern"))
    editor.placeBlock((x+17,y+9,z-11),Block("lantern"))




def window_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for zz in range(5):
        editor.placeBlock((x,y,z-zz),Block(q_id,{"facing": "east", "half": "top"}))
        editor.placeBlock((x-1,y,z-zz),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-1,y-2,z),Block(e_id))
    editor.placeBlock((x-1,y-2,z-1),Block(r_id))
    editor.placeBlock((x-1,y-2,z-2),Block(t_id))
    editor.placeBlock((x-1,y-2,z-3),Block(t_id))
    editor.placeBlock((x-1,y-2,z-4),Block(y_id))
def garden_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for xx in range(7):
        for zz in range(5):
            editor.placeBlock((x+xx,y+6,z+3+zz),Block(q_id,{"type": "bottom"}))
    for yy in range(6):
        editor.placeBlock((x,y+yy,z+6),Block(w_id))
        editor.placeBlock((x+6,y+yy,z+6),Block(w_id))
    for xx in range(6):
        for zz in range(5):
            editor.placeBlock((x+xx,y-1,z+1+zz),Block("grass_block"))
    for zz in range(8):
        editor.placeBlock((x-1,y,z+2+zz),Block(w_id))
        editor.placeBlock((x+17,y,z+2+zz),Block(w_id))
    for xx in range(10):
        editor.placeBlock((x-1+xx,y,z+9),Block(w_id))
    for xx in range(5):
        editor.placeBlock((x+1+xx,y,z+2),Block(e_id))
        editor.placeBlock((x+1+xx,y,z+3),Block(r_id))
        editor.placeBlock((x+1+xx,y,z+4),Block(t_id))
    for xx in range(4):
        editor.placeBlock((x+11+xx,y,z),Block(y_id,{"facing": "north", "half": "bottom"}))
    #light
    editor.placeBlock((x-1,y+1,z+2),Block("lantern"))
    editor.placeBlock((x-1,y+1,z+9),Block("lantern"))
    editor.placeBlock((x+8,y+1,z+9),Block("lantern"))
    editor.placeBlock((x+17,y+1,z+9),Block("lantern"))
    editor.placeBlock((x+17,y+1,z+3),Block("lantern"))
    light(x+3,y,z+6)
    light(x+6,y,z+3)
    light(x-3,y,z-2)
    light(x-3,y,z-10)
    light(x-3,y,z-15)
    light(x+8,y,z-15)
    light(x+19,y,z-15)
    light(x+19,y,z-6)
    light(x+10,y,z+6)
    light(x+15,y,z+6)



    
def indoor_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(15):
        for zz in range(12):
            editor.placeBlock((x+1+xx,y+7,z-1-zz),Block(q_id))
    for xx in range(3):
        editor.placeBlock((x+8+xx,y+3,z-11),Block(w_id))
    for yy in range(4):
        editor.placeBlock((x+7,y+1+yy,z-11),Block(w_id))
        editor.placeBlock((x+11,y+1+yy,z-11),Block(w_id))
        editor.placeBlock((x+12,y+1+yy,z-11),Block(y_id,{"facing": "south", "type": "right"}))
        editor.placeBlock((x+13,y+1+yy,z-11),Block(y_id,{"facing": "south", "type": "left"}))
        editor.placeBlock((x+14,y+1+yy,z-11),Block(u_id))
    editor.placeBlock((x+8,y+1,z-11),Block(e_id))
    editor.placeBlock((x+9,y+1,z-11),Block(r_id))
    editor.placeBlock((x+10,y+1,z-11),Block(t_id))
    for zz in range(5):
        editor.placeBlock((x+6,y+2,z-10+zz),Block(i_id,{"facing": "west", "half": "lower", "hinge": "left"}))
        editor.placeBlock((x+6,y+3,z-10+zz),Block(i_id,{"facing": "west", "half": "upper", "hinge": "left"}))
def bed_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(3):
        editor.placeBlock((x+xx,y,z),Block(q_id))
        editor.placeBlock((x+xx,y,z+2),Block(w_id,{"facing": "north", "part": "foot"}))
        command = f"summon panda {x+xx} {y+2} {z+1}"
        runCommand(command)
        editor.placeBlock((x+xx,y,z+3),Block(e_id,{"facing": "west", "lit": "false"}))
        editor.placeBlock((x+xx,y,z+4),Block(t_id,{"facing": "south", "half": "bottom", "open": "true"}))
    for xx in range(5):
        editor.placeBlock((x+xx,y+3,z),Block(r_id,{"axis": "x"}))
    for yy in range(6):
        editor.placeBlock((x+5,y+yy,z),Block(r_id,{"axis": "y"}))
        editor.placeBlock((x+5,y+yy,z+6),Block(r_id,{"axis": "y"}))
    for zz in range(5):
        editor.placeBlock((x+5,y,z+1+zz),Block(r_id,{"axis": "z"}))
        editor.placeBlock((x+5,y+3,z+1+zz),Block(r_id,{"axis": "z"}))
    editor.placeBlock((x,y+1,z),Block(y_id))
    editor.placeBlock((x+1,y+1,z),Block(i_id))
    editor.placeBlock((x+2,y+1,z),Block(u_id))
    editor.placeBlock((x,y+5,z),Block(i_id))
    editor.placeBlock((x,y+5,z+10),Block(i_id))
    editor.placeBlock((x+14,y+5,z),Block(i_id))
    editor.placeBlock((x+14,y+5,z+10),Block(i_id))
    editor.placeBlock((x+5,y+4,z+2),Block(i_id))
    editor.placeBlock((x+5,y+4,z+4),Block(i_id))
    editor.placeBlock((x+8,y+3,z),Block(i_id))

def kagu_n(x,y,z,r_id,o_id,g_id,l_id,t_id,a_id): #("red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((x+11+xx,y+1,z-1-zz),Block(r_id))

    c1=[[8,4],[12,4],[10,6],[8,8],[12,8]] #coor
    for i in range(5):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+c1[i][0]+xx,y+1,z-c1[i][1]-zz),Block(o_id))
    c2=[[10,4],[8,6],[12,6],[10,8]]
    for i in range(4):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((x+c2[i][0]+xx,y+1,z-c2[i][1]-zz),Block(g_id))
    editor.placeBlock((x+8,y,z-4),Block(l_id))
    editor.placeBlock((x+8,y,z-9),Block(l_id))
    editor.placeBlock((x+13,y,z-4),Block(l_id))
    editor.placeBlock((x+13,y,z-9),Block(l_id))
    editor.placeBlock((x+2,y,z-2),Block(l_id))

    for zz in range(2):
        editor.placeBlock((x+1,y+1,z-1-zz),Block(t_id,{"facing":"west","half":"top"}))
        editor.placeBlock((x+2,y+1,z-1-zz),Block(a_id,{"type":"top"}))
        editor.placeBlock((x+3,y+1,z-1-zz),Block(t_id,{"facing":"east","half":"top"}))
    editor.placeBlock((x+2,y+1,z-4),Block(t_id,{"facing":"north","half":"bottom"}))


#east
def buildHouse_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((z+1+zz,y,x+1+xx),Block(w_id))
    for yy in range(2):       
        editor.placeBlock((z,y+yy,x+15),Block(q_id))
        for xx in range(10):
            editor.placeBlock((z,y+yy,x+1+xx),Block(q_id))
        for zz in range(13):
            editor.placeBlock((z+zz,y+yy,x),Block(q_id))
            editor.placeBlock((z+zz,y+yy,x+16),Block(q_id))
        for xx in range(15):            
            editor.placeBlock((z+12,y+yy,x+1+xx),Block(q_id))
    for yy in range(6):
        editor.placeBlock((z,y+2+yy,x+15),Block(e_id))
        for xx in range(10):
            editor.placeBlock((z,y+2+yy,x+1+xx),Block(e_id))
        for zz in range(13):
            editor.placeBlock((z+zz,y+2+yy,x),Block(e_id))
            editor.placeBlock((z+zz,y+2+yy,x+16),Block(e_id))
        for xx in range(15):            
            editor.placeBlock((z+12,y+2+yy,x+1+xx),Block(e_id))
    for yy in range(7):
        editor.placeBlock((z-1,y+yy,x+17),Block(r_id))
        editor.placeBlock((z-1,y+yy,x+6),Block(r_id))
        editor.placeBlock((z-1,y+yy,x-1),Block(r_id))
        editor.placeBlock((z+13,y+yy,x-1),Block(r_id))
        editor.placeBlock((z+13,y+yy,x+17),Block(r_id))
    for yy in range(3):
        for xx in range(4):
            editor.placeBlock((z,y+5+yy,x+11+xx),Block(e_id))

    for xx in range(9):
        editor.placeBlock((z-1,y+7,x+2*xx),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z-2,y+6,x+2*xx),Block(t_id,{"type": "top"}))
        editor.placeBlock((z-1,y+8,x+2*xx),Block(y_id))
        editor.placeBlock((z-2,y+7,x+2*xx),Block(y_id))
        editor.placeBlock((z-3,y+7,x+2*xx),Block(u_id))
        editor.placeBlock((z-2,y+8,x+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-1,y+6,x+2*xx),Block(y_id))
    for xx in range(8):
        editor.placeBlock((z-1,y+7,x+1+2*xx),Block(y_id))
        editor.placeBlock((z-2,y+6,x+1+2*xx),Block(y_id))
        editor.placeBlock((z-1,y+6,x+1+2*xx),Block(o_id))
        editor.placeBlock((z+6,y+13,x+1+2*xx),Block(i_id,{"type": "bottom"}))
    for xx in range(15):
        editor.placeBlock((z+1,y+8,x+1+xx),Block(y_id))
        editor.placeBlock((z+4,y+10,x+1+xx),Block(y_id))
        editor.placeBlock((z+5,y+11,x+1+xx),Block(y_id))
        editor.placeBlock((z+6,y+12,x+1+xx),Block(y_id))
        for zz in range(2):
            editor.placeBlock((z+2+zz,y+9,x+1+xx),Block(y_id))
    for xx in range(7):
        editor.placeBlock((z+5,y+12,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+4,y+11,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+3,y+10,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+1,y+9,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+2,y+10,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z,y+9,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+6,y+13,x+2+2*xx),Block(y_id))
    for xx in range(6):
        editor.placeBlock((z-1,y+3,x+xx),Block(r_id))

    for yy in range(5):
        editor.placeBlock((z+6,y+8+yy,x),Block(e_id))
    for yy in range(4):
        editor.placeBlock((z+5,y+8+yy,x),Block(e_id))
        editor.placeBlock((z+7,y+8+yy,x),Block(e_id))
    for yy in range(3):
        editor.placeBlock((z+4,y+8+yy,x),Block(e_id))
        editor.placeBlock((z+8,y+8+yy,x),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((z+9+zz,y+8+yy,x),Block(e_id))
            editor.placeBlock((z+2+zz,y+8+yy,x),Block(e_id))
    editor.placeBlock((z+1,y+8,x),Block(e_id))
    editor.placeBlock((z+11,y+8,x),Block(e_id))

    editor.placeBlock((z+6,y+13,x),Block(y_id))
    editor.placeBlock((z+5,y+12,x),Block(y_id))
    editor.placeBlock((z+7,y+12,x),Block(y_id))
    editor.placeBlock((z+4,y+11,x),Block(y_id))
    editor.placeBlock((z+8,y+11,x),Block(y_id))
    for zz in range(2):
        editor.placeBlock((z+2+zz,y+10,x),Block(y_id))
        editor.placeBlock((z+9+zz,y+10,x),Block(y_id))
        editor.placeBlock((z+zz,y+9,x),Block(y_id))
        editor.placeBlock((z+11+zz,y+9,x),Block(y_id))
    for yy in range(2):
        editor.placeBlock((z+6,y+11+yy,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+5,y+11,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+5,y+10,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+4,y+10,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+3,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+2,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+2,y+8,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+8,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z,y+8,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z,y+7,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+7,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-2,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-3,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-2,y+6,x-1),Block(p_id,{"type": "top"}))

    editor.placeBlock((z+7,y+11,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+7,y+10,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+8,y+10,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+9,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+10,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+10,y+8,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+8,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+12,y+8,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+12,y+7,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+13,y+7,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+14,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+15,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+14,y+6,x-1),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((z+zz,y+5,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((z+1+2*zz,y+6,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((z+1+zz,y+7,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((z+4+2*zz,y+8,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((z+4+zz,y+9,x-1),Block(r_id,{"axis": "z"}))
    editor.placeBlock((z+6,y+10,x-1),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((z+3,y+yy,x-1),Block(r_id,{"axis": "z"}))
        editor.placeBlock((z+9,y+yy,x-1),Block(r_id,{"axis": "z"}))
    for yy in range(3):
        for zz in range(5):
            editor.placeBlock((z+4+zz,y+2+yy,x),Block(a_id))
    for zz in range(5):
        for xx in range(2):
            editor.placeBlock((z+4+zz,y+1,x-1-xx),Block(q_id))


    for yy in range(5):
        editor.placeBlock((z+6,y+8+yy,x+16),Block(e_id))
    for yy in range(4):
        editor.placeBlock((z+5,y+8+yy,x+16),Block(e_id))
        editor.placeBlock((z+7,y+8+yy,x+16),Block(e_id))
    for yy in range(3):
        editor.placeBlock((z+4,y+8+yy,x+16),Block(e_id))
        editor.placeBlock((z+8,y+8+yy,x+16),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((z+9+zz,y+8+yy,x+16),Block(e_id))
            editor.placeBlock((z+2+zz,y+8+yy,x+16),Block(e_id))
    editor.placeBlock((z+1,y+8,x+16),Block(e_id))
    editor.placeBlock((z+11,y+8,x+16),Block(e_id))

    editor.placeBlock((z+6,y+13,x+16),Block(y_id))
    editor.placeBlock((z+5,y+12,x+16),Block(y_id))
    editor.placeBlock((z+7,y+12,x+16),Block(y_id))
    editor.placeBlock((z+4,y+11,x+16),Block(y_id))
    editor.placeBlock((z+8,y+11,x+16),Block(y_id))
    for zz in range(2):
        editor.placeBlock((z+2+zz,y+10,x+16),Block(y_id))
        editor.placeBlock((z+9+zz,y+10,x+16),Block(y_id))
        editor.placeBlock((z+zz,y+9,x+16),Block(y_id))
        editor.placeBlock((z+11+zz,y+9,x+16),Block(y_id))

    for xx in range(17):
        editor.placeBlock((z,y+8,x+xx),Block(y_id))
        editor.placeBlock((z+12,y+8,x+xx),Block(y_id))
    for yy in range(2):
        editor.placeBlock((z+6,y+11+yy,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+5,y+11,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+5,y+10,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+4,y+10,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+3,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+2,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+2,y+8,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+8,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z,y+8,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z,y+7,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+7,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-2,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-3,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-2,y+6,x+17),Block(p_id,{"type": "top"}))

    editor.placeBlock((z+7,y+11,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+7,y+10,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+8,y+10,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+9,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+10,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+10,y+8,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+8,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+12,y+8,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+12,y+7,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+13,y+7,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+14,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+15,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+14,y+6,x+17),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((z+zz,y+5,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((z+1+2*zz,y+6,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((z+1+zz,y+7,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((z+4+2*zz,y+8,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((z+4+zz,y+9,x+17),Block(r_id,{"axis": "z"}))
    editor.placeBlock((z+6,y+10,x+17),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((z+3,y+yy,x+17),Block(r_id,{"axis": "z"}))
        editor.placeBlock((z+9,y+yy,x+17),Block(r_id,{"axis": "z"}))

    for xx in range(9):
        editor.placeBlock((z+13,y+7,x+2*xx),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z+14,y+6,x+2*xx),Block(t_id,{"type": "top"}))
        editor.placeBlock((z+13,y+8,x+2*xx),Block(y_id))
        editor.placeBlock((z+14,y+7,x+2*xx),Block(y_id))
        editor.placeBlock((z+15,y+7,x+2*xx),Block(u_id))
        editor.placeBlock((z+14,y+8,x+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+13,y+6,x+2*xx),Block(y_id))
    for xx in range(8):
        editor.placeBlock((z+13,y+7,x+1+2*xx),Block(y_id))
        editor.placeBlock((z+14,y+6,x+1+2*xx),Block(y_id))
        editor.placeBlock((z+13,y+6,x+1+2*xx),Block(o_id))
    for xx in range(15):
        editor.placeBlock((z+11,y+8,x+1+xx),Block(y_id))
        editor.placeBlock((z+8,y+10,x+1+xx),Block(y_id))
        editor.placeBlock((z+7,y+11,x+1+xx),Block(y_id))
        for zz in range(2):
            editor.placeBlock((z+9+zz,y+9,x+1+xx),Block(y_id))
    for xx in range(7):
        editor.placeBlock((z+7,y+12,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+8,y+11,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+9,y+10,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+11,y+9,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+10,y+10,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+12,y+9,x+2+2*xx),Block(i_id,{"type": "bottom"}))
    #light
    editor.placeBlock((z+1,y+9,x-1),Block("lantern"))
    editor.placeBlock((z+6,y+13,x-1),Block("lantern"))
    editor.placeBlock((z+11,y+9,x-1),Block("lantern"))
    editor.placeBlock((z-3,y+8,x+8),Block("lantern"))
    editor.placeBlock((z+1,y+10,x+8),Block("lantern"))
    editor.placeBlock((z+6,y+14,x+8),Block("lantern"))
    editor.placeBlock((z+11,y+10,x+8),Block("lantern"))
    editor.placeBlock((z+15,y+8,x+8),Block("lantern"))
    editor.placeBlock((z+1,y+9,x+17),Block("lantern"))
    editor.placeBlock((z+6,y+13,x+17),Block("lantern"))
    editor.placeBlock((z+11,y+9,x+17),Block("lantern"))





def window_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for zz in range(5):
        editor.placeBlock((z+zz,y,x),Block(q_id,{"facing": "south", "half": "top"}))
        editor.placeBlock((z+zz,y,x-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((z,y-2,x-1),Block(e_id))
    editor.placeBlock((z+1,y-2,x-1),Block(r_id))
    editor.placeBlock((z+2,y-2,x-1),Block(t_id))
    editor.placeBlock((z+3,y-2,x-1),Block(t_id))
    editor.placeBlock((z+4,y-2,x-1),Block(y_id))
def garden_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for xx in range(7):
        for zz in range(5):
            editor.placeBlock((z-3-zz,y+6,x+xx),Block(q_id,{"type": "bottom"}))
    for yy in range(6):
        editor.placeBlock((z-6,y+yy,x),Block(w_id))
        editor.placeBlock((z-6,y+yy,x+6),Block(w_id))
    for xx in range(6):
        for zz in range(5):
            editor.placeBlock((z-1-zz,y-1,x+xx),Block("grass_block"))
        
    for zz in range(8):
        editor.placeBlock((z-2-zz,y,x-1),Block(w_id))
        editor.placeBlock((z-2-zz,y,x+17),Block(w_id))
    for xx in range(10):
        editor.placeBlock((z-9,y,x-1+xx),Block(w_id))
    for xx in range(5):
        editor.placeBlock((z-2,y,x+1+xx),Block(e_id))
        editor.placeBlock((z-3,y,x+1+xx),Block(r_id))
        editor.placeBlock((z-4,y,x+1+xx),Block(t_id))
    for xx in range(4):
        editor.placeBlock((z,y,x+11+xx),Block(y_id,{"facing": "east", "half": "bottom"}))
    #light
    editor.placeBlock((z-2,y+1,x-1),Block("lantern"))
    editor.placeBlock((z-9,y+1,x-1),Block("lantern"))
    editor.placeBlock((z-9,y+1,x+8),Block("lantern"))
    editor.placeBlock((z-9,y+1,x+17),Block("lantern"))
    editor.placeBlock((z-3,y+1,x+17),Block("lantern"))
    light(z-6,y,x+3)
    light(z-3,y,x+6)
    light(z+2,y,x-3)
    light(z+10,y,x-3)
    light(z+15,y,x-3)
    light(z+15,y,x+8)
    light(z+15,y,x+19)
    light(z+6,y,x+19)
    light(z-6,y,x+10)
    light(z-6,y,x+15)



def indoor_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(15):
        for zz in range(12):
            editor.placeBlock((z+1+zz,y+7,x+1+xx),Block(q_id))
    for xx in range(3):
        editor.placeBlock((z+11,y+3,x+8+xx),Block(w_id))
    for yy in range(4):
        editor.placeBlock((z+11,y+1+yy,x+7),Block(w_id))
        editor.placeBlock((z+11,y+1+yy,x+11),Block(w_id))
        editor.placeBlock((z+11,y+1+yy,x+12),Block(y_id,{"facing": "west", "type": "right"}))
        editor.placeBlock((z+11,y+1+yy,x+13),Block(y_id,{"facing": "west", "type": "left"}))
        editor.placeBlock((z+11,y+1+yy,x+14),Block(u_id))
    editor.placeBlock((z+11,y+1,x+8),Block(e_id))
    editor.placeBlock((z+11,y+1,x+9),Block(r_id))
    editor.placeBlock((z+11,y+1,x+10),Block(t_id))
    for zz in range(5):
        editor.placeBlock((z+10-zz,y+2,x+6),Block(i_id,{"facing": "north", "half": "lower", "hinge": "left"}))
        editor.placeBlock((z+10-zz,y+3,x+6),Block(i_id,{"facing": "north", "half": "upper", "hinge": "left"}))
def bed_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(3):
        editor.placeBlock((z,y,x+xx),Block(q_id))
        editor.placeBlock((z-2,y,x+xx),Block(w_id,{"facing": "east", "part": "foot"}))
        command = f"summon panda {z-1} {y+2} {x+xx}"
        runCommand(command)
        editor.placeBlock((z-3,y,x+xx),Block(e_id,{"facing": "north", "lit": "false"}))
        editor.placeBlock((z-4,y,x+xx),Block(t_id,{"facing": "west", "half": "bottom", "open": "true"}))
    for xx in range(5):
        editor.placeBlock((z,y+3,x+xx),Block(r_id,{"axis": "x"}))
    for yy in range(6):
        editor.placeBlock((z,y+yy,x+5),Block(r_id,{"axis": "y"}))
        editor.placeBlock((z-6,y+yy,x+5),Block(r_id,{"axis": "y"}))
    for zz in range(5):
        editor.placeBlock((z-1-zz,y,x+5),Block(r_id,{"axis": "z"}))
        editor.placeBlock((z-1-zz,y+3,x+5),Block(r_id,{"axis": "z"}))
    editor.placeBlock((z,y+1,x),Block(y_id))
    editor.placeBlock((z,y+1,x+1),Block(i_id))
    editor.placeBlock((z,y+1,x+2),Block(u_id))
    editor.placeBlock((z,y+5,x),Block(i_id))
    editor.placeBlock((z-10,y+5,x),Block(i_id))
    editor.placeBlock((z,y+5,x+14),Block(i_id))
    editor.placeBlock((z-10,y+5,x+14),Block(i_id))
    editor.placeBlock((z-2,y+4,x+5),Block(i_id))
    editor.placeBlock((z-4,y+4,x+5),Block(i_id))
    editor.placeBlock((z,y+3,x+8),Block(i_id))

def kagu_e(x,y,z,r_id,o_id,g_id,l_id,t_id,a_id): #("red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((z+1+zz,y+1,x+11+xx),Block(r_id))

    c1=[[8,4],[12,4],[10,6],[8,8],[12,8]] #coor
    for i in range(5):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((z+c1[i][1]+zz,y+1,x+c1[i][0]+xx),Block(o_id))
    c2=[[10,4],[8,6],[12,6],[10,8]]
    for i in range(4):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((z+c2[i][1]+zz,y+1,x+c2[i][0]+xx),Block(g_id))
    editor.placeBlock((z+4,y,x+8),Block(l_id))
    editor.placeBlock((z+9,y,x+8),Block(l_id))
    editor.placeBlock((z+4,y,x+13),Block(l_id))
    editor.placeBlock((z+9,y,x+13),Block(l_id))
    editor.placeBlock((z+2,y,x+2),Block(l_id))

    for zz in range(2):
        editor.placeBlock((z+1+zz,y+1,x+1),Block(t_id,{"facing":"north","half":"top"}))
        editor.placeBlock((z+1+zz,y+1,x+2),Block(a_id,{"type":"top"}))
        editor.placeBlock((z+1+zz,y+1,x+3),Block(t_id,{"facing":"south","half":"top"}))
    editor.placeBlock((z+4,y+1,x+2),Block(t_id,{"facing":"east","half":"bottom"}))





#west
def buildHouse_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((z-1-zz,y,x+1+xx),Block(w_id))
    for yy in range(2):       
        editor.placeBlock((z,y+yy,x+15),Block(q_id))
        for xx in range(10):
            editor.placeBlock((z,y+yy,x+1+xx),Block(q_id))
        for zz in range(13):
            editor.placeBlock((z-zz,y+yy,x),Block(q_id))
            editor.placeBlock((z-zz,y+yy,x+16),Block(q_id))
        for xx in range(15):            
            editor.placeBlock((z-12,y+yy,x+1+xx),Block(q_id))
    for yy in range(6):
        editor.placeBlock((z,y+2+yy,x+15),Block(e_id))
        for xx in range(10):
            editor.placeBlock((z,y+2+yy,x+1+xx),Block(e_id))
        for zz in range(13):
            editor.placeBlock((z-zz,y+2+yy,x),Block(e_id))
            editor.placeBlock((z-zz,y+2+yy,x+16),Block(e_id))
        for xx in range(15):            
            editor.placeBlock((z-12,y+2+yy,x+1+xx),Block(e_id))
    for yy in range(7):
        editor.placeBlock((z+1,y+yy,x+17),Block(r_id))
        editor.placeBlock((z+1,y+yy,x+6),Block(r_id))
        editor.placeBlock((z+1,y+yy,x-1),Block(r_id))
        editor.placeBlock((z-13,y+yy,x-1),Block(r_id))
        editor.placeBlock((z-13,y+yy,x+17),Block(r_id))
    for yy in range(3):
        for xx in range(4):
            editor.placeBlock((z,y+5+yy,x+11+xx),Block(e_id))

    for xx in range(9):
        editor.placeBlock((z+1,y+7,x+2*xx),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z+2,y+6,x+2*xx),Block(t_id,{"type": "top"}))
        editor.placeBlock((z+1,y+8,x+2*xx),Block(y_id))
        editor.placeBlock((z+2,y+7,x+2*xx),Block(y_id))
        editor.placeBlock((z+3,y+7,x+2*xx),Block(u_id))
        editor.placeBlock((z+2,y+8,x+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+1,y+6,x+2*xx),Block(y_id))
    for xx in range(8):
        editor.placeBlock((z+1,y+7,x+1+2*xx),Block(y_id))
        editor.placeBlock((z+2,y+6,x+1+2*xx),Block(y_id))
        editor.placeBlock((z+1,y+6,x+1+2*xx),Block(o_id))
        editor.placeBlock((z-6,y+13,x+1+2*xx),Block(i_id,{"type": "bottom"}))
    for xx in range(15):
        editor.placeBlock((z-1,y+8,x+1+xx),Block(y_id))
        editor.placeBlock((z-4,y+10,x+1+xx),Block(y_id))
        editor.placeBlock((z-5,y+11,x+1+xx),Block(y_id))
        editor.placeBlock((z-6,y+12,x+1+xx),Block(y_id))
        for zz in range(2):
            editor.placeBlock((z-2-zz,y+9,x+1+xx),Block(y_id))
    for xx in range(7):
        editor.placeBlock((z-5,y+12,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-4,y+11,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-3,y+10,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-1,y+9,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-2,y+10,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z,y+9,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-6,y+13,x+2+2*xx),Block(y_id))
    for xx in range(6):
        editor.placeBlock((z+1,y+3,x+xx),Block(r_id))

    for yy in range(5):
        editor.placeBlock((z-6,y+8+yy,x),Block(e_id))
    for yy in range(4):
        editor.placeBlock((z-5,y+8+yy,x),Block(e_id))
        editor.placeBlock((z-7,y+8+yy,x),Block(e_id))
    for yy in range(3):
        editor.placeBlock((z-4,y+8+yy,x),Block(e_id))
        editor.placeBlock((z-8,y+8+yy,x),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((z-9-zz,y+8+yy,x),Block(e_id))
            editor.placeBlock((z-2-zz,y+8+yy,x),Block(e_id))
    editor.placeBlock((z-1,y+8,x),Block(e_id))
    editor.placeBlock((z-11,y+8,x),Block(e_id))

    editor.placeBlock((z-6,y+13,x),Block(y_id))
    editor.placeBlock((z-5,y+12,x),Block(y_id))
    editor.placeBlock((z-7,y+12,x),Block(y_id))
    editor.placeBlock((z-4,y+11,x),Block(y_id))
    editor.placeBlock((z-8,y+11,x),Block(y_id))
    for zz in range(2):
        editor.placeBlock((z-2-zz,y+10,x),Block(y_id))
        editor.placeBlock((z-9-zz,y+10,x),Block(y_id))
        editor.placeBlock((z-zz,y+9,x),Block(y_id))
        editor.placeBlock((z-11-zz,y+9,x),Block(y_id))
    for yy in range(2):
        editor.placeBlock((z-6,y+11+yy,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-5,y+11,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-5,y+10,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-4,y+10,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-3,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-2,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-2,y+8,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+8,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z,y+8,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z,y+7,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+7,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+2,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+3,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+2,y+6,x-1),Block(p_id,{"type": "top"}))

    editor.placeBlock((z-7,y+11,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-7,y+10,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-8,y+10,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-9,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-10,y+9,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-10,y+8,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+8,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-12,y+8,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-12,y+7,x-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-13,y+7,x-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-14,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-15,y+7,x-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-14,y+6,x-1),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((z-zz,y+5,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((z-1-2*zz,y+6,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((z-1-zz,y+7,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((z-4-2*zz,y+8,x-1),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((z-4-zz,y+9,x-1),Block(r_id,{"axis": "z"}))
    editor.placeBlock((z-6,y+10,x-1),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((z-3,y+yy,x-1),Block(r_id,{"axis": "z"}))
        editor.placeBlock((z-9,y+yy,x-1),Block(r_id,{"axis": "z"}))
    for yy in range(3):
        for zz in range(5):
            editor.placeBlock((z-4-zz,y+2+yy,x),Block(a_id))
    for zz in range(5):
        for xx in range(2):
            editor.placeBlock((z-4-zz,y+1,x-1-xx),Block(q_id))


    for yy in range(5):
        editor.placeBlock((z-6,y+8+yy,x+16),Block(e_id))
    for yy in range(4):
        editor.placeBlock((z-5,y+8+yy,x+16),Block(e_id))
        editor.placeBlock((z-7,y+8+yy,x+16),Block(e_id))
    for yy in range(3):
        editor.placeBlock((z-4,y+8+yy,x+16),Block(e_id))
        editor.placeBlock((z-8,y+8+yy,x+16),Block(e_id))
    for yy in range(2):
        for zz in range(2):
            editor.placeBlock((z-9-zz,y+8+yy,x+16),Block(e_id))
            editor.placeBlock((z-2-zz,y+8+yy,x+16),Block(e_id))
    editor.placeBlock((z-1,y+8,x+16),Block(e_id))
    editor.placeBlock((z-11,y+8,x+16),Block(e_id))

    editor.placeBlock((z-6,y+13,x+16),Block(y_id))
    editor.placeBlock((z-5,y+12,x+16),Block(y_id))
    editor.placeBlock((z-7,y+12,x+16),Block(y_id))
    editor.placeBlock((z-4,y+11,x+16),Block(y_id))
    editor.placeBlock((z-8,y+11,x+16),Block(y_id))
    for zz in range(2):
        editor.placeBlock((z-2-zz,y+10,x+16),Block(y_id))
        editor.placeBlock((z-9-zz,y+10,x+16),Block(y_id))
        editor.placeBlock((z-zz,y+9,x+16),Block(y_id))
        editor.placeBlock((z-11-zz,y+9,x+16),Block(y_id))

    for xx in range(17):
        editor.placeBlock((z,y+8,x+xx),Block(y_id))
        editor.placeBlock((z-12,y+8,x+xx),Block(y_id))
    for yy in range(2):
        editor.placeBlock((z-6,y+11+yy,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-5,y+11,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-5,y+10,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-4,y+10,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-3,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-2,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-2,y+8,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+8,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z,y+8,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z,y+7,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+7,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+2,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+3,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+2,y+6,x+17),Block(p_id,{"type": "top"}))

    editor.placeBlock((z-7,y+11,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-7,y+10,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-8,y+10,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-9,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-10,y+9,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-10,y+8,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+8,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-12,y+8,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-12,y+7,x+17),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-13,y+7,x+17),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-14,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-15,y+7,x+17),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-14,y+6,x+17),Block(p_id,{"type": "top"}))
    for zz in range(13):
        editor.placeBlock((z-zz,y+5,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(6):
        editor.placeBlock((z-1-2*zz,y+6,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(11):
        editor.placeBlock((z-1-zz,y+7,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((z-4-2*zz,y+8,x+17),Block(r_id,{"axis": "z"}))
    for zz in range(5):
        editor.placeBlock((z-4-zz,y+9,x+17),Block(r_id,{"axis": "z"}))
    editor.placeBlock((z-6,y+10,x+17),Block(r_id,{"axis": "z"}))
    for yy in range(5):
        editor.placeBlock((z-3,y+yy,x+17),Block(r_id,{"axis": "z"}))
        editor.placeBlock((z-9,y+yy,x+17),Block(r_id,{"axis": "z"}))

    for xx in range(9):
        editor.placeBlock((z-13,y+7,x+2*xx),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z-14,y+6,x+2*xx),Block(t_id,{"type": "top"}))
        editor.placeBlock((z-13,y+8,x+2*xx),Block(y_id))
        editor.placeBlock((z-14,y+7,x+2*xx),Block(y_id))
        editor.placeBlock((z-15,y+7,x+2*xx),Block(u_id))
        editor.placeBlock((z-14,y+8,x+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-13,y+6,x+2*xx),Block(y_id))
    for xx in range(8):
        editor.placeBlock((z-13,y+7,x+1+2*xx),Block(y_id))
        editor.placeBlock((z-14,y+6,x+1+2*xx),Block(y_id))
        editor.placeBlock((z-13,y+6,x+1+2*xx),Block(o_id))
    for xx in range(15):
        editor.placeBlock((z-11,y+8,x+1+xx),Block(y_id))
        editor.placeBlock((z-8,y+10,x+1+xx),Block(y_id))
        editor.placeBlock((z-7,y+11,x+1+xx),Block(y_id))
        for zz in range(2):
            editor.placeBlock((z-9-zz,y+9,x+1+xx),Block(y_id))
    for xx in range(7):
        editor.placeBlock((z-7,y+12,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-8,y+11,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-9,y+10,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-11,y+9,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-10,y+10,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-12,y+9,x+2+2*xx),Block(i_id,{"type": "bottom"}))
    #light
    editor.placeBlock((z-1,y+9,x-1),Block("lantern"))
    editor.placeBlock((z-6,y+13,x-1),Block("lantern"))
    editor.placeBlock((z-11,y+9,x-1),Block("lantern"))
    editor.placeBlock((z+3,y+8,x+8),Block("lantern"))
    editor.placeBlock((z-1,y+10,x+8),Block("lantern"))
    editor.placeBlock((z-6,y+14,x+8),Block("lantern"))
    editor.placeBlock((z-11,y+10,x+8),Block("lantern"))
    editor.placeBlock((z-15,y+8,x+8),Block("lantern"))
    editor.placeBlock((z-1,y+9,x+17),Block("lantern"))
    editor.placeBlock((z-6,y+13,x+17),Block("lantern"))
    editor.placeBlock((z-11,y+9,x+17),Block("lantern"))





def window_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for zz in range(5):
        editor.placeBlock((z-zz,y,x),Block(q_id,{"facing": "south", "half": "top"}))
        editor.placeBlock((z-zz,y,x-1),Block(w_id,{"type": "top"}))
    editor.placeBlock((z,y-2,x-1),Block(e_id))
    editor.placeBlock((z-1,y-2,x-1),Block(r_id))
    editor.placeBlock((z-2,y-2,x-1),Block(t_id))
    editor.placeBlock((z-3,y-2,x-1),Block(t_id))
    editor.placeBlock((z-4,y-2,x-1),Block(y_id))
def garden_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for xx in range(7):
        for zz in range(5):
            editor.placeBlock((z+3+zz,y+6,x+xx),Block(q_id,{"type": "bottom"}))
    for yy in range(6):
        editor.placeBlock((z+6,y+yy,x),Block(w_id))
        editor.placeBlock((z+6,y+yy,x+6),Block(w_id))
    for xx in range(6):
        for zz in range(5):
            editor.placeBlock((z+1+zz,y-1,x+xx),Block("grass_block"))
    for zz in range(8):
        editor.placeBlock((z+2+zz,y,x-1),Block(w_id))
        editor.placeBlock((z+2+zz,y,x+17),Block(w_id))
    for xx in range(10):
        editor.placeBlock((z+9,y,x-1+xx),Block(w_id))
    for xx in range(5):
        editor.placeBlock((z+2,y,x+1+xx),Block(e_id))
        editor.placeBlock((z+3,y,x+1+xx),Block(r_id))
        editor.placeBlock((z+4,y,x+1+xx),Block(t_id))
    for xx in range(4):
        editor.placeBlock((z,y,x+11+xx),Block(y_id,{"facing": "west", "half": "bottom"}))
    #light
    editor.placeBlock((z+2,y+1,x-1),Block("lantern"))
    editor.placeBlock((z+9,y+1,x-1),Block("lantern"))
    editor.placeBlock((z+9,y+1,x+8),Block("lantern"))
    editor.placeBlock((z+9,y+1,x+17),Block("lantern"))
    editor.placeBlock((z+3,y+1,x+17),Block("lantern"))
    light(z+6,y,x+3)
    light(z+3,y,x+6)
    light(z-2,y,x-3)
    light(z-10,y,x-3)
    light(z-15,y,x-3)
    light(z-15,y,x+8)
    light(z-15,y,x+19)
    light(z-6,y,x+19)
    light(z+6,y,x+10)
    light(z+6,y,x+15)



def indoor_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(15):
        for zz in range(12):
            editor.placeBlock((z-1-zz,y+7,x+1+xx),Block(q_id))
    for xx in range(3):
        editor.placeBlock((z-11,y+3,x+8+xx),Block(w_id))
    for yy in range(4):
        editor.placeBlock((z-11,y+1+yy,x+7),Block(w_id))
        editor.placeBlock((z-11,y+1+yy,x+11),Block(w_id))
        editor.placeBlock((z-11,y+1+yy,x+12),Block(y_id,{"facing": "east", "type": "left"}))
        editor.placeBlock((z-11,y+1+yy,x+13),Block(y_id,{"facing": "east", "type": "right"}))
        editor.placeBlock((z-11,y+1+yy,x+14),Block(u_id))
    editor.placeBlock((z-11,y+1,x+8),Block(e_id))
    editor.placeBlock((z-11,y+1,x+9),Block(r_id))
    editor.placeBlock((z-11,y+1,x+10),Block(t_id))
    for zz in range(5):
        editor.placeBlock((z-10+zz,y+2,x+6),Block(i_id,{"facing": "north", "half": "lower", "hinge": "left"}))
        editor.placeBlock((z-10+zz,y+3,x+6),Block(i_id,{"facing": "north", "half": "upper", "hinge": "left"}))
def bed_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for xx in range(3):
        editor.placeBlock((z,y,x+xx),Block(q_id))
        editor.placeBlock((z+2,y,x+xx),Block(w_id,{"facing": "west", "part": "foot"}))
        command = f"summon panda {z+1} {y+2} {x+xx}"
        runCommand(command)
        editor.placeBlock((z+3,y,x+xx),Block(e_id,{"facing": "north", "lit": "false"}))
        editor.placeBlock((z+4,y,x+xx),Block(t_id,{"facing": "east", "half": "bottom", "open": "true"}))
    for xx in range(5):
        editor.placeBlock((z,y+3,x+xx),Block(r_id,{"axis": "x"}))
    for yy in range(6):
        editor.placeBlock((z,y+yy,x+5),Block(r_id,{"axis": "y"}))
        editor.placeBlock((z+6,y+yy,x+5),Block(r_id,{"axis": "y"}))
    for zz in range(5):
        editor.placeBlock((z+1+zz,y,x+5),Block(r_id,{"axis": "z"}))
        editor.placeBlock((z+1+zz,y+3,x+5),Block(r_id,{"axis": "z"}))
    editor.placeBlock((z,y+1,x),Block(y_id))
    editor.placeBlock((z,y+1,x+1),Block(i_id))
    editor.placeBlock((z,y+1,x+2),Block(u_id))
    editor.placeBlock((z,y+5,x),Block(i_id))
    editor.placeBlock((z+10,y+5,x),Block(i_id))
    editor.placeBlock((z,y+5,x+14),Block(i_id))
    editor.placeBlock((z+10,y+5,x+14),Block(i_id))
    editor.placeBlock((z+2,y+4,x+5),Block(i_id))
    editor.placeBlock((z+4,y+4,x+5),Block(i_id))
    editor.placeBlock((z,y+3,x+8),Block(i_id))
def kagu_w(x,y,z,r_id,o_id,g_id,l_id,t_id,a_id): #("red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((z-1-zz,y+1,x+11+xx),Block(r_id))

    c1=[[8,4],[12,4],[10,6],[8,8],[12,8]] #coor
    for i in range(5):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((z-c1[i][1]-zz,y+1,x+c1[i][0]+xx),Block(o_id))
    c2=[[10,4],[8,6],[12,6],[10,8]]
    for i in range(4):
        for xx in range(2):
            for zz in range(2):
                editor.placeBlock((z-c2[i][1]-zz,y+1,x+c2[i][0]+xx),Block(g_id))
    editor.placeBlock((z-4,y,x+8),Block(l_id))
    editor.placeBlock((z-9,y,x+8),Block(l_id))
    editor.placeBlock((z-4,y,x+13),Block(l_id))
    editor.placeBlock((z-9,y,x+13),Block(l_id))
    editor.placeBlock((z-2,y,x+2),Block(l_id))

    for zz in range(2):
        editor.placeBlock((z-1-zz,y+1,x+1),Block(t_id,{"facing":"north","half":"top"}))
        editor.placeBlock((z-1-zz,y+1,x+2),Block(a_id,{"type":"top"}))
        editor.placeBlock((z-1-zz,y+1,x+3),Block(t_id,{"facing":"south","half":"top"}))
    editor.placeBlock((z-4,y+1,x+2),Block(t_id,{"facing":"west","half":"bottom"}))




def road_s(x,y,z,q_id):
    for xx in range(23):
        for zz in range(27):
            editor.placeBlock((x-3+xx,y-1,z-11+zz),Block(q_id))
def road_n(x,y,z,q_id):
    for xx in range(23):
        for zz in range(27):
            editor.placeBlock((x-3+xx,y-1,z+11-zz),Block(q_id))
def road_e(x,y,z,q_id):
    for xx in range(23):
        for zz in range(27):
            editor.placeBlock((z-11+zz,y-1,x-3+xx),Block(q_id))
def road_w(x,y,z,q_id):
    for xx in range(23):
        for zz in range(27):
            editor.placeBlock((z+11-zz,y-1,x-3+xx),Block(q_id))
def house3_s(x,y,z):
    road_s(x,y,z,"smooth_stone")
    buildHouse_s(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","dark_prismarine","dark_prismarine","dark_prismarine_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_s(x-1,y+4,z+4,"spruce_stairs","spruce_slab","potted_lily_of_the_valley","potted_oxeye_daisy","potted_poppy","potted_dandelion")
    garden_s(x,y,z,"petrified_oak_slab","stone_brick_wall","poppy","oxeye_daisy","dandelion","polished_andesite_stairs")
    indoor_s(x,y,z,"oak_slab","bookshelf","lectern","enchanting_table","crafting_table","chest","barrel","acacia_door")
    bed_s(x+1,y+1,z+11,"oak_log","light_blue_bed","campfire","stripped_spruce_log","oak_trapdoor","potted_cactus","potted_acacia_sapling","lantern")
    kagu_s(x,y,z,"red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
def house3_n(x,y,z):
    road_n(x,y,z,"smooth_stone")
    buildHouse_n(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","dark_prismarine","dark_prismarine","dark_prismarine_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_n(x-1,y+4,z-4,"spruce_stairs","spruce_slab","potted_lily_of_the_valley","potted_oxeye_daisy","potted_poppy","potted_dandelion")
    garden_n(x,y,z,"petrified_oak_slab","stone_brick_wall","poppy","oxeye_daisy","dandelion","polished_andesite_stairs")
    indoor_n(x,y,z,"oak_slab","bookshelf","lectern","enchanting_table","crafting_table","chest","barrel","acacia_door")
    bed_n(x+1,y+1,z-11,"oak_log","light_blue_bed","campfire","stripped_spruce_log","oak_trapdoor","potted_cactus","potted_acacia_sapling","lantern")
    kagu_n(x,y,z,"red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
def house3_e(z,y,x):
    road_e(x,y,z,"smooth_stone")
    buildHouse_e(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","dark_prismarine","dark_prismarine","dark_prismarine_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_e(x-1,y+4,z+4,"spruce_stairs","spruce_slab","potted_lily_of_the_valley","potted_oxeye_daisy","potted_poppy","potted_dandelion")
    garden_e(x,y,z,"petrified_oak_slab","stone_brick_wall","poppy","oxeye_daisy","dandelion","polished_andesite_stairs")
    indoor_e(x,y,z,"oak_slab","bookshelf","lectern","enchanting_table","crafting_table","chest","barrel","acacia_door")
    bed_e(x+1,y+1,z+11,"oak_log","light_blue_bed","campfire","stripped_spruce_log","oak_trapdoor","potted_cactus","potted_acacia_sapling","lantern")
    kagu_e(x,y,z,"red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
def house3_w(z,y,x):
    road_w(x,y,z,"smooth_stone")
    buildHouse_w(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","dark_prismarine","dark_prismarine","dark_prismarine_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_w(x-1,y+4,z-4,"spruce_stairs","spruce_slab","potted_lily_of_the_valley","potted_oxeye_daisy","potted_poppy","potted_dandelion")
    garden_w(x,y,z,"petrified_oak_slab","stone_brick_wall","poppy","oxeye_daisy","dandelion","polished_andesite_stairs")
    indoor_w(x,y,z,"oak_slab","bookshelf","lectern","enchanting_table","crafting_table","chest","barrel","acacia_door")
    bed_w(x+1,y+1,z-11,"oak_log","light_blue_bed","campfire","stripped_spruce_log","oak_trapdoor","potted_cactus","potted_acacia_sapling","lantern")
    kagu_w(x,y,z,"red_carpet","orange_carpet","green_carpet","glowstone","birch_stairs","birch_slab")
def house3(x,y,z,f):
    if f=="n":
        house3_n(x,y,z)
    elif f=="s":
        house3_s(x,y,z)
    elif f=="e":
        house3_e(x,y,z)
    elif f=="w":
        house3_w(x,y,z)


def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True

