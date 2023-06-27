from interfaceUtils import runCommand
from gdpc import Editor, Block

editor = Editor(buffering=True)

def air(x,y,z,q_id):
    for xx in range(34):
        for yy in range(10):
            for zz in range(36):
                editor.placeBlock((x-17+xx,y-1+yy,z-16+zz),Block(q_id))

def floor(x,y,z,q_id,w_id,e_id,r_id):
    for zz in range(5):
        for xx in range(25):
            editor.placeBlock((x - 12 + xx, y+8, z + 13 + zz), Block(q_id, {"axis": "x"}))
    for xx in range(11):
        editor.placeBlock((x+2+xx,y,z+2),Block(q_id,{"axis":"x"}))
        editor.placeBlock((x -2 - xx, y, z + 2), Block(q_id, {"axis": "x"}))
        editor.placeBlock((x + 2 + xx, y, z - 2), Block(q_id, {"axis": "x"}))
        editor.placeBlock((x - 2 - xx, y, z - 2), Block(q_id, {"axis": "x"}))
        editor.placeBlock((x + 2 + xx, y, z + 12), Block(q_id, {"axis": "x"}))
        editor.placeBlock((x - 2 - xx, y, z + 12), Block(q_id, {"axis": "x"}))
        editor.placeBlock((x + 2 + xx, y, z - 12), Block(q_id, {"axis": "x"}))
        editor.placeBlock((x - 2 - xx, y, z - 12), Block(q_id, {"axis": "x"}))

    for zz in range(11):
        editor.placeBlock((x+2, y, z+2+zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x - 2, y, z + 2 + zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x - 2, y, z - 2 - zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x + 2, y, z - 2 - zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x + 12, y, z + 2 + zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x - 12, y, z + 2 + zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x - 12, y, z - 2 - zz), Block(q_id, {"axis": "z"}))
        editor.placeBlock((x + 12, y, z - 2 - zz), Block(q_id, {"axis": "z"}))

    for xx in range(9):
        editor.placeBlock((x+3+xx,y,z+3),Block(w_id,{"facing":"east","half":"top"}))
        editor.placeBlock((x + 3 + xx, y, z - 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 3 - xx, y, z + 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 3 - xx, y, z - 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x + 3 + xx, y, z + 11), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x + 3 + xx, y, z - 11), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 3 - xx, y, z + 11), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 3 - xx, y, z - 11), Block(w_id, {"facing": "east", "half": "top"}))
    for zz in range(9):
        editor.placeBlock((x + 3 , y, z +zz+ 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 3, y, z + zz + 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 3, y, z - zz - 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x + 3, y, z - zz - 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x + 11, y, z + zz + 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 11, y, z + zz + 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x - 11, y, z - zz - 3), Block(w_id, {"facing": "east", "half": "top"}))
        editor.placeBlock((x + 11, y, z - zz - 3), Block(w_id, {"facing": "east", "half": "top"}))

    for xx in range(7):
        for zz in range(7):
            editor.placeBlock((x+4+xx,y,z+4+zz),Block(e_id))
            editor.placeBlock((x - 4 - xx, y, z + 4 + zz), Block(e_id))
            editor.placeBlock((x - 4 - xx, y, z - 4 - zz), Block(e_id))
            editor.placeBlock((x + 4 + xx, y, z - 4 - zz), Block(e_id))

    for xx in range(28):
        for zz in range(3):
            editor.placeBlock((x-12+xx,y,z-1+zz),Block(r_id))
    for zz in range(28):
        for xx in range(3):
            editor.placeBlock((x-1+xx,y,z-12+zz),Block(r_id))

