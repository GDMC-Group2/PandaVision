import interfaceUtils
from gdpc import Editor, Block, Transform, geometry
editor = Editor(buffering=True)


def lantern(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for yy in range(2):
        for xx in range(3):
            editor.placeBlock((x-1+xx,y-2+yy,z),Block(q_id))
        for zz in range(3):
            editor.placeBlock((x,y-2+yy,z-1+zz),Block(q_id))
        editor.placeBlock((x,y+yy,z),Block(q_id))
    editor.placeBlock((x,y,z+1),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x,y,z-1),Block(w_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+1,y,z),Block(w_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-1,y,z),Block(w_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x,y+3,z+1),Block(w_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x,y+3,z-1),Block(w_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x+1,y+3,z),Block(w_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-1,y+3,z),Block(w_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x-1,y+1,z),Block(e_id,{"type": "top"}))
    editor.placeBlock((x+1,y+1,z),Block(e_id,{"type": "top"}))
    editor.placeBlock((x,y+1,z+1),Block(e_id,{"type": "top"}))
    editor.placeBlock((x,y+1,z-1),Block(e_id,{"type": "top"}))
    editor.placeBlock((x,y+2,z),Block(t_id))
    editor.placeBlock((x,y+3,z),Block(q_id))
    editor.placeBlock((x,y+4,z),Block(e_id,{"type": "bottom"}))
    editor.placeBlock((x-1,y+2,z),Block(r_id,{"facing": "west", "half": "top", "open": "true"}))
    editor.placeBlock((x+1,y+2,z),Block(r_id,{"facing": "east", "half": "top", "open": "true"}))
    editor.placeBlock((x,y+2,z+1),Block(r_id,{"facing": "south", "half": "top", "open": "true"}))
    editor.placeBlock((x,y+2,z-1),Block(r_id,{"facing": "north", "half": "top", "open": "true"}))

def Lantern(x,y,z):
    lantern(x,y,z,"polished_andesite","polished_andesite_stairs","polished_andesite_slab","oak_trapdoor","shroomlight")

def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True