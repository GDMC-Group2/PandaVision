from interfaceUtils import runCommand

from gdpc import Editor, Block, Transform, geometry
editor=Editor(buffering=True)


#south
#基底
def ground_s(x,y,z,q_id,w_id):
    for xx in range(19):
        for zz in range(11):
            editor.placeBlock((x+xx,y,z+zz),Block(q_id))
  
#柱
def pillar_s(x,y,z,q_id,w_id,e_id):
    #柱第一層
    for yy in range(3):
        editor.placeBlock((x,y+yy,z),Block(q_id))
        editor.placeBlock((x+4,y+yy,z),Block(q_id))
        
        editor.placeBlock((x,y+yy,z+6),Block(q_id))
        editor.placeBlock((x+4,y+yy,z+6),Block(q_id))

        editor.placeBlock((x+14,y+yy,z),Block(q_id))
        editor.placeBlock((x+10,y+yy,z),Block(q_id))

        editor.placeBlock((x+14,y+yy,z+6),Block(q_id))
        editor.placeBlock((x+10,y+yy,z+6),Block(q_id))

    editor.placeBlock((x,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x,y+3,z+6),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+14,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+14,y+3,z+6),Block(w_id,{"type": "double"}))
    

    for zz in range(5):
        editor.placeBlock((x,y+3,z+1+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+14,y+3,z+1+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+4,y+3,z+1+zz),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+10,y+3,z+1+zz),Block(w_id,{"type": "double"}))
    
    for xx in range(13):
        editor.placeBlock((x+1+xx,y+3,z),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+1+xx,y+3,z+6),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+4,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+4,y+3,z+6),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+10,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+10,y+3,z+6),Block(w_id,{"type": "double"}))

    #柱大二層
    for zz in range(2):
        editor.placeBlock((x,y+4,z-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+4,y+4,z-zz),Block(e_id,{"axis": "z"}))
        
        editor.placeBlock((x,y+4,z+6+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+4,y+4,z+6+zz),Block(e_id,{"axis": "z"}))

        editor.placeBlock((x+14,y+4,z-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+10,y+4,z-zz),Block(e_id,{"axis": "z"}))

        editor.placeBlock((x+14,y+4,z+6+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+10,y+4,z+6+zz),Block(e_id,{"axis": "z"}))

def girder_s(x,y,z,q_id,w_id,e_id):
    #一層
    for xx in range(17):
        editor.placeBlock((x+xx,y,z),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x+xx,y,z+8),Block(q_id,{"axis": "x"}))
    
    for xx in range(2):
        editor.placeBlock((x+1+4*xx,y,z+2),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+1+4*xx,y,z+6),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+1+4*xx,y-1,z+2),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+1+4*xx,y-1,z+6),Block(w_id,{"type": "top"}))

        editor.placeBlock((x+15-4*xx,y,z+2),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+15-4*xx,y,z+6),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+15-4*xx,y-1,z+2),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+15-4*xx,y-1,z+6),Block(w_id,{"type": "top"}))
        for zz in range(3):
            editor.placeBlock((x+1+4*xx,y,z+3+zz),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((x+15-4*xx,y,z+3+zz),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((x+1+4*xx,y-1,z+3+zz),Block(w_id,{"type": "top"}))
            editor.placeBlock((x+15-4*xx,y-1,z+3+zz),Block(w_id,{"type": "top"}))
    #二層
    editor.placeBlock((x,y,z+2),Block(e_id,{"type": "top"}))
    editor.placeBlock((x,y,z+6),Block(e_id,{"type": "top"}))
    editor.placeBlock((x+16,y,z+2),Block(e_id,{"type": "top"}))
    editor.placeBlock((x+16,y,z+6),Block(e_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x+2+xx,y,z+2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+12+xx,y,z+2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+2+xx,y,z+6),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+12+xx,y,z+6),Block(e_id,{"type": "top"}))
    for xx in range(5):
        editor.placeBlock((x+6+xx,y,z+2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+6+xx,y,z+6),Block(e_id,{"type": "top"}))
    for xx in range(17):
        editor.placeBlock((x+xx,y+1,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+xx,y+1,z+6),Block(e_id,{"type": "bottom"}))
    #三層
    editor.placeBlock((x+1,y+1,z+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+4,y+1,z+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+11,y+1,z+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+15,y+1,z+4),Block(w_id,{"type": "double"}))
    for zz in range(2):
        editor.placeBlock((x+1,y+1,z+3+2*zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+4,y+1,z+3+2*zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+11,y+1,z+3+2*zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+15,y+1,z+3+2*zz),Block(w_id,{"type": "bottom"}))
    #四層
    for xx in range(17):
        editor.placeBlock((x+xx,y+2,z+4),Block(q_id,{"axis": "x"}))
    
def wall_s(x,y,z,q_id,w_id,e_id,r_id):
    #wall
    for yy in range(3):
        for xx in range(3):
            editor.placeBlock((x+xx,y+yy,z+6),Block(q_id))
            editor.placeBlock((x+10+xx,y+yy,z+6),Block(q_id))
        for xx in range(5):
            editor.placeBlock((x+4+xx,y+yy,z+6),Block(q_id))

    for xx in range(3):
        editor.placeBlock((x+xx,y,z),Block(q_id))
        editor.placeBlock((x+10+xx,y,z),Block(q_id))
    for yy in range(2):
        editor.placeBlock((x+4,y+yy,z),Block(q_id))
        editor.placeBlock((x+8,y+yy,z),Block(q_id))
        editor.placeBlock((x-1,y+1+yy,z+1),Block(q_id))
        editor.placeBlock((x-1,y+1+yy,z+4),Block(q_id))
        editor.placeBlock((x-1,y+1+yy,z+5),Block(q_id))
        editor.placeBlock((x+13,y+1+yy,z+1),Block(q_id))
        editor.placeBlock((x+13,y+1+yy,z+4),Block(q_id))
        editor.placeBlock((x+13,y+1+yy,z+5),Block(q_id))
    for zz in range(5):
        editor.placeBlock((x-1,y,z+1+zz),Block(q_id))
        editor.placeBlock((x+13,y,z+1+zz),Block(q_id))
    #door
    for xx in range(5):
        editor.placeBlock((x+4+xx,y+2,z),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
    for xx in range(2):
        editor.placeBlock((x+5+xx,y,z),Block(e_id,{"facing": "south", "half": "lower", "hinge": "right"}))
        editor.placeBlock((x+5+xx,y+1,z),Block(e_id,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+7,y,z),Block(e_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+7,y+1,z),Block(e_id,{"facing": "south", "half": "upper", "hinge": "left"}))
    #window
    for xx in range(2):
        editor.placeBlock((x+xx,y+1,z),Block(r_id,{"facing": "south", "half": "lower", "hinge": "right"}))
        editor.placeBlock((x+xx,y+2,z),Block(r_id,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+2,y+1,z),Block(r_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+2,y+2,z),Block(r_id,{"facing": "south", "half": "upper", "hinge": "left"}))

    for xx in range(2):
        editor.placeBlock((x+10+xx,y+1,z),Block(r_id,{"facing": "south", "half": "lower", "hinge": "right"}))
        editor.placeBlock((x+10+xx,y+2,z),Block(r_id,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+12,y+1,z),Block(r_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+12,y+2,z),Block(r_id,{"facing": "south", "half": "upper", "hinge": "left"}))

    editor.placeBlock((x-1,y+1,z+2),Block(r_id,{"facing": "west", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x-1,y+2,z+2),Block(r_id,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x-1,y+1,z+3),Block(r_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x-1,y+2,z+3),Block(r_id,{"facing": "west", "half": "upper", "hinge": "left"}))

    editor.placeBlock((x+13,y+1,z+2),Block(r_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+13,y+2,z+2),Block(r_id,{"facing": "east", "half": "upper", "hinge": "left"}))
    editor.placeBlock((x+13,y+1,z+3),Block(r_id,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+13,y+2,z+3),Block(r_id,{"facing": "east", "half": "upper", "hinge": "right"}))

#屋根
def tiles_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    #前
    for xx in range(17):
        for yy in range(2):
            editor.placeBlock((x+xx,y+yy,z),Block(q_id))
    for xx in range(9):
        editor.placeBlock((x+2*xx,y,z-1),Block(w_id))
        editor.placeBlock((x+2*xx,y,z-2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y-1,z-4),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+2*xx,y-1,z-2-zz),Block(w_id))
            editor.placeBlock((x+2*xx,y-2,z-3-zz),Block(w_id))
        editor.placeBlock((x+2*xx,y-2,z-5),Block(e_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y-1,z-1),Block(w_id))
        editor.placeBlock((x+1+2*xx,y-1,z-2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+1+2*xx,y-2,z-5),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+1+2*xx,y-2,z-3-zz),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+2+2*xx,y-4,z-4),Block(q_id))
        editor.placeBlock((x+7+2*xx,y-4,z-4),Block(q_id))
        editor.placeBlock((x+12+2*xx,y-4,z-4),Block(q_id))
    editor.placeBlock((x+3,y-4,z-4),Block(t_id))
    editor.placeBlock((x+13,y-4,z-4),Block(t_id))
    for xx in range(3):
        editor.placeBlock((x+6+2*xx,y-4,z-4),Block(t_id))
    #後ろ
    for xx in range(9):
        editor.placeBlock((x+2*xx,y,z+1),Block(w_id))
        editor.placeBlock((x+2*xx,y,z+2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y-1,z+4),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+2*xx,y-1,z+2+zz),Block(w_id))
            editor.placeBlock((x+2*xx,y-2,z+3+zz),Block(w_id))
        editor.placeBlock((x+2*xx,y-2,z+5),Block(e_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y-1,z+1),Block(w_id))
        editor.placeBlock((x+1+2*xx,y-1,z+2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+1+2*xx,y-2,z+5),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+1+2*xx,y-2,z+3+zz),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+2+2*xx,y-4,z+4),Block(q_id))
        editor.placeBlock((x+7+2*xx,y-4,z+4),Block(q_id))
        editor.placeBlock((x+12+2*xx,y-4,z+4),Block(q_id))
    editor.placeBlock((x+3,y-4,z+4),Block(t_id))
    editor.placeBlock((x+13,y-4,z+4),Block(t_id))
    for xx in range(3):
        editor.placeBlock((x+6+2*xx,y-4,z+4),Block(t_id))
    #左
    for yy in range(6):
        editor.placeBlock((x+16,y-8+yy,z-3),Block(w_id))
        editor.placeBlock((x+16,y-8+yy,z+3),Block(w_id))
    editor.placeBlock((x+16,y-1,z),Block(t_id))
    editor.placeBlock((x+16,y-2,z+2),Block(t_id))
    editor.placeBlock((x+16,y-2,z-2),Block(t_id))
    editor.placeBlock((x+16,y-1,z+1),Block(w_id))
    editor.placeBlock((x+16,y-1,z-1),Block(w_id))
    for zz in range(3):
        editor.placeBlock((x+16,y-2,z-1+zz),Block(w_id))
    for zz in range(5):
        editor.placeBlock((x+16,y-3,z-2+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+16-1,y-4,z-2+zz),Block(y_id,{"type": "double"}))
    #右
    for yy in range(6):
        editor.placeBlock((x,y-8+yy,z-3),Block(w_id))
        editor.placeBlock((x,y-8+yy,z+3),Block(w_id))
    editor.placeBlock((x,y-1,z),Block(t_id))
    editor.placeBlock((x,y-2,z+2),Block(t_id))
    editor.placeBlock((x,y-2,z-2),Block(t_id))
    editor.placeBlock((x,y-1,z+1),Block(w_id))
    editor.placeBlock((x,y-1,z-1),Block(w_id))
    for zz in range(3):
        editor.placeBlock((x,y-2,z-1+zz),Block(w_id))
    for zz in range(5):
        editor.placeBlock((x,y-3,z-2+zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+1,y-4,z-2+zz),Block(y_id,{"type": "double"}))
    #light
    editor.placeBlock((x+8,y+2,z),Block("lantern"))



