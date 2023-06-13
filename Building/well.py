from gdpc import Editor, Block, Transform, geometry
import os

editor = Editor(buffering=True) #Trueだとうごかない




def well(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    
    editor.placeBlock((x+1,y,z+1),Block(q_id))
    editor.placeBlock((x-1,y,z+1),Block(q_id))
    editor.placeBlock((x-1,y,z-1),Block(q_id))
    editor.placeBlock((x+1,y,z-1),Block(q_id))

    editor.placeBlock((x+1,y,z),Block(w_id))
    editor.placeBlock((x-1,y,z),Block(w_id))
    editor.placeBlock((x,y,z+1),Block(w_id))
    editor.placeBlock((x,y,z-1),Block(w_id))

    for yy in range(2):
        editor.placeBlock((x+1,y+1+yy,z+1),Block(w_id))
        editor.placeBlock((x-1,y+1+yy,z+1),Block(w_id))
        editor.placeBlock((x-1,y+1+yy,z-1),Block(w_id))
        editor.placeBlock((x+1,y+1+yy,z-1),Block(w_id))
    for xx in range(3):
        for zz in range(3):
            editor.placeBlock((x-1+xx,y+3,z-1+zz),Block(e_id))
    for yy in range(4):
        editor.placeBlock((x,y-yy,z),Block(t_id))
    editor.placeBlock((x,y-1,z),Block(r_id))
    editor.placeBlock((x-1,y,z-2),Block(y_id))

def Wells(x,y,z):
    well(x,y,z,"cobblestone","cobblestone_wall","hay_block","water","air","wall_torch")

def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True