def entrance(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for yy in range(8):
        editor.placeBlock((x,y+1+yy,z),Block(q_id))
    for yy in range(3):
        editor.placeBlock((x+1, y + 1 + yy, z+1), Block(w_id))
        editor.placeBlock((x - 1, y + 1 + yy, z + 1), Block(w_id))
        editor.placeBlock((x - 1, y + 1 + yy, z - 1), Block(w_id))
        editor.placeBlock((x + 1, y + 1 + yy, z - 1), Block(w_id))
    for yy in range(4):
        editor.placeBlock((x + 1, y + 4 + yy, z + 1), Block(r_id))
        editor.placeBlock((x - 1, y + 4 + yy, z + 1), Block(r_id))
        editor.placeBlock((x - 1, y + 4 + yy, z - 1), Block(r_id))
        editor.placeBlock((x + 1, y + 4 + yy, z - 1), Block(r_id))
    editor.placeBlock((x+1,y+1,z+2),Block(r_id))
    editor.placeBlock((x - 1, y + 1, z + 2), Block(r_id))
    editor.placeBlock((x - 1, y + 1, z - 2), Block(r_id))
    editor.placeBlock((x + 1, y + 1, z - 2), Block(r_id))
    editor.placeBlock((x + 2, y + 1, z + 1), Block(r_id))
    editor.placeBlock((x - 2, y + 1, z + 1), Block(r_id))
    editor.placeBlock((x - 2, y + 1, z - 1), Block(r_id))
    editor.placeBlock((x + 2, y + 1, z - 1), Block(r_id))

    editor.placeBlock((x + 1, y + 2, z + 2), Block(e_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x - 1, y + 2, z + 2), Block(e_id,{"facing":"north","half":"bottom","shape":"straight"}))
    editor.placeBlock((x - 1, y + 2, z - 2), Block(e_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x + 1, y + 2, z - 2), Block(e_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x + 2, y + 2, z + 1), Block(e_id,{"facing":"west","half":"bottom","shape":"straight"}))
    editor.placeBlock((x - 2, y + 2, z + 1), Block(e_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x - 2, y + 2, z - 1), Block(e_id,{"facing":"east","half":"bottom","shape":"straight"}))
    editor.placeBlock((x + 2, y + 2, z - 1), Block(e_id,{"facing":"west","half":"bottom","shape":"straight"}))

    editor.placeBlock((x + 1, y+6, z + 2), Block(e_id, {"facing": "north", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 1, y+6, z + 2), Block(e_id, {"facing": "north", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 1, y+6, z - 2), Block(e_id, {"facing": "south", "half": "top", "shape": "straight"}))
    editor.placeBlock((x + 1, y+6, z - 2), Block(e_id, {"facing": "south", "half": "top", "shape": "straight"}))
    editor.placeBlock((x + 2, y+6, z + 1), Block(e_id, {"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 2, y+6, z + 1), Block(e_id, {"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 2, y+6, z - 1), Block(e_id, {"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x + 2, y+6, z - 1), Block(e_id, {"facing": "west", "half": "top", "shape": "straight"}))

    editor.placeBlock((x+2,y+1,z+2),Block(t_id))
    editor.placeBlock((x - 2, y + 1, z + 2), Block(t_id))
    editor.placeBlock((x - 2, y + 1, z - 2), Block(t_id))
    editor.placeBlock((x + 2, y + 1, z - 2), Block(t_id))
    editor.placeBlock((x + 2, y + 2, z + 2), Block(y_id))
    editor.placeBlock((x - 2, y + 2, z + 2), Block(y_id))
    editor.placeBlock((x - 2, y + 2, z - 2), Block(y_id))
    editor.placeBlock((x + 2, y + 2, z - 2), Block(y_id))

    editor.placeBlock((x + 2, y+6, z + 2), Block(t_id,{"up":"true"}))
    editor.placeBlock((x - 2, y+6, z + 2), Block(t_id,{"up":"true"}))
    editor.placeBlock((x - 2, y+6, z - 2), Block(t_id,{"up":"true"}))
    editor.placeBlock((x + 2, y+6, z - 2), Block(t_id,{"up":"true"}))
    editor.placeBlock((x + 2, y + 5, z + 2), Block(y_id,{"hanging":"true"}))
    editor.placeBlock((x - 2, y + 5, z + 2), Block(y_id,{"hanging":"true"}))
    editor.placeBlock((x - 2, y + 5, z - 2), Block(y_id,{"hanging":"true"}))
    editor.placeBlock((x + 2, y + 5, z - 2), Block(y_id,{"hanging":"true"}))

def ceiling(x,y,z,q_id,w_id,e_id,r_id):
    for xx in range(30):
        for zz in range(30):
            editor.placeBlock((x-15+xx,y+8,z-15+zz),Block(q_id))
    for zz in range(30):
        editor.placeBlock((x+2,y+7,z-12+zz),Block(e_id, {"axis": "z"}))
        editor.placeBlock((x - 2, y + 7, z -12 + zz), Block(e_id, {"axis": "z"}))
        editor.placeBlock((x + 12, y + 7, z -12 + zz), Block(e_id, {"axis": "z"}))
        editor.placeBlock((x - 12, y + 7, z -12 + zz), Block(e_id, {"axis": "z"}))
    for xx in range(25):
        editor.placeBlock((x-12+xx,y+7,z-2),Block(e_id,{"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z - 5), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z - 9), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z - 12), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z - 18), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z + 2), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z +5), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z + 9), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z +12), Block(e_id, {"axis": "x"}))
        editor.placeBlock((x-12+xx, y + 7, z + 18), Block(e_id, {"axis": "x"}))
    for xx in range(27):
        editor.placeBlock((x-11+xx,y+7,z),Block(r_id,{"facing":"south","half":"top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z+4), Block(r_id, {"facing": "south", "half": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z+7), Block(r_id, {"facing": "south", "half": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z+12), Block(r_id, {"facing": "south", "half": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 4), Block(r_id, {"facing": "south", "half": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 7), Block(r_id, {"facing": "south", "half": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 12), Block(r_id, {"facing": "south", "half": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z+1), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z + 6), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z + 8), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z + 11), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 1), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 6), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 8), Block(w_id, {"type": "top"}))
        editor.placeBlock((x -11 + xx, y+ 7, z - 11), Block(w_id, {"type": "top"}))

def wall1(x,y,z,q_id,w_id,e_id,r_id,t_id):
    for yy in range(7):
        for zz in range(34):
            editor.placeBlock((x-14,y+1+yy,z-15+zz),Block(q_id))
        for zz in range(2):
            editor.placeBlock((x-13,y+1+yy,z-3-zz),Block(w_id))
            editor.placeBlock((x - 13, y + 1 + yy, z - 10 - zz), Block(w_id))
            editor.placeBlock((x - 13, y + 1 + yy, z + 3 + zz), Block(w_id))
            editor.placeBlock((x - 13, y + 1 + yy, z + 10 + zz), Block(w_id))
        for zz in range(3):
            editor.placeBlock((x-13,y+1+yy,z-6-zz),Block(w_id))
            editor.placeBlock((x - 13, y + 1 + yy, z + 6 + zz), Block(w_id))
        editor.placeBlock((x - 12, y + 1 + yy, z -2), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z - 5), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z - 9), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z - 12), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z + 2), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z + 5), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z + 9), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z + 12), Block(e_id))

        editor.placeBlock((x - 11, y + 6, z + 2), Block(r_id,{"face":"ceiling","facing":"west"}))
        editor.placeBlock((x - 11, y + 6, z + 5), Block(r_id, {"face": "ceiling", "facing": "west"}))
        editor.placeBlock((x - 11, y + 6, z + 9), Block(r_id, {"face": "ceiling", "facing": "west"}))
        editor.placeBlock((x - 11, y + 6, z - 2), Block(r_id, {"face": "ceiling", "facing": "west"}))
        editor.placeBlock((x - 11, y + 6, z - 5), Block(r_id, {"face": "ceiling", "facing": "west"}))
        editor.placeBlock((x - 11, y + 6, z - 9), Block(r_id, {"face": "ceiling", "facing": "west"}))

        editor.placeBlock((x - 11, y + 5, z + 2), Block(t_id, {"hanging":"true"}))
        editor.placeBlock((x - 11, y + 5, z + 5), Block(t_id, {"hanging":"true"}))
        editor.placeBlock((x - 11, y + 5, z + 9), Block(t_id, {"hanging":"true"}))
        editor.placeBlock((x - 11, y + 5, z - 2), Block(t_id, {"hanging":"true"}))
        editor.placeBlock((x - 11, y + 5, z - 5), Block(t_id, {"hanging":"true"}))
        editor.placeBlock((x - 11, y + 5, z - 9), Block(t_id, {"hanging":"true"}))


def wall2(x,y,z,q_id,w_id,e_id,r_id):
    for yy in range(7):
        editor.placeBlock((x-2,y+1+yy,z-12),Block(e_id))
        editor.placeBlock((x + 2, y + 1 + yy, z - 12), Block(e_id))
        editor.placeBlock((x - 12, y + 1 + yy, z - 12), Block(e_id))
        editor.placeBlock((x + 12, y + 1 + yy, z - 12), Block(e_id))

        for xx in range(3):
            editor.placeBlock((x - 1+xx, y + 1 + yy, z - 13), Block(r_id,{"facing":"south"}))
        for xx in range(25):
            editor.placeBlock((x-12+xx,y+1+yy,z-15),Block(q_id))
    for yy in range(6):
        for xx in range(9):
            editor.placeBlock((x - 11 + xx, y + 1 + yy, z - 14), Block(w_id,{"facing":"east","type":"left"}))
            editor.placeBlock((x - 11 + xx, y + 1 + yy, z - 13), Block(w_id, {"facing": "east", "type": "right"}))
            editor.placeBlock((x +3 + xx, y + 1 + yy, z - 14), Block(w_id, {"facing": "east", "type": "left"}))
            editor.placeBlock((x +3 + xx, y + 1 + yy, z - 13), Block(w_id, {"facing": "east", "type": "right"}))

def wall3(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id,o_id):
    for yy in range(7):
        editor.placeBlock((x+12,y+1+yy,z-2),Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z - 5), Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z - 9), Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z - 12), Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z + 2), Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z + 5), Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z + 9), Block(q_id))
        editor.placeBlock((x + 12, y + 1 + yy, z + 12), Block(q_id))
        for zz in range(2):
            editor.placeBlock((x+13,y+1+yy,z-10-zz),Block(w_id))
            editor.placeBlock((x + 13, y + 1 + yy, z - 3 - zz), Block(w_id))
            editor.placeBlock((x + 13, y + 1 + yy, z +3+ zz), Block(w_id))
            editor.placeBlock((x + 13, y + 1 + yy, z + 10 + zz), Block(w_id))
        for zz in range(3):
            editor.placeBlock((x+16,y+1+yy,z-1+zz),Block(w_id))
        for xx in range(3):
            editor.placeBlock((x+13+xx,y+1+yy,z-2),Block(w_id))
            editor.placeBlock((x + 13 + xx, y + 1 + yy, z + 2), Block(w_id))
            editor.placeBlock((x - 1 + xx, y + 1 + yy, z + 12), Block(w_id))
            editor.placeBlock((x + 13 + xx, y + 1 + yy, z - 4), Block(w_id))
            editor.placeBlock((x + 13 + xx, y + 1 + yy, z - 10), Block(w_id))
    editor.placeBlock((x+14,y+1,z),Block(e_id))
    for zz in range(3):
        editor.placeBlock((x+13,y+1,z+6+zz),Block(r_id,{"facing":"west"}))
        editor.placeBlock((x+13,y+2,z+6+zz),Block(t_id,{"facing":"west"}))
        editor.placeBlock((x + 13, y + 3, z + 6 + zz), Block(y_id, {"facing": "west"}))
        editor.placeBlock((x + 13, y + 4, z + 6 + zz), Block(u_id, {"facing": "west"}))

        editor.placeBlock((x+16,y+1,z-6-zz),Block(i_id))

        editor.placeBlock((x + 14, y + 1, z - 6 - zz), Block(o_id,{"facing":"east","part":"foot"}))
        editor.placeBlock((x + 15, y + 1, z - 6 - zz), Block(o_id, {"facing": "east", "part": "head"}))
        for yy in range(2):
            editor.placeBlock((x + 13, y + 5+yy, z + 6 + zz), Block(r_id, {"facing": "west"}))
            editor.placeBlock((x + 16, y + 6+yy, z - 6 - zz), Block(i_id))
    for zz in range(4):
        for yy in range(7):
            editor.placeBlock((x+13+xx,y+1+yy,z-5),Block(i_id))
            editor.placeBlock((x + 13 + xx, y + 1 + yy, z - 9), Block(i_id))