def furniture_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    #レジ
    editor.placeBlock((x+3,y+2,z+1),Block(q_id))
    editor.placeBlock((x+3,y+2,z-1),Block(q_id))
    editor.placeBlock((x-3,y+2,z+1),Block(q_id))
    editor.placeBlock((x-3,y+2,z-1),Block(q_id))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((x+6,y+yy,z+1+zz),Block(w_id,{"facing": "west"}))
    for xx in range(2):
        editor.placeBlock((x+4+xx,y+2,z+2),Block(e_id,{"facing": "north"}))
    editor.placeBlock((x+4,y,z+1),Block(r_id))
    command = f"summon panda {x+4} {y+2} {z+1}"
    runCommand(command)
    runCommand(command)
    for xx in range(3):
        editor.placeBlock((x+4+xx,y,z),Block(t_id,{"axis": "x"}))
    editor.placeBlock((x+6,y+1,z),Block(y_id))
    editor.placeBlock((x+6,y+2,z+2),Block(u_id,{"facing": "west", "type": "left"}))
    editor.placeBlock((x+6,y+2,z+1),Block(u_id,{"facing": "west", "type": "right"}))




def food_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    for xx in range(4):
        editor.placeBlock((x-6+xx,y,z-2),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x-6+xx,y+1,z-2),Block(w_id))
        editor.placeBlock((x-6+xx,y,z),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x-6+xx,y+1,z),Block(w_id))
    for xx in range(6):
        editor.placeBlock((x-6+xx,y,z+2),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x-6+xx,y+1,z+2),Block(e_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((x+xx,y+yy,z+2),Block(t_id,{"axis": "y"}))
    editor.placeBlock((x+6,y,z-1),Block(y_id,{"facing": "west"}))
    editor.placeBlock((x+6,y,z-2),Block(u_id))
    editor.placeBlock((x+3,y,z-2),Block(i_id,{"facing": "south"}))
    editor.placeBlock((x+4,y,z-2),Block(o_id))

def weapons_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id):
    editor.placeBlock((x+6,y,z-2),Block(q_id))
    editor.placeBlock((x+6,y,z-1),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+2+xx,y,z-2),Block(e_id))
        editor.placeBlock((x-5+2*xx,y,z-2),Block(r_id,{"facing": "east"}))
        editor.placeBlock((x-4+xx,y,z),Block(y_id))
    for zz in range(3):
        editor.placeBlock((x-6,y,z-1+zz),Block(t_id,{"facing": "east"}))
    for xx in range(3):
        editor.placeBlock((x-5+xx,y,z+2),Block(u_id,{"facing": "north"}))
    for yy in range(2):
        editor.placeBlock((x-1,y+yy,z+2),Block(i_id))
        editor.placeBlock((x,y+yy,z+2),Block(o_id))
        editor.placeBlock((x+1,y+yy,z+2),Block(p_id))
        editor.placeBlock((x+2,y+yy,z+2),Block(a_id))
def book_s(x,y,z,q_id,w_id,e_id,r_id,t_id):
    editor.placeBlock((x,y,z+1),Block(q_id))
    editor.placeBlock((x+1,y,z+1),Block(w_id,{"facing": "north"}))
    for zz in range(2):
        editor.placeBlock((x+6,y,z-2+zz),Block(e_id))
    editor.placeBlock((x+4,y+1,z),Block(r_id))
    for yy in range(2):
        editor.placeBlock((x-1,y+yy,z+1),Block(t_id))
        editor.placeBlock((x+2,y+yy,z+1),Block(t_id))
        for xx in range(4):
            editor.placeBlock((x-6+xx,y+yy,z-2),Block(t_id))
            editor.placeBlock((x-6+xx,y+yy,z+2),Block(t_id))
            editor.placeBlock((x-1+xx,y+yy,z+2),Block(t_id))
    for xx in range(3):
        editor.placeBlock((x-5+xx,y,z),Block(t_id))
    for zz in range(3):
        editor.placeBlock((x-6,y,z-1+zz),Block(t_id))
    editor.placeBlock((x-1,y,z),Block(t_id))
    editor.placeBlock((x+2,y,z),Block(t_id))


#north
def ground_n(x,y,z,q_id,w_id):
    for xx in range(19):
        for zz in range(11):
            editor.placeBlock((x+xx,y,z-zz),Block(q_id))
  
#柱
def pillar_n(x,y,z,q_id,w_id,e_id):
    #柱第一層
    for yy in range(3):
        editor.placeBlock((x,y+yy,z),Block(q_id))
        editor.placeBlock((x+4,y+yy,z),Block(q_id))
        
        editor.placeBlock((x,y+yy,z-6),Block(q_id))
        editor.placeBlock((x+4,y+yy,z-6),Block(q_id))

        editor.placeBlock((x+14,y+yy,z),Block(q_id))
        editor.placeBlock((x+10,y+yy,z),Block(q_id))

        editor.placeBlock((x+14,y+yy,z-6),Block(q_id))
        editor.placeBlock((x+10,y+yy,z-6),Block(q_id))

    editor.placeBlock((x,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x,y+3,z-6),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+14,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+14,y+3,z-6),Block(w_id,{"type": "double"}))
    

    for zz in range(5):
        editor.placeBlock((x,y+3,z-1-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+14,y+3,z-1-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+4,y+3,z-1-zz),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+10,y+3,z-1-zz),Block(w_id,{"type": "double"}))
    
    for xx in range(13):
        editor.placeBlock((x+1+xx,y+3,z),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+1+xx,y+3,z-6),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+4,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+4,y+3,z-6),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+10,y+3,z),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+10,y+3,z-6),Block(w_id,{"type": "double"}))

    #柱第二層
    for zz in range(2):
        editor.placeBlock((x,y+4,z+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+4,y+4,z+zz),Block(e_id,{"axis": "z"}))
        
        editor.placeBlock((x,y+4,z-6-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+4,y+4,z-6-zz),Block(e_id,{"axis": "z"}))

        editor.placeBlock((x+14,y+4,z+zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+10,y+4,z+zz),Block(e_id,{"axis": "z"}))

        editor.placeBlock((x+14,y+4,z-6-zz),Block(e_id,{"axis": "z"}))
        editor.placeBlock((x+10,y+4,z-6-zz),Block(e_id,{"axis": "z"}))

