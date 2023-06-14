from interfaceUtils import runCommand
from gdpc import Editor, Block, Transform, geometry

editor = Editor()

def air(x,y,z,q_id):
    for xx in range(34):
        for yy in range(10):
            for zz in range(36):
                editor.placeBlock((x-17+xx,y-1+yy,z-16+zz),Block(q_id))
def Air(x,y,z):
    air(x,y-20,z,"air")