def lantern(x,y,z,q_id,w_id):
    editor.placeBlock((x+14,y+6,z),Block(q_id,{"face":"ceiling","facing":"east"}))
    editor.placeBlock((x + 14, y + 5, z), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 14, y + 6, z - 7), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 14, y + 5, z - 7), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 11, y + 6, z-2), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 11, y + 5, z-2), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 11, y + 6, z - 5), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 11, y + 5, z - 5), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 11, y + 6, z - 9), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 11, y + 5, z - 9), Block(w_id, {"hanging": "true"}))

    editor.placeBlock((x + 11, y + 6, z +2), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 11, y + 5, z +2), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 11, y + 6, z +5), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 11, y + 5, z +5), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 11, y + 6, z +9), Block(q_id, {"face": "ceiling", "facing": "east"}))
    editor.placeBlock((x + 11, y + 5, z +9), Block(w_id, {"hanging": "true"}))

    editor.placeBlock((x + 2, y + 6, z+11), Block(q_id, {"face": "ceiling", "facing": "south"}))
    editor.placeBlock((x + 2, y + 5, z+11), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x - 2, y + 6, z + 11), Block(q_id, {"face": "ceiling", "facing": "south"}))
    editor.placeBlock((x - 2, y + 5, z + 11), Block(w_id, {"hanging": "true"}))

    editor.placeBlock((x + 3, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x + 6, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x + 8, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x + 11, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x - 3, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x - 5, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x - 9, y + 2, z + 12), Block(w_id))
    editor.placeBlock((x - 11, y + 2, z + 12), Block(w_id))

    editor.placeBlock((x - 2, y + 6, z - 7), Block(w_id, {"hanging": "true"}))
    editor.placeBlock((x + 2, y + 6, z - 7), Block(w_id, {"hanging": "true"}))
