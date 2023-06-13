__all__ = []
# __version__
#import lantern
from interfaceUtils import runCommand
from lantern import Lantern
from gdpc import Editor, Block, Transform, geometry
editor = Editor(buffering=True) #Trueだと動かない


def bridge(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    
    for xx in range(5):
        editor.placeBlock((x-2+xx,y-1,z+5),Block(w_id))
        editor.placeBlock((x-2+xx,y-1,z-5),Block(w_id))
        
        editor.placeBlock((x-2+xx,y,z+4),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2+xx,y,z-4),Block(e_id,{"type": "bottom"}))

        editor.placeBlock((x-2+xx,y,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-2+xx,y,z-3),Block(e_id,{"type": "top"}))

        editor.placeBlock((x-2+xx,y+1,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2+xx,y+1,z-2),Block(e_id,{"type": "bottom"}))
            
        for zz in range(3):
            editor.placeBlock((x-2+xx,y+1,z-1+zz),Block(e_id,{"type": "top"}))
            
    for zz in range(3):
        editor.placeBlock((x+3,y,z+5-zz),Block(q_id))
        editor.placeBlock((x+3,y,z-5+zz),Block(q_id))
        editor.placeBlock((x-3,y,z+5-zz),Block(q_id))
        editor.placeBlock((x-3,y,z-5+zz),Block(q_id))

        editor.placeBlock((x+3,y+1,z+3-zz),Block(q_id))
        editor.placeBlock((x+3,y+1,z-3+zz),Block(q_id))
        editor.placeBlock((x-3,y+1,z+3-zz),Block(q_id))
        editor.placeBlock((x-3,y+1,z-3+zz),Block(q_id))

        editor.placeBlock((x+3,y+2,z-1+zz),Block(q_id))
        editor.placeBlock((x-3,y+2,z-1+zz),Block(q_id))
      
    editor.placeBlock((x+3,y,z+3),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x+3,y,z-3),Block(r_id,{"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-3,y,z+3),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x-3,y,z-3),Block(r_id,{"facing": "east", "half": "top", "shape": "straight"}))

    for yy in range(3):
        editor.placeBlock((x+3,y-1-yy,z+4),Block(q_id))
        editor.placeBlock((x+3,y-1-yy,z-4),Block(q_id))
        editor.placeBlock((x-3,y-1-yy,z+4),Block(q_id))
        editor.placeBlock((x-3,y-1-yy,z-4),Block(q_id))

    for yy in range(4):
        editor.placeBlock((x+3,y-yy,z+2),Block(q_id))
        editor.placeBlock((x+3,y-yy,z-2),Block(q_id))
        editor.placeBlock((x-3,y-yy,z+2),Block(q_id))
        editor.placeBlock((x-3,y-yy,z-2),Block(q_id))

    editor.placeBlock((x+3,y+1,z+5),Block(t_id))
    editor.placeBlock((x+3,y+1,z-5),Block(t_id))
    editor.placeBlock((x-3,y+1,z+5),Block(t_id))
    editor.placeBlock((x-3,y+1,z-5),Block(t_id))

    editor.placeBlock((x+3,y+2,z+3),Block(t_id))
    editor.placeBlock((x+3,y+2,z-3),Block(t_id))
    editor.placeBlock((x-3,y+2,z+3),Block(t_id))
    editor.placeBlock((x-3,y+2,z-3),Block(t_id))

    editor.placeBlock((x+3,y+1,z+4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+3,y+1,z-4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+1,z+4),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+1,z-4),Block(y_id,{"type": "bottom"}))

    editor.placeBlock((x+3,y+2,z+2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x+3,y+2,z-2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+2,z+2),Block(y_id,{"type": "bottom"}))
    editor.placeBlock((x-3,y+2,z-2),Block(y_id,{"type": "bottom"}))

    Lantern(x-5,y,z-6)
    Lantern(x-5,y,z+6)
    Lantern(x+5,y,z-6)
    Lantern(x+5,y,z+6)

def Bridge(x,y,z):
    bridge(x,y,z,"polished_andesite","smooth_stone","smooth_stone_slab","polished_andesite_stairs","lantern","polished_andesite_slab")

def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True