def girder_n(x,y,z,q_id,w_id,e_id):
    #一層
    for xx in range(17):
        editor.placeBlock((x+xx,y,z),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x+xx,y,z-8),Block(q_id,{"axis": "x"}))
    
    for xx in range(2):
        editor.placeBlock((x+1+4*xx,y,z-2),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+1+4*xx,y,z-6),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+1+4*xx,y-1,z-2),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+1+4*xx,y-1,z-6),Block(w_id,{"type": "top"}))

        editor.placeBlock((x+15-4*xx,y,z-2),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+15-4*xx,y,z-6),Block(w_id,{"type": "double"}))
        editor.placeBlock((x+15-4*xx,y-1,z-2),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+15-4*xx,y-1,z-6),Block(w_id,{"type": "top"}))
        for zz in range(3):
            editor.placeBlock((x+1+4*xx,y,z-3-zz),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((x+15-4*xx,y,z-3-zz),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((x+1+4*xx,y-1,z-3-zz),Block(w_id,{"type": "top"}))
            editor.placeBlock((x+15-4*xx,y-1,z-3-zz),Block(w_id,{"type": "top"}))
    #二層
    editor.placeBlock((x,y,z-2),Block(e_id,{"type": "top"}))
    editor.placeBlock((x,y,z-6),Block(e_id,{"type": "top"}))
    editor.placeBlock((x+16,y,z-2),Block(e_id,{"type": "top"}))
    editor.placeBlock((x+16,y,z-6),Block(e_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((x+2+xx,y,z-2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+12+xx,y,z-2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+2+xx,y,z-6),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+12+xx,y,z-6),Block(e_id,{"type": "top"}))
    for xx in range(5):
        editor.placeBlock((x+6+xx,y,z-2),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+6+xx,y,z-6),Block(e_id,{"type": "top"}))
    for xx in range(17):
        editor.placeBlock((x+xx,y+1,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+xx,y+1,z-6),Block(e_id,{"type": "bottom"}))
    #三層
    editor.placeBlock((x+1,y+1,z-4),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+4,y+1,z-4),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+11,y+1,z-4),Block(w_id,{"type": "double"}))
    editor.placeBlock((x+15,y+1,z-4),Block(w_id,{"type": "double"}))
    for zz in range(2):
        editor.placeBlock((x+1,y+1,z-3-2*zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+4,y+1,z-3-2*zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+11,y+1,z-3-2*zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+15,y+1,z-3-2*zz),Block(w_id,{"type": "bottom"}))
    #四層
    for xx in range(17):
        editor.placeBlock((x+xx,y+2,z-4),Block(q_id,{"axis": "x"}))
    
def wall_n(x,y,z,q_id,w_id,e_id,r_id):
    #wall
    for yy in range(3):
        for xx in range(3):
            editor.placeBlock((x+xx,y+yy,z-6),Block(q_id))
            editor.placeBlock((x+10+xx,y+yy,z-6),Block(q_id))
        for xx in range(5):
            editor.placeBlock((x+4+xx,y+yy,z-6),Block(q_id))

    for xx in range(3):
        editor.placeBlock((x+xx,y,z),Block(q_id))
        editor.placeBlock((x+10+xx,y,z),Block(q_id))
    for yy in range(2):
        editor.placeBlock((x+4,y+yy,z),Block(q_id))
        editor.placeBlock((x+8,y+yy,z),Block(q_id))
        editor.placeBlock((x-1,y+1+yy,z-1),Block(q_id))
        editor.placeBlock((x-1,y+1+yy,z-4),Block(q_id))
        editor.placeBlock((x-1,y+1+yy,z-5),Block(q_id))
        editor.placeBlock((x+13,y+1+yy,z-1),Block(q_id))
        editor.placeBlock((x+13,y+1+yy,z-4),Block(q_id))
        editor.placeBlock((x+13,y+1+yy,z-5),Block(q_id))
    for zz in range(5):
        editor.placeBlock((x-1,y,z-1-zz),Block(q_id))
        editor.placeBlock((x+13,y,z-1-zz),Block(q_id))
    #door
    for xx in range(5):
        editor.placeBlock((x+4+xx,y+2,z),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
    for xx in range(2):
        editor.placeBlock((x+5+xx,y,z),Block(e_id,{"facing": "north", "half": "lower", "hinge": "right"}))
        editor.placeBlock((x+5+xx,y+1,z),Block(e_id,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+7,y,z),Block(e_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+7,y+1,z),Block(e_id,{"facing": "north", "half": "upper", "hinge": "left"}))
    #window
    for xx in range(2):
        editor.placeBlock((x+xx,y+1,z),Block(r_id,{"facing": "north", "half": "lower", "hinge": "right"}))
        editor.placeBlock((x+xx,y+2,z),Block(r_id,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+2,y+1,z),Block(r_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+2,y+2,z),Block(r_id,{"facing": "north", "half": "upper", "hinge": "left"}))

    for xx in range(2):
        editor.placeBlock((x+10+xx,y+1,z),Block(r_id,{"facing": "north", "half": "lower", "hinge": "right"}))
        editor.placeBlock((x+10+xx,y+2,z),Block(r_id,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+12,y+1,z),Block(r_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+12,y+2,z),Block(r_id,{"facing": "north", "half": "upper", "hinge": "left"}))

    editor.placeBlock((x-1,y+1,z-2),Block(r_id,{"facing": "west", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x-1,y+2,z-2),Block(r_id,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x-1,y+1,z-3),Block(r_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x-1,y+2,z-3),Block(r_id,{"facing": "west", "half": "upper", "hinge": "left"}))

    editor.placeBlock((x+13,y+1,z-2),Block(r_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+13,y+2,z-2),Block(r_id,{"facing": "east", "half": "upper", "hinge": "left"}))
    editor.placeBlock((x+13,y+1,z-3),Block(r_id,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+13,y+2,z-3),Block(r_id,{"facing": "east", "half": "upper", "hinge": "right"}))

#屋根
def tiles_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    #前
    for xx in range(17):
        for yy in range(2):
            editor.placeBlock((x+xx,y+yy,z),Block(q_id))
    for xx in range(9):
        editor.placeBlock((x+2*xx,y,z+1),Block(w_id))
        editor.placeBlock((x+2*xx,y,z+2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y-1,z+4),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+2*xx,y-1,z+2+zz),Block(w_id))
            editor.placeBlock((x+2*xx,y-2,z+3+zz),Block(w_id))
        editor.placeBlock((x+2*xx,y-2,z+5),Block(e_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y-1,z+1),Block(w_id))
        editor.placeBlock((x+1+2*xx,y-1,z+2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+1+2*xx,y-2,z+5),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+1+2*xx,y-2,z+3+zz),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+2+2*xx,y-4,z+4),Block(q_id))
        editor.placeBlock((x+7+2*xx,y-4,z+4),Block(q_id))
        editor.placeBlock((x+12+2*xx,y-4,z+4),Block(q_id))
    editor.placeBlock((x+3,y-4,z+4),Block(t_id))
    editor.placeBlock((x+13,y-4,z+4),Block(t_id))
    for xx in range(3):
        editor.placeBlock((x+6+2*xx,y-4,z+4),Block(t_id))
    #後ろ
    for xx in range(9):
        editor.placeBlock((x+2*xx,y,z-1),Block(w_id))
        editor.placeBlock((x+2*xx,y,z-2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+2*xx,y-1,z-4),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+2*xx,y-1,z-2-zz),Block(w_id))
            editor.placeBlock((x+2*xx,y-2,z-3-zz),Block(w_id))
        editor.placeBlock((x+2*xx,y-2,z-5),Block(e_id))
    for xx in range(8):
        editor.placeBlock((x+1+2*xx,y-1,z-1),Block(w_id))
        editor.placeBlock((x+1+2*xx,y-1,z-2),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((x+1+2*xx,y-2,z-5),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x+1+2*xx,y-2,z-3-zz),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+2+2*xx,y-4,z-4),Block(q_id))
        editor.placeBlock((x+7+2*xx,y-4,z-4),Block(q_id))
        editor.placeBlock((x+12+2*xx,y-4,z-4),Block(q_id))
    editor.placeBlock((x+3,y-4,z-4),Block(t_id))
    editor.placeBlock((x+13,y-4,z-4),Block(t_id))
    for xx in range(3):
        editor.placeBlock((x+6+2*xx,y-4,z-4),Block(t_id))
    #左
    for yy in range(6):
        editor.placeBlock((x+16,y-8+yy,z+3),Block(w_id))
        editor.placeBlock((x+16,y-8+yy,z-3),Block(w_id))
    editor.placeBlock((x+16,y-1,z),Block(t_id))
    editor.placeBlock((x+16,y-2,z-2),Block(t_id))
    editor.placeBlock((x+16,y-2,z+2),Block(t_id))
    editor.placeBlock((x+16,y-1,z-1),Block(w_id))
    editor.placeBlock((x+16,y-1,z+1),Block(w_id))
    for zz in range(3):
        editor.placeBlock((x+16,y-2,z+1-zz),Block(w_id))
    for zz in range(5):
        editor.placeBlock((x+16,y-3,z+2-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+16-1,y-4,z+2-zz),Block(y_id,{"type": "double"}))
    #右
    for yy in range(6):
        editor.placeBlock((x,y-8+yy,z+3),Block(w_id))
        editor.placeBlock((x,y-8+yy,z-3),Block(w_id))
    editor.placeBlock((x,y-1,z),Block(t_id))
    editor.placeBlock((x,y-2,z-2),Block(t_id))
    editor.placeBlock((x,y-2,z+2),Block(t_id))
    editor.placeBlock((x,y-1,z-1),Block(w_id))
    editor.placeBlock((x,y-1,z+1),Block(w_id))
    for zz in range(3):
        editor.placeBlock((x,y-2,z+1-zz),Block(w_id))
    for zz in range(5):
        editor.placeBlock((x,y-3,z+2-zz),Block(r_id,{"type": "top"}))
        editor.placeBlock((x+1,y-4,z+2-zz),Block(y_id,{"type": "double"}))
    #light
    editor.placeBlock((x+8,y+2,z),Block("lantern"))



