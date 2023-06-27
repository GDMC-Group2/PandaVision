from interfaceUtils import runCommand
from gdpc import Editor, Block, Transform, geometry

editor = Editor(buffering=True)

def air(x,y,z,q_id):
    for yy in range(12):
        for xx in range(36):
            for zz in range(38):
                editor.placeBlock((x-18+xx,y-yy,z-17+zz),Block("spruce_planks"))

    for yy in range(10):
        for xx in range(34):
            for zz in range(36):
                editor.placeBlock((x-17+xx,y-1-yy,z-16+zz),Block(q_id))
def Air(x,y,z):
    air(x,y-10,z,"air")
