from interfaceUtils import runCommand
import interfaceUtils
from gdpc import Editor, Block, Transform, geometry
 
editor = Editor(buffering=True)


def check_coor(x,y,z):
    command = f"summon minecraft:shulker {x} {y} {z} {{Invulnerable:true,Glowing:true,Silent:true,Tags:[test],NoAI:true,PersistenceRequired:true}}"
    print("座標確認用ブロックを生成")
    runCommand(command)

def light(x,y,z): #c=cobblestone_wall,l=lantern
    editor.placeBlock((x,y,z),Block("cobblestone_wall"))
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
        for zz in range(3):
            editor.placeBlock((x,y+yy,z+5+zz),Block(a_id))


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
       
    ##house2
    for yy in range(3):
        for xx in range(4):            
            editor.placeBlock((x-1-xx,y+yy,z),Block(e_id))
        for xx in range(13):
            editor.placeBlock((x-1-xx,y+yy,z+12),Block(e_id))
        for zz in range(11):
            editor.placeBlock((x-13,y+yy,z+1+zz),Block(e_id))
    for xx in range(9):
        editor.placeBlock((x-5-xx,y,z),Block(q_id))
        editor.placeBlock((x-5-xx,y,z-10),Block(q_id))
        for yy in range(5):
            editor.placeBlock((x-5-xx,y+1+yy,z),Block(e_id))
            editor.placeBlock((x-5-xx,y+1+yy,z-10),Block(e_id))
    for zz in range(9):
        editor.placeBlock((x-5,y,z-1-zz),Block(q_id))
        editor.placeBlock((x-13,y,z-1-zz),Block(q_id))
        for yy in range(5):
            editor.placeBlock((x-5,y+1+yy,z-1-zz),Block(e_id))
            editor.placeBlock((x-13,y+1+yy,z-1-zz),Block(e_id))
    for xx in range(3):
        for yy in range(3):
            editor.placeBlock((x-8-xx,y+yy,z),Block(a_id))
        for yy in range(2):
            editor.placeBlock((x-8-xx,y+1+yy,z-10),Block(a_id))

    for zz in range(6):
        editor.placeBlock((x-14,y+5,z-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-15,y+4,z-2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-14,y+6,z-2*zz),Block(y_id))
        editor.placeBlock((x-15,y+5,z-2*zz),Block(y_id))
        editor.placeBlock((x-16,y+5,z-2*zz),Block(u_id))
        editor.placeBlock((x-15,y+6,z-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+4,z-2*zz),Block(y_id))
    for zz in range(5):
        editor.placeBlock((x-14,y+5,z-1-2*zz),Block(y_id))
        editor.placeBlock((x-15,y+4,z-1-2*zz),Block(y_id))
        editor.placeBlock((x-9,y+10,z-1-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+4,z-1-2*zz),Block(o_id))
    for zz in range(9):
        editor.placeBlock((x-13,y+6,z-1-zz),Block(y_id))
        editor.placeBlock((x-12,y+6,z-1-zz),Block(y_id))
        editor.placeBlock((x-11,y+7,z-1-zz),Block(y_id))
        editor.placeBlock((x-10,y+8,z-1-zz),Block(y_id))
        editor.placeBlock((x-9,y+9,z-1-zz),Block(y_id))
    for zz in range(4):
        editor.placeBlock((x-13,y+7,z-2-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+7,z-2-2*zz),Block(y_id))
        editor.placeBlock((x-11,y+8,z-2-2*zz),Block(y_id))
        editor.placeBlock((x-10,y+9,z-2-2*zz),Block(y_id))
        editor.placeBlock((x-9,y+10,z-2-2*zz),Block(y_id))
   


    editor.placeBlock((x-9,y+10,z-10),Block(y_id))
    editor.placeBlock((x-10,y+9,z-10),Block(y_id))
    editor.placeBlock((x-8,y+9,z-10),Block(y_id))
    editor.placeBlock((x-7,y+8,z-10),Block(y_id))
    editor.placeBlock((x-11,y+8,z-10),Block(y_id))
    for xx in range(2):
        editor.placeBlock((x-12-xx,y+7,z-10),Block(y_id))
        editor.placeBlock((x-5-xx,y+7,z-10),Block(y_id))
    editor.placeBlock((x-5,y+6,z-10),Block(y_id))
    editor.placeBlock((x-13,y+6,z-10),Block(y_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+6+yy,z-10),Block(e_id))
        for yy in range(3):
            editor.placeBlock((x-8,y+6+yy,z-10),Block(e_id))
            editor.placeBlock((x-10,y+6+yy,z-10),Block(e_id))
        for yy in range(2):
             editor.placeBlock((x-11,y+6+yy,z-10),Block(e_id))
             editor.placeBlock((x-7,y+6+yy,z-10),Block(e_id))
    editor.placeBlock((x-12,y+6,z-10),Block(e_id))
    editor.placeBlock((x-6,y+6,z-10),Block(e_id))
    for zz in range(4):
        editor.placeBlock((x-5,y+7,z-2-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-6,y+7,z-2-2*zz),Block(y_id))
        editor.placeBlock((x-7,y+8,z-2-2*zz),Block(y_id))
        editor.placeBlock((x-8,y+9,z-2-2*zz),Block(y_id))
    editor.placeBlock((x-9,y+9,z-11),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((x-10,y+8,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-8,y+8,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-10,y+7,z-11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-8,y+7,z-11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-11,y+7,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-7,y+7,z-11),Block(p_id,{"type": "double"}))
    
    editor.placeBlock((x-12,y+6,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-6,y+6,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-13,y+6,z-11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+5,z-11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-5,y+6,z-11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+5,z-11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-14,y+5,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-4,y+5,z-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-15,y+5,z-11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-16,y+5,z-11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+5,z-11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+5,z-11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-15,y+4,z-11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-3,y+4,z-11),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((x-4,y+yy,z-11),Block(r_id))
        editor.placeBlock((x-14,y+yy,z-11),Block(r_id))
    for yy in range(7):
        editor.placeBlock((x-7,y+yy,z-11),Block(r_id))
        editor.placeBlock((x-11,y+yy,z-11),Block(r_id))
    for xx in range(9):
        editor.placeBlock((x-5-xx,y+4,z-11),Block(r_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+5+yy,z-11),Block(r_id))
    editor.placeBlock((x-8,y+6,z-11),Block(r_id))
    editor.placeBlock((x-10,y+6,z-11),Block(r_id))

    for zz in range(6):
        editor.placeBlock((x-4,y+5,z-2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-3,y+4,z-2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-4,y+6,z-2*zz),Block(y_id))
        editor.placeBlock((x-3,y+5,z-2*zz),Block(y_id))
        editor.placeBlock((x-2,y+5,z-2*zz),Block(u_id))
        editor.placeBlock((x-3,y+6,z-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-4,y+4,z-2*zz),Block(y_id))
    for zz in range(5):
        editor.placeBlock((x-4,y+5,z-1-2*zz),Block(y_id))
        editor.placeBlock((x-3,y+4,z-1-2*zz),Block(y_id))
        editor.placeBlock((x-4,y+4,z-1-2*zz),Block(o_id))
    for zz in range(9):
        editor.placeBlock((x-5,y+6,z-1-zz),Block(y_id))
        editor.placeBlock((x-6,y+6,z-1-zz),Block(y_id))
        editor.placeBlock((x-7,y+7,z-1-zz),Block(y_id))
        editor.placeBlock((x-8,y+8,z-1-zz),Block(y_id))

    editor.placeBlock((x-9,y+10,z),Block(y_id))
    editor.placeBlock((x-10,y+9,z),Block(y_id))
    editor.placeBlock((x-8,y+9,z),Block(y_id))
    editor.placeBlock((x-7,y+8,z),Block(y_id))
    editor.placeBlock((x-11,y+8,z),Block(y_id))
    for xx in range(2):
        editor.placeBlock((x-12-xx,y+7,z),Block(y_id))
        editor.placeBlock((x-5-xx,y+7,z),Block(y_id))
    editor.placeBlock((x-5,y+6,z),Block(y_id))
    editor.placeBlock((x-13,y+6,z),Block(y_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+6+yy,z),Block(e_id))
        for yy in range(3):
            editor.placeBlock((x-8,y+6+yy,z),Block(e_id))
            editor.placeBlock((x-10,y+6+yy,z),Block(e_id))
        for yy in range(2):
             editor.placeBlock((x-11,y+6+yy,z),Block(e_id))
             editor.placeBlock((x-7,y+6+yy,z),Block(e_id))
    editor.placeBlock((x-12,y+6,z),Block(e_id))
    editor.placeBlock((x-6,y+6,z),Block(e_id))
     
    editor.placeBlock((x-9,y+9,z+1),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((x-10,y+8,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-8,y+8,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-10,y+7,z+1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-8,y+7,z+1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-11,y+7,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-7,y+7,z+1),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((x-12,y+6,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-6,y+6,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-13,y+6,z+1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+5,z+1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-5,y+6,z+1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+5,z+1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-14,y+5,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-4,y+5,z+1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-15,y+5,z+1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-16,y+5,z+1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+5,z+1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+5,z+1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-15,y+4,z+1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-3,y+4,z+1),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((x-4,y+yy,z+1),Block(r_id))
        editor.placeBlock((x-14,y+yy,z+1),Block(r_id))
    for yy in range(7):
        editor.placeBlock((x-7,y+yy,z+1),Block(r_id))
        editor.placeBlock((x-11,y+yy,z+1),Block(r_id))
    for xx in range(9):
        editor.placeBlock((x-5-xx,y+4,z+1),Block(r_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+5+yy,z+1),Block(r_id))
    editor.placeBlock((x-8,y+6,z+1),Block(r_id))
    editor.placeBlock((x-10,y+6,z+1),Block(r_id))
    for xx in range(7):
        editor.placeBlock((x-13+2*xx,y+3,z+12),Block(y_id))
    for xx in range(6):
        editor.placeBlock((x-12+2*xx,y+3,z+12),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-13+2*xx,y+3,z+13),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-11+2*xx,y+3,z+11),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-12+2*xx,y+2,z+11),Block(i_id,{"type": "top"}))
        editor.placeBlock((x-12+2*xx,y+2,z+13),Block(i_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((x-13,y+3,z+2+2*zz),Block(y_id))
        editor.placeBlock((x-13,y+3,z+3+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+3,z+2+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+2,z+3+2*zz),Block(i_id,{"type": "top"}))
        editor.placeBlock((x-12,y+2,z+3+2*zz),Block(i_id,{"type": "top"}))
    for zz in range(6):
        editor.placeBlock((x-14,y+3,z+2+2*zz),Block(i_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x+11+xx,y,z),Block(s_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
   
    for zz in range(3):
        editor.placeBlock((x,y,z+5+zz),Block(s_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    #light
    light(x-1,y,z-3)
    light(x+5,y,z-3)
    light(x+18,y,z-3)
    light(x+10,y,z-11)
    light(x+15,y,z-11)
    light(x+10,y,z-7)
    light(x+15,y,z-7)
    light(x-6,y,z-12)
    light(x-15,y,z-12)
    light(x+19,y,z+3)
    light(x+19,y,z+9)
    light(x+18,y,z+16)
    light(x+13,y,z+16)
    light(x+8,y,z+16)
    light(x+3,y,z+16)
    light(x-2,y,z+16)
    light(x-7,y,z+16)
    light(x-14,y,z+16)
    editor.placeBlock((x+17,y+6,z-3),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((x-7,y+2,z+13),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((x-14,y+2,z+8),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((x-14,y+2,z+4),Block("lantern",{"hanging": "true"}))
    #house1
    editor.placeBlock((x+5,y+8,z-1),Block("lantern"))
    editor.placeBlock((x+5,y+10,z+3),Block("lantern"))
    editor.placeBlock((x+5,y+10,z+9),Block("lantern"))
    editor.placeBlock((x+5,y+8,z+13),Block("lantern"))
    editor.placeBlock((x+11,y+8,z-1),Block("lantern"))
    editor.placeBlock((x+11,y+10,z+3),Block("lantern"))
    editor.placeBlock((x+11,y+10,z+9),Block("lantern"))
    editor.placeBlock((x+11,y+8,z+13),Block("lantern"))
    editor.placeBlock((x-1,y+9,z+1),Block("lantern"))
    editor.placeBlock((x-1,y+13,z+6),Block("lantern"))
    editor.placeBlock((x-1,y+9,z+11),Block("lantern"))
    editor.placeBlock((x+17,y+9,z+1),Block("lantern"))
    editor.placeBlock((x+17,y+13,z+6),Block("lantern"))
    editor.placeBlock((x+17,y+9,z+11),Block("lantern"))
    editor.placeBlock((x+8,y+14,z+6),Block("lantern"))
    #house2
    editor.placeBlock((x-3,y+5,z-1),Block("lantern"))
    editor.placeBlock((x-3,y+5,z-9),Block("lantern"))
    editor.placeBlock((x-5,y+7,z-5),Block("lantern"))
    editor.placeBlock((x-9,y+10,z-11),Block("lantern"))
    editor.placeBlock((x-9,y+10,z+1),Block("lantern"))
    editor.placeBlock((x-13,y+7,z-5),Block("lantern"))
    editor.placeBlock((x-15,y+5,z-9),Block("lantern"))
    editor.placeBlock((x-15,y+5,z-1),Block("lantern"))






def window_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    editor.placeBlock((x,y+1,z-1),Block(w_id,{"facing": "west", "half": "top", "open": "true"}))
    editor.placeBlock((x+5,y+1,z-1),Block(w_id,{"facing": "east", "half": "top", "open": "true"}))
    for xx in range(3):
        editor.placeBlock((x-8-xx,y,z-11),Block(q_id))
        editor.placeBlock((x-8-xx,y,z-12),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x-8-xx,y+3,z-12),Block(w_id,{"facing": "north", "half": "bottom"}))
        editor.placeBlock((x-8-xx,y+3,z-11),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-10+xx,y+1,z-11),Block(y_id))
    for xx in range(4):
        editor.placeBlock((x+1+xx,y+1,z-1),Block(q_id))
        editor.placeBlock((x+1+xx,y,z-1),Block(w_id,{"facing": "north", "half": "top"}))
        editor.placeBlock((x+1+xx,y+1,z-2),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x+1+xx,y+5,z-1),Block(t_id,{"facing": "south", "lit": "false"}))
        editor.placeBlock((x+1+xx,y+2,z-1),Block(y_id))
        editor.placeBlock((x+1+xx,y+4,z-1),Block(u_id))
        for yy in range(3):
            editor.placeBlock((x+1+xx,y+2+yy,z),Block(r_id))
    for xx in range(2):
        editor.placeBlock((x+2+xx,y+5,z-2),Block(t_id,{"facing": "south", "lit": "false"}))
    for zz in range(30):
        for xx in range(35):
            editor.placeBlock((x-15+xx,y-1,z-12+zz),Block(i_id))
    for xx in range(6):
        editor.placeBlock((x+10+xx,y+5,z-4),Block(w_id,{"facing": "north", "half": "bottom"}))
        for zz in range(3):
            editor.placeBlock((x+10+xx,y+5,z-1-zz),Block(t_id,{"facing": "south", "lit": "false"}))
    for yy in range(5):
        editor.placeBlock((x+10,y+yy,z-3),Block(o_id))
        editor.placeBlock((x+15,y+yy,z-3),Block(o_id))
def niwa_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(4):
        editor.placeBlock((x+1+xx,y,z-11),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+1+xx,y,z-5),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+1+xx,y,z-12),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+1+xx,y,z-4),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
        for zz in range(3):
            editor.placeBlock((x+1+xx,y,z-7-zz),Block(q_id))
    editor.placeBlock((x+5,y,z-11),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    editor.placeBlock((x,y,z-11),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((x,y,z-5),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((x+5,y,z-5),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    for zz in range(3):
        editor.placeBlock((x+6,y,z-7-zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x-1,y,z-7-zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+7,y,z-7-zz),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
        editor.placeBlock((x-2,y,z-7-zz),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
    editor.placeBlock((x-1,y,z-6),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    editor.placeBlock((x-1,y,z-10),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((x+6,y,z-10),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((x+6,y,z-6),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    for xx in range(2):
        editor.placeBlock((x+2+xx,y+1,z-8),Block(t_id))
    editor.placeBlock((x+3,y+1,z-9),Block(y_id))
    editor.placeBlock((x+1,y+1,z-9),Block(u_id))
    editor.placeBlock((x-8,y+1,z+6),Block(u_id))
    for zz in range(4):
        editor.placeBlock((x-6,y,z+8+zz),Block(i_id))
    editor.placeBlock((x-7,y,z+7),Block(i_id))
    editor.placeBlock((x-7,y,z+8),Block(i_id))
    editor.placeBlock((x-8,y,z+7),Block(i_id))
    for xx in range(5):
        editor.placeBlock((x-8-xx,y,z+6),Block(i_id))
    for yy in range(2):
        for xx in range(3):
            for zz in range(5):
                editor.placeBlock((x-10-xx,y-1-yy,z+7+zz),Block(o_id))
        for zz in range(4):
            editor.placeBlock((x-9,y-1-yy,z+8+zz),Block(o_id))
        for zz in range(3):
            editor.placeBlock((x-8,y-1-yy,z+9+zz),Block(o_id))
        for zz in range(2):
            editor.placeBlock((x-7,y-1-yy,z+10+zz),Block(o_id))
    editor.placeBlock((x-9,y-1,z+7),Block(p_id))
    editor.placeBlock((x-8,y-1,z+8),Block(p_id))
    editor.placeBlock((x-7,y-1,z+9),Block(p_id))
    editor.placeBlock((x-11,y,z+8),Block(a_id))
    editor.placeBlock((x-9,y,z+10),Block(a_id))
    for yy in range(12):
        editor.placeBlock((x-7,y+yy,z+9),Block(s_id))
    for yy in range(15):
        editor.placeBlock((x-8,y+yy,z+8),Block(s_id))
    for yy in range(13):
        editor.placeBlock((x-9,y+yy,z+7),Block(s_id))
    editor.placeBlock((x-1,y,z+1),Block("chiseled_stone_bricks"))
    editor.placeBlock((x-1,y+1,z+1),Block("lantern"))
    editor.placeBlock((x-1,y,z+11),Block("chiseled_stone_bricks"))
    editor.placeBlock((x-1,y+1,z+11),Block("lantern"))
    editor.placeBlock((x-12,y,z+1),Block("chiseled_stone_bricks"))
    editor.placeBlock((x-12,y+1,z+1),Block("lantern"))
    
    editor.placeBlock((x-13,y+4,z+12),Block("lantern"))
    editor.placeBlock((x-7,y+4,z+12),Block("lantern"))
    editor.placeBlock((x-13,y+4,z+6),Block("lantern"))

def kagu1_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((x+1+xx,y+7,z+1+zz),Block(q_id))
    for xx in range(7):
        for zz in range(9):
            editor.placeBlock((x-12+xx,y+5,z-1-zz),Block(q_id))
    for yy in range(2):
        for xx in range(4):
            editor.placeBlock((x+12+xx,y+1+yy,z+11),Block(w_id))
        for zz in range(3):
            editor.placeBlock((x+15,y+1+yy,z+8+zz),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+14+xx,y+3,z+11),Block(w_id))
    editor.placeBlock((x+15,y+3,z+10),Block(w_id))
    editor.placeBlock((x+15,y+1,z+7),Block(w_id))
    editor.placeBlock((x+11,y+1,z+11),Block(e_id))
    for yy in range(2):
        editor.placeBlock((x+11,y+2+yy,z+11),Block(r_id))
    editor.placeBlock((x+15,y+1,z+6),Block(e_id))
    for yy in range(2):
        editor.placeBlock((x+15,y+2+yy,z+6),Block(r_id))
    editor.placeBlock((x+13,y+1,z+9),Block(t_id))
    editor.placeBlock((x+15,y+4,z+11),Block(y_id))
    editor.placeBlock((x+15,y+3,z+9),Block(u_id,{"facing": "west"}))
    editor.placeBlock((x+15,y+3,z+7),Block(i_id,{"facing": "west"}))
    editor.placeBlock((x+15,y+2,z+7),Block(o_id))
    editor.placeBlock((x+15,y+3,z+8),Block(p_id))
    editor.placeBlock((x+13,y+3,z+11),Block(a_id))
    editor.placeBlock((x+12,y+3,z+11),Block(s_id))
    for yy in range(4):
        editor.placeBlock((x+15,y+1+yy,z+5),Block(d_id))
        editor.placeBlock((x+11,y+1+yy,z+5),Block(d_id))
    for xx in range(3):
        editor.placeBlock((x+12+xx,y+1,z+5),Block(d_id))
        editor.placeBlock((x+12+xx,y+4,z+5),Block(d_id))
  
    editor.placeBlock((x+12,y+3,z+4),Block(f_id,{"facing": "north", "half": "upper", "hinge": "left"}))
    editor.placeBlock((x+12,y+2,z+4),Block(f_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+13,y+3,z+4),Block(f_id,{"facing": "north", "half": "upper", "hinge": "left"}))
    editor.placeBlock((x+13,y+2,z+4),Block(f_id,{"facing": "north", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+14,y+3,z+4),Block(f_id,{"facing": "north", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+14,y+2,z+4),Block(f_id,{"facing": "north", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+14,y+5,z+5),Block(y_id))
    editor.placeBlock((x+12,y+5,z+5),Block(g_id))
    for zz in range(2):
        editor.placeBlock((x+15,y+3,z+2+zz),Block(d_id,{"facing": "west"}))
        editor.placeBlock((x+15,y+1,z+2+zz),Block(d_id,{"facing": "west"}))
    editor.placeBlock((x+15,y+4,z+2),Block(y_id))
    editor.placeBlock((x+15,y+4,z+3),Block(p_id))
    editor.placeBlock((x+6,y+6,z+3),Block(y_id))
    editor.placeBlock((x-12,y+1,z-8),Block(y_id))
    editor.placeBlock((x-6,y+4,z-9),Block(y_id))
    editor.placeBlock((x-6,y+4,z-1),Block(y_id))
    editor.placeBlock((x-12,y+4,z-1),Block(y_id))
    #enchant
    editor.placeBlock((x+11,y+1,z+7),Block("white_carpet"))
    editor.placeBlock((x+11,y,z+7),Block("glowstone"))
    editor.placeBlock((x+12,y,z+7),Block("black_wool"))
    editor.placeBlock((x+14,y,z+7),Block("black_wool"))
    editor.placeBlock((x+11,y,z+8),Block("black_wool"))
    editor.placeBlock((x+11,y,z+10),Block("black_wool"))
    editor.placeBlock((x+13,y,z+8),Block("white_wool"))
    editor.placeBlock((x+12,y,z+9),Block("white_wool"))
    editor.placeBlock((x+14,y,z+9),Block("white_wool"))
    editor.placeBlock((x+13,y,z+10),Block("white_wool"))

    editor.placeBlock((x+13,y,z+7),Block("light_gray_wool"))
    editor.placeBlock((x+11,y,z+9),Block("light_gray_wool"))
    editor.placeBlock((x+12,y,z+8),Block("light_gray_wool"))
    editor.placeBlock((x+14,y,z+8),Block("light_gray_wool"))
    editor.placeBlock((x+12,y,z+10),Block("light_gray_wool"))
    editor.placeBlock((x+14,y,z+10),Block("light_gray_wool"))
    #玄関
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((x+11+xx,y+1,z+2-zz),Block("red_carpet"))
    editor.placeBlock((x+12,y,z+1),Block("glowstone"))
    editor.placeBlock((x+13,y,z+1),Block("glowstone"))
def kitchen_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for yy in range(3):
        editor.placeBlock((x+15,y+1+yy,z+1),Block(q_id,{"facing": "north", "half": "top", "open": "true"}))
        editor.placeBlock((x+15,y+1+yy,z+4),Block(q_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+9,y+1+yy,z+11),Block(q_id,{"facing": "east", "half": "top", "open": "true"}))
        editor.placeBlock((x+7,y+1+yy,z+11),Block(q_id,{"facing": "west", "half": "top", "open": "true"}))
    for zz in range(2):
        editor.placeBlock((x+15,y+2,z+2+zz),Block(p_id,{"facing": "east", "half": "top", "shape": "straight"}))
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+1,z+11),Block(w_id,{"facing": "north"}))
    editor.placeBlock((x+1,y+1,z+10),Block(e_id,{"facing": "east"}))
    editor.placeBlock((x+1,y+1,z+9),Block(r_id,{"facing": "east"}))
    editor.placeBlock((x+7+xx,y+2,z+11),Block(p_id,{"facing": "south", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+7+xx,y+1,z+11),Block(t_id,{"facing": "north"}))
    editor.placeBlock((x+7+xx,y+3,z+11),Block(t_id,{"facing": "north"}))
    for xx in range(4):
        editor.placeBlock((x+3+xx,y+1,z+11),Block(r_id,{"facing": "north"}))
    for yy in range(2):
        editor.placeBlock((x+6,y+1+yy,z+11),Block(t_id,{"facing": "north"}))
    editor.placeBlock((x+5,y+4,z+11),Block(t_id,{"facing": "north"}))
    for zz in range(2):
        editor.placeBlock((x+1,y+4,z+9+2*zz),Block(t_id,{"facing": "east"}))
        editor.placeBlock((x+1,y+3,z+9+zz),Block(q_id,{"facing": "east", "half": "top"}))
    for xx in range(5):
        editor.placeBlock((x+1+xx,y+3,z+11),Block(q_id,{"facing": "north", "half": "top"}))
    editor.placeBlock((x+4,y+6,z+9),Block(y_id))
    editor.placeBlock((x+3,y+4,z+11),Block(y_id))
    editor.placeBlock((x+9,y+6,z+11),Block(y_id))
    editor.placeBlock((x+4,y+4,z+11),Block(u_id,{"facing": "north", "type": "single"}))
    editor.placeBlock((x+1,y+4,z+10),Block(u_id,{"facing": "east", "type": "single"}))
    editor.placeBlock((x+2,y+4,z+11),Block(i_id))
    editor.placeBlock((x+5,y+2,z+11),Block(o_id,{"facing": "south"}))
    for xx in range(3):
        editor.placeBlock((x+2+xx,y+1,z+8),Block(a_id,{"axis": "x"}))
    editor.placeBlock((x+1,y+1,z+8),Block(s_id))
    editor.placeBlock((x+1,y+2,z+8),Block(d_id))
    editor.placeBlock((x+3,y+2,z+11),Block(f_id))
    editor.placeBlock((x+3,y+2,z+8),Block(g_id))
    editor.placeBlock((x+1,y+4,z+4),Block(q_id,{"half": "top"}))
    editor.placeBlock((x+1,y+3,z+3),Block(q_id,{"half": "top"}))
    editor.placeBlock((x+1,y+2,z+2),Block(q_id,{"half": "top"}))

    for xx in range(2):
        for zz in range(3):
            editor.placeBlock((x+1+xx,y+1,z+5+zz),Block("orange_carpet"))
    editor.placeBlock((x+1,y,z+6),Block("glowstone"))


def table_s(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for xx in range(3):
        editor.placeBlock((x+5+xx,y+1,z+4),Block(q_id))
        editor.placeBlock((x+5+xx,y+1,z+2),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+5+xx,y+1,z+1),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+5+xx,y+1,z+3),Block("white_carpet"))
    editor.placeBlock((x+6,y,z+3),Block("glowstone"))
    editor.placeBlock((x+4,y+1,z+2),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
    editor.placeBlock((x+8,y+1,z+2),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
    editor.placeBlock((x+1,y+5,z+4),Block(r_id))
    editor.placeBlock((x+1,y+4,z+3),Block(t_id))
    editor.placeBlock((x+1,y+3,z+2),Block(y_id))
    editor.placeBlock((x+6,y+2,z+4),Block(u_id))
def bed_s(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for zz in range(3):
        editor.placeBlock((x-12,y,z-7-zz),Block(q_id,{"axis": "z"}))
        editor.placeBlock((x-9,y,z-7-zz),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-10,y,z-7-zz),Block(w_id,{"facing": "west", "part": "foot"}))
        command = f"summon panda {x-10} {y+2} {z-7+zz}"
        runCommand(command)
        runCommand(command)
        runCommand(command)
    for yy in range(3):
        for zz in range(2):
            editor.placeBlock((x-6,y+yy,z-8-zz),Block(r_id))
    for yy in range(2):
        editor.placeBlock((x-6,y+yy,z-7),Block(r_id))
    editor.placeBlock((x-12,y+1,z-9),Block(t_id))
    for xx in range(5):
        for zz in range(3):
            editor.placeBlock((x-7-xx,y,z-1-zz),Block("light_blue_carpet"))
    editor.placeBlock((x-9,y-1,z-2),Block("glowstone"))

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
            pass
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
        for zz in range(3):
            editor.placeBlock((x,y+yy,z-5-zz),Block(a_id))


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
            pass
    for xx in range(7):
        editor.placeBlock((x+2+2*xx,y+12,z-7),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+11,z-8),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z-9),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+9,z-11),Block(y_id))
        editor.placeBlock((x+2+2*xx,y+10,z-10),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x+2+2*xx,y+9,z-12),Block(i_id,{"type": "bottom"}))
       
    ##house2
    for yy in range(3):
        for xx in range(4):            
            editor.placeBlock((x-1-xx,y+yy,z),Block(e_id))
        for xx in range(13):
            editor.placeBlock((x-1-xx,y+yy,z-12),Block(e_id))
        for zz in range(11):
            editor.placeBlock((x-13,y+yy,z-1-zz),Block(e_id))
    for xx in range(9):
        editor.placeBlock((x-5-xx,y,z),Block(q_id))
        editor.placeBlock((x-5-xx,y,z+10),Block(q_id))
        for yy in range(5):
            editor.placeBlock((x-5-xx,y+1+yy,z),Block(e_id))
            editor.placeBlock((x-5-xx,y+1+yy,z+10),Block(e_id))
    for zz in range(9):
        editor.placeBlock((x-5,y,z+1+zz),Block(q_id))
        editor.placeBlock((x-13,y,z+1+zz),Block(q_id))
        for yy in range(5):
            editor.placeBlock((x-5,y+1+yy,z+1+zz),Block(e_id))
            editor.placeBlock((x-13,y+1+yy,z+1+zz),Block(e_id))
    for xx in range(3):
        for yy in range(3):
            editor.placeBlock((x-8-xx,y+yy,z),Block(a_id))
        for yy in range(2):
            editor.placeBlock((x-8-xx,y+1+yy,z+10),Block(a_id))


    for zz in range(6):
        editor.placeBlock((x-14,y+5,z+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-15,y+4,z+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-14,y+6,z+2*zz),Block(y_id))
        editor.placeBlock((x-15,y+5,z+2*zz),Block(y_id))
        editor.placeBlock((x-16,y+5,z+2*zz),Block(u_id))
        editor.placeBlock((x-15,y+6,z+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+4,z+2*zz),Block(y_id))
    for zz in range(5):
        editor.placeBlock((x-14,y+5,z+1+2*zz),Block(y_id))
        editor.placeBlock((x-15,y+4,z+1+2*zz),Block(y_id))
        editor.placeBlock((x-9,y+10,z+1+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+4,z+1+2*zz),Block(o_id))
    for zz in range(9):
        editor.placeBlock((x-13,y+6,z+1+zz),Block(y_id))
        editor.placeBlock((x-12,y+6,z+1+zz),Block(y_id))
        editor.placeBlock((x-11,y+7,z+1+zz),Block(y_id))
        editor.placeBlock((x-10,y+8,z+1+zz),Block(y_id))
        editor.placeBlock((x-9,y+9,z+1+zz),Block(y_id))
    for zz in range(4):
        editor.placeBlock((x-13,y+7,z+2+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+7,z+2+2*zz),Block(y_id))
        editor.placeBlock((x-11,y+8,z+2+2*zz),Block(y_id))
        editor.placeBlock((x-10,y+9,z+2+2*zz),Block(y_id))
        editor.placeBlock((x-9,y+10,z+2+2*zz),Block(y_id))
   


    editor.placeBlock((x-9,y+10,z+10),Block(y_id))
    editor.placeBlock((x-10,y+9,z+10),Block(y_id))
    editor.placeBlock((x-8,y+9,z+10),Block(y_id))
    editor.placeBlock((x-7,y+8,z+10),Block(y_id))
    editor.placeBlock((x-11,y+8,z+10),Block(y_id))
    for xx in range(2):
        editor.placeBlock((x-12-xx,y+7,z+10),Block(y_id))
        editor.placeBlock((x-5-xx,y+7,z+10),Block(y_id))
    editor.placeBlock((x-5,y+6,z+10),Block(y_id))
    editor.placeBlock((x-13,y+6,z+10),Block(y_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+6+yy,z+10),Block(e_id))
        for yy in range(3):
            editor.placeBlock((x-8,y+6+yy,z+10),Block(e_id))
            editor.placeBlock((x-10,y+6+yy,z+10),Block(e_id))
        for yy in range(2):
             editor.placeBlock((x-11,y+6+yy,z+10),Block(e_id))
             editor.placeBlock((x-7,y+6+yy,z+10),Block(e_id))
    editor.placeBlock((x-12,y+6,z+10),Block(e_id))
    editor.placeBlock((x-6,y+6,z+10),Block(e_id))
    for zz in range(4):
        editor.placeBlock((x-5,y+7,z+2+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-6,y+7,z+2+2*zz),Block(y_id))
        editor.placeBlock((x-7,y+8,z+2+2*zz),Block(y_id))
        editor.placeBlock((x-8,y+9,z+2+2*zz),Block(y_id))
    editor.placeBlock((x-9,y+9,z+11),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((x-10,y+8,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-8,y+8,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-10,y+7,z+11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-8,y+7,z+11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-11,y+7,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-7,y+7,z+11),Block(p_id,{"type": "double"}))
    
    editor.placeBlock((x-12,y+6,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-6,y+6,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-13,y+6,z+11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+5,z+11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-5,y+6,z+11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+5,z+11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-14,y+5,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-4,y+5,z+11),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-15,y+5,z+11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-16,y+5,z+11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+5,z+11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+5,z+11),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-15,y+4,z+11),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-3,y+4,z+11),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((x-4,y+yy,z+11),Block(r_id))
        editor.placeBlock((x-14,y+yy,z+11),Block(r_id))
    for yy in range(7):
        editor.placeBlock((x-7,y+yy,z+11),Block(r_id))
        editor.placeBlock((x-11,y+yy,z+11),Block(r_id))
    for xx in range(9):
        editor.placeBlock((x-5-xx,y+4,z+11),Block(r_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+5+yy,z+11),Block(r_id))
    editor.placeBlock((x-8,y+6,z+11),Block(r_id))
    editor.placeBlock((x-10,y+6,z+11),Block(r_id))

    for zz in range(6):
        editor.placeBlock((x-4,y+5,z+2*zz),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((x-3,y+4,z+2*zz),Block(t_id,{"type": "top"}))
        editor.placeBlock((x-4,y+6,z+2*zz),Block(y_id))
        editor.placeBlock((x-3,y+5,z+2*zz),Block(y_id))
        editor.placeBlock((x-2,y+5,z+2*zz),Block(u_id))
        editor.placeBlock((x-3,y+6,z+2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-4,y+4,z+2*zz),Block(y_id))
    for zz in range(5):
        editor.placeBlock((x-4,y+5,z+1+2*zz),Block(y_id))
        editor.placeBlock((x-3,y+4,z+1+2*zz),Block(y_id))
        editor.placeBlock((x-4,y+4,z+1+2*zz),Block(o_id))
    for zz in range(9):
        editor.placeBlock((x-5,y+6,z+1+zz),Block(y_id))
        editor.placeBlock((x-6,y+6,z+1+zz),Block(y_id))
        editor.placeBlock((x-7,y+7,z+1+zz),Block(y_id))
        editor.placeBlock((x-8,y+8,z+1+zz),Block(y_id))

    editor.placeBlock((x-9,y+10,z),Block(y_id))
    editor.placeBlock((x-10,y+9,z),Block(y_id))
    editor.placeBlock((x-8,y+9,z),Block(y_id))
    editor.placeBlock((x-7,y+8,z),Block(y_id))
    editor.placeBlock((x-11,y+8,z),Block(y_id))
    for xx in range(2):
        editor.placeBlock((x-12-xx,y+7,z),Block(y_id))
        editor.placeBlock((x-5-xx,y+7,z),Block(y_id))
    editor.placeBlock((x-5,y+6,z),Block(y_id))
    editor.placeBlock((x-13,y+6,z),Block(y_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+6+yy,z),Block(e_id))
        for yy in range(3):
            editor.placeBlock((x-8,y+6+yy,z),Block(e_id))
            editor.placeBlock((x-10,y+6+yy,z),Block(e_id))
        for yy in range(2):
             editor.placeBlock((x-11,y+6+yy,z),Block(e_id))
             editor.placeBlock((x-7,y+6+yy,z),Block(e_id))
    editor.placeBlock((x-12,y+6,z),Block(e_id))
    editor.placeBlock((x-6,y+6,z),Block(e_id))
     
    editor.placeBlock((x-9,y+9,z-1),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((x-10,y+8,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-8,y+8,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-10,y+7,z-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-8,y+7,z-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-11,y+7,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-7,y+7,z-1),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((x-12,y+6,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-6,y+6,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-13,y+6,z-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-13,y+5,z-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-5,y+6,z-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-5,y+5,z-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-14,y+5,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-4,y+5,z-1),Block(p_id,{"type": "double"}))
    editor.placeBlock((x-15,y+5,z-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-16,y+5,z-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+5,z-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-2,y+5,z-1),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((x-15,y+4,z-1),Block(p_id,{"type": "top"}))
    editor.placeBlock((x-3,y+4,z-1),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((x-4,y+yy,z-1),Block(r_id))
        editor.placeBlock((x-14,y+yy,z-1),Block(r_id))
    for yy in range(7):
        editor.placeBlock((x-7,y+yy,z-1),Block(r_id))
        editor.placeBlock((x-11,y+yy,z-1),Block(r_id))
    for xx in range(9):
        editor.placeBlock((x-5-xx,y+4,z-1),Block(r_id))
    for yy in range(4):
        editor.placeBlock((x-9,y+5+yy,z-1),Block(r_id))
    editor.placeBlock((x-8,y+6,z-1),Block(r_id))
    editor.placeBlock((x-10,y+6,z-1),Block(r_id))
    for xx in range(7):
        editor.placeBlock((x-13+2*xx,y+3,z-12),Block(y_id))
    for xx in range(6):
        editor.placeBlock((x-12+2*xx,y+3,z-12),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-13+2*xx,y+3,z-13),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-11+2*xx,y+3,z-11),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-12+2*xx,y+2,z-11),Block(i_id,{"type": "top"}))
        editor.placeBlock((x-12+2*xx,y+2,z-13),Block(i_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((x-13,y+3,z-2-2*zz),Block(y_id))
        editor.placeBlock((x-13,y+3,z-3-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-12,y+3,z-2-2*zz),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((x-14,y+2,z-3-2*zz),Block(i_id,{"type": "top"}))
        editor.placeBlock((x-12,y+2,z-3-2*zz),Block(i_id,{"type": "top"}))
    for zz in range(6):
        editor.placeBlock((x-14,y+3,z-2-2*zz),Block(i_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((x+11+xx,y,z),Block(s_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
   
    for zz in range(3):
        editor.placeBlock((x,y,z-5-zz),Block(s_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    #light
    light(x-1,y,z+3)
    light(x+5,y,z+3)
    light(x+18,y,z+3)
    light(x+10,y,z+11)
    light(x+15,y,z+11)
    light(x+10,y,z+7)
    light(x+15,y,z+7)
    light(x-6,y,z+12)
    light(x-15,y,z+12)
    light(x+19,y,z-3)
    light(x+19,y,z-9)
    light(x+18,y,z-16)
    light(x+13,y,z-16)
    light(x+8,y,z-16)
    light(x+3,y,z-16)
    light(x-2,y,z-16)
    light(x-7,y,z-16)
    light(x-14,y,z-16)
    editor.placeBlock((x+17,y+6,z+3),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((x-7,y+2,z-13),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((x-14,y+2,z-8),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((x-14,y+2,z-4),Block("lantern",{"hanging": "true"}))
    #house1
    editor.placeBlock((x+5,y+8,z+1),Block("lantern"))
    editor.placeBlock((x+5,y+10,z-3),Block("lantern"))
    editor.placeBlock((x+5,y+10,z-9),Block("lantern"))
    editor.placeBlock((x+5,y+8,z-13),Block("lantern"))
    editor.placeBlock((x+11,y+8,z+1),Block("lantern"))
    editor.placeBlock((x+11,y+10,z-3),Block("lantern"))
    editor.placeBlock((x+11,y+10,z-9),Block("lantern"))
    editor.placeBlock((x+11,y+8,z-13),Block("lantern"))
    editor.placeBlock((x-1,y+9,z-1),Block("lantern"))
    editor.placeBlock((x-1,y+13,z-6),Block("lantern"))
    editor.placeBlock((x-1,y+9,z-11),Block("lantern"))
    editor.placeBlock((x+17,y+9,z-1),Block("lantern"))
    editor.placeBlock((x+17,y+13,z-6),Block("lantern"))
    editor.placeBlock((x+17,y+9,z-11),Block("lantern"))
    #house2
    editor.placeBlock((x-3,y+5,z+1),Block("lantern"))
    editor.placeBlock((x-3,y+5,z+9),Block("lantern"))
    editor.placeBlock((x-5,y+7,z+5),Block("lantern"))
    editor.placeBlock((x-9,y+10,z+11),Block("lantern"))
    editor.placeBlock((x-9,y+10,z-1),Block("lantern"))
    editor.placeBlock((x-13,y+7,z+5),Block("lantern"))
    editor.placeBlock((x-15,y+5,z+9),Block("lantern"))
    editor.placeBlock((x-15,y+5,z+1),Block("lantern"))


def window_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    editor.placeBlock((x,y+1,z+1),Block(w_id,{"facing": "west", "half": "top", "open": "true"}))
    editor.placeBlock((x+5,y+1,z-1),Block(w_id,{"facing": "east", "half": "top", "open": "true"}))
    for xx in range(3):
        editor.placeBlock((x-8-xx,y,z+11),Block(q_id))
        editor.placeBlock((x-8-xx,y,z+12),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
        editor.placeBlock((x-8-xx,y+3,z+12),Block(w_id,{"facing": "south", "half": "bottom"}))
        editor.placeBlock((x-8-xx,y+3,z+11),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-10+xx,y+1,z+11),Block(y_id))
    for xx in range(4):
        editor.placeBlock((x+1+xx,y+1,z+1),Block(q_id))
        editor.placeBlock((x+1+xx,y,z+1),Block(w_id,{"facing": "south", "half": "top"}))
        editor.placeBlock((x+1+xx,y+1,z+2),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
        editor.placeBlock((x+1+xx,y+5,z+1),Block(t_id,{"facing": "north", "lit": "false"}))
        editor.placeBlock((x+1+xx,y+2,z+1),Block(y_id))
        editor.placeBlock((x+1+xx,y+4,z+1),Block(u_id))
        for yy in range(3):
            editor.placeBlock((x+1+xx,y+2+yy,z),Block(r_id))
    for xx in range(2):
        editor.placeBlock((x+2+xx,y+5,z+2),Block(t_id,{"facing": "north", "lit": "false"}))
    for zz in range(30):
        for xx in range(35):
            editor.placeBlock((x-15+xx,y-1,z+12-zz),Block(i_id))
    for xx in range(6):
        editor.placeBlock((x+10+xx,y+5,z+4),Block(w_id,{"facing": "south", "half": "bottom"}))
        for zz in range(3):
            editor.placeBlock((x+10+xx,y+5,z+1+zz),Block(t_id,{"facing": "north", "lit": "false"}))
    for yy in range(5):
        editor.placeBlock((x+10,y+yy,z+3),Block(o_id))
        editor.placeBlock((x+15,y+yy,z+3),Block(o_id))
def niwa_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(4):
        editor.placeBlock((x+1+xx,y,z+11),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+1+xx,y,z+5),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+1+xx,y,z+12),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+1+xx,y,z+4),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
        for zz in range(3):
            editor.placeBlock((x+1+xx,y,z+7+zz),Block(q_id))
    editor.placeBlock((x+5,y,z+11),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    editor.placeBlock((x,y,z+11),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((x,y,z+5),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((x+5,y,z+5),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    for zz in range(3):
        editor.placeBlock((x+6,y,z+7+zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x-1,y,z+7+zz),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+7,y,z+7+zz),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
        editor.placeBlock((x-2,y,z+7+zz),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
    editor.placeBlock((x-1,y,z+6),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((x-1,y,z+10),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    editor.placeBlock((x+6,y,z+10),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    editor.placeBlock((x+6,y,z+6),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    for xx in range(2):
        editor.placeBlock((x+2+xx,y+1,z+8),Block(t_id))
    editor.placeBlock((x+3,y+1,z+9),Block(y_id))
    editor.placeBlock((x+1,y+1,z+9),Block(u_id))
    editor.placeBlock((x-8,y+1,z-6),Block(u_id))
    for zz in range(4):
        editor.placeBlock((x-6,y,z-8-zz),Block(i_id))
    editor.placeBlock((x-7,y,z-7),Block(i_id))
    editor.placeBlock((x-7,y,z-8),Block(i_id))
    editor.placeBlock((x-8,y,z-7),Block(i_id))
    for xx in range(5):
        editor.placeBlock((x-8-xx,y,z-6),Block(i_id))
    for yy in range(2):
        for xx in range(3):
            for zz in range(5):
                editor.placeBlock((x-10-xx,y-1-yy,z-7-zz),Block(o_id))
        for zz in range(4):
            editor.placeBlock((x-9,y-1-yy,z-8-zz),Block(o_id))
        for zz in range(3):
            editor.placeBlock((x-8,y-1-yy,z-9-zz),Block(o_id))
        for zz in range(2):
            editor.placeBlock((x-7,y-1-yy,z-10-zz),Block(o_id))
    editor.placeBlock((x-9,y-1,z-7),Block(p_id))
    editor.placeBlock((x-8,y-1,z-8),Block(p_id))
    editor.placeBlock((x-7,y-1,z-9),Block(p_id))
    editor.placeBlock((x-11,y,z-8),Block(a_id))
    editor.placeBlock((x-9,y,z-10),Block(a_id))
    for yy in range(12):
        editor.placeBlock((x-7,y+yy,z-9),Block(s_id))
    for yy in range(15):
        editor.placeBlock((x-8,y+yy,z-8),Block(s_id))
    for yy in range(13):
        editor.placeBlock((x-9,y+yy,z-7),Block(s_id))
    editor.placeBlock((x-1,y,z-1),Block("chiseled_stone_bricks"))
    editor.placeBlock((x-1,y+1,z-1),Block("lantern"))
    editor.placeBlock((x-1,y,z-11),Block("chiseled_stone_bricks"))
    editor.placeBlock((x-1,y+1,z-11),Block("lantern"))
    editor.placeBlock((x-12,y,z-1),Block("chiseled_stone_bricks"))
    editor.placeBlock((x-12,y+1,z-1),Block("lantern"))
    
    editor.placeBlock((x-13,y+4,z-12),Block("lantern"))
    editor.placeBlock((x-7,y+4,z-12),Block("lantern"))
    editor.placeBlock((x-13,y+4,z-6),Block("lantern"))


def kagu1_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((x+1+xx,y+7,z-1-zz),Block(q_id))
    for xx in range(7):
        for zz in range(9):
            editor.placeBlock((x-12+xx,y+5,z+1+zz),Block(q_id))
    for yy in range(2):
        for xx in range(4):
            editor.placeBlock((x+12+xx,y+1+yy,z-11),Block(w_id))
        for zz in range(3):
            editor.placeBlock((x+15,y+1+yy,z-8-zz),Block(w_id))
    for xx in range(2):
        editor.placeBlock((x+14+xx,y+3,z-11),Block(w_id))
    editor.placeBlock((x+15,y+3,z-10),Block(w_id))
    editor.placeBlock((x+15,y+1,z-7),Block(w_id))
    editor.placeBlock((x+11,y+1,z-11),Block(e_id))
    for yy in range(2):
        editor.placeBlock((x+11,y+2+yy,z-11),Block(r_id))
    editor.placeBlock((x+15,y+1,z-6),Block(e_id))
    for yy in range(2):
        editor.placeBlock((x+15,y+2+yy,z-6),Block(r_id))
    editor.placeBlock((x+13,y+1,z-9),Block(t_id))
    editor.placeBlock((x+15,y+4,z-11),Block(y_id))
    editor.placeBlock((x+15,y+3,z-9),Block(u_id,{"facing": "west"}))
    editor.placeBlock((x+15,y+3,z-7),Block(i_id,{"facing": "west"}))
    editor.placeBlock((x+15,y+2,z-7),Block(o_id))
    editor.placeBlock((x+15,y+3,z-8),Block(p_id))
    editor.placeBlock((x+13,y+3,z-11),Block(a_id))
    editor.placeBlock((x+12,y+3,z-11),Block(s_id,{"rotation": "8"}))
    for yy in range(4):
        editor.placeBlock((x+15,y+1+yy,z-5),Block(d_id))
        editor.placeBlock((x+11,y+1+yy,z-5),Block(d_id))
    for xx in range(3):
        editor.placeBlock((x+12+xx,y+1,z-5),Block(d_id))
        editor.placeBlock((x+12+xx,y+4,z-5),Block(d_id))
  
    editor.placeBlock((x+12,y+3,z-4),Block(f_id,{"facing": "south", "half": "upper", "hinge": "left"}))
    editor.placeBlock((x+12,y+2,z-4),Block(f_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+13,y+3,z-4),Block(f_id,{"facing": "south", "half": "upper", "hinge": "left"}))
    editor.placeBlock((x+13,y+2,z-4),Block(f_id,{"facing": "south", "half": "lower", "hinge": "left"}))
    editor.placeBlock((x+14,y+3,z-4),Block(f_id,{"facing": "south", "half": "upper", "hinge": "right"}))
    editor.placeBlock((x+14,y+2,z-4),Block(f_id,{"facing": "south", "half": "lower", "hinge": "right"}))
    editor.placeBlock((x+14,y+5,z-5),Block(y_id))
    editor.placeBlock((x+12,y+5,z-5),Block(g_id))
    for zz in range(2):
        editor.placeBlock((x+15,y+3,z-2-zz),Block(d_id,{"facing": "west"}))
        editor.placeBlock((x+15,y+1,z-2-zz),Block(d_id,{"facing": "west"}))
    editor.placeBlock((x+15,y+4,z-2),Block(y_id))
    editor.placeBlock((x+15,y+4,z-3),Block(p_id))
    editor.placeBlock((x+6,y+6,z-3),Block(y_id,{"hanging": "true"}))
    editor.placeBlock((x-12,y+1,z+8),Block(y_id))
    editor.placeBlock((x-6,y+4,z+9),Block(y_id))
    editor.placeBlock((x-6,y+4,z+1),Block(y_id))
    editor.placeBlock((x-12,y+4,z+1),Block(y_id))
    #���Ɩ�
    editor.placeBlock((x+11,y+1,z-7),Block("white_carpet"))
    editor.placeBlock((x+11,y,z-7),Block("glowstone"))
    editor.placeBlock((x+12,y,z-7),Block("black_wool"))
    editor.placeBlock((x+14,y,z-7),Block("black_wool"))
    editor.placeBlock((x+11,y,z-8),Block("black_wool"))
    editor.placeBlock((x+11,y,z-10),Block("black_wool"))
    editor.placeBlock((x+13,y,z-8),Block("white_wool"))
    editor.placeBlock((x+12,y,z-9),Block("white_wool"))
    editor.placeBlock((x+14,y,z-9),Block("white_wool"))
    editor.placeBlock((x+13,y,z-10),Block("white_wool"))

    editor.placeBlock((x+13,y,z-7),Block("light_gray_wool"))
    editor.placeBlock((x+11,y,z-9),Block("light_gray_wool"))
    editor.placeBlock((x+12,y,z-8),Block("light_gray_wool"))
    editor.placeBlock((x+14,y,z-8),Block("light_gray_wool"))
    editor.placeBlock((x+12,y,z-10),Block("light_gray_wool"))
    editor.placeBlock((x+14,y,z-10),Block("light_gray_wool"))
    #���֏Ɩ�
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((x+11+xx,y+1,z-2+zz),Block("red_carpet"))
    editor.placeBlock((x+12,y,z-1),Block("glowstone"))
    editor.placeBlock((x+13,y,z-1),Block("glowstone"))





def kitchen_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for yy in range(3):
        editor.placeBlock((x+15,y+1+yy,z-1),Block(q_id,{"facing": "south", "half": "top", "open": "true"}))
        editor.placeBlock((x+15,y+1+yy,z-4),Block(q_id,{"facing": "north", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+9,y+1+yy,z-11),Block(q_id,{"facing": "east", "half": "top", "open": "true"}))
        editor.placeBlock((x+7,y+1+yy,z-11),Block(q_id,{"facing": "west", "half": "top", "open": "true"}))
    for zz in range(2):
        editor.placeBlock((x+15,y+2,z-2-zz),Block(p_id,{"facing": "east", "half": "top", "shape": "straight"}))
    for xx in range(2):
        editor.placeBlock((x+1+xx,y+1,z-11),Block(w_id,{"facing": "south"}))
    editor.placeBlock((x+1,y+1,z-10),Block(e_id,{"facing": "east"}))
    editor.placeBlock((x+1,y+1,z-9),Block(r_id,{"facing": "east"}))
    editor.placeBlock((x+7+xx,y+2,z-11),Block(p_id,{"facing": "north", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+7+xx,y+1,z-11),Block(t_id,{"facing": "south"}))
    editor.placeBlock((x+7+xx,y+3,z-11),Block(t_id,{"facing": "south"}))
    for xx in range(4):
        editor.placeBlock((x+3+xx,y+1,z-11),Block(r_id,{"facing": "south"}))
    for yy in range(2):
        editor.placeBlock((x+6,y+1+yy,z-11),Block(t_id,{"facing": "south"}))
    editor.placeBlock((x+5,y+4,z-11),Block(t_id,{"facing": "south"}))
    for zz in range(2):
        editor.placeBlock((x+1,y+4,z-9-2*zz),Block(t_id,{"facing": "east"}))
        editor.placeBlock((x+1,y+3,z-9-zz),Block(q_id,{"facing": "east", "half": "top"}))
    for xx in range(5):
        editor.placeBlock((x+1+xx,y+3,z-11),Block(q_id,{"facing": "south", "half": "top"}))
    editor.placeBlock((x+4,y+6,z-9),Block(y_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+4,z-11),Block(y_id))
    editor.placeBlock((x+9,y+6,z-11),Block(y_id,{"hanging": "true"}))
    editor.placeBlock((x+4,y+4,z-11),Block(u_id,{"facing": "south", "type": "single"}))
    editor.placeBlock((x+1,y+4,z-10),Block(u_id,{"facing": "east", "type": "single"}))
    editor.placeBlock((x+2,y+4,z-11),Block(i_id))
    editor.placeBlock((x+5,y+2,z-11),Block(o_id,{"facing": "north"}))
    for xx in range(3):
        editor.placeBlock((x+2+xx,y+1,z-8),Block(a_id,{"axis": "x"}))
    editor.placeBlock((x+1,y+1,z-8),Block(s_id))
    editor.placeBlock((x+1,y+2,z-8),Block(d_id))
    editor.placeBlock((x+3,y+2,z-11),Block(f_id))
    editor.placeBlock((x+3,y+2,z-8),Block(g_id))
    editor.placeBlock((x+1,y+4,z-4),Block(q_id,{"half": "top"}))
    editor.placeBlock((x+1,y+3,z-3),Block(q_id,{"half": "top"}))
    editor.placeBlock((x+1,y+2,z-2),Block(q_id,{"half": "top"}))
    for xx in range(2):
        for zz in range(3):
            editor.placeBlock((x+1+xx,y+1,z-5-zz),Block("orange_carpet"))
    editor.placeBlock((x+1,y,z-6),Block("glowstone"))




def table_n(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for xx in range(3):
        editor.placeBlock((x+5+xx,y+1,z-4),Block(q_id))
        editor.placeBlock((x+5+xx,y+1,z-2),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+5+xx,y+1,z-1),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((x+5+xx,y+1,z-3),Block("white_carpet"))
    editor.placeBlock((x+6,y,z-3),Block("glowstone"))
    editor.placeBlock((x+4,y+1,z-2),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
    editor.placeBlock((x+8,y+1,z-2),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
    editor.placeBlock((x+1,y+5,z-4),Block(r_id))
    editor.placeBlock((x+1,y+4,z-3),Block(t_id))
    editor.placeBlock((x+1,y+3,z-2),Block(y_id))
    editor.placeBlock((x+6,y+2,z-4),Block(u_id))


def bed_n(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for zz in range(3):
        editor.placeBlock((x-12,y,z+7+zz),Block(q_id,{"axis": "z"}))
        editor.placeBlock((x-9,y,z+7+zz),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-10,y,z+7+zz),Block(w_id,{"facing": "west", "part": "foot"}))
        command = f"summon panda {x-10} {y+2} {z+7-zz}"
        runCommand(command)
        runCommand(command)
        runCommand(command)
    for yy in range(3):
        for zz in range(2):
            editor.placeBlock((x-6,y+yy,z+8-zz),Block(r_id))
    for yy in range(2):
        editor.placeBlock((x-6,y+yy,z+7),Block(r_id))
    editor.placeBlock((x-12,y+1,z+9),Block(t_id))
    for xx in range(5):
        for zz in range(3):
            editor.placeBlock((x-7-xx,y,z+1+zz),Block("light_blue_carpet"))
    editor.placeBlock((x-9,y-1,z+2),Block("glowstone"))

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
        for zz in range(3):
            editor.placeBlock((z-5-zz,y+yy,x),Block(a_id))

 
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
            pass
    for xx in range(7):
        editor.placeBlock((z-7,y+12,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-8,y+11,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-9,y+10,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-11,y+9,x+2+2*xx),Block(y_id))
        editor.placeBlock((z-10,y+10,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-12,y+9,x+2+2*xx),Block(i_id,{"type": "bottom"}))
       
    ##house2
    for yy in range(3):
        for xx in range(4):            
            editor.placeBlock((z,y+yy,x-1-xx),Block(e_id))
        for xx in range(13):
            editor.placeBlock((z-12,y+yy,x-1-xx),Block(e_id))
        for zz in range(11):
            editor.placeBlock((z-1-zz,y+yy,x-13),Block(e_id))
    for xx in range(9):
        editor.placeBlock((z,y,x-5-xx),Block(q_id))
        editor.placeBlock((z+10,y,x-5-xx),Block(q_id))
        for yy in range(5):
            editor.placeBlock((z,y+1+yy,x-5-xx),Block(e_id))
            editor.placeBlock((z+10,y+1+yy,x-5-xx),Block(e_id))
    for zz in range(9):
        editor.placeBlock((z+1+zz,y,x-5),Block(q_id))
        editor.placeBlock((z+1+zz,y,x-13),Block(q_id))
        for yy in range(5):
            editor.placeBlock((z+1+zz,y+1+yy,x-5),Block(e_id))
            editor.placeBlock((z+1+zz,y+1+yy,x-13),Block(e_id))
    for xx in range(3):
        for yy in range(3):
            editor.placeBlock((z,y+yy,x-8-xx),Block(a_id))
        for yy in range(2):
            editor.placeBlock((z+10,y+1+yy,x-8-xx),Block(a_id))

 
    for zz in range(6):
        editor.placeBlock((z+2*zz,y+5,x-14),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x-15),Block(t_id,{"type": "top"}))
        editor.placeBlock((z+2*zz,y+6,x-14),Block(y_id))
        editor.placeBlock((z+2*zz,y+5,x-15),Block(y_id))
        editor.placeBlock((z+2*zz,y+5,x-16),Block(u_id))
        editor.placeBlock((z+2*zz,y+6,x-15),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x-14),Block(y_id))
    for zz in range(5):
        editor.placeBlock((z+1+2*zz,y+5,x-14),Block(y_id))
        editor.placeBlock((z+1+2*zz,y+4,x-15),Block(y_id))
        editor.placeBlock((z+1+2*zz,y+10,x-9),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+1+2*zz,y+4,x-14),Block(o_id))
    for zz in range(9):
        editor.placeBlock((z+1+zz,y+6,x-13),Block(y_id))
        editor.placeBlock((z+1+zz,y+6,x-12),Block(y_id))
        editor.placeBlock((z+1+zz,y+7,x-11),Block(y_id))
        editor.placeBlock((z+1+zz,y+8,x-10),Block(y_id))
        editor.placeBlock((z+1+zz,y+9,x-9),Block(y_id))
    for zz in range(4):
        editor.placeBlock((z+2+2*zz,y+7,x-13),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+2+2*zz,y+7,x-12),Block(y_id))
        editor.placeBlock((z+2+2*zz,y+8,x-11),Block(y_id))
        editor.placeBlock((z+2+2*zz,y+9,x-10),Block(y_id))
        editor.placeBlock((z+2+2*zz,y+10,x-9),Block(y_id))
   

 
    editor.placeBlock((z+10,y+10,x-9),Block(y_id))
    editor.placeBlock((z+10,y+9,x-10),Block(y_id))
    editor.placeBlock((z+10,y+9,x-8),Block(y_id))
    editor.placeBlock((z+10,y+8,x-7),Block(y_id))
    editor.placeBlock((z+10,y+8,x-11),Block(y_id))
    for xx in range(2):
        editor.placeBlock((z+10,y+7,x-12-xx),Block(y_id))
        editor.placeBlock((z+10,y+7,x-5-xx),Block(y_id))
    editor.placeBlock((z+10,y+6,x-5),Block(y_id))
    editor.placeBlock((z+10,y+6,x-13),Block(y_id))
    for yy in range(4):
        editor.placeBlock((z+10,y+6+yy,x-9),Block(e_id))
        for yy in range(3):
            editor.placeBlock((z+10,y+6+yy,x-8),Block(e_id))
            editor.placeBlock((z+10,y+6+yy,x-10),Block(e_id))
        for yy in range(2):
             editor.placeBlock((z+10,y+6+yy,x-11),Block(e_id))
             editor.placeBlock((z+10,y+6+yy,x-7),Block(e_id))
    editor.placeBlock((z+10,y+6,x-12),Block(e_id))
    editor.placeBlock((z+10,y+6,x-6),Block(e_id))
    for zz in range(4):
        editor.placeBlock((z+2+2*zz,y+7,x-5),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+2+2*zz,y+7,x-6),Block(y_id))
        editor.placeBlock((z+2+2*zz,y+8,x-7),Block(y_id))
        editor.placeBlock((z+2+2*zz,y+9,x-8),Block(y_id))
    editor.placeBlock((z+11,y+9,x-9),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((z+11,y+8,x-10),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+8,x-8),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+7,x-10),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+7,x-8),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+7,x-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+7,x-7),Block(p_id,{"type": "double"}))
    
    editor.placeBlock((z+11,y+6,x-12),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+6,x-6),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+6,x-13),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+11,y+5,x-13),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+6,x-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+11,y+5,x-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+5,x-14),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+5,x-4),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+11,y+5,x-15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+11,y+5,x-16),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+11,y+5,x-3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+11,y+5,x-2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+11,y+4,x-15),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+11,y+4,x-3),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((z+11,y+yy,x-4),Block(r_id))
        editor.placeBlock((z+11,y+yy,x-14),Block(r_id))
    for yy in range(7):
        editor.placeBlock((z+11,y+yy,x-7),Block(r_id))
        editor.placeBlock((z+11,y+yy,x-11),Block(r_id))
    for xx in range(9):
        editor.placeBlock((z+11,y+4,x-5-xx),Block(r_id))
    for yy in range(4):
        editor.placeBlock((z+11,y+5+yy,x-9),Block(r_id))
    editor.placeBlock((z+11,y+6,x-8),Block(r_id))
    editor.placeBlock((z+11,y+6,x-10),Block(r_id))

    for zz in range(6):
        editor.placeBlock((z+2*zz,y+5,x-4),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x-3),Block(t_id,{"type": "top"}))
        editor.placeBlock((z+2*zz,y+6,x-4),Block(y_id))
        editor.placeBlock((z+2*zz,y+5,x-3),Block(y_id))
        editor.placeBlock((z+2*zz,y+5,x-2),Block(u_id))
        editor.placeBlock((z+2*zz,y+6,x-3),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+2*zz,y+4,x-4),Block(y_id))
    for zz in range(5):
        editor.placeBlock((z+1+2*zz,y+4,x-3),Block(y_id))
        editor.placeBlock((z+1+2*zz,y+4,x-4),Block(o_id))
        editor.placeBlock((z+1+2*zz,y+5,x-4),Block(y_id))
    for zz in range(9):
        editor.placeBlock((z+1+zz,y+6,x-5),Block(y_id))
        editor.placeBlock((z+1+zz,y+6,x-6),Block(y_id))
        editor.placeBlock((z+1+zz,y+7,x-7),Block(y_id))
        editor.placeBlock((z+1+zz,y+8,x-8),Block(y_id))

    editor.placeBlock((z,y+10,x-9),Block(y_id))
    editor.placeBlock((z,y+9,x-10),Block(y_id))
    editor.placeBlock((z,y+9,x-8),Block(y_id))
    editor.placeBlock((z,y+8,x-7),Block(y_id))
    editor.placeBlock((z,y+8,x-11),Block(y_id))
    for xx in range(2):
        editor.placeBlock((z,y+7,x-12-xx),Block(y_id))
        editor.placeBlock((z,y+7,x-5-xx),Block(y_id))
    editor.placeBlock((z,y+6,x-5),Block(y_id))
    editor.placeBlock((z,y+6,x-13),Block(y_id))
    for yy in range(4):
        editor.placeBlock((z,y+6+yy,x-9),Block(e_id))
        for yy in range(3):
            editor.placeBlock((z,y+6+yy,x-8),Block(e_id))
            editor.placeBlock((z,y+6+yy,x-10),Block(e_id))
        for yy in range(2):
             editor.placeBlock((z,y+6+yy,x-11),Block(e_id))
             editor.placeBlock((z,y+6+yy,x-7),Block(e_id))
    editor.placeBlock((z,y+6,x-12),Block(e_id))
    editor.placeBlock((z,y+6,x-6),Block(e_id))
     
    editor.placeBlock((z-1,y+9,x-9),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((z-1,y+8,x-10),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+8,x-8),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x-10),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+7,x-8),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+7,x-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+7,x-7),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((z-1,y+6,x-12),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+6,x-6),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+6,x-13),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-1,y+5,x-13),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+6,x-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-1,y+5,x-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+5,x-14),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+5,x-4),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-1,y+5,x-15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-1,y+5,x-16),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-1,y+5,x-3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-1,y+5,x-2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-1,y+4,x-15),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-1,y+4,x-3),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((z-1,y+yy,x-4),Block(r_id))
        editor.placeBlock((z-1,y+yy,x-14),Block(r_id))
    for yy in range(7):
        editor.placeBlock((z-1,y+yy,x-7),Block(r_id))
        editor.placeBlock((z-1,y+yy,x-11),Block(r_id))
    for xx in range(9):
        editor.placeBlock((z-1,y+4,x-5-xx),Block(r_id))
    for yy in range(4):
        editor.placeBlock((z-1,y+5+yy,x-9),Block(r_id))
    editor.placeBlock((z-1,y+6,x-8),Block(r_id))
    editor.placeBlock((z-1,y+6,x-10),Block(r_id))
    for xx in range(7):
        editor.placeBlock((z-12,y+3,x-13+2*xx),Block(y_id))
    for xx in range(6):
        editor.placeBlock((z-12,y+3,x-12+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-13,y+3,x-13+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-11,y+3,x-11+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-11,y+2,x-12+2*xx),Block(i_id,{"type": "top"}))
        editor.placeBlock((z-13,y+2,x-12+2*xx),Block(i_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((z-2-2*zz,y+3,x-13),Block(y_id))
        editor.placeBlock((z-3-2*zz,y+3,x-13),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-2-2*zz,y+3,x-12),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-3-2*zz,y+2,x-14),Block(i_id,{"type": "top"}))
        editor.placeBlock((z-3-2*zz,y+2,x-12),Block(i_id,{"type": "top"}))
    for zz in range(6):
        editor.placeBlock((z-2-2*zz,y+3,x-14),Block(i_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((z,y,x+11+xx),Block(s_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
   
    for zz in range(3):
        editor.placeBlock((z-5-zz,y,x),Block(s_id,{"facing": "south", "half": "bottom", "shape": "straight"}))

    #light
    light(z+3,y,x-1) 
    light(z+3,y,x+5)
    light(z+3,y,x+18)
    light(z+11,y,x+10)
    light(z+11,y,x+15)
    light(z+7,y,x+10)
    light(z+7,y,x+15)
    light(z+12,y,x-6)
    light(z+12,y,x-15)
    light(z-3,y,x+19)
    light(z-9,y,x+19)
    light(z-16,y,x+18)
    light(z-16,y,x+13)
    light(z-16,y,x+8)
    light(z-16,y,x+3)
    light(z-16,y,x-2)
    light(z-16,y,x-7)
    light(z-16,y,x-14)
    editor.placeBlock((z+3,y+6,x+17),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((z-13,y+2,x-7),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((z-8,y+2,x-14),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((z-4,y+2,x-14),Block("lantern",{"hanging": "true"}))
    #house1
    editor.placeBlock((z+1,y+8,x+5),Block("lantern"))
    editor.placeBlock((z-3,y+10,x+5),Block("lantern"))
    editor.placeBlock((z-9,y+10,x+5),Block("lantern"))
    editor.placeBlock((z-13,y+8,x+5),Block("lantern"))
    editor.placeBlock((z+1,y+8,x+11),Block("lantern"))
    editor.placeBlock((z-3,y+10,x+11),Block("lantern"))
    editor.placeBlock((z-9,y+10,x+11),Block("lantern"))
    editor.placeBlock((z-13,y+8,x+11),Block("lantern"))
    editor.placeBlock((z-1,y+9,x-1),Block("lantern"))
    editor.placeBlock((z-6,y+13,x-1),Block("lantern"))
    editor.placeBlock((z-11,y+9,x-1),Block("lantern"))
    editor.placeBlock((z-1,y+9,x+17),Block("lantern"))
    editor.placeBlock((z-6,y+13,x+17),Block("lantern"))
    editor.placeBlock((z-11,y+9,x+17),Block("lantern"))
    editor.placeBlock((z-6,y+14,x+8),Block("lantern"))   
    #house2
    editor.placeBlock((z+1,y+5,x-3),Block("lantern"))
    editor.placeBlock((z+9,y+5,x-3),Block("lantern"))
    editor.placeBlock((z+5,y+7,x-5),Block("lantern"))
    editor.placeBlock((z+11,y+10,x-9),Block("lantern"))
    editor.placeBlock((z-1,y+10,x-9),Block("lantern"))
    editor.placeBlock((z+5,y+7,x-13),Block("lantern"))
    editor.placeBlock((z+9,y+5,x-15),Block("lantern"))
    editor.placeBlock((z+1,y+5,x-15),Block("lantern"))






def window_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    editor.placeBlock((z+1,y+1,x),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
    editor.placeBlock((z-1,y+1,x+5),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
    for xx in range(3):
        editor.placeBlock((z+11,y,x-8-xx),Block(q_id))
        editor.placeBlock((z+12,y,x-8-xx),Block(w_id,{"facing": "east", "half": "top", "open": "true"}))
        editor.placeBlock((z+12,y+3,x-8-xx),Block(w_id,{"facing": "east", "half": "bottom"}))
        editor.placeBlock((z+11,y+3,x-8-xx),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+11,y+1,x-10+xx),Block(y_id))
    for xx in range(4):
        editor.placeBlock((z+1,y+1,x+1+xx),Block(q_id))
        editor.placeBlock((z+1,y,x+1+xx),Block(w_id,{"facing": "east", "half": "top"}))
        editor.placeBlock((z+2,y+1,x+1+xx),Block(w_id,{"facing": "east", "half": "top", "open": "true"}))
        editor.placeBlock((z+1,y+5,x+1+xx),Block(t_id,{"facing": "west", "lit": "false"}))
        editor.placeBlock((z+1,y+2,x+1+xx),Block(y_id))
        editor.placeBlock((z+1,y+4,x+1+xx),Block(u_id))
        for yy in range(3):
            editor.placeBlock((z,y+2+yy,x+1+xx),Block(r_id))
    for xx in range(2):
        editor.placeBlock((z+2,y+5,x+2+xx),Block(t_id,{"facing": "east", "lit": "false"}))
    for zz in range(30):
        for xx in range(35):
            editor.placeBlock((z+12-zz,y-1,x-15+xx),Block(i_id))
    for xx in range(6):
        editor.placeBlock((z+4,y+5,x+10+xx),Block(w_id,{"facing": "east", "half": "bottom"}))
        for zz in range(3):
            editor.placeBlock((z+1+zz,y+5,x+10+xx),Block(t_id,{"facing": "east", "lit": "false"}))
    for yy in range(5):
        editor.placeBlock((z+3,y+yy,x+10),Block(o_id))
        editor.placeBlock((z+3,y+yy,x+15),Block(o_id))
def niwa_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(4):
        editor.placeBlock((z+11,y,x+1+xx),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+5,y,x+1+xx),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+12,y,x+1+xx),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
        editor.placeBlock((z+4,y,x+1+xx),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
        for zz in range(3):
            editor.placeBlock((z+7+zz,y,x+1+xx),Block(q_id))
    editor.placeBlock((z+11,y,x+5),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    editor.placeBlock((z+11,y,x),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((z+5,y,x),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((z+5,y,x+5),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    for zz in range(3):
        editor.placeBlock((z+7+zz,y,x+6),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+7+zz,y,x-1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+7+zz,y,x+7),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((z+7+zz,y,x-2),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
    editor.placeBlock((z+6,y,x-1),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((z+10,y,x-1),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    editor.placeBlock((z+10,y,x+6),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    editor.placeBlock((z+6,y,x+6),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    for xx in range(2):
        editor.placeBlock((z+8,y+1,x+2+xx),Block(t_id))
    editor.placeBlock((z+9,y+1,x+3),Block(y_id))
    editor.placeBlock((z+9,y+1,x+1),Block(u_id))
    editor.placeBlock((z-6,y+1,x-8),Block(u_id))
    for zz in range(4):
        editor.placeBlock((z-8-zz,y,x-6),Block(i_id))
    editor.placeBlock((z-7,y,x-7),Block(i_id))
    editor.placeBlock((z-8,y,x-7),Block(i_id))
    editor.placeBlock((z-7,y,x-8),Block(i_id))
    for xx in range(5):
        editor.placeBlock((z-6,y,x-8-xx),Block(i_id))
    for yy in range(2):
        for xx in range(3):
            for zz in range(5):
                editor.placeBlock((z-7-zz,y-1-yy,x-10-xx),Block(o_id))
        for zz in range(4):
            editor.placeBlock((z-8-zz,y-1-yy,x-9),Block(o_id))
        for zz in range(3):
            editor.placeBlock((z-9-zz,y-1-yy,x-8),Block(o_id))
        for zz in range(2):
            editor.placeBlock((z-10-zz,y-1-yy,x-7),Block(o_id))
    editor.placeBlock((z-7,y-1,x-9),Block(p_id))
    editor.placeBlock((z-8,y-1,x-8),Block(p_id))
    editor.placeBlock((z-9,y-1,x-7),Block(p_id))
    editor.placeBlock((z-8,y,x-11),Block(a_id))
    editor.placeBlock((z-10,y,x-9),Block(a_id))
    for yy in range(12):
        editor.placeBlock((z-9,y+yy,x-7),Block(s_id))
    for yy in range(15):
        editor.placeBlock((z-8,y+yy,x-8),Block(s_id))
    for yy in range(13):
        editor.placeBlock((z-7,y+yy,x-9),Block(s_id))
    editor.placeBlock((z-1,y,x-1),Block("chiseled_stone_bricks"))
    editor.placeBlock((z-1,y+1,x-1),Block("lantern"))
    editor.placeBlock((z-11,y,x-1),Block("chiseled_stone_bricks"))
    editor.placeBlock((z-11,y+1,x-1),Block("lantern"))
    editor.placeBlock((z-1,y,x-12),Block("chiseled_stone_bricks"))
    editor.placeBlock((z-1,y+1,x-12),Block("lantern"))
    
    editor.placeBlock((z-12,y+4,x-13),Block("lantern"))
    editor.placeBlock((z-12,y+4,x-7),Block("lantern"))
    editor.placeBlock((z-6,y+4,x-13),Block("lantern"))

def kagu1_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((z-1-zz,y+7,x+1+xx),Block(q_id))
    for xx in range(7):
        for zz in range(9):
            editor.placeBlock((z+1+zz,y+5,x-12+xx),Block(q_id))
    for yy in range(2):
        for xx in range(4):
            editor.placeBlock((z-11,y+1+yy,x+12+xx),Block(w_id))
        for zz in range(3):
            editor.placeBlock((z-8-zz,y+1+yy,x+15),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z-11,y+3,x+14+xx),Block(w_id))
    editor.placeBlock((z-10,y+3,x+15),Block(w_id))
    editor.placeBlock((z-7,y+1,x+15),Block(w_id))
    editor.placeBlock((z-11,y+1,x+11),Block(e_id))
    for yy in range(2):
        editor.placeBlock((z-11,y+2+yy,x+11),Block(r_id))
    editor.placeBlock((z-6,y+1,x+15),Block(e_id))
    for yy in range(2):
        editor.placeBlock((z-6,y+2+yy,x+15),Block(r_id))
    editor.placeBlock((z-9,y+1,x+13),Block(t_id))
    editor.placeBlock((z-11,y+4,x+15),Block(y_id))
    editor.placeBlock((z-9,y+3,x+15),Block(u_id,{"facing": "north"}))
    editor.placeBlock((z-7,y+3,x+15),Block(i_id,{"facing": "north"}))
    editor.placeBlock((z-7,y+2,x+15),Block(o_id))
    editor.placeBlock((z-8,y+3,x+15),Block(p_id))
    editor.placeBlock((z-11,y+3,x+13),Block(a_id))
    editor.placeBlock((z-11,y+3,x+12),Block(s_id,{"rotation":"4"}))
    for yy in range(4):
        editor.placeBlock((z-5,y+1+yy,x+15),Block(d_id))
        editor.placeBlock((z-5,y+1+yy,x+11),Block(d_id))
    for xx in range(3):
        editor.placeBlock((z-5,y+1,x+12+xx),Block(d_id))
        editor.placeBlock((z-5,y+4,x+12+xx),Block(d_id))
  
    editor.placeBlock((z-4,y+3,x+12),Block(f_id,{"facing": "east", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z-4,y+2,x+12),Block(f_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z-4,y+3,x+13),Block(f_id,{"facing": "east", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z-4,y+2,x+13),Block(f_id,{"facing": "east", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z-4,y+3,x+14),Block(f_id,{"facing": "east", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z-4,y+2,x+14),Block(f_id,{"facing": "east", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z-5,y+5,x+14),Block(y_id))
    editor.placeBlock((z-5,y+5,x+12),Block(g_id))
    for zz in range(2):
        editor.placeBlock((z-2-zz,y+3,x+15),Block(d_id,{"facing": "north"}))
        editor.placeBlock((z-2-zz,y+1,x+15),Block(d_id,{"facing": "north"}))
    editor.placeBlock((z-2,y+4,x+15),Block(y_id))
    editor.placeBlock((z-3,y+4,x+15),Block(p_id))
    editor.placeBlock((z-3,y+6,x+6),Block(y_id))
    editor.placeBlock((z+8,y+1,x-12),Block(y_id))
    editor.placeBlock((z+9,y+4,x-6),Block(y_id))
    editor.placeBlock((z+1,y+4,x-6),Block(y_id))
    editor.placeBlock((z+1,y+4,x-12),Block(y_id))
    #enchant
    editor.placeBlock((z-7,y+1,x+11),Block("white_carpet"))
    editor.placeBlock((z-7,y,x+11),Block("glowstone"))
    editor.placeBlock((z-7,y,x+12),Block("black_wool"))
    editor.placeBlock((z-7,y,x+14),Block("black_wool"))
    editor.placeBlock((z-8,y,x+11),Block("black_wool"))
    editor.placeBlock((z-10,y,x+11),Block("black_wool"))
    editor.placeBlock((z-8,y,x+13),Block("white_wool"))
    editor.placeBlock((z-9,y,x+12),Block("white_wool"))
    editor.placeBlock((z-9,y,x+14),Block("white_wool"))
    editor.placeBlock((z-10,y,x+13),Block("white_wool"))

    editor.placeBlock((z-7,y,x+13),Block("light_gray_wool"))
    editor.placeBlock((z-9,y,x+11),Block("light_gray_wool"))
    editor.placeBlock((z-8,y,x+12),Block("light_gray_wool"))
    editor.placeBlock((z-8,y,x+14),Block("light_gray_wool"))
    editor.placeBlock((z-10,y,x+12),Block("light_gray_wool"))
    editor.placeBlock((z-10,y,x+14),Block("light_gray_wool"))
    #玄関
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((z-2+zz,y+1,x+11+xx),Block("red_carpet"))
    editor.placeBlock((z-1,y,x+12),Block("glowstone"))
    editor.placeBlock((z-1,y,x+13),Block("glowstone"))

    




def kitchen_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for yy in range(3):
        editor.placeBlock((z-1,y+1+yy,x+15),Block(q_id,{"facing": "east", "half": "top", "open": "true"}))
        editor.placeBlock((z-4,y+1+yy,x+15),Block(q_id,{"facing": "west", "half": "bottom", "open": "true"}))
        editor.placeBlock((z-11,y+1+yy,x+9),Block(q_id,{"facing": "south", "half": "top", "open": "true"}))
        editor.placeBlock((z-11,y+1+yy,x+7),Block(q_id,{"facing": "north", "half": "top", "open": "true"}))
    for zz in range(2):
        editor.placeBlock((z-2-zz,y+2,x+15),Block(p_id,{"facing": "south", "half": "top", "shape": "straight"}))
    for xx in range(2):
        editor.placeBlock((z-11,y+1,x+1+xx),Block(w_id,{"facing": "east"}))
    editor.placeBlock((z-10,y+1,x+1),Block(e_id,{"facing": "south"}))
    editor.placeBlock((z-9,y+1,x+1),Block(r_id,{"facing": "south"}))
    editor.placeBlock((z-11,y+2,x+7+xx),Block(p_id,{"facing": "south", "half": "top", "shape": "straight"}))
    editor.placeBlock((z-11,y+1,x+7+xx),Block(t_id,{"facing": "east"}))
    editor.placeBlock((z-11,y+3,x+7+xx),Block(t_id,{"facing": "east"}))
    for xx in range(4):
        editor.placeBlock((z-11,y+1,x+3+xx),Block(r_id,{"facing": "east"}))
    for yy in range(2):
        editor.placeBlock((z-11,y+1+yy,x+6),Block(t_id,{"facing": "east"}))
    editor.placeBlock((z-11,y+4,x+5),Block(t_id,{"facing": "east"}))
    for zz in range(2):
        editor.placeBlock((z-9-2*zz,y+4,x+1),Block(t_id,{"facing": "south"}))
        editor.placeBlock((z-9-zz,y+3,x+1),Block(q_id,{"facing": "east", "half": "top"}))
    for xx in range(5):
        editor.placeBlock((z-11,y+3,x+1+xx),Block(q_id,{"facing": "south", "half": "top"}))
    editor.placeBlock((z-9,y+6,x+4),Block(y_id))
    editor.placeBlock((z-11,y+4,x+3),Block(y_id))
    editor.placeBlock((z-11,y+6,x+9),Block(y_id))
    editor.placeBlock((z-11,y+4,x+4),Block(u_id,{"facing": "east", "type": "single"}))
    editor.placeBlock((z-10,y+4,x+1),Block(u_id,{"facing": "south", "type": "single"}))
    editor.placeBlock((z-11,y+4,x+2),Block(i_id))
    editor.placeBlock((z-11,y+2,x+5),Block(o_id,{"facing": "west"}))
    for xx in range(3):
        editor.placeBlock((z-8,y+1,x+2+xx),Block(a_id,{"axis": "x"}))
    editor.placeBlock((z-8,y+1,x+1),Block(s_id))
    editor.placeBlock((z-8,y+2,x+1),Block(d_id))
    editor.placeBlock((z-11,y+2,x+3),Block(f_id))
    editor.placeBlock((z-8,y+2,x+3),Block(g_id))
    editor.placeBlock((z-4,y+4,x+1),Block(q_id,{"half": "top"}))
    editor.placeBlock((z-3,y+3,x+1),Block(q_id,{"half": "top"}))
    editor.placeBlock((z-2,y+2,x+1),Block(q_id,{"half": "top"}))
    for xx in range(2):
        for zz in range(3):
            editor.placeBlock((z-5-zz,y+1,x+1+xx),Block("orange_carpet"))
    editor.placeBlock((z-6,y,x+1),Block("glowstone"))



def table_w(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for xx in range(3):
        editor.placeBlock((z-4,y+1,x+5+xx),Block(q_id))
        editor.placeBlock((z-2,y+1,x+5+xx),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-1,y+1,x+5+xx),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
    editor.placeBlock((z-2,y+1,x+4),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
    editor.placeBlock((z-2,y+1,x+8),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
    editor.placeBlock((z-4,y+5,x+1),Block(r_id))
    editor.placeBlock((z-3,y+4,x+1),Block(t_id))
    editor.placeBlock((z-2,y+3,x+1),Block(y_id))
    editor.placeBlock((z-4,y+2,x+6),Block(u_id))
def bed_w(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for zz in range(3):
        editor.placeBlock((z+7+zz,y,x-12),Block(q_id,{"axis": "z"}))
        editor.placeBlock((z+7+zz,y,x-9),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z+7+zz,y,x-10),Block(w_id,{"facing": "north", "part": "foot"}))
        command = f"summon panda {z+7-zz} {y+2} {x-10}"
        runCommand(command)
        runCommand(command)
        runCommand(command)
    for yy in range(3):
        for zz in range(2):
            editor.placeBlock((z+8-zz,y+yy,x-6),Block(r_id))
    for yy in range(2):
        editor.placeBlock((z+7,y+yy,x-6),Block(r_id))
    editor.placeBlock((z+9,y+1,x-12),Block(t_id))
    for xx in range(5):
        for zz in range(3):
            editor.placeBlock((z+1+zz,y,x-7-xx),Block("light_blue_carpet"))
    editor.placeBlock((z+2,y-1,x-9),Block("glowstone"))



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
    for yy in range(7):
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
            editor.placeBlock((z+3-zz,y+9,x+1+xx),Block(y_id))
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
            editor.placeBlock((z+9-zz,y+8+yy,x),Block(e_id))
            editor.placeBlock((z+2-zz,y+8+yy,x),Block(e_id))
    editor.placeBlock((z+1,y+8,x),Block(e_id))
    editor.placeBlock((z+11,y+8,x),Block(e_id))

    editor.placeBlock((z+6,y+13,x),Block(y_id))
    editor.placeBlock((z+5,y+12,x),Block(y_id))
    editor.placeBlock((z+7,y+12,x),Block(y_id))
    editor.placeBlock((z+4,y+11,x),Block(y_id))
    editor.placeBlock((z+8,y+11,x),Block(y_id))
    for zz in range(2):
        editor.placeBlock((z+2+zz,y+10,x),Block(y_id))
        editor.placeBlock((z+10-zz,y+10,x),Block(y_id))
        editor.placeBlock((z+zz,y+9,x),Block(y_id))
        editor.placeBlock((z+11-zz,y+9,x),Block(y_id))
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
        for zz in range(3):
            editor.placeBlock((z+7-zz,y+yy,x),Block(a_id))


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
            editor.placeBlock((z+10-zz,y+9,x+1+xx),Block(y_id))
    for xx in range(7):
        editor.placeBlock((z+7,y+12,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+8,y+11,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+9,y+10,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+11,y+9,x+2+2*xx),Block(y_id))
        editor.placeBlock((z+10,y+10,x+2+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+12,y+9,x+2+2*xx),Block(i_id,{"type": "bottom"}))
    ##house2
    for yy in range(3):
        for xx in range(4):            
            editor.placeBlock((z,y+yy,x-1-xx),Block(e_id))
        for xx in range(13):
            editor.placeBlock((z+12,y+yy,x-1-xx),Block(e_id))
        for zz in range(11):
            editor.placeBlock((z+1+zz,y+yy,x-13),Block(e_id))
    for xx in range(9):
        editor.placeBlock((z,y,x-5-xx),Block(q_id))
        editor.placeBlock((z-10,y,x-5-xx),Block(q_id))
        for yy in range(5):
            editor.placeBlock((z,y+1+yy,x-5-xx),Block(e_id))
            editor.placeBlock((z-10,y+1+yy,x-5-xx),Block(e_id))
    for zz in range(9):
        editor.placeBlock((z-1-zz,y,x-5),Block(q_id))
        editor.placeBlock((z-1-zz,y,x-13),Block(q_id))
        for yy in range(5):
            editor.placeBlock((z-1-zz,y+1+yy,x-5),Block(e_id))
            editor.placeBlock((z-1-zz,y+1+yy,x-13),Block(e_id))
    for xx in range(3):
        for yy in range(3):
            editor.placeBlock((z,y+yy,x-8-xx),Block(a_id))
        for yy in range(2):
            editor.placeBlock((z-10,y+1+yy,x-8-xx),Block(a_id))


    for zz in range(6):
        editor.placeBlock((z-2*zz,y+5,x-14),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z-2*zz,y+4,x-15),Block(t_id,{"type": "top"}))
        editor.placeBlock((z-2*zz,y+6,x-14),Block(y_id))
        editor.placeBlock((z-2*zz,y+5,x-15),Block(y_id))
        editor.placeBlock((z-2*zz,y+5,x-16),Block(u_id))
        editor.placeBlock((z-2*zz,y+6,x-15),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-2*zz,y+4,x-14),Block(y_id))
    for zz in range(5):
        editor.placeBlock((z-1-2*zz,y+5,x-14),Block(y_id))
        editor.placeBlock((z-1-2*zz,y+4,x-15),Block(y_id))
        editor.placeBlock((z-1-2*zz,y+10,x-9),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-1-2*zz,y+4,x-14),Block(o_id))
    for zz in range(9):
        editor.placeBlock((z-1-zz,y+6,x-13),Block(y_id))
        editor.placeBlock((z-1-zz,y+6,x-12),Block(y_id))
        editor.placeBlock((z-1-zz,y+7,x-11),Block(y_id))
        editor.placeBlock((z-1-zz,y+8,x-10),Block(y_id))
        editor.placeBlock((z-1-zz,y+9,x-9),Block(y_id))
    for zz in range(4):
        editor.placeBlock((z-2-2*zz,y+7,x-13),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-2-2*zz,y+7,x-12),Block(y_id))
        editor.placeBlock((z-2-2*zz,y+8,x-11),Block(y_id))
        editor.placeBlock((z-2-2*zz,y+9,x-10),Block(y_id))
        editor.placeBlock((z-2-2*zz,y+10,x-9),Block(y_id))
   


    editor.placeBlock((z-10,y+10,x-9),Block(y_id))
    editor.placeBlock((z-10,y+9,x-10),Block(y_id))
    editor.placeBlock((z-10,y+9,x-8),Block(y_id))
    editor.placeBlock((z-10,y+8,x-7),Block(y_id))
    editor.placeBlock((z-10,y+8,x-11),Block(y_id))
    for xx in range(2):
        editor.placeBlock((z-10,y+7,x-12-xx),Block(y_id))
        editor.placeBlock((z-10,y+7,x-5-xx),Block(y_id))
    editor.placeBlock((z-10,y+6,x-5),Block(y_id))
    editor.placeBlock((z-10,y+6,x-13),Block(y_id))
    for yy in range(4):
        editor.placeBlock((z-10,y+6+yy,x-9),Block(e_id))
        for yy in range(3):
            editor.placeBlock((z-10,y+6+yy,x-8),Block(e_id))
            editor.placeBlock((z-10,y+6+yy,x-10),Block(e_id))
        for yy in range(2):
             editor.placeBlock((z-10,y+6+yy,x-11),Block(e_id))
             editor.placeBlock((z-10,y+6+yy,x-7),Block(e_id))
    editor.placeBlock((z-10,y+6,x-12),Block(e_id))
    editor.placeBlock((z-10,y+6,x-6),Block(e_id))
    for zz in range(4):
        editor.placeBlock((z-2-2*zz,y+7,x-5),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-2-2*zz,y+7,x-6),Block(y_id))
        editor.placeBlock((z-2-2*zz,y+8,x-7),Block(y_id))
        editor.placeBlock((z-2-2*zz,y+9,x-8),Block(y_id))
    editor.placeBlock((z-11,y+9,x-9),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((z-11,y+8,x-10),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+8,x-8),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+7,x-10),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+7,x-8),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+7,x-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+7,x-7),Block(p_id,{"type": "double"}))
    
    editor.placeBlock((z-11,y+6,x-12),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+6,x-6),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+6,x-13),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-11,y+5,x-13),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+6,x-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-11,y+5,x-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+5,x-14),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+5,x-4),Block(p_id,{"type": "double"}))
    editor.placeBlock((z-11,y+5,x-15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-11,y+5,x-16),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-11,y+5,x-3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-11,y+5,x-2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z-11,y+4,x-15),Block(p_id,{"type": "top"}))
    editor.placeBlock((z-11,y+4,x-3),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((z-11,y+yy,x-4),Block(r_id))
        editor.placeBlock((z-11,y+yy,x-14),Block(r_id))
    for yy in range(7):
        editor.placeBlock((z-11,y+yy,x-7),Block(r_id))
        editor.placeBlock((z-11,y+yy,x-11),Block(r_id))
    for xx in range(9):
        editor.placeBlock((z-11,y+4,x-5-xx),Block(r_id))
    for yy in range(4):
        editor.placeBlock((z-11,y+5+yy,x-9),Block(r_id))
    editor.placeBlock((z-11,y+6,x-8),Block(r_id))
    editor.placeBlock((z-11,y+6,x-10),Block(r_id))

    for zz in range(6):
        editor.placeBlock((z-2*zz,y+5,x-4),Block(t_id,{"type": "bottom"}))
        editor.placeBlock((z-2*zz,y+4,x-3),Block(t_id,{"type": "top"}))
        editor.placeBlock((z-2*zz,y+6,x-4),Block(y_id))
        editor.placeBlock((z-2*zz,y+5,x-3),Block(y_id))
        editor.placeBlock((z-2*zz,y+5,x-2),Block(u_id))
        editor.placeBlock((z-2*zz,y+6,x-3),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z-2*zz,y+4,x-4),Block(y_id))
    for zz in range(5):
        editor.placeBlock((z-1-2*zz,y+5,x-4),Block(y_id))
        editor.placeBlock((z-1-2*zz,y+4,x-3),Block(y_id))
        editor.placeBlock((z-1-2*zz,y+4,x-4),Block(o_id))
    for zz in range(9):
        editor.placeBlock((z-1-zz,y+6,x-5),Block(y_id))
        editor.placeBlock((z-1-zz,y+6,x-6),Block(y_id))
        editor.placeBlock((z-1-zz,y+7,x-7),Block(y_id))
        editor.placeBlock((z-1-zz,y+8,x-8),Block(y_id))

    editor.placeBlock((z,y+10,x-9),Block(y_id))
    editor.placeBlock((z,y+9,x-10),Block(y_id))
    editor.placeBlock((z,y+9,x-8),Block(y_id))
    editor.placeBlock((z,y+8,x-7),Block(y_id))
    editor.placeBlock((z,y+8,x-11),Block(y_id))
    for xx in range(2):
        editor.placeBlock((z,y+7,x-12-xx),Block(y_id))
        editor.placeBlock((z,y+7,x-5-xx),Block(y_id))
    editor.placeBlock((z,y+6,x-5),Block(y_id))
    editor.placeBlock((z,y+6,x-13),Block(y_id))
    for yy in range(4):
        editor.placeBlock((z,y+6+yy,x-9),Block(e_id))
        for yy in range(3):
            editor.placeBlock((z,y+6+yy,x-8),Block(e_id))
            editor.placeBlock((z,y+6+yy,x-10),Block(e_id))
        for yy in range(2):
             editor.placeBlock((z,y+6+yy,x-11),Block(e_id))
             editor.placeBlock((z,y+6+yy,x-7),Block(e_id))
    editor.placeBlock((z,y+6,x-12),Block(e_id))
    editor.placeBlock((z,y+6,x-6),Block(e_id))
     
    editor.placeBlock((z+1,y+9,x-9),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((z+1,y+8,x-10),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+8,x-8),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+7,x-10),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+7,x-8),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+7,x-11),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+7,x-7),Block(p_id,{"type": "double"}))
   
    editor.placeBlock((z+1,y+6,x-12),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+6,x-6),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+6,x-13),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+1,y+5,x-13),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+6,x-5),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+1,y+5,x-5),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+5,x-14),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+5,x-4),Block(p_id,{"type": "double"}))
    editor.placeBlock((z+1,y+5,x-15),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+1,y+5,x-16),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+1,y+5,x-3),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+1,y+5,x-2),Block(p_id,{"type": "bottom"}))
    editor.placeBlock((z+1,y+4,x-15),Block(p_id,{"type": "top"}))
    editor.placeBlock((z+1,y+4,x-3),Block(p_id,{"type": "top"}))
    for yy in range(5):
        editor.placeBlock((z+1,y+yy,x-4),Block(r_id))
        editor.placeBlock((z+1,y+yy,x-14),Block(r_id))
    for yy in range(7):
        editor.placeBlock((z+1,y+yy,x-7),Block(r_id))
        editor.placeBlock((z+1,y+yy,x-11),Block(r_id))
    for xx in range(9):
        editor.placeBlock((z+1,y+4,x-5-xx),Block(r_id))
    for yy in range(4):
        editor.placeBlock((z+1,y+5+yy,x-9),Block(r_id))
    editor.placeBlock((z+1,y+6,x-8),Block(r_id))
    editor.placeBlock((z+1,y+6,x-10),Block(r_id))
    for xx in range(7):
        editor.placeBlock((z+12,y+3,x-13+2*xx),Block(y_id))
    for xx in range(6):
        editor.placeBlock((z+12,y+3,x-12+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+13,y+3,x-13+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+11,y+3,x-11+2*xx),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+11,y+2,x-12+2*xx),Block(i_id,{"type": "top"}))
        editor.placeBlock((z+13,y+2,x-12+2*xx),Block(i_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((z+2+2*zz,y+3,x-13),Block(y_id))
        editor.placeBlock((z+3+2*zz,y+3,x-13),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+2+2*zz,y+3,x-12),Block(i_id,{"type": "bottom"}))
        editor.placeBlock((z+3+2*zz,y+2,x-14),Block(i_id,{"type": "top"}))
        editor.placeBlock((z+3+2*zz,y+2,x-12),Block(i_id,{"type": "top"}))
    for zz in range(6):
        editor.placeBlock((z+2+2*zz,y+3,x-14),Block(i_id,{"type": "bottom"}))
    for xx in range(4):
        editor.placeBlock((z,y,x+11+xx),Block(s_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
   
    for zz in range(3):
        editor.placeBlock((z+5+zz,y,x),Block(s_id,{"facing": "south", "half": "bottom", "shape": "straight"}))

    #light
    light(z-3,y,x-1) 
    light(z-3,y,x+5)
    light(z-3,y,x+18)
    light(z-11,y,x+10)
    light(z-11,y,x+15)
    light(z-7,y,x+10)
    light(z-7,y,x+15)
    light(z-12,y,x-6)
    light(z-12,y,x-15)
    light(z+3,y,x+19)
    light(z+9,y,x+19)
    light(z+16,y,x+18)
    light(z+16,y,x+13)
    light(z+16,y,x+8)
    light(z+16,y,x+3)
    light(z+16,y,x-2)
    light(z+16,y,x-7)
    light(z+16,y,x-14)
    editor.placeBlock((z-3,y+6,x+17),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((z+13,y+2,x-7),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((z+8,y+2,x-14),Block("lantern",{"hanging": "true"}))
    editor.placeBlock((z+4,y+2,x-14),Block("lantern",{"hanging": "true"}))
    #house1
    editor.placeBlock((z-1,y+8,x+5),Block("lantern"))
    editor.placeBlock((z+3,y+10,x+5),Block("lantern"))
    editor.placeBlock((z+9,y+10,x+5),Block("lantern"))
    editor.placeBlock((z+13,y+8,x+5),Block("lantern"))
    editor.placeBlock((z-1,y+8,x+11),Block("lantern"))
    editor.placeBlock((z+3,y+10,x+11),Block("lantern"))
    editor.placeBlock((z+9,y+10,x+11),Block("lantern"))
    editor.placeBlock((z+13,y+8,x+11),Block("lantern"))
    editor.placeBlock((z+1,y+9,x-1),Block("lantern"))
    editor.placeBlock((z+6,y+13,x-1),Block("lantern"))
    editor.placeBlock((z+11,y+9,x-1),Block("lantern"))
    editor.placeBlock((z+1,y+9,x+17),Block("lantern"))
    editor.placeBlock((z+6,y+13,x+17),Block("lantern"))
    editor.placeBlock((z+11,y+9,x+17),Block("lantern"))
    editor.placeBlock((z+6,y+14,x+8),Block("lantern"))   
    #house2
    editor.placeBlock((z-1,y+5,x-3),Block("lantern"))
    editor.placeBlock((z-9,y+5,x-3),Block("lantern"))
    editor.placeBlock((z-5,y+7,x-5),Block("lantern"))
    editor.placeBlock((z-11,y+10,x-9),Block("lantern"))
    editor.placeBlock((z+1,y+10,x-9),Block("lantern"))
    editor.placeBlock((z-5,y+7,x-13),Block("lantern"))
    editor.placeBlock((z-9,y+5,x-15),Block("lantern"))
    editor.placeBlock((z-1,y+5,x-15),Block("lantern"))





def window_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    editor.placeBlock((z-1,y+1,x),Block(w_id,{"facing": "north", "half": "top", "open": "true"}))
    editor.placeBlock((z+1,y+1,x+5),Block(w_id,{"facing": "south", "half": "top", "open": "true"}))
    for xx in range(3):
        editor.placeBlock((z-11,y,x-8-xx),Block(q_id))
        editor.placeBlock((z-12,y,x-8-xx),Block(w_id,{"facing": "west", "half": "top", "open": "true"}))
        editor.placeBlock((z-12,y+3,x-8-xx),Block(w_id,{"facing": "west", "half": "bottom"}))
        editor.placeBlock((z-11,y+3,x-8-xx),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z-11,y+1,x-10+xx),Block(y_id))
    for xx in range(4):
        editor.placeBlock((z-1,y+1,x+1+xx),Block(q_id))
        editor.placeBlock((z-1,y,x+1+xx),Block(w_id,{"facing": "west", "half": "top"}))
        editor.placeBlock((z-2,y+1,x+1+xx),Block(w_id,{"facing": "west", "half": "top", "open": "true"}))
        editor.placeBlock((z-1,y+5,x+1+xx),Block(t_id,{"facing": "east", "lit": "false"}))
        editor.placeBlock((z-1,y+2,x+1+xx),Block(y_id))
        editor.placeBlock((z-1,y+4,x+1+xx),Block(u_id))
        for yy in range(3):
            editor.placeBlock((z,y+2+yy,x+1+xx),Block(r_id))
    for xx in range(2):
        editor.placeBlock((z-2,y+5,x+2+xx),Block(t_id,{"facing": "west", "lit": "false"}))
    for zz in range(30):
        for xx in range(35):
            editor.placeBlock((z-12+zz,y-1,x-15+xx),Block(i_id))
    for xx in range(6):
        editor.placeBlock((z-4,y+5,x+10+xx),Block(w_id,{"facing": "west", "half": "bottom"}))
        for zz in range(3):
            editor.placeBlock((z-1-zz,y+5,x+10+xx),Block(t_id,{"facing": "west", "lit": "false"}))
    for yy in range(5):
        editor.placeBlock((z-3,y+yy,x+10),Block(o_id))
        editor.placeBlock((z-3,y+yy,x+15),Block(o_id))
def niwa_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id):
    for xx in range(4):
        editor.placeBlock((z-11,y,x+1+xx),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-5,y,x+1+xx),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-12,y,x+1+xx),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
        editor.placeBlock((z-4,y,x+1+xx),Block(e_id,{"facing": "east", "half": "bottom", "open": "true"}))
        for zz in range(3):
            editor.placeBlock((z-7-zz,y,x+1+xx),Block(q_id))
    editor.placeBlock((z-11,y,x+5),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    editor.placeBlock((z-11,y,x),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((z-5,y,x),Block(r_id,{"facing": "north", "waterlogged": "false"}))
    editor.placeBlock((z-5,y,x+5),Block(r_id,{"facing": "south", "waterlogged": "false"}))
    for zz in range(3):
        editor.placeBlock((z-7-zz,y,x+6),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-7-zz,y,x-1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z-7-zz,y,x+7),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
        editor.placeBlock((z-7-zz,y,x-2),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
    editor.placeBlock((z-6,y,x-1),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    editor.placeBlock((z-10,y,x-1),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((z-10,y,x+6),Block(r_id,{"facing": "west", "waterlogged": "false"}))
    editor.placeBlock((z-6,y,x+6),Block(r_id,{"facing": "east", "waterlogged": "false"}))
    for xx in range(2):
        editor.placeBlock((z-8,y+1,x+2+xx),Block(t_id))
    editor.placeBlock((z-9,y+1,x+3),Block(y_id))
    editor.placeBlock((z-9,y+1,x+1),Block(u_id))
    editor.placeBlock((z+6,y+1,x-8),Block(u_id))
    for zz in range(4):
        editor.placeBlock((z+8+zz,y,x-6),Block(i_id))
    editor.placeBlock((z+7,y,x-7),Block(i_id))
    editor.placeBlock((z+8,y,x-7),Block(i_id))
    editor.placeBlock((z+7,y,x-8),Block(i_id))
    for xx in range(5):
        editor.placeBlock((z+6,y,x-8-xx),Block(i_id))
    for yy in range(2):
        for xx in range(3):
            for zz in range(5):
                editor.placeBlock((z+7+zz,y-1-yy,x-10-xx),Block(o_id))
        for zz in range(4):
            editor.placeBlock((z+8+zz,y-1-yy,x-9),Block(o_id))
        for zz in range(3):
            editor.placeBlock((z+9+zz,y-1-yy,x-8),Block(o_id))
        for zz in range(2):
            editor.placeBlock((z+10+zz,y-1-yy,x-7),Block(o_id))
    editor.placeBlock((z+7,y-1,x-9),Block(p_id))
    editor.placeBlock((z+8,y-1,x-8),Block(p_id))
    editor.placeBlock((z+9,y-1,x-7),Block(p_id))
    editor.placeBlock((z+8,y,x-11),Block(a_id))
    editor.placeBlock((z+10,y,x-9),Block(a_id))
    for yy in range(12):
        editor.placeBlock((z+9,y+yy,x-7),Block(s_id))
    for yy in range(15):
        editor.placeBlock((z+8,y+yy,x-8),Block(s_id))
    for yy in range(13):
        editor.placeBlock((z+7,y+yy,x-9),Block(s_id))
    editor.placeBlock((z+1,y,x-1),Block("chiseled_stone_bricks"))
    editor.placeBlock((z+1,y+1,x-1),Block("lantern"))
    editor.placeBlock((z+11,y,x-1),Block("chiseled_stone_bricks"))
    editor.placeBlock((z+11,y+1,x-1),Block("lantern"))
    editor.placeBlock((z+1,y,x-12),Block("chiseled_stone_bricks"))
    editor.placeBlock((z+1,y+1,x-12),Block("lantern"))
    
    editor.placeBlock((z+12,y+4,x-13),Block("lantern"))
    editor.placeBlock((z+12,y+4,x-7),Block("lantern"))
    editor.placeBlock((z+6,y+4,x-13),Block("lantern"))


def kagu1_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for xx in range(15):
        for zz in range(11):
            editor.placeBlock((z+1+zz,y+7,x+1+xx),Block(q_id))
    for xx in range(7):
        for zz in range(9):
            editor.placeBlock((z-1-zz,y+5,x-12+xx),Block(q_id))
    for yy in range(2):
        for xx in range(4):
            editor.placeBlock((z+11,y+1+yy,x+12+xx),Block(w_id))
        for zz in range(3):
            editor.placeBlock((z+8+zz,y+1+yy,x+15),Block(w_id))
    for xx in range(2):
        editor.placeBlock((z+11,y+3,x+14+xx),Block(w_id))
    editor.placeBlock((z+10,y+3,x+15),Block(w_id))
    editor.placeBlock((z+7,y+1,x+15),Block(w_id))
    editor.placeBlock((z+11,y+1,x+11),Block(e_id))
    for yy in range(2):
        editor.placeBlock((z+11,y+2+yy,x+11),Block(r_id))
    editor.placeBlock((z+6,y+1,x+15),Block(e_id))
    for yy in range(2):
        editor.placeBlock((z+6,y+2+yy,x+15),Block(r_id))
    editor.placeBlock((z+9,y+1,x+13),Block(t_id))
    editor.placeBlock((z+11,y+4,x+15),Block(y_id))
    editor.placeBlock((z+9,y+3,x+15),Block(u_id,{"facing": "north"}))
    editor.placeBlock((z+7,y+3,x+15),Block(i_id,{"facing": "north"}))
    editor.placeBlock((z+7,y+2,x+15),Block(o_id))
    editor.placeBlock((z+8,y+3,x+15),Block(p_id))
    editor.placeBlock((z+11,y+3,x+13),Block(a_id))
    editor.placeBlock((z+11,y+3,x+12),Block(s_id,{"rotation":"12"}))
    for yy in range(4):
        editor.placeBlock((z+5,y+1+yy,x+15),Block(d_id))
        editor.placeBlock((z+5,y+1+yy,x+11),Block(d_id))
    for xx in range(3):
        editor.placeBlock((z+5,y+1,x+12+xx),Block(d_id))
        editor.placeBlock((z+5,y+4,x+12+xx),Block(d_id))
  
    editor.placeBlock((z+4,y+3,x+12),Block(f_id,{"facing": "west", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+4,y+2,x+12),Block(f_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+4,y+3,x+13),Block(f_id,{"facing": "west", "half": "upper", "hinge": "left"}))
    editor.placeBlock((z+4,y+2,x+13),Block(f_id,{"facing": "west", "half": "lower", "hinge": "left"}))
    editor.placeBlock((z+4,y+3,x+14),Block(f_id,{"facing": "west", "half": "upper", "hinge": "right"}))
    editor.placeBlock((z+4,y+2,x+14),Block(f_id,{"facing": "west", "half": "lower", "hinge": "right"}))
    editor.placeBlock((z+5,y+5,x+14),Block(y_id))
    editor.placeBlock((z+5,y+5,x+12),Block(g_id))
    for zz in range(2):
        editor.placeBlock((z+3-zz,y+3,x+15),Block(d_id,{"facing": "north"}))
        editor.placeBlock((z+3-zz,y+1,x+15),Block(d_id,{"facing": "north"}))
    editor.placeBlock((z+2,y+4,x+15),Block(y_id))
    editor.placeBlock((z+3,y+4,x+15),Block(p_id))
    editor.placeBlock((z+3,y+6,x+6),Block(y_id))
    editor.placeBlock((z-8,y+1,x-12),Block(y_id))
    editor.placeBlock((z-9,y+4,x-6),Block(y_id))
    editor.placeBlock((z-1,y+4,x-6),Block(y_id))
    editor.placeBlock((z-1,y+4,x-12),Block(y_id))

    #enchant
    editor.placeBlock((z+7,y+1,x+11),Block("white_carpet"))
    editor.placeBlock((z+7,y,x+11),Block("glowstone"))
    editor.placeBlock((z+7,y,x+12),Block("black_wool"))
    editor.placeBlock((z+7,y,x+14),Block("black_wool"))
    editor.placeBlock((z+8,y,x+11),Block("black_wool"))
    editor.placeBlock((z+10,y,x+11),Block("black_wool"))
    editor.placeBlock((z+8,y,x+13),Block("white_wool"))
    editor.placeBlock((z+9,y,x+12),Block("white_wool"))
    editor.placeBlock((z+9,y,x+14),Block("white_wool"))
    editor.placeBlock((z+10,y,x+13),Block("white_wool"))

    editor.placeBlock((z+7,y,x+13),Block("light_gray_wool"))
    editor.placeBlock((z+9,y,x+11),Block("light_gray_wool"))
    editor.placeBlock((z+8,y,x+12),Block("light_gray_wool"))
    editor.placeBlock((z+8,y,x+14),Block("light_gray_wool"))
    editor.placeBlock((z+10,y,x+12),Block("light_gray_wool"))
    editor.placeBlock((z+10,y,x+14),Block("light_gray_wool"))
    #玄関
    for xx in range(4):
        for zz in range(2):
            editor.placeBlock((z+2-zz,y+1,x+11+xx),Block("red_carpet"))
    editor.placeBlock((z+1,y,x+12),Block("glowstone"))
    editor.placeBlock((z+1,y,x+13),Block("glowstone"))
def kitchen_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id,p_id,a_id,s_id,d_id,f_id,g_id):
    for yy in range(3):
        editor.placeBlock((z+1,y+1+yy,x+15),Block(q_id,{"facing": "west", "half": "top", "open": "true"}))
        editor.placeBlock((z+4,y+1+yy,x+15),Block(q_id,{"facing": "east", "half": "bottom", "open": "true"}))
        editor.placeBlock((z+11,y+1+yy,x+9),Block(q_id,{"facing": "south", "half": "top", "open": "true"}))
        editor.placeBlock((z+11,y+1+yy,x+7),Block(q_id,{"facing": "north", "half": "top", "open": "true"}))
    for zz in range(2):
        editor.placeBlock((z+2+zz,y+2,x+15),Block(p_id,{"facing": "south", "half": "top", "shape": "straight"}))
    for xx in range(2):
        editor.placeBlock((z+11,y+1,x+1+xx),Block(w_id,{"facing": "west"}))
    editor.placeBlock((z+10,y+1,x+1),Block(e_id,{"facing": "south"}))
    editor.placeBlock((z+9,y+1,x+1),Block(r_id,{"facing": "south"}))
    editor.placeBlock((z+11,y+2,x+7+xx),Block(p_id,{"facing": "south", "half": "top", "shape": "straight"}))
    editor.placeBlock((z+11,y+1,x+7+xx),Block(t_id,{"facing": "west"}))
    editor.placeBlock((z+11,y+3,x+7+xx),Block(t_id,{"facing": "west"}))
    for xx in range(4):
        editor.placeBlock((z+11,y+1,x+3+xx),Block(r_id,{"facing": "west"}))
    for yy in range(2):
        editor.placeBlock((z+11,y+1+yy,x+6),Block(t_id,{"facing": "west"}))
    editor.placeBlock((z+11,y+4,x+5),Block(t_id,{"facing": "west"}))
    for zz in range(2):
        editor.placeBlock((z+9+2*zz,y+4,x+1),Block(t_id,{"facing": "south"}))
        editor.placeBlock((z+10-zz,y+3,x+1),Block(q_id,{"facing": "west", "half": "top"}))
    for xx in range(5):
        editor.placeBlock((z+11,y+3,x+1+xx),Block(q_id,{"facing": "south", "half": "top"}))
    editor.placeBlock((z+9,y+6,x+4),Block(y_id))
    editor.placeBlock((z+11,y+4,x+3),Block(y_id))
    editor.placeBlock((z+11,y+6,x+9),Block(y_id))
    editor.placeBlock((z+11,y+4,x+4),Block(u_id,{"facing": "west", "type": "single"}))
    editor.placeBlock((z+10,y+4,x+1),Block(u_id,{"facing": "south", "type": "single"}))
    editor.placeBlock((z+11,y+4,x+2),Block(i_id))
    editor.placeBlock((z+11,y+2,x+5),Block(o_id,{"facing": "east"}))
    for xx in range(3):
        editor.placeBlock((z+8,y+1,x+2+xx),Block(a_id,{"axis": "x"}))
    editor.placeBlock((z+8,y+1,x+1),Block(s_id))
    editor.placeBlock((z+8,y+2,x+1),Block(d_id))
    editor.placeBlock((z+11,y+2,x+3),Block(f_id))
    editor.placeBlock((z+8,y+2,x+3),Block(g_id))
    editor.placeBlock((z+4,y+4,x+1),Block(q_id,{"half": "top"}))
    editor.placeBlock((z+3,y+3,x+1),Block(q_id,{"half": "top"}))
    editor.placeBlock((z+2,y+2,x+1),Block(q_id,{"half": "top"}))
    for xx in range(2):
        for zz in range(3):
            editor.placeBlock((z+5+zz,y+1,x+1+xx),Block("orange_carpet"))
    editor.placeBlock((z+6,y,x+1),Block("glowstone"))



def table_e(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id):
    for xx in range(3):
        editor.placeBlock((z+4,y+1,x+5+xx),Block(q_id))
        editor.placeBlock((z+2,y+1,x+5+xx),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((z+1,y+1,x+5+xx),Block(e_id,{"facing": "west", "half": "bottom", "open": "true"}))
        editor.placeBlock((z+3,y+1,x+5+xx),Block("white_carpet"))
    editor.placeBlock((z+3,y,x+6),Block("glowstone"))
    editor.placeBlock((z+2,y+1,x+4),Block(e_id,{"facing": "north", "half": "bottom", "open": "true"}))
    editor.placeBlock((z+2,y+1,x+8),Block(e_id,{"facing": "south", "half": "bottom", "open": "true"}))
    editor.placeBlock((z+4,y+5,x+1),Block(r_id))
    editor.placeBlock((z+3,y+4,x+1),Block(t_id))
    editor.placeBlock((z+2,y+3,x+1),Block(y_id))
    editor.placeBlock((z+4,y+2,x+6),Block(u_id))
def bed_e(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for zz in range(3):
        editor.placeBlock((z-7-zz,y,x-12),Block(q_id,{"axis": "z"}))
        editor.placeBlock((z-7-zz,y,x-9),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((z-7-zz,y,x-10),Block(w_id,{"facing": "north", "part": "foot"}))
        command = f"summon panda {z-7+zz} {y+2} {x-10}"
        runCommand(command)
        runCommand(command)
        runCommand(command)
    for yy in range(3):
        for zz in range(2):
            editor.placeBlock((z-8+zz,y+yy,x-6),Block(r_id))
    for yy in range(2):
        editor.placeBlock((z-7,y+yy,x-6),Block(r_id))
    editor.placeBlock((z-9,y+1,x-12),Block(t_id))
    for xx in range(5):
        for zz in range(3):
            editor.placeBlock((z-1-zz,y,x-7-xx),Block("light_blue_carpet"))
    editor.placeBlock((z-2,y-1,x-9),Block("glowstone"))


def house2_s(x,y,z):
    buildHouse_s(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_s(x,y,z,"grass_block","oak_trapdoor","birch_stairs","air","campfire","poppy","potted_allium","smooth_stone","andesite_wall")
    niwa_s(x,y,z,"stripped_spruce_log","spruce_slab","spruce_trapdoor","spruce_wall_sign","cake","potted_oxeye_daisy","lantern","stone_brick_wall","water","grass_block","lily_pad","bamboo")
    kagu1_s(x,y,z,"oak_planks","bookshelf","jungle_log","jungle_leaves","enchanting_table","lantern","chest","ender_chest","anvil","potted_dark_oak_sapling","potted_poppy","creeper_head","barrel","acacia_door","potted_birch_sapling")
    kitchen_s(x,y,z,"spruce_trapdoor","furnace","smoker","blast_furnace","barrel","lantern","chest","potted_blue_orchid","campfire","oak_stairs","stripped_jungle_log","acacia_log","acacia_leaves","cake","brewing_stand")
    table_s(x,y,z,"oak_planks","oak_slab","oak_trapdoor","potted_fern","potted_cornflower","potted_jungle_sapling","potted_oxeye_daisy")
    bed_s(x,y,z,"stripped_dark_oak_log","light_blue_bed","spruce_stairs","bookshelf","potted_poppy")
def house2_n(x,y,z):
    buildHouse_n(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_n(x,y,z,"grass_block","oak_trapdoor","birch_stairs","air","campfire","poppy","potted_allium","smooth_stone","andesite_wall")
    niwa_n(x,y,z,"stripped_spruce_log","spruce_slab","spruce_trapdoor","spruce_wall_sign","cake","potted_oxeye_daisy","lantern","stone_brick_wall","water","grass_block","lily_pad","bamboo")
    kagu1_n(x,y,z,"oak_planks","bookshelf","jungle_log","jungle_leaves","enchanting_table","lantern","chest","ender_chest","anvil","potted_dark_oak_sapling","potted_poppy","creeper_head","barrel","acacia_door","potted_birch_sapling")
    kitchen_n(x,y,z,"spruce_trapdoor","furnace","smoker","blast_furnace","barrel","lantern","chest","potted_blue_orchid","campfire","oak_stairs","stripped_jungle_log","acacia_log","acacia_leaves","cake","brewing_stand")
    table_n(x,y,z,"oak_planks","oak_slab","oak_trapdoor","potted_fern","potted_cornflower","potted_jungle_sapling","potted_oxeye_daisy")
    bed_n(x,y,z,"stripped_dark_oak_log","light_blue_bed","spruce_stairs","bookshelf","potted_poppy")
def house2_w(z,y,x):
    buildHouse_w(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_w(x,y,z,"grass_block","oak_trapdoor","birch_stairs","air","campfire","poppy","potted_allium","smooth_stone","andesite_wall")
    niwa_w(x,y,z,"stripped_spruce_log","spruce_slab","spruce_trapdoor","spruce_wall_sign","cake","potted_oxeye_daisy","lantern","stone_brick_wall","water","grass_block","lily_pad","bamboo")
    kagu1_w(x,y,z,"oak_planks","bookshelf","jungle_log","jungle_leaves","enchanting_table","lantern","chest","ender_chest","anvil","potted_dark_oak_sapling","potted_poppy","creeper_head","barrel","acacia_door","potted_birch_sapling")
    kitchen_w(x,y,z,"spruce_trapdoor","furnace","smoker","blast_furnace","barrel","lantern","chest","potted_blue_orchid","campfire","oak_stairs","stripped_jungle_log","acacia_log","acacia_leaves","cake","brewing_stand")
    table_w(x,y,z,"oak_planks","oak_slab","oak_trapdoor","potted_fern","potted_cornflower","potted_jungle_sapling","potted_oxeye_daisy")
    bed_w(x,y,z,"stripped_dark_oak_log","light_blue_bed","spruce_stairs","bookshelf","potted_poppy")
def house2_e(z,y,x):
    buildHouse_e(x,y,z, "polished_andesite","smooth_stone","smooth_quartz","stripped_spruce_log","spruce_slab","stone_bricks","infested_chiseled_stone_bricks","stone_brick_slab","sea_lantern","smooth_stone_slab","air","polished_andesite_stairs")
    window_e(x,y,z,"grass_block","oak_trapdoor","birch_stairs","air","campfire","poppy","potted_allium","smooth_stone","andesite_wall")
    niwa_e(x,y,z,"stripped_spruce_log","spruce_slab","spruce_trapdoor","spruce_wall_sign","cake","potted_oxeye_daisy","lantern","stone_brick_wall","water","grass_block","lily_pad","bamboo")
    kagu1_e(x,y,z,"oak_planks","bookshelf","jungle_log","jungle_leaves","enchanting_table","lantern","chest","ender_chest","anvil","potted_dark_oak_sapling","potted_poppy","creeper_head","barrel","acacia_door","potted_birch_sapling")
    kitchen_e(x,y,z,"spruce_trapdoor","furnace","smoker","blast_furnace","barrel","lantern","chest","potted_blue_orchid","campfire","oak_stairs","stripped_jungle_log","acacia_log","acacia_leaves","cake","brewing_stand")
    table_e(x,y,z,"oak_planks","oak_slab","oak_trapdoor","potted_fern","potted_cornflower","potted_jungle_sapling","potted_oxeye_daisy")
    bed_e(x,y,z,"stripped_dark_oak_log","light_blue_bed","spruce_stairs","bookshelf","potted_poppy")
def house2(x,y,z,f):
    if f=="n":
        house2_n(x,y,z)
    elif f=="s":
        house2_s(x,y,z)
    elif f=="e":
        house2_e(x,y,z)
    elif f=="w":
        house2_w(x,y,z)

house2(-120,4,-45,"n")

house2(-120,4,-85,"w")

house2(-120,4,-125,"e")

house2(-120,4,-165,"s")

def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True