def furniture_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    #レジ
    editor.placeBlock((x+3,y+2,z-1),Block(q_id))
    editor.placeBlock((x+3,y+2,z+1),Block(q_id))
    editor.placeBlock((x-3,y+2,z-1),Block(q_id))
    editor.placeBlock((x-3,y+2,z+1),Block(q_id))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((x+6,y+yy,z-1-zz),Block(w_id,{"facing": "west"}))
    for xx in range(2):
        editor.placeBlock((x+4+xx,y+2,z-2),Block(e_id,{"facing": "south"}))
    editor.placeBlock((x+4,y,z-1),Block(r_id))
    command = f"summon panda {x+4} {y+2} {z-1}"
    runCommand(command)
    runCommand(command)
    for xx in range(3):
        editor.placeBlock((x+4+xx,y,z),Block(t_id,{"axis": "x"}))
    editor.placeBlock((x+6,y+1,z),Block(y_id))
    editor.placeBlock((x+6,y+2,z-2),Block(u_id,{"facing": "west", "type": "left"}))
    editor.placeBlock((x+6,y+2,z-1),Block(u_id,{"facing": "west", "type": "right"}))
    

def food_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    for xx in range(4):
        editor.placeBlock((x-6+xx,y,z+2),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x-6+xx,y+1,z+2),Block(w_id))
        editor.placeBlock((x-6+xx,y,z),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x-6+xx,y+1,z),Block(w_id))
    for xx in range(6):
        editor.placeBlock((x-6+xx,y,z-2),Block(q_id,{"axis": "x"}))
        editor.placeBlock((x-6+xx,y+1,z-2),Block(e_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((x+xx,y+yy,z-2),Block(t_id,{"axis": "y"}))
    editor.placeBlock((x+6,y,z+1),Block(y_id,{"facing": "west"}))
    editor.placeBlock((x+6,y,z+2),Block(u_id))
    editor.placeBlock((x+3,y,z+2),Block(i_id,{"facing": "north"}))
    editor.placeBlock((x+4,y,z+2),Block(o_id))

def weapons_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id):
    editor.placeBlock((x+6,y,z+2),Block(q_id))
    editor.placeBlock((x+6,y,z+1),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+2+xx,y,z+2),Block(e_id))
        editor.placeBlock((x-5+2*xx,y,z+2),Block(r_id,{"facing": "east"}))
        editor.placeBlock((x-4+xx,y,z),Block(y_id))
    for zz in range(3):
        editor.placeBlock((x-6,y,z+1-zz),Block(t_id,{"facing": "east"}))
    for xx in range(3):
        editor.placeBlock((x-5+xx,y,z-2),Block(u_id,{"facing": "south"}))
    for yy in range(2):
        editor.placeBlock((x-1,y+yy,z-2),Block(i_id))
        editor.placeBlock((x,y+yy,z-2),Block(o_id))
        editor.placeBlock((x+1,y+yy,z-2),Block(p_id))
        editor.placeBlock((x+2,y+yy,z-2),Block(a_id))
def book_n(x,y,z,q_id,w_id,e_id,r_id,t_id):
    editor.placeBlock((x,y,z-1),Block(q_id))
    editor.placeBlock((x+1,y,z-1),Block(w_id,{"facing": "south"}))
    for zz in range(2):
        editor.placeBlock((x+6,y,z+2-zz),Block(e_id))
    editor.placeBlock((x+4,y+1,z),Block(r_id))
    for yy in range(2):
        editor.placeBlock((x-1,y+yy,z-1),Block(t_id))
        editor.placeBlock((x+2,y+yy,z-1),Block(t_id))
        for xx in range(4):
            editor.placeBlock((x-6+xx,y+yy,z+2),Block(t_id))
            editor.placeBlock((x-6+xx,y+yy,z-2),Block(t_id))
            editor.placeBlock((x-1+xx,y+yy,z-2),Block(t_id))
    for xx in range(3):
        editor.placeBlock((x-5+xx,y,z),Block(t_id))
    for zz in range(3):
        editor.placeBlock((x-6,y,z+1-zz),Block(t_id))
    editor.placeBlock((x-1,y,z),Block(t_id))
    editor.placeBlock((x+2,y,z),Block(t_id))

#west
def ground_w(x,y,z,q_id,w_id):
    for xx in range(19):
        for zz in range(11):
            editor.placeBlock((z-zz,y,x+xx),Block(q_id))
   
#柱
def pillar_w(x,y,z,q_id,w_id,e_id):
    #柱第一層
    for yy in range(3):
        editor.placeBlock((z,y+yy,x),Block(q_id))
        editor.placeBlock((z,y+yy,x+4),Block(q_id))
        
        editor.placeBlock((z-6,y+yy,x),Block(q_id))
        editor.placeBlock((z-6,y+yy,x+4),Block(q_id))

        editor.placeBlock((z,y+yy,x+14),Block(q_id))
        editor.placeBlock((z,y+yy,x+10),Block(q_id))

        editor.placeBlock((z-6,y+yy,x+14),Block(q_id))
        editor.placeBlock((z-6,y+yy,x+10),Block(q_id))

    editor.placeBlock((z,y+3,x),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-6,y+3,x),Block(w_id,{"type": "double"}))
    editor.placeBlock((z,y+3,x+14),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-6,y+3,x+14),Block(w_id,{"type": "double"}))
    

    for zz in range(5):
        editor.placeBlock((z-1-zz,y+3,x),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z-1-zz,y+3,x+14),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z-1-zz,y+3,x+4),Block(w_id,{"type": "double"}))
        editor.placeBlock((z-1-zz,y+3,x+10),Block(w_id,{"type": "double"}))
    
    for xx in range(13):
        editor.placeBlock((z,y+3,x+1+xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z-6,y+3,x+1+xx),Block(w_id,{"type": "double"}))
    editor.placeBlock((z,y+3,x+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-6,y+3,x+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((z,y+3,x+10),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-6,y+3,x+10),Block(w_id,{"type": "double"}))

    #柱第一層
    for zz in range(2):
        editor.placeBlock((z+zz,y+4,x),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z+zz,y+4,x+4),Block(e_id,{"axis": "z"}))
        
        editor.placeBlock((z-6-zz,y+4,x),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z-6-zz,y+4,x+4),Block(e_id,{"axis": "z"}))

        editor.placeBlock((z+zz,y+4,x+14),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z+zz,y+4,x+10),Block(e_id,{"axis": "z"}))

        editor.placeBlock((z-6-zz,y+4,x+14),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z-6-zz,y+4,x+10),Block(e_id,{"axis": "z"}))