def wall4(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id):
    for yy in range(7):
        editor.placeBlock((x+2,y+1+yy,z+12),Block(w_id))
        editor.placeBlock((x - 2, y + 1 + yy, z + 12), Block(w_id))
        editor.placeBlock((x + 7, y + 1 + yy, z + 12), Block(w_id))
        editor.placeBlock((x + 12, y + 1 + yy, z + 12), Block(w_id))
        for xx in range(9):
            editor.placeBlock((x+3+xx,y+1+yy,z+18),Block(q_id))
        for zz in range(6):
            editor.placeBlock((x+12,y+1+yy,z+13+zz),Block(q_id))
            editor.placeBlock((x + 2, y + 1 + yy, z + 13 + zz), Block(q_id))
            editor.placeBlock((x -2, y + 1 + yy, z + 13 + zz), Block(q_id))
            editor.placeBlock((x - 12, y + 1 + yy, z + 13 + zz), Block(q_id))
    for xx in range(5):
        for zz in range(6):
            editor.placeBlock((x+8,y,z+13+zz),Block(e_id))
            editor.placeBlock((x + 8+xx, y, z + 13 + zz), Block(e_id))
            editor.placeBlock((x + 3+xx, y, z + 13 + zz), Block(e_id))
    for xx in range(9):
        editor.placeBlock((x-3-xx,y+1,z+12),Block(r_id))
        for zz in range(5):
            for yy in range(2):
                editor.placeBlock((x-3-xx,y-1+yy,z+13+zz),Block(y_id))
    for xx in range(4):
        editor.placeBlock((x+3+xx,y+1,z+12),Block(r_id))
        editor.placeBlock((x + 8 + xx, y + 1, z + 12), Block(r_id))
    editor.placeBlock((x-7,y+1,z+12),Block(t_id,{"facing":"south"}))
    editor.placeBlock((x + 10, y + 1, z + 12), Block(t_id, {"facing": "south"}))
    editor.placeBlock((x + 5, y + 1, z + 12), Block(t_id, {"facing": "south"}))
    for zz in range(5):
        editor.placeBlock((x+7,y+1,z+13+zz),Block(q_id))
    for yy in range(7):
        for xx in range(9):
            for zz in range(2):
                editor.placeBlock((x - 3 - xx, y + yy, z + 18 + zz), Block(q_id))