def girder_w(x,y,z,q_id,w_id,e_id):
    #一層
    for xx in range(17):
        editor.placeBlock((z,y,x+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z-8,y,x+xx),Block(q_id,{"axis": "x"}))
    
    for xx in range(2):
        editor.placeBlock((z-2,y,x+1+4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z-6,y,x+1+4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z-2,y-1,x+1+4*xx),Block(w_id,{"type": "top"}))
        editor.placeBlock((z-6,y-1,x+1+4*xx),Block(w_id,{"type": "top"}))

        editor.placeBlock((z-2,y,x+15-4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z-6,y,x+15-4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z-2,y-1,x+15-4*xx),Block(w_id,{"type": "top"}))
        editor.placeBlock((z-6,y-1,x+15-4*xx),Block(w_id,{"type": "top"}))
        for zz in range(3):
            editor.placeBlock((z-3-zz,y,x+1+4*xx),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((z-3-zz,y,x+15-4*xx),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((z-3-zz,y-1,x+1+4*xx),Block(w_id,{"type": "top"}))
            editor.placeBlock((z-3-zz,y-1,x+15-4*xx),Block(w_id,{"type": "top"}))
    #二層
    editor.placeBlock((z-2,y,x),Block(e_id,{"type": "top"}))
    editor.placeBlock((z-6,y,x),Block(e_id,{"type": "top"}))
    editor.placeBlock((z-2,y,x+16),Block(e_id,{"type": "top"}))
    editor.placeBlock((z-6,y,x+16),Block(e_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((z-2,y,x+2+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z-2,y,x+12+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z-6,y,x+2+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z-6,y,x+12+xx),Block(e_id,{"type": "top"}))
    for xx in range(5):
        editor.placeBlock((z-2,y,x+6+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z-6,y,x+6+xx),Block(e_id,{"type": "top"}))
    for xx in range(17):
        editor.placeBlock((z-2,y+1,x+xx),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((z-6,y+1,x+xx),Block(e_id,{"type": "bottom"}))
    #三層
    editor.placeBlock((z-4,y+1,x+1),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-4,y+1,x+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-4,y+1,x+11),Block(w_id,{"type": "double"}))
    editor.placeBlock((z-4,y+1,x+15),Block(w_id,{"type": "double"}))
    for zz in range(2):
        editor.placeBlock((z-3-2*zz,y+1,x+1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-3-2*zz,y+1,x+4),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-3-2*zz,y+1,x+11),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-3-2*zz,y+1,x+15),Block(w_id,{"type": "bottom"}))
    #四層
    for xx in range(17):
        editor.placeBlock((z-4,y+2,x+xx),Block(q_id,{"axis": "x"}))
    
def wall_w(x,y,z,q_id,w_id,e_id,r_id):
    #wall
    for yy in range(3):
        for xx in range(3):
            editor.placeBlock((z-6,y+yy,x+xx),Block(q_id))
            editor.placeBlock((z-6,y+yy,x+10+xx),Block(q_id))
        for xx in range(5):
            editor.placeBlock((z-6,y+yy,x+4+xx),Block(q_id))

    for xx in range(3):
        editor.placeBlock((z,y,x+xx),Block(q_id))
        editor.placeBlock((z,y,x+10+xx),Block(q_id))
    for yy in range(2):
        editor.placeBlock((z,y+yy,x+4),Block(q_id))
        editor.placeBlock((z,y+yy,x+8),Block(q_id))
        editor.placeBlock((z-1,y+1+yy,x-1),Block(q_id))
        editor.placeBlock((z-4,y+1+yy,x-1),Block(q_id))
        editor.placeBlock((z-5,y+1+yy,x-1),Block(q_id))
        editor.placeBlock((z-1,y+1+yy,x+13),Block(q_id))
        editor.placeBlock((z-4,y+1+yy,x+13),Block(q_id))
        editor.placeBlock((z-5,y+1+yy,x+13),Block(q_id))
    for zz in range(5):
        editor.placeBlock((z-1-zz,y,x-1),Block(q_id))
        editor.placeBlock((z-1-zz,y,x+13),Block(q_id))
    #door
    for xx in range(5):
        editor.placeBlock((z,y+2,x+4+xx),Block(w_id,{"facing": "west", "half": "top", "open": "true"}))
    for xx in range(2):
        editor.placeBlock((z,y,x+5+xx),Block(e_id,{"facing": "west", "half": "lower", "hinge": "right"}))
        editor.placeBlock((z,y+1,x+5+xx),Block(e_id,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z,y,x+7),Block(e_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z,y+1,x+7),Block(e_id,{"facing": "west", "half": "upper", "hinge": "left"}))
    #window
    for xx in range(2):
        editor.placeBlock((z,y+1,x+xx),Block(r_id,{"facing": "west", "half": "lower", "hinge": "right"}))
        editor.placeBlock((z,y+2,x+xx),Block(r_id,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z,y+1,x+2),Block(r_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z,y+2,x+2),Block(r_id,{"facing": "west", "half": "upper", "hinge": "left"}))

    for xx in range(2):
        editor.placeBlock((z,y+1,x+10+xx),Block(r_id,{"facing": "west", "half": "lower", "hinge": "right"}))
        editor.placeBlock((z,y+2,x+10+xx),Block(r_id,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z,y+1,x+12),Block(r_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z,y+2,x+12),Block(r_id,{"facing": "west", "half": "upper", "hinge": "left"}))

    editor.placeBlock((z-2,y+1,x-1),Block(r_id,{"facing": "north", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z-2,y+2,x-1),Block(r_id,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z-3,y+1,x-1),Block(r_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z-3,y+2,x-1),Block(r_id,{"facing": "north", "half": "upper", "hinge": "left"}))

    editor.placeBlock((z-2,y+1,x+13),Block(r_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z-2,y+2,x+13),Block(r_id,{"facing": "south", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z-3,y+1,x+13),Block(r_id,{"facing": "south", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z-3,y+2,x+13),Block(r_id,{"facing": "south", "half": "upper", "hinge": "right"}))

#屋根
def tiles_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    #前
    for xx in range(17):
        for yy in range(2):
            editor.placeBlock((z,y+yy,x+xx),Block(q_id))
    for xx in range(9):
        editor.placeBlock((z+1,y,x+2*xx),Block(w_id))
        editor.placeBlock((z+2,y,x+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z+4,y-1,x+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z+2+zz,y-1,x+2*xx),Block(w_id))
            editor.placeBlock((z+3+zz,y-2,x+2*xx),Block(w_id))
        editor.placeBlock((z+5,y-2,x+2*xx),Block(e_id))
    for xx in range(8):
        editor.placeBlock((z+1,y-1,x+1+2*xx),Block(w_id))
        editor.placeBlock((z+2,y-1,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z+5,y-2,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z+3+zz,y-2,x+1+2*xx),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z+4,y-4,x+2+2*xx),Block(q_id))
        editor.placeBlock((z+4,y-4,x+7+2*xx),Block(q_id))
        editor.placeBlock((z+4,y-4,x+12+2*xx),Block(q_id))
    editor.placeBlock((z+4,y-4,x+3),Block(t_id))
    editor.placeBlock((z+4,y-4,x+13),Block(t_id))
    for xx in range(3):
        editor.placeBlock((z+4,y-4,x+6+2*xx),Block(t_id))
    #後ろ
    for xx in range(9):
        editor.placeBlock((z-1,y,x+2*xx),Block(w_id))
        editor.placeBlock((z-2,y,x+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z-4,y-1,x+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z-2-zz,y-1,x+2*xx),Block(w_id))
            editor.placeBlock((z-3-zz,y-2,x+2*xx),Block(w_id))
        editor.placeBlock((z-5,y-2,x+2*xx),Block(e_id))
    for xx in range(8):
        editor.placeBlock((z-1,y-1,x+1+2*xx),Block(w_id))
        editor.placeBlock((z-2,y-1,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z-5,y-2,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z-3-zz,y-2,x+1+2*xx),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z-4,y-4,x+2+2*xx),Block(q_id))
        editor.placeBlock((z-4,y-4,x+7+2*xx),Block(q_id))
        editor.placeBlock((z-4,y-4,x+12+2*xx),Block(q_id))
    editor.placeBlock((z-4,y-4,x+3),Block(t_id))
    editor.placeBlock((z-4,y-4,x+13),Block(t_id))
    for xx in range(3):
        editor.placeBlock((z-4,y-4,x+6+2*xx),Block(t_id))
    #左
    for yy in range(6):
        editor.placeBlock((z+3,y-8+yy,x+16),Block(w_id))
        editor.placeBlock((z-3,y-8+yy,x+16),Block(w_id))
    editor.placeBlock((z,y-1,x+16),Block(t_id))
    editor.placeBlock((z-2,y-2,x+16),Block(t_id))
    editor.placeBlock((z+2,y-2,x+16),Block(t_id))
    editor.placeBlock((z-1,y-1,x+16),Block(w_id))
    editor.placeBlock((z+1,y-1,x+16),Block(w_id))
    for zz in range(3):
        editor.placeBlock((z+1-zz,y-2,x+16),Block(w_id))
    for zz in range(5):
        editor.placeBlock((z+2-zz,y-3,x+16),Block(r_id,{"type": "top"}))
        editor.placeBlock((z+2-zz,y-4,x+16-1),Block(y_id,{"type": "double"}))
    #右
    for yy in range(6):
        editor.placeBlock((z+3,y-8+yy,x),Block(w_id))
        editor.placeBlock((z-3,y-8+yy,x),Block(w_id))
    editor.placeBlock((z,y-1,x),Block(t_id))
    editor.placeBlock((z-2,y-2,x),Block(t_id))
    editor.placeBlock((z+2,y-2,x),Block(t_id))
    editor.placeBlock((z-1,y-1,x),Block(w_id))
    editor.placeBlock((z+1,y-1,x),Block(w_id))
    for zz in range(3):
        editor.placeBlock((z+1-zz,y-2,x),Block(w_id))
    for zz in range(5):
        editor.placeBlock((z+2-zz,y-3,x),Block(r_id,{"type": "top"}))
        editor.placeBlock((z+2-zz,y-4,x+1),Block(y_id,{"type": "double"}))
    #light
    editor.placeBlock((z,y+2,x+8),Block("lantern"))



def furniture_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    #レジ
    editor.placeBlock((z-1,y+2,x+3),Block(q_id))
    editor.placeBlock((z+1,y+2,x+3),Block(q_id))
    editor.placeBlock((z-1,y+2,x-3),Block(q_id))
    editor.placeBlock((z+1,y+2,x-3),Block(q_id))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((z-1-zz,y+yy,x+6),Block(w_id,{"facing": "north"}))
    for xx in range(2):
        editor.placeBlock((z-2,y+2,x+4+xx),Block(e_id,{"facing": "east"}))
    editor.placeBlock((z-1,y,x+4),Block(r_id))
    command = f"summon panda {z-1} {y+2} {x+4}"
    runCommand(command)
    runCommand(command)
    for xx in range(3):
        editor.placeBlock((z,y,x+4+xx),Block(t_id,{"axis": "x"}))
    editor.placeBlock((z,y+1,x+6),Block(y_id))
    editor.placeBlock((z-2,y+2,x+6),Block(u_id,{"facing": "north", "type": "left"}))
    editor.placeBlock((z-1,y+2,x+6),Block(u_id,{"facing": "north", "type": "right"}))
    

def food_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    for xx in range(4):
        editor.placeBlock((z+2,y,x-6+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z+2,y+1,x-6+xx),Block(w_id))
        editor.placeBlock((z,y,x-6+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z,y+1,x-6+xx),Block(w_id))
    for xx in range(6):
        editor.placeBlock((z-2,y,x-6+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z-2,y+1,x-6+xx),Block(e_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((z-2,y+yy,x+xx),Block(t_id,{"axis": "y"}))
    editor.placeBlock((z+1,y,x+6),Block(y_id,{"facing": "north"}))
    editor.placeBlock((z+2,y,x+6),Block(u_id))
    editor.placeBlock((z+2,y,x+3),Block(i_id,{"facing": "west"}))
    editor.placeBlock((z+2,y,x+4),Block(o_id))

def weapons_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id):
    editor.placeBlock((z+2,y,x+6),Block(q_id))
    editor.placeBlock((z+1,y,x+6),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z+2,y,x+2+xx),Block(e_id))
        editor.placeBlock((z+2,y,x-5+2*xx),Block(r_id,{"facing": "south"}))
        editor.placeBlock((z,y,x-4+xx),Block(y_id))
    for zz in range(3):
        editor.placeBlock((z+1-zz,y,x-6),Block(t_id,{"facing": "south"}))
    for xx in range(3):
        editor.placeBlock((z-2,y,x-5+xx),Block(u_id,{"facing": "east"}))
    for yy in range(2):
        editor.placeBlock((z-2,y+yy,x-1),Block(i_id))
        editor.placeBlock((z-2,y+yy,x),Block(o_id))
        editor.placeBlock((z-2,y+yy,x+1),Block(p_id))
        editor.placeBlock((z-2,y+yy,x+2),Block(a_id))
def book_w(x,y,z,q_id,w_id,e_id,r_id,t_id):
    editor.placeBlock((z-1,y,x),Block(q_id))
    editor.placeBlock((z-1,y,x+1),Block(w_id,{"facing": "east"}))
    for zz in range(2):
        editor.placeBlock((z+2-zz,y,x+6),Block(e_id))
    editor.placeBlock((z,y+1,x+4),Block(r_id))
    for yy in range(2):
        editor.placeBlock((z-1,y+yy,x-1),Block(t_id))
        editor.placeBlock((z-1,y+yy,x+2),Block(t_id))
        for xx in range(4):
            editor.placeBlock((z+2,y+yy,x-6+xx),Block(t_id))
            editor.placeBlock((z-2,y+yy,x-6+xx),Block(t_id))
            editor.placeBlock((z-2,y+yy,x-1+xx),Block(t_id))
    for xx in range(3):
        editor.placeBlock((z,y,x-5+xx),Block(t_id))
    for zz in range(3):
        editor.placeBlock((z+1-zz,y,x-6),Block(t_id))
    editor.placeBlock((z,y,x-1),Block(t_id))
    editor.placeBlock((z,y,x+2),Block(t_id))

#east
def ground_e(x,y,z,q_id,w_id):
    for xx in range(19):
        for zz in range(11):
            editor.placeBlock((z+zz,y,x+xx),Block(q_id))
  
#柱
def pillar_e(x,y,z,q_id,w_id,e_id):
    #柱第一層
    for yy in range(3):
        editor.placeBlock((z,y+yy,x),Block(q_id))
        editor.placeBlock((z,y+yy,x+4),Block(q_id))
        
        editor.placeBlock((z+6,y+yy,x),Block(q_id))
        editor.placeBlock((z+6,y+yy,x+4),Block(q_id))

        editor.placeBlock((z,y+yy,x+14),Block(q_id))
        editor.placeBlock((z,y+yy,x+10),Block(q_id))

        editor.placeBlock((z+6,y+yy,x+14),Block(q_id))
        editor.placeBlock((z+6,y+yy,x+10),Block(q_id))

    editor.placeBlock((z,y+3,x),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+6,y+3,x),Block(w_id,{"type": "double"}))
    editor.placeBlock((z,y+3,x+14),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+6,y+3,x+14),Block(w_id,{"type": "double"}))
    

    for zz in range(5):
        editor.placeBlock((z+1+zz,y+3,x),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z+1+zz,y+3,x+14),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z+1+zz,y+3,x+4),Block(w_id,{"type": "double"}))
        editor.placeBlock((z+1+zz,y+3,x+10),Block(w_id,{"type": "double"}))
    
    for xx in range(13):
        editor.placeBlock((z,y+3,x+1+xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z+6,y+3,x+1+xx),Block(w_id,{"type": "double"}))
    editor.placeBlock((z,y+3,x+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+6,y+3,x+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((z,y+3,x+10),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+6,y+3,x+10),Block(w_id,{"type": "double"}))

    #柱第2層
    for zz in range(2):
        editor.placeBlock((z-zz,y+4,x),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z-zz,y+4,x+4),Block(e_id,{"axis": "z"}))
        
        editor.placeBlock((z+6+zz,y+4,x),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z+6+zz,y+4,x+4),Block(e_id,{"axis": "z"}))

        editor.placeBlock((z-zz,y+4,x+14),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z-zz,y+4,x+10),Block(e_id,{"axis": "z"}))

        editor.placeBlock((z+6+zz,y+4,x+14),Block(e_id,{"axis": "z"}))
        editor.placeBlock((z+6+zz,y+4,x+10),Block(e_id,{"axis": "z"}))

def girder_e(x,y,z,q_id,w_id,e_id):
    #一層
    for xx in range(17):
        editor.placeBlock((z,y,x+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z+8,y,x+xx),Block(q_id,{"axis": "x"}))
    
    for xx in range(2):
        editor.placeBlock((z+2,y,x+1+4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z+6,y,x+1+4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z+2,y-1,x+1+4*xx),Block(w_id,{"type": "top"}))
        editor.placeBlock((z+6,y-1,x+1+4*xx),Block(w_id,{"type": "top"}))

        editor.placeBlock((z+2,y,x+15-4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z+6,y,x+15-4*xx),Block(w_id,{"type": "double"}))
        editor.placeBlock((z+2,y-1,x+15-4*xx),Block(w_id,{"type": "top"}))
        editor.placeBlock((z+6,y-1,x+15-4*xx),Block(w_id,{"type": "top"}))
        for zz in range(3):
            editor.placeBlock((z+3+zz,y,x+1+4*xx),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((z+3+zz,y,x+15-4*xx),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((z+3+zz,y-1,x+1+4*xx),Block(w_id,{"type": "top"}))
            editor.placeBlock((z+3+zz,y-1,x+15-4*xx),Block(w_id,{"type": "top"}))
    #二層
    editor.placeBlock((z+2,y,x),Block(e_id,{"type": "top"}))
    editor.placeBlock((z+6,y,x),Block(e_id,{"type": "top"}))
    editor.placeBlock((z+2,y,x+16),Block(e_id,{"type": "top"}))
    editor.placeBlock((z+6,y,x+16),Block(e_id,{"type": "top"}))
    for xx in range(3):
        editor.placeBlock((z+2,y,x+2+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z+2,y,x+12+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z+6,y,x+2+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z+6,y,x+12+xx),Block(e_id,{"type": "top"}))
    for xx in range(5):
        editor.placeBlock((z+2,y,x+6+xx),Block(e_id,{"type": "top"}))
        editor.placeBlock((z+6,y,x+6+xx),Block(e_id,{"type": "top"}))
    for xx in range(17):
        editor.placeBlock((z+2,y+1,x+xx),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((z+6,y+1,x+xx),Block(e_id,{"type": "bottom"}))
    #三層
    editor.placeBlock((z+4,y+1,x+1),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+4,y+1,x+4),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+4,y+1,x+11),Block(w_id,{"type": "double"}))
    editor.placeBlock((z+4,y+1,x+15),Block(w_id,{"type": "double"}))
    for zz in range(2):
        editor.placeBlock((z+3+2*zz,y+1,x+1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+3+2*zz,y+1,x+4),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+3+2*zz,y+1,x+11),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+3+2*zz,y+1,x+15),Block(w_id,{"type": "bottom"}))
    #四層
    for xx in range(17):
        editor.placeBlock((z+4,y+2,x+xx),Block(q_id,{"axis": "x"}))
    