def window(x,y,z,q_id,w_id,e_id,t_id):
    for xx in range(2):
        editor.placeBlock((x + 4+xx, y + 2, z + 18), Block(w_id, {"facing":"south","half": "top","shape":"straight"}))
        editor.placeBlock((x + 9 + xx, y + 2, z + 18),Block(w_id, {"facing": "south", "half": "top", "shape": "straight"}))
        for yy in range(3):
            editor.placeBlock((x+4+xx,y+3+yy,z+19),Block(q_id))
            editor.placeBlock((x + 9 + xx, y + 3 + yy, z + 19), Block(q_id))
        for yy in range(2):
            editor.placeBlock((x + 4 + xx, y + 3 + yy, z + 18), Block(t_id))
            editor.placeBlock((x + 9 + xx, y + 3 + yy, z + 18), Block(t_id))
    for yy in range(3):
        for xx in range(5):
            editor.placeBlock((x - 5 - xx, y + 3 + yy, z + 19), Block(q_id))
        for xx in range(3):
            editor.placeBlock((x - 6 - xx, y + 3 + yy, z + 18), Block(t_id))
    for zz in range(5):
        editor.placeBlock((x+7,y+2,z+13+zz),Block(e_id,{"type":"top"}))
    editor.placeBlock((x + 4, y + 5, z + 18),Block(w_id, {"facing":"west","half": "top","shape":"straight"}))
    editor.placeBlock((x + 5, y + 5, z + 18), Block(w_id, {"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x + 9, y + 5, z + 18), Block(w_id, {"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x + 10, y + 5, z + 18), Block(w_id, {"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 5, y + 5, z + 18), Block(w_id, {"facing": "east", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 5, y + 3, z + 18), Block(w_id, {"facing": "east", "half": "bottom", "shape": "straight"}))
    editor.placeBlock((x - 9, y + 5, z + 18), Block(w_id, {"facing": "west", "half": "top", "shape": "straight"}))
    editor.placeBlock((x - 9, y + 3, z + 18), Block(w_id, {"facing": "west", "half": "bottom", "shape": "straight"}))

    editor.placeBlock((x - 9, y + 4, z + 18), Block(t_id))
    editor.placeBlock((x - 5, y + 4, z + 18), Block(t_id))

def add(x,y,z,q_id,w_id,e_id,r_id):
    for zz in range(2):
        editor.placeBlock((x+12,y+7,z+11+zz),Block(q_id,{"axis":"z"}))
        editor.placeBlock((x + 12, y + 7, z - 11 - zz), Block(q_id, {"axis": "z"}))
        for yy in range(7):
            editor.placeBlock((x + 12, y +1+yy, z -13-zz),Block(q_id))
    for zz in range(7):
        for xx in range(4):
            editor.placeBlock((x + 13 + xx, y, z - 5 - zz), Block(q_id, {"axis": "z"}))
    for zz in range(3):
        editor.placeBlock((x + 13, y + 7, z + 6 + zz), Block(q_id, {"axis": "z"}))
        for xx in range(24):
            editor.placeBlock((x + 12 - xx, y, z - 15 + zz), Block(q_id, {"axis": "z"}))
        for yy in range(4):
            editor.placeBlock((x +16, y + 2+yy, z -6-zz), Block(w_id))
    for xx in range(3):
        for zz in range(34):
            editor.placeBlock((x-12-xx,y,z-15+zz),Block(q_id,{"axis":"z"}))
    for xx in range(9):
        for zz in range(5):
            editor.placeBlock((x-3-xx,y+1,z+13+zz),Block(r_id,{"age":"5"}))
    editor.placeBlock((x-7,y,z+15),Block(e_id))
    command = f"summon cow {x + 9} {y + 2} {z+14}"
    for i in range(4):
        runCommand(command)
    command = f"summon sheep {x + 5} {y + 2} {z + 14}"
    for i in range(4):
        runCommand(command)
    command = f"summon cat {x + 9} {y + 2} {z + 7}"
    for i in range(2):
        runCommand(command)


def well(x,y,z,q_id,w_id,e_id,r_id,t_id,y_id,u_id,i_id):
    for yy in range(12):
        for xx in range(3):
            for zz in range(3):
                editor.placeBlock((x-1+xx,y+9+yy,z-1+zz),Block(q_id))
        editor.placeBlock((x, y + 9 + yy, z), Block(w_id))
    for zz in range(3):
        editor.placeBlock((x+1,y+21,z-1+zz),Block(q_id))
        editor.placeBlock((x - 1, y + 21, z - 1 + zz), Block(q_id))
        editor.placeBlock((x + 1, y + 24, z - 1 + zz), Block(t_id))
        editor.placeBlock((x - 1, y + 24, z - 1 + zz), Block(t_id))
        editor.placeBlock((x,y+25,z-1+zz),Block(u_id,{"type":"bottom"}))
    editor.placeBlock((x+1, y + 25, z), Block(u_id, {"type": "bottom"}))
    editor.placeBlock((x - 1, y + 25, z), Block(u_id, {"type": "bottom"}))
    editor.placeBlock((x, y + 25, z), Block(u_id, {"type": "double"}))
    editor.placeBlock((x, y + 24, z - 1), Block(t_id))
    editor.placeBlock((x, y + 24, z + 1 ), Block(t_id))
    editor.placeBlock((x,y+21,z-1),Block(e_id,{"facing":"south","half":"bottom","shape":"straight"}))
    editor.placeBlock((x,y+21,z+1),Block(e_id,{"facing":"north","half":"bottom","shape":"straight"}))
    for yy in range(2):
        editor.placeBlock((x+1,y+22+yy,z+1),Block(r_id))
        editor.placeBlock((x - 1, y + 22 + yy, z + 1), Block(r_id))
        editor.placeBlock((x - 1, y + 22 + yy, z - 1), Block(r_id))
        editor.placeBlock((x + 1, y + 22 + yy, z - 1), Block(r_id))
    editor.placeBlock((x+1, y + 25, z + 1), Block(y_id, {"facing": "north", "half": "bottom"}))
    editor.placeBlock((x - 1, y + 25, z + 1), Block(y_id, {"facing": "north", "half": "bottom"}))
    editor.placeBlock((x - 1, y + 25, z - 1), Block(y_id, {"facing": "north", "half": "bottom"}))
    editor.placeBlock((x + 1, y + 25, z - 1), Block(y_id, {"facing": "north", "half": "bottom"}))
    editor.placeBlock((x,y+24,z),Block(i_id,{"face":"ceiling","facing":"south"}))


def Basement(x,y,z):
    air(x,y-20,z,"air")
    floor(x,y-20,z,"stripped_dark_oak_log","dark_oak_trapdoor","spruce_planks","stone_bricks")
    wall1(x,y-20,z,"spruce_planks","bookshelf","stripped_dark_oak_log","grindstone","lantern")
    wall2(x,y-20,z,"spruce_planks","chest","stripped_dark_oak_log","barrel")
    wall3(x,y-20,z,"stripped_dark_oak_log","bookshelf","enchanting_table","barrel","blast_furnace","smoker","furnace","spruce_planks","red_bed")
    wall4(x,y-20,z,"spruce_planks","stripped_dark_oak_log","grass_block","spruce_fence","spruce_fence_gate","farmland")
    ceiling(x,y-20,z,"stone","dark_oak_slab","stripped_dark_oak_log","dark_oak_trapdoor")
    entrance(x, y-20, z, "scaffolding", "stone_bricks", "stone_brick_stairs", "stone", "cobblestone_wall", "lantern")
    lantern(x,y-20,z,"grindstone","lantern")
    window(x,y-20,z,"glass","spruce_stairs","spruce_slab","air")
    add(x,y-20,z,"stripped_dark_oak_log","glass","water","wheat")
    well(x,y-20,z,"stone_bricks","water","mossy_stone_brick_stairs","mossy_stone_brick_wall","jungle_fence","spruce_trapdoor","spruce_slab","grindstone")