def wall_e(x,y,z,q_id,w_id,e_id,r_id):
    #wall
    for yy in range(3):
        for xx in range(3):
            editor.placeBlock((z+6,y+yy,x+xx),Block(q_id))
            editor.placeBlock((z+6,y+yy,x+10+xx),Block(q_id))
        for xx in range(5):
            editor.placeBlock((z+6,y+yy,x+4+xx),Block(q_id))

    for xx in range(3):
        editor.placeBlock((z,y,x+xx),Block(q_id))
        editor.placeBlock((z,y,x+10+xx),Block(q_id))
    for yy in range(2):
        editor.placeBlock((z,y+yy,x+4),Block(q_id))
        editor.placeBlock((z,y+yy,x+8),Block(q_id))
        editor.placeBlock((z+1,y+1+yy,x-1),Block(q_id))
        editor.placeBlock((z+4,y+1+yy,x-1),Block(q_id))
        editor.placeBlock((z+5,y+1+yy,x-1),Block(q_id))
        editor.placeBlock((z+1,y+1+yy,x+13),Block(q_id))
        editor.placeBlock((z+4,y+1+yy,x+13),Block(q_id))
        editor.placeBlock((z+5,y+1+yy,x+13),Block(q_id))
    for zz in range(5):
        editor.placeBlock((z+1+zz,y,x-1),Block(q_id))
        editor.placeBlock((z+1+zz,y,x+13),Block(q_id))
    #door
    for xx in range(5):
        editor.placeBlock((z,y+2,x+4+xx),Block(w_id,{"facing": "east", "half": "top", "open": "true"}))
    for xx in range(2):
        editor.placeBlock((z,y,x+5+xx),Block(e_id,{"facing": "east", "half": "lower", "hinge": "right"}))
        editor.placeBlock((z,y+1,x+5+xx),Block(e_id,{"facing": "east", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z,y,x+7),Block(e_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z,y+1,x+7),Block(e_id,{"facing": "east", "half": "upper", "hinge": "left"}))
    #window
    for xx in range(2):
        editor.placeBlock((z,y+1,x+xx),Block(r_id,{"facing": "east", "half": "lower", "hinge": "right"}))
        editor.placeBlock((z,y+2,x+xx),Block(r_id,{"facing": "east", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z,y+1,x+2),Block(r_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z,y+2,x+2),Block(r_id,{"facing": "east", "half": "upper", "hinge": "left"}))

    for xx in range(2):
        editor.placeBlock((z,y+1,x+10+xx),Block(r_id,{"facing": "east", "half": "lower", "hinge": "right"}))
        editor.placeBlock((z,y+2,x+10+xx),Block(r_id,{"facing": "east", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z,y+1,x+12),Block(r_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z,y+2,x+12),Block(r_id,{"facing": "east", "half": "upper", "hinge": "left"}))

    editor.placeBlock((z+2,y+1,x-1),Block(r_id,{"facing": "north", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+2,y+2,x-1),Block(r_id,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z+3,y+1,x-1),Block(r_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+3,y+2,x-1),Block(r_id,{"facing": "north", "half": "upper", "hinge": "left"}))

    editor.placeBlock((z+2,y+1,x+13),Block(r_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+2,y+2,x+13),Block(r_id,{"facing": "south", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+3,y+1,x+13),Block(r_id,{"facing": "south", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+3,y+2,x+13),Block(r_id,{"facing": "south", "half": "upper", "hinge": "right"}))

#屋根
def tiles_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    #前
    for xx in range(17):
        for yy in range(2):
            editor.placeBlock((z,y+yy,x+xx),Block(q_id))
    for xx in range(9):
        editor.placeBlock((z-1,y,x+2*xx),Block(w_id))
        editor.placeBlock((z-2,y,x+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z-4,y-1,x+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z-2-zz,y-1,x+2*xx),Block(w_id))
            editor.placeBlock((z-3-zz,y-2,x+2*xx),Block(w_id))
        editor.placeBlock((z-5,y-2,x+2*xx),Block(e_id))
    for xx in range(8):
        editor.placeBlock((z-1,y-1,x+1+2*xx),Block(w_id))
        editor.placeBlock((z-2,y-1,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z-5,y-2,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z-3-zz,y-2,x+1+2*xx),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z-4,y-4,x+2+2*xx),Block(q_id))
        editor.placeBlock((z-4,y-4,x+7+2*xx),Block(q_id))
        editor.placeBlock((z-4,y-4,x+12+2*xx),Block(q_id))
    editor.placeBlock((z-4,y-4,x+3),Block(t_id))
    editor.placeBlock((z-4,y-4,x+13),Block(t_id))
    for xx in range(3):
        editor.placeBlock((z-4,y-4,x+6+2*xx),Block(t_id))
    #後ろ
    for xx in range(9):
        editor.placeBlock((z+1,y,x+2*xx),Block(w_id))
        editor.placeBlock((z+2,y,x+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z+4,y-1,x+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z+2+zz,y-1,x+2*xx),Block(w_id))
            editor.placeBlock((z+3+zz,y-2,x+2*xx),Block(w_id))
        editor.placeBlock((z+5,y-2,x+2*xx),Block(e_id))
    for xx in range(8):
        editor.placeBlock((z+1,y-1,x+1+2*xx),Block(w_id))
        editor.placeBlock((z+2,y-1,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        editor.placeBlock((z+5,y-2,x+1+2*xx),Block(r_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((z+3+zz,y-2,x+1+2*xx),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z+4,y-4,x+2+2*xx),Block(q_id))
        editor.placeBlock((z+4,y-4,x+7+2*xx),Block(q_id))
        editor.placeBlock((z+4,y-4,x+12+2*xx),Block(q_id))
    editor.placeBlock((z+4,y-4,x+3),Block(t_id))
    editor.placeBlock((z+4,y-4,x+13),Block(t_id))
    for xx in range(3):
        editor.placeBlock((z+4,y-4,x+6+2*xx),Block(t_id))
    #左
    for yy in range(6):
        editor.placeBlock((z-3,y-8+yy,x+16),Block(w_id))
        editor.placeBlock((z+3,y-8+yy,x+16),Block(w_id))
    editor.placeBlock((z,y-1,x+16),Block(t_id))
    editor.placeBlock((z+2,y-2,x+16),Block(t_id))
    editor.placeBlock((z-2,y-2,x+16),Block(t_id))
    editor.placeBlock((z+1,y-1,x+16),Block(w_id))
    editor.placeBlock((z-1,y-1,x+16),Block(w_id))
    for zz in range(3):
        editor.placeBlock((z-1+zz,y-2,x+16),Block(w_id))
    for zz in range(5):
        editor.placeBlock((z-2+zz,y-3,x+16),Block(r_id,{"type": "top"}))
        editor.placeBlock((z-2+zz,y-4,x+16-1),Block(y_id,{"type": "double"}))
    #右
    for yy in range(6):
        editor.placeBlock((z-3,y-8+yy,x),Block(w_id))
        editor.placeBlock((z+3,y-8+yy,x),Block(w_id))
    editor.placeBlock((z,y-1,x),Block(t_id))
    editor.placeBlock((z+2,y-2,x),Block(t_id))
    editor.placeBlock((z-2,y-2,x),Block(t_id))
    editor.placeBlock((z+1,y-1,x),Block(w_id))
    editor.placeBlock((z-1,y-1,x),Block(w_id))
    for zz in range(3):
        editor.placeBlock((z-1+zz,y-2,x),Block(w_id))
    for zz in range(5):
        editor.placeBlock((z-2+zz,y-3,x),Block(r_id,{"type": "top"}))
        editor.placeBlock((z-2+zz,y-4,x+1),Block(y_id,{"type": "double"}))
    #light
    editor.placeBlock((z,y+2,x+8),Block("lantern"))



def furniture_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    #レジ
    editor.placeBlock((z+1,y+2,x+3),Block(q_id))
    editor.placeBlock((z-1,y+2,x+3),Block(q_id))
    editor.placeBlock((z+1,y+2,x-3),Block(q_id))
    editor.placeBlock((z-1,y+2,x-3),Block(q_id))
    for zz in range(2):
        for yy in range(2):
            editor.placeBlock((z+1+zz,y+yy,x+6),Block(w_id,{"facing": "north"}))
    for xx in range(2):
        editor.placeBlock((z+2,y+2,x+4+xx),Block(e_id,{"facing": "west"}))
    editor.placeBlock((z+1,y,x+4),Block(r_id))
    command = f"summon panda {z+1} {y+2} {x+4}"
    runCommand(command)
    runCommand(command)
    for xx in range(3):
        editor.placeBlock((z,y,x+4+xx),Block(t_id,{"axis": "x"}))
    editor.placeBlock((z,y+1,x+6),Block(y_id))
    editor.placeBlock((z+2,y+2,x+6),Block(u_id,{"facing": "north", "type": "left"}))
    editor.placeBlock((z+1,y+2,x+6),Block(u_id,{"facing": "north", "type": "right"}))
    

def food_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    for xx in range(4):
        editor.placeBlock((z-2,y,x-6+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z-2,y+1,x-6+xx),Block(w_id))
        editor.placeBlock((z,y,x-6+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z,y+1,x-6+xx),Block(w_id))
    for xx in range(6):
        editor.placeBlock((z+2,y,x-6+xx),Block(q_id,{"axis": "x"}))
        editor.placeBlock((z+2,y+1,x-6+xx),Block(e_id))
    for xx in range(2):
        for yy in range(2):
            editor.placeBlock((z+2,y+yy,x+xx),Block(t_id,{"axis": "y"}))
    editor.placeBlock((z-1,y,x+6),Block(y_id,{"facing": "north"}))
    editor.placeBlock((z-2,y,x+6),Block(u_id))
    editor.placeBlock((z-2,y,x+3),Block(i_id,{"facing": "east"}))
    editor.placeBlock((z-2,y,x+4),Block(o_id))

def weapons_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id):
    editor.placeBlock((z-2,y,x+6),Block(q_id))
    editor.placeBlock((z-1,y,x+6),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z-2,y,x+2+xx),Block(e_id))
        editor.placeBlock((z-2,y,x-5+2*xx),Block(r_id,{"facing": "south"}))
        editor.placeBlock((z,y,x-4+xx),Block(y_id))
    for zz in range(3):
        editor.placeBlock((z-1+zz,y,x-6),Block(t_id,{"facing": "south"}))
    for xx in range(3):
        editor.placeBlock((z+2,y,x-5+xx),Block(u_id,{"facing": "west"}))
    for yy in range(2):
        editor.placeBlock((z+2,y+yy,x-1),Block(i_id))
        editor.placeBlock((z+2,y+yy,x),Block(o_id))
        editor.placeBlock((z+2,y+yy,x+1),Block(p_id))
        editor.placeBlock((z+2,y+yy,x+2),Block(a_id))
def book_e(x,y,z,q_id,w_id,e_id,r_id,t_id):
    editor.placeBlock((z+1,y,x),Block(q_id))
    editor.placeBlock((z+1,y,x+1),Block(w_id,{"facing": "west"}))
    for zz in range(2):
        editor.placeBlock((z-2+zz,y,x+6),Block(e_id))
    editor.placeBlock((z,y+1,x+4),Block(r_id))
    for yy in range(2):
        editor.placeBlock((z+1,y+yy,x-1),Block(t_id))
        editor.placeBlock((z+1,y+yy,x+2),Block(t_id))
        for xx in range(4):
            editor.placeBlock((z-2,y+yy,x-6+xx),Block(t_id))
            editor.placeBlock((z+2,y+yy,x-6+xx),Block(t_id))
            editor.placeBlock((z+2,y+yy,x-1+xx),Block(t_id))
    for xx in range(3):
        editor.placeBlock((z,y,x-5+xx),Block(t_id))
    for zz in range(3):
        editor.placeBlock((z+1-zz,y,x-6),Block(t_id))
    editor.placeBlock((z,y,x-1),Block(t_id))
    editor.placeBlock((z,y,x+2),Block(t_id))
def store1_s(x,y,z):
    ground_s(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_s(x+2,y,z+2,"stone_bricks","spruce_slab","oak_log")
    girder_s(x+1,y+5,z+1,"oak_log","spruce_slab","oak_slab")
    wall_s(x+3,y,z+2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_s(x+1,y+8,z+5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_s(x+9,y,z+5,"lantern","barrel","green_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    food_s(x+9,y,z+5,"stripped_oak_log","cake","melon","honeycomb_block","hay_block","smoker","cartography_table","loom","composter")

def store2_s(x,y,z):
    ground_s(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_s(x+2,y,z+2,"stone_bricks","spruce_slab","oak_log")
    girder_s(x+1,y+5,z+1,"oak_log","spruce_slab","oak_slab")
    wall_s(x+3,y,z+2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_s(x+1,y+8,z+5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_s(x+9,y,z+5,"lantern","barrel","red_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    weapons_s(x+9,y,z+5,"target","fletching_table","stonecutter","anvil","blast_furnace","smithing_table","furnace","iron_block","gold_block","diamond_block","netherite_block")

def store3_s(x,y,z):
    ground_s(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_s(x+2,y,z+2,"stone_bricks","spruce_slab","oak_log")
    girder_s(x+1,y+5,z+1,"oak_log","spruce_slab","oak_slab")
    wall_s(x+3,y,z+2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_s(x+1,y+8,z+5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_s(x+9,y,z+5,"lantern","barrel","blue_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    book_s(x+9,y,z+5,"enchanting_table","lectern","cartography_table","brewing_stand","bookshelf")

def store1_n(x,y,z):
    ground_n(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_n(x+2,y,z-2,"stone_bricks","spruce_slab","oak_log")
    girder_n(x+1,y+5,z-1,"oak_log","spruce_slab","oak_slab")
    wall_n(x+3,y,z-2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_n(x+1,y+8,z-5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_n(x+9,y,z-5,"lantern","barrel","green_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    food_n(x+9,y,z-5,"stripped_oak_log","cake","melon","honeycomb_block","hay_block","smoker","cartography_table","loom","composter")
 
def store2_n(x,y,z):
    ground_n(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_n(x+2,y,z-2,"stone_bricks","spruce_slab","oak_log")
    girder_n(x+1,y+5,z-1,"oak_log","spruce_slab","oak_slab")
    wall_n(x+3,y,z-2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_n(x+1,y+8,z-5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_n(x+9,y,z-5,"lantern","barrel","red_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    weapons_n(x+9,y,z-5,"target","fletching_table","stonecutter","anvil","blast_furnace","smithing_table","furnace","iron_block","gold_block","diamond_block","netherite_block")

def store3_n(x,y,z):
    ground_n(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_n(x+2,y,z-2,"stone_bricks","spruce_slab","oak_log")
    girder_n(x+1,y+5,z-1,"oak_log","spruce_slab","oak_slab")
    wall_n(x+3,y,z-2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_n(x+1,y+8,z-5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_n(x+9,y,z-5,"lantern","barrel","blue_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    book_n(x+9,y,z-5,"enchanting_table","lectern","cartography_table","brewing_stand","bookshelf")
 
def store1_w(z,y,x):
    ground_w(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_w(x+2,y,z-2,"stone_bricks","spruce_slab","oak_log")
    girder_w(x+1,y+5,z-1,"oak_log","spruce_slab","oak_slab")
    wall_w(x+3,y,z-2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_w(x+1,y+8,z-5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_w(x+9,y,z-5,"lantern","barrel","green_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    food_w(x+9,y,z-5,"stripped_oak_log","cake","melon","honeycomb_block","hay_block","smoker","cartography_table","loom","composter")

def store2_w(z,y,x):
    ground_w(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_w(x+2,y,z-2,"stone_bricks","spruce_slab","oak_log")
    girder_w(x+1,y+5,z-1,"oak_log","spruce_slab","oak_slab")
    wall_w(x+3,y,z-2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_w(x+1,y+8,z-5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_w(x+9,y,z-5,"lantern","barrel","red_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    weapons_w(x+9,y,z-5,"target","fletching_table","stonecutter","anvil","blast_furnace","smithing_table","furnace","iron_block","gold_block","diamond_block","netherite_block")
 
def store3_w(z,y,x):
    ground_w(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_w(x+2,y,z-2,"stone_bricks","spruce_slab","oak_log")
    girder_w(x+1,y+5,z-1,"oak_log","spruce_slab","oak_slab")
    wall_w(x+3,y,z-2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_w(x+1,y+8,z-5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_w(x+9,y,z-5,"lantern","barrel","blue_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    book_w(x+9,y,z-5,"enchanting_table","lectern","cartography_table","brewing_stand","bookshelf")
   
def store1_e(z,y,x):
    ground_e(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_e(x+2,y,z+2,"stone_bricks","spruce_slab","oak_log")
    girder_e(x+1,y+5,z+1,"oak_log","spruce_slab","oak_slab")
    wall_e(x+3,y,z+2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_e(x+1,y+8,z+5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_e(x+9,y,z+5,"lantern","barrel","green_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    food_e(x+9,y,z+5,"stripped_oak_log","cake","melon","honeycomb_block","hay_block","smoker","cartography_table","loom","composter")

def store2_e(z,y,x):
    ground_e(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_e(x+2,y,z+2,"stone_bricks","spruce_slab","oak_log")
    girder_e(x+1,y+5,z+1,"oak_log","spruce_slab","oak_slab")
    wall_e(x+3,y,z+2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_e(x+1,y+8,z+5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_e(x+9,y,z+5,"lantern","barrel","red_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    weapons_e(x+9,y,z+5,"target","fletching_table","stonecutter","anvil","blast_furnace","smithing_table","furnace","iron_block","gold_block","diamond_block","netherite_block")
  
def store3_e(z,y,x):
    ground_e(x,y-1,z,"smooth_stone","stone_brick_slab")
    pillar_e(x+2,y,z+2,"stone_bricks","spruce_slab","oak_log")
    girder_e(x+1,y+5,z+1,"oak_log","spruce_slab","oak_slab")
    wall_e(x+3,y,z+2,"smooth_quartz","acacia_trapdoor","oak_door","acacia_door")
    tiles_e(x+1,y+8,z+5,"polished_andesite","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","spruce_slab")
    furniture_e(x+9,y,z+5,"lantern","barrel","blue_wall_banner","crafting_table","stripped_oak_log","potted_red_tulip","chest")
    book_e(x+9,y,z+5,"enchanting_table","lectern","cartography_table","brewing_stand","bookshelf")
    
def store1(x,y,z,f):
    if f=="n":
        store1_n(x,y,z)
    elif f=="s":
        store1_s(x,y,z)
    elif f=="w":
        store1_w(x,y,z)
    elif f=="e":
        store1_e(x,y,z)
def store2(x,y,z,f):
    if f=="n":
        store2_n(x,y,z)
    elif f=="s":
        store2_s(x,y,z)
    elif f=="w":
        store2_w(x,y,z)
    elif f=="e":
        store2_e(x,y,z)
def store3(x,y,z,f):
    if f=="n":
        store3_n(x,y,z)
    elif f=="s":
        store3_s(x,y,z)
    elif f=="w":
        store3_w(x,y,z)
    elif f=="e":
        store3_e(x,y,z)


def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True



