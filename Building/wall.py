from gdpc import Editor,Block
from interfaceUtils import runCommand

editor = Editor(buffering=True)


def buildHouse(x, y, z, t_id, w_id,r_id,q_id,p_id):
    def wall(x,y,z):
        for yy in range(12):
            for xx in range(11):
                for zz in range(27):
                    editor.placeBlock((x-5+xx,y+yy,z+zz),Block("air"))

        for xx in range(12):
            for zz in range(27):
                for yy in range(16):
                    editor.placeBlock((x+6+xx,y+yy,z+zz),Block(t_id))
                    editor.placeBlock((x-6-xx,y+yy,z+zz),Block(t_id))

        for xx in range(6):
            for yy in range(4):
                for zz in range(27):
                    editor.placeBlock((x+xx,y+12+yy,z+zz),Block(t_id))
                    editor.placeBlock((x-xx,y+12+yy,z+zz),Block(t_id))


    def door(x,y,z):
        for zz in range(27):

            editor.placeBlock((x,y+11,z+zz),Block(r_id,{"type": "top"}))
            editor.placeBlock((x+2,y+10,z+zz),Block(r_id,{"type": "top"}))
            editor.placeBlock((x-2,y+10,z+zz),Block(r_id,{"type": "top"}))
            editor.placeBlock((x+4,y+9,z+zz),Block(r_id,{"type": "top"}))
            editor.placeBlock((x-4,y+9,z+zz),Block(r_id,{"type": "top"}))

            for yy in range(11):
                editor.placeBlock((x+5,y+yy,z+zz),Block(w_id))
                editor.placeBlock((x-5,y+yy,z+zz),Block(w_id))
            for xx in range(5):

                editor.placeBlock((x+1+xx,y+11,z+zz),Block(w_id))
                editor.placeBlock((x-1-xx,y+11,z+zz),Block(w_id))
            for xx in range(2):

                editor.placeBlock((x+3+xx,y+10,z+zz),Block(w_id))
                editor.placeBlock((x-3-xx,y+10,z+zz),Block(w_id))

        for xx in range(5):
            for zz in range(14):
                editor.placeBlock((x+xx,y+8,z+2*zz),Block(w_id))
                editor.placeBlock((x-xx,y+8,z+2*zz),Block(w_id))

    


    wall(x,y,z)
    door(x,y,z)
    
    

def stairs1(x,y,z,t_id,q_id,p_id):
    

    def stairs_l(x,y,z):
        h=0
        for xx in range(20):
            h=h+1
            for zz in range(7):
                for yy in range(20-h):
                    editor.placeBlock((x+xx,y-4+yy,z+1+zz),Block(t_id))
            for yyy in range(22-h):
                editor.placeBlock((x+xx,y-4+yyy,z),Block(t_id))
                editor.placeBlock((x+xx,y-4+yyy,z+8),Block(t_id))

        h=19
        for xx in range(20):
            if h != -1:
                for zz in range(7):                           
                    editor.placeBlock((x+xx,y-4+h,z+1+zz),Block(q_id,{"facing": "west", "half": "bottom"}))
                h=h-1


    def wall_l(x,y,z):
        for xx in range(17):
            for yy in range(16):
                for zz in range(11):
                    editor.placeBlock((x+xx,y+yy,z+zz),Block(t_id))

        for xx in range(9):
            editor.placeBlock((x+2*xx,y+16,z),Block(p_id,{"type": "top"}))
            editor.placeBlock((x+2*xx,y+16,z+10),Block(p_id,{"type": "top"}))
        for xx in range(8):
            for yy in range(2):
                editor.placeBlock((x+1+2*xx,y+16+yy,z),Block(t_id))
                editor.placeBlock((x+1+2*xx,y+16+yy,z+10),Block(t_id))


    def stairs_r(x,y,z):
        h=0
        for xx in range(20):
            h=h+1
            for zz in range(7):
                for yy in range(20-h):
                    editor.placeBlock((x-xx,y-4+yy,z+1+zz),Block(t_id))
            for yyy in range(22-h):
                editor.placeBlock((x-xx,y-4+yyy,z),Block(t_id))
                editor.placeBlock((x-xx,y-4+yyy,z+8),Block(t_id))

        h=19
        for xx in range(20):
            if h != -1:
                for zz in range(7):                           
                    editor.placeBlock((x-xx,y-4+h,z+1+zz),Block(q_id,{"facing": "east", "half": "bottom"}))
                h=h-1


    def wall_r(x,y,z):
        for xx in range(17):
            for yy in range(16):
                for zz in range(11):
                    editor.placeBlock((x-xx,y+yy,z+zz),Block(t_id))

        for xx in range(9):
            editor.placeBlock((x-2*xx,y+16,z),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-2*xx,y+16,z+10),Block(p_id,{"type": "top"}))
        for xx in range(8):
            for yy in range(2):
                editor.placeBlock((x-1-2*xx,y+16+yy,z),Block(t_id))
                editor.placeBlock((x-1-2*xx,y+16+yy,z+10),Block(t_id))

    def wall_n(x,y,z):

        for xx in range(9):
            editor.placeBlock((x+2*xx,y,z),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-2*xx,y,z),Block(p_id,{"type": "top"}))
            for yy in range(2):
                editor.placeBlock((x+1+2*xx,y+yy,z),Block(t_id))
                editor.placeBlock((x-1-2*xx,y+yy,z),Block(t_id))
        for xx in range(9):
            editor.placeBlock((x+2*xx,y,z+26),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-2*xx,y,z+26),Block(p_id,{"type": "top"}))
            for yy in range(2):
                editor.placeBlock((x+1+2*xx,y+yy,z+26),Block(t_id))
                editor.placeBlock((x-1-2*xx,y+yy,z+26),Block(t_id))

        for zz in range(3):
            editor.placeBlock((x+17,y,z+21+2*zz),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-17,y,z+21+2*zz),Block(p_id,{"type": "top"}))
            for yy in range(2):
                editor.placeBlock((x+17,y+yy,z+20+2*zz),Block(t_id))
                editor.placeBlock((x-17,y+yy,z+20+2*zz),Block(t_id))
                editor.placeBlock((x+17,y+yy,z+10),Block(t_id))
                editor.placeBlock((x-17,y+yy,z+10),Block(t_id))


    stairs_l(x+18,y,z+1)
    stairs_r(x-18,y,z+1)
    wall_l(x+18,y,z+10)
    wall_r(x-18,y,z+10)
    wall_n(x,y+16,z)
def stairs2(x,y,z,t_id,q_id,p_id):
    

    def stairs_l(x,y,z):
        h=0
        for xx in range(20):
            h=h+1
            for zz in range(7):
                for yy in range(20-h):
                    editor.placeBlock((x+xx,y-4+yy,z+1+zz),Block(t_id))
            for yyy in range(22-h):
                editor.placeBlock((x+xx,y-4+yyy,z),Block(t_id))
                editor.placeBlock((x+xx,y-4+yyy,z+8),Block(t_id))

        h=19
        for xx in range(20):
            if h != -1:
                for zz in range(7):                           
                    editor.placeBlock((x+xx,y-4+h,z+1+zz),Block(q_id,{"facing": "west", "half": "bottom"}))
                h=h-1


    def wall_l(x,y,z):
        for xx in range(17):
            for yy in range(16):
                for zz in range(11):
                    editor.placeBlock((x+xx,y+yy,z+zz),Block(t_id))

        for xx in range(9):
            editor.placeBlock((x+2*xx,y+16,z),Block(p_id,{"type": "top"}))
            editor.placeBlock((x+2*xx,y+16,z+10),Block(p_id,{"type": "top"}))
        for xx in range(8):
            for yy in range(2):
                editor.placeBlock((x+1+2*xx,y+16+yy,z),Block(t_id))
                editor.placeBlock((x+1+2*xx,y+16+yy,z+10),Block(t_id))


    def stairs_r(x,y,z):
        h=0
        for xx in range(20):
            h=h+1
            for zz in range(7):
                for yy in range(20-h):
                    editor.placeBlock((x-xx,y-4+yy,z+1+zz),Block(t_id))
            for yyy in range(22-h):
                editor.placeBlock((x-xx,y-4+yyy,z),Block(t_id))
                editor.placeBlock((x-xx,y-4+yyy,z+8),Block(t_id))

        h=19
        for xx in range(20):
            if h != -1:
                for zz in range(7):                           
                    editor.placeBlock((x-xx,y-4+h,z+1+zz),Block(q_id,{"facing": "east", "half": "bottom"}))
                h=h-1


    def wall_r(x,y,z):
        for xx in range(17):
            for yy in range(16):
                for zz in range(11):
                    editor.placeBlock((x-xx,y+yy,z+zz),Block(t_id))

        for xx in range(9):
            editor.placeBlock((x-2*xx,y+16,z),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-2*xx,y+16,z+10),Block(p_id,{"type": "top"}))
        for xx in range(8):
            for yy in range(2):
                editor.placeBlock((x-1-2*xx,y+16+yy,z),Block(t_id))
                editor.placeBlock((x-1-2*xx,y+16+yy,z+10),Block(t_id))

    def wall_n(x,y,z):

        for xx in range(9):
            editor.placeBlock((x+2*xx,y,z),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-2*xx,y,z),Block(p_id,{"type": "top"}))
            for yy in range(2):
                editor.placeBlock((x+1+2*xx,y+yy,z),Block(t_id))
                editor.placeBlock((x-1-2*xx,y+yy,z),Block(t_id))
        for xx in range(9):
            editor.placeBlock((x+2*xx,y,z+26),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-2*xx,y,z+26),Block(p_id,{"type": "top"}))
            for yy in range(2):
                editor.placeBlock((x+1+2*xx,y+yy,z+26),Block(t_id))
                editor.placeBlock((x-1-2*xx,y+yy,z+26),Block(t_id))

        for zz in range(3):
            editor.placeBlock((x+17,y,z+1+2*zz),Block(p_id,{"type": "top"}))
            editor.placeBlock((x-17,y,z+1+2*zz),Block(p_id,{"type": "top"}))
            for yy in range(2):
                editor.placeBlock((x+17,y+yy,z+2+2*zz),Block(t_id))
                editor.placeBlock((x-17,y+yy,z+2+2*zz),Block(t_id))
                editor.placeBlock((x+17,y+yy,z+16),Block(t_id))
                editor.placeBlock((x-17,y+yy,z+16),Block(t_id))


    stairs_l(x+18,y,z+17)
    stairs_r(x-18,y,z+17)
    wall_l(x+18,y,z+6)
    wall_r(x-18,y,z+6)
    wall_n(x,y+16,z)
def buildlou(x,y,z,q_id,w_id,e_id):

    for xx in range(14):
        for zz in range(10):
            editor.placeBlock((x+xx,y,z+zz),Block(q_id))
            editor.placeBlock((x-xx,y,z+zz),Block(q_id))
            editor.placeBlock((x+xx,y,z-zz),Block(q_id))
            editor.placeBlock((x-xx,y,z-zz),Block(q_id))

    def zhuzi_w(x,y,z):

        editor.placeBlock((x+3,y,z-2),Block(w_id))
        editor.placeBlock((x+9,y,z-2),Block(w_id))
        editor.placeBlock((x+13,y,z-2),Block(w_id))

        editor.placeBlock((x-3,y,z-2),Block(w_id))
        editor.placeBlock((x-9,y,z-2),Block(w_id))
        editor.placeBlock((x-13,y,z-2),Block(w_id))

        editor.placeBlock((x+3,y,z+2),Block(w_id))
        editor.placeBlock((x+9,y,z+2),Block(w_id))
        editor.placeBlock((x+13,y,z+2),Block(w_id))

        editor.placeBlock((x-3,y,z+2),Block(w_id))
        editor.placeBlock((x-9,y,z+2),Block(w_id))
        editor.placeBlock((x-13,y,z+2),Block(w_id))

        for yy in range(12):
            editor.placeBlock((x+3,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x+9,y+1+yy,z-2),Block(e_id))
 
            editor.placeBlock((x-3,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x-9,y+1+yy,z-2),Block(e_id))

        for yy in range(5):
            editor.placeBlock((x+3,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x+9,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x+13,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x+13,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x-3,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x-9,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x-13,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x-13,y+1+yy,z-2),Block(e_id))
        for zz in range(5):
            for xx in range(4):
                editor.placeBlock((x-9+6*xx,y+5,z-1+zz),Block(e_id))
        for xx in range(29):
            editor.placeBlock((x-14+xx,y+6,z+2),Block(e_id))
         

    def zhuzi_n(x,y,z):

        editor.placeBlock((x+3,y,z-2),Block(w_id))
        editor.placeBlock((x+9,y,z-2),Block(w_id))
        editor.placeBlock((x+13,y,z-2),Block(w_id))

        editor.placeBlock((x-3,y,z-2),Block(w_id))
        editor.placeBlock((x-9,y,z-2),Block(w_id))
        editor.placeBlock((x-13,y,z-2),Block(w_id))

        editor.placeBlock((x+3,y,z+2),Block(w_id))
        editor.placeBlock((x+9,y,z+2),Block(w_id))
        editor.placeBlock((x+13,y,z+2),Block(w_id))

        editor.placeBlock((x-3,y,z+2),Block(w_id))
        editor.placeBlock((x-9,y,z+2),Block(w_id))
        editor.placeBlock((x-13,y,z+2),Block(w_id))

        for yy in range(12):
            editor.placeBlock((x-3,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x-9,y+1+yy,z+2),Block(e_id))
 
            editor.placeBlock((x+3,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x+9,y+1+yy,z+2),Block(e_id))

        for yy in range(5):
            editor.placeBlock((x+3,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x+9,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x+13,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x+13,y+1+yy,z+2),Block(e_id))
            editor.placeBlock((x-3,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x-9,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x-13,y+1+yy,z-2),Block(e_id))
            editor.placeBlock((x-13,y+1+yy,z+2),Block(e_id))
        for zz in range(5):
            for xx in range(4):
                editor.placeBlock((x-9+6*xx,y+5,z+1-zz),Block(e_id))
        for xx in range(5):
            editor.placeBlock((x+10+xx,y+5,z+2),Block(e_id))
            editor.placeBlock((x+10+xx,y+5,z+12),Block(e_id))
            editor.placeBlock((x-10-xx,y+5,z+2),Block(e_id))
            editor.placeBlock((x-10-xx,y+5,z+12),Block(e_id))
        for xx in range(29):
            editor.placeBlock((x-14+xx,y+6,z-2),Block(e_id))
        for zz in range(21):
            editor.placeBlock((x-13,y+6,z-3+zz),Block(e_id))
            editor.placeBlock((x+13,y+6,z-3+zz),Block(e_id))

    zhuzi_w(x,y+1,z+7)
    zhuzi_n(x,y+1,z-7)

def buildhen(x,y,z,q_id,w_id,e_id):
    def zhuzi_w(x,y,z):

        for xx in range(21):
            editor.placeBlock((x-10+xx,y,z-2),Block(q_id))
        
    def zhuzi_n(x,y,z):

        for xx in range(21):
            editor.placeBlock((x-10+xx,y,z+2),Block(q_id))
        for zz in range(13):
            editor.placeBlock((x-9,y,z+1+zz),Block(q_id))
            editor.placeBlock((x-3,y,z+1+zz),Block(q_id))
            editor.placeBlock((x+9,y,z+1+zz),Block(q_id))
            editor.placeBlock((x+3,y,z+1+zz),Block(q_id))


    def wuding_1(x,y,z):
        for xx in range(26):
            for zz in range(17):
                editor.placeBlock((x+xx,y,z+zz),Block(w_id))
    def wuding_2(x,y,z):
        for xx in range(20):
            for zz in range(11):
                editor.placeBlock((x+xx,y,z+zz),Block(w_id))
    def wuding_3(x,y,z):
        for xx in range(20):
            for zz in range(7):
                editor.placeBlock((x+xx,y,z+zz),Block(w_id))
    def wuding_4(x,y,z):
        for xx in range(20):
            for zz in range(5):
                editor.placeBlock((x+xx,y,z+zz),Block(w_id))
    def wuding_5(x,y,z):
        for xx in range(20):
            for zz in range(3):
                editor.placeBlock((x+xx,y,z+zz),Block(w_id))
    for xx in range(20):
        editor.placeBlock((x-10+xx,y+20,z),Block(w_id))
    for xx in range(18):
        for yy in range(2):
            editor.placeBlock((x-9+xx,y+21+yy,z),Block(e_id))
 
    zhuzi_w(x,y+14,z+7)
    zhuzi_n(x,y+14,z-7)
    wuding_1(x-13,y+15,z-8)
    wuding_2(x-10,y+16,z-5)
    wuding_3(x-10,y+17,z-3)
    wuding_4(x-10,y+18,z-2)
    wuding_5(x-10,y+19,z-1)

def buildwa(x,y,z,q_id,w_id,e_id):
    def wa1_1(x,y,z):
        for xx in range(10):
            editor.placeBlock((x+2*xx,y,z),Block(q_id))
            editor.placeBlock((x+2*xx,y-1,z-1),Block(q_id))
            editor.placeBlock((x+2*xx,y-2,z-2),Block(q_id))
            editor.placeBlock((x+2*xx,y+1,z),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y,z-1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-1,z-2),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-2,z-3),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x+2*xx,y-3,z-3-zz),Block(q_id))
                editor.placeBlock((x+2*xx,y-3,z-5-zz),Block(w_id,{"type": "bottom"}))
            for zz in range(4):
                editor.placeBlock((x+2*xx,y-4,z-5-zz),Block(q_id))
    def wa2_1(x,y,z):
        for xx in range(10):
            editor.placeBlock((x+2*xx,y,z),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-1,z-1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-2,z-2),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-3,z-3),Block(q_id))
            editor.placeBlock((x+2*xx,y-4,z-5),Block(q_id))
            editor.placeBlock((x+2*xx,y-3,z-4),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-5,z-8),Block(w_id,{"type": "top"}))
            for zz in range(2):
                editor.placeBlock((x+2*xx,y-4,z-6-zz),Block(w_id,{"type": "bottom"}))

    def wa1_2(x,y,z):
        for xx in range(10):
            editor.placeBlock((x+2*xx,y,z),Block(q_id))
            editor.placeBlock((x+2*xx,y-1,z+1),Block(q_id))
            editor.placeBlock((x+2*xx,y-2,z+2),Block(q_id))
            editor.placeBlock((x+2*xx,y+1,z),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y,z+1),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-1,z+2),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-2,z+3),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            for zz in range(2):
                editor.placeBlock((x+2*xx,y-3,z+3+zz),Block(q_id))
                editor.placeBlock((x+2*xx,y-3,z+5+zz),Block(w_id,{"type": "bottom"}))
            for zz in range(4):
                editor.placeBlock((x+2*xx,y-4,z+5+zz),Block(q_id))
    def wa2_2(x,y,z):
        for xx in range(10):
            editor.placeBlock((x+2*xx,y,z),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-1,z+1),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-2,z+2),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
            editor.placeBlock((x+2*xx,y-3,z+3),Block(q_id))
            editor.placeBlock((x+2*xx,y-4,z+5),Block(q_id))
            editor.placeBlock((x+2*xx,y-3,z+4),Block(w_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-5,z+8),Block(w_id,{"type": "top"}))
            for zz in range(2):
                editor.placeBlock((x+2*xx,y-4,z+6+zz),Block(w_id,{"type": "bottom"}))
    def wa1_3(x,y,z):
        for zz in range(8):
            for xx in range(4):
                editor.placeBlock((x-xx,y,z+2*zz),Block(q_id))
            for xx in range(2):
                editor.placeBlock((x-xx,y+1,z+2*zz),Block(w_id,{"type": "bottom"}))
    def wa2_3(x,y,z):
        for zz in range(7):
            editor.placeBlock((x,y,z+2*zz),Block(q_id))
            editor.placeBlock((x-3,y-1,z+2*zz),Block(w_id,{"type": "top"}))
            for xx in range(2):
                editor.placeBlock((x-1-xx,y,z+2*zz),Block(w_id,{"type": "bottom"}))
    def wa1_4(x,y,z):
        for zz in range(8):
            for xx in range(4):
                editor.placeBlock((x+xx,y,z+2*zz),Block(q_id))
            for xx in range(2):
                editor.placeBlock((x+xx,y+1,z+2*zz),Block(w_id,{"type": "bottom"}))
    def wa2_4(x,y,z):
        for zz in range(7):
            editor.placeBlock((x,y,z+2*zz),Block(q_id))
            editor.placeBlock((x+3,y-1,z+2*zz),Block(w_id,{"type": "top"}))
            for xx in range(2):
                editor.placeBlock((x+1+xx,y,z+2*zz),Block(w_id,{"type": "bottom"}))
    for zz in range(2):
        editor.placeBlock((x-11,y-4,z+8+zz),Block(q_id))
        editor.placeBlock((x-11,y-4,z-8-zz),Block(q_id))
    editor.placeBlock((x-12,y-4,z-8),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-12,y-5,z-9),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-12,y-4,z+8),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x-12,y-5,z+9),Block(w_id,{"type": "top"}))
    for zz in range(2):
        editor.placeBlock((x+11,y-4,z+8+zz),Block(q_id))
        editor.placeBlock((x+11,y-4,z-8-zz),Block(q_id))
    editor.placeBlock((x+10,y-4,z-8),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+10,y-5,z-9),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+10,y-4,z+8),Block(w_id,{"type": "bottom"}))
    editor.placeBlock((x+10,y-5,z+9),Block(w_id,{"type": "top"}))

    wa1_1(x-9,y,z-1)
    wa2_1(x-10,y,z-1)
    wa1_2(x-9,y,z+1)
    wa2_2(x-10,y,z+1)
    wa1_3(x-11,y-4,z-7)
    wa2_3(x-11,y-4,z-6)
    wa1_4(x+10,y-4,z-7)
    wa2_4(x+10,y-4,z-6)

def buildfeiyan(x,y,z,q_id,w_id,e_id,r_id):
    editor.placeBlock((x+10,y-2,z-6),Block(r_id,{"up": "true"}))
    editor.placeBlock((x+11,y-2,z-7),Block(r_id,{"up": "true"}))
    editor.placeBlock((x+12,y-2,z-8),Block(r_id,{"up": "true"}))
    editor.placeBlock((x+13,y-5,z-9),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+13,y-4,z-9),Block(q_id))
    editor.placeBlock((x+13,y-3,z-9),Block(r_id,{"up": "true"}))


    editor.placeBlock((x+10,y-2,z+6),Block(r_id,{"up": "true"}))
    editor.placeBlock((x+11,y-2,z+7),Block(r_id,{"up": "true"}))
    editor.placeBlock((x+12,y-2,z+8),Block(r_id,{"up": "true"}))
    editor.placeBlock((x+13,y-5,z+9),Block(w_id,{"type": "top"}))
    editor.placeBlock((x+13,y-4,z+9),Block(q_id))
    editor.placeBlock((x+13,y-3,z+9),Block(r_id,{"up": "true"}))

    editor.placeBlock((x-11,y-2,z-6),Block(r_id,{"up": "true"}))
    editor.placeBlock((x-12,y-2,z-7),Block(r_id,{"up": "true"}))
    editor.placeBlock((x-13,y-2,z-8),Block(r_id,{"up": "true"}))
    editor.placeBlock((x-14,y-5,z-9),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-14,y-4,z-9),Block(q_id))
    editor.placeBlock((x-14,y-3,z-9),Block(r_id,{"up": "true"}))

    editor.placeBlock((x-11,y-2,z+6),Block(r_id,{"up": "true"}))
    editor.placeBlock((x-12,y-2,z+7),Block(r_id,{"up": "true"}))
    editor.placeBlock((x-13,y-2,z+8),Block(r_id,{"up": "true"}))
    editor.placeBlock((x-14,y-5,z+9),Block(w_id,{"type": "top"}))
    editor.placeBlock((x-14,y-4,z+9),Block(q_id))
    editor.placeBlock((x-14,y-3,z+9),Block(r_id,{"up": "true"}))
    def feiyan1(x,y,z):
        for yy in range(2):
            editor.placeBlock((x,y+yy,z),Block(q_id))
            editor.placeBlock((x,y-1+yy,z-1),Block(q_id))
            editor.placeBlock((x,y-2+yy,z-2),Block(q_id))
            editor.placeBlock((x+2,y-4+yy,z-5),Block(q_id))
            editor.placeBlock((x+3,y-4+yy,z-6),Block(q_id))
            editor.placeBlock((x+4,y-4+yy,z-7),Block(q_id))
            for zz in range(2):
                editor.placeBlock((x,y-3+yy,z-3-zz),Block(q_id))
                editor.placeBlock((x,y-4+yy,z-5-zz),Block(q_id))
        editor.placeBlock((x,y+2,z),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z-1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-2),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-3),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    
    def feiyan2(x,y,z):
        for yy in range(2):
            editor.placeBlock((x,y+yy,z),Block(q_id))
            editor.placeBlock((x,y-1+yy,z+1),Block(q_id))
            editor.placeBlock((x,y-2+yy,z+2),Block(q_id))
            editor.placeBlock((x+2,y-4+yy,z+5),Block(q_id))
            editor.placeBlock((x+3,y-4+yy,z+6),Block(q_id))
            editor.placeBlock((x+4,y-4+yy,z+7),Block(q_id))
            for zz in range(2):
                editor.placeBlock((x,y-3+yy,z+3+zz),Block(q_id))
                editor.placeBlock((x,y-4+yy,z+5+zz),Block(q_id))
        editor.placeBlock((x,y+2,z),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z+1),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+2),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+3),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
    def feiyan3(x,y,z):
        for yy in range(2):
            editor.placeBlock((x,y+yy,z),Block(q_id))
            editor.placeBlock((x,y-1+yy,z-1),Block(q_id))
            editor.placeBlock((x,y-2+yy,z-2),Block(q_id))
            editor.placeBlock((x-2,y-4+yy,z-5),Block(q_id))
            editor.placeBlock((x-3,y-4+yy,z-6),Block(q_id))
            editor.placeBlock((x-4,y-4+yy,z-7),Block(q_id))
            for zz in range(2):
                editor.placeBlock((x,y-3+yy,z-3-zz),Block(q_id))
                editor.placeBlock((x,y-4+yy,z-5-zz),Block(q_id))
        editor.placeBlock((x,y+2,z),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z-1),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z-2),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z-3),Block(e_id,{"facing": "south", "half": "bottom", "shape": "straight"}))
    def feiyan4(x,y,z):
        for yy in range(2):
            editor.placeBlock((x,y+yy,z),Block(q_id))
            editor.placeBlock((x,y-1+yy,z+1),Block(q_id))
            editor.placeBlock((x,y-2+yy,z+2),Block(q_id))
            editor.placeBlock((x-2,y-4+yy,z+5),Block(q_id))
            editor.placeBlock((x-3,y-4+yy,z+6),Block(q_id))
            editor.placeBlock((x-4,y-4+yy,z+7),Block(q_id))
            for zz in range(2):
                editor.placeBlock((x,y-3+yy,z+3+zz),Block(q_id))
                editor.placeBlock((x,y-4+yy,z+5+zz),Block(q_id))
        editor.placeBlock((x,y+2,z),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y+1,z+1),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y,z+2),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x,y-1,z+3),Block(e_id,{"facing": "north", "half": "bottom", "shape": "straight"}))

    def shou_1(x,y,z):
        for xx in range(3):
            editor.placeBlock((x+xx,y,z),Block(q_id))
        editor.placeBlock((x+3,y,z),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+4,y,z),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y+1,z),Block(q_id))
        editor.placeBlock((x+3,y+1,z),Block(e_id,{"facing": "west", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"up": "true"}))
        editor.placeBlock((x+2,y+2,z),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+3,y+2,z),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-1,y-2,z),Block(q_id))
    def shou_2(x,y,z):
        for xx in range(3):
            editor.placeBlock((x-xx,y,z),Block(q_id))
        editor.placeBlock((x-3,y,z),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-4,y,z),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y+1,z),Block(q_id))
        editor.placeBlock((x-3,y+1,z),Block(e_id,{"facing": "east", "half": "top", "shape": "straight"}))
        editor.placeBlock((x,y+1,z),Block(r_id,{"up": "true"}))
        editor.placeBlock((x-2,y+2,z),Block(e_id,{"facing": "west", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x-3,y+2,z),Block(e_id,{"facing": "east", "half": "bottom", "shape": "straight"}))
        editor.placeBlock((x+1,y-2,z),Block(q_id))

    def xiaofeiyan1(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        editor.placeBlock((x-1,y-1,z+1),Block(q_id))
        editor.placeBlock((x-1,y,z+1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y-1,z+2),Block(q_id))
        editor.placeBlock((x-3,y-1,z+3),Block(q_id))
        editor.placeBlock((x-4,y-2,z+4),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-2,y,z+2),Block(r_id,{"up": "true"}))
        editor.placeBlock((x-3,y,z+3),Block(r_id,{"up": "true"}))
        editor.placeBlock((x-4,y-1,z+4),Block(r_id,{"up": "true"}))
    def xiaofeiyan2(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        editor.placeBlock((x-1,y-1,z-1),Block(q_id))
        editor.placeBlock((x-1,y,z-1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y-1,z-2),Block(q_id))
        editor.placeBlock((x-3,y-1,z-3),Block(q_id))
        editor.placeBlock((x-4,y-2,z-4),Block(w_id,{"type": "top"}))
        editor.placeBlock((x-2,y,z-2),Block(r_id,{"up": "true"}))
        editor.placeBlock((x-3,y,z-3),Block(r_id,{"up": "true"}))
        editor.placeBlock((x-4,y-1,z-4),Block(r_id,{"up": "true"}))
    def xiaofeiyan3(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        editor.placeBlock((x+1,y-1,z-1),Block(q_id))
        editor.placeBlock((x+1,y,z-1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y-1,z-2),Block(q_id))
        editor.placeBlock((x+3,y-1,z-3),Block(q_id))
        editor.placeBlock((x+4,y-2,z-4),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+2,y,z-2),Block(r_id,{"up": "true"}))
        editor.placeBlock((x+3,y,z-3),Block(r_id,{"up": "true"}))
        editor.placeBlock((x+4,y-1,z-4),Block(r_id,{"up": "true"}))
    def xiaofeiyan4(x,y,z):
        editor.placeBlock((x,y,z),Block(q_id))
        editor.placeBlock((x+1,y-1,z+1),Block(q_id))
        editor.placeBlock((x+1,y,z+1),Block(w_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y-1,z+2),Block(q_id))
        editor.placeBlock((x+3,y-1,z+3),Block(q_id))
        editor.placeBlock((x+4,y-2,z+4),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+2,y,z+2),Block(r_id,{"up": "true"}))
        editor.placeBlock((x+3,y,z+3),Block(r_id,{"up": "true"}))
        editor.placeBlock((x+4,y-1,z+4),Block(r_id,{"up": "true"}))
    feiyan1(x+8,y,z-1)
    feiyan2(x+8,y,z+1)
    feiyan3(x-9,y,z-1)
    feiyan4(x-9,y,z+1)
    shou_1(x-9,y+3,z)
    shou_2(x+8,y+3,z)
    xiaofeiyan1(x-13,y-10,z+9)
    xiaofeiyan2(x-13,y-10,z-9)
    xiaofeiyan3(x+13,y-10,z-9)
    xiaofeiyan4(x+13,y-10,z+9)
def buildxiawuding(x,y,z,q_id,w_id,e_id,r_id):
    def muliang_1(x,y,z):
        for xx in range(23):
            for zz in range(2):
                editor.placeBlock((x+xx,y,z+zz),Block(q_id))
    def muliang_2(x,y,z):
        for xx in range(23):
            for zz in range(2):
                editor.placeBlock((x+xx,y,z-zz),Block(q_id))
    def muliang_3(x,y,z):
        for xx in range(2):
            for zz in range(12):
                editor.placeBlock((x+xx,y,z+zz),Block(q_id))
    def muliang_4(x,y,z):
        for xx in range(2):
            for zz in range(12):
                editor.placeBlock((x-xx,y,z+zz),Block(q_id))

    def muliang2_1(x,y,z):
        for xx in range(27):
            for zz in range(6):
                editor.placeBlock((x+xx,y,z+zz),Block(q_id))
    def muliang2_2(x,y,z):
        for xx in range(27):
            for zz in range(6):
                editor.placeBlock((x+xx,y,z-zz),Block(q_id))
    def muliang2_3(x,y,z):
        for xx in range(6):
            for zz in range(16):
                editor.placeBlock((x+xx,y,z+zz),Block(q_id))
    def muliang2_4(x,y,z):
        for xx in range(6):
            for zz in range(16):
                editor.placeBlock((x-xx,y,z+zz),Block(q_id))

    def muliang3_1(x,y,z):
        for xx in range(33):
            for zz in range(12):
                editor.placeBlock((x+xx,y,z+zz),Block(q_id))
    def muliang3_2(x,y,z):
        for xx in range(33):
            for zz in range(12):
                editor.placeBlock((x+xx,y,z-zz),Block(q_id))
    def muliang3_3(x,y,z):
        for xx in range(12):
            for zz in range(22):
                editor.placeBlock((x+xx,y,z+zz),Block(q_id))
    def muliang3_4(x,y,z):
        for xx in range(12):
            for zz in range(22):
                editor.placeBlock((x-xx,y,z+zz),Block(q_id))
    def qiang(x,y,z):
        for yy in range(2):
            for xx in range(19):
                editor.placeBlock((x+xx,y+yy,z),Block(w_id))
                editor.placeBlock((x+xx,y+yy,z+12),Block(w_id))
            for zz in range(13):
                editor.placeBlock((x-1,y+yy,z+zz),Block(w_id))
                editor.placeBlock((x+19,y+yy,z+zz),Block(w_id))

    def wa1_1(x,y,z):
        for xx in range(13):
            editor.placeBlock((x+2*xx,y,z),Block(w_id))
            editor.placeBlock((x+2*xx,y+1,z),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y,z-2),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-1,z-4),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y,z-1),Block(w_id))
            editor.placeBlock((x+2*xx,y-1,z-3),Block(w_id))
            editor.placeBlock((x+2*xx,y-2,z-6),Block(e_id,{"type": "bottom"}))
            for zz in range(3):
                editor.placeBlock((x+2*xx,y-1,z-1-zz),Block(w_id))
                editor.placeBlock((x+2*xx,y-2,z-3-zz),Block(w_id))
                
    def wa1_2(x,y,z):
        for xx in range(12):
            editor.placeBlock((x+2*xx,y,z),Block(w_id))
            editor.placeBlock((x+2*xx,y-1,z-1),Block(w_id))
            editor.placeBlock((x+2*xx,y,z-1),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-1,z-2),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-2,z-5),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-3,z-6),Block(e_id,{"type": "top"}))
            for zz in range(2):
                editor.placeBlock((x+2*xx,y-2,z-3-zz),Block(w_id))
    def wa2_1(x,y,z):
        for xx in range(13):
            editor.placeBlock((x+2*xx,y,z),Block(w_id))
            editor.placeBlock((x+2*xx,y+1,z),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y,z+2),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-1,z+4),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y,z+1),Block(w_id))
            editor.placeBlock((x+2*xx,y-1,z+3),Block(w_id))
            editor.placeBlock((x+2*xx,y-2,z+6),Block(e_id,{"type": "bottom"}))
            for zz in range(3):
                editor.placeBlock((x+2*xx,y-1,z+1+zz),Block(w_id))
                editor.placeBlock((x+2*xx,y-2,z+3+zz),Block(w_id))
                
    def wa2_2(x,y,z):
        for xx in range(12):
            editor.placeBlock((x+2*xx,y,z),Block(w_id))
            editor.placeBlock((x+2*xx,y-1,z+1),Block(w_id))
            editor.placeBlock((x+2*xx,y,z+1),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-1,z+2),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-2,z+5),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2*xx,y-3,z+6),Block(e_id,{"type": "top"}))
            for zz in range(2):
                editor.placeBlock((x+2*xx,y-2,z+3+zz),Block(w_id))
    def wa3_1(x,y,z):       
        for zz in range(9):
            editor.placeBlock((x,y+1,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+2,y,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+4,y-1,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+6,y-2,z+2*zz),Block(e_id,{"type": "top"}))
            for xx in range(2):
                editor.placeBlock((x+xx,y,z+2*zz),Block(w_id))
            for xx in range(3):
                editor.placeBlock((x+1+xx,y-1,z+2*zz),Block(w_id))
                editor.placeBlock((x+3+xx,y-2,z+2*zz),Block(w_id))
    def wa3_2(x,y,z):
        for zz in range(8):
            editor.placeBlock((x,y,z+2*zz),Block(w_id))
            editor.placeBlock((x+5,y-2,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x+6,y-3,z+2*zz),Block(e_id,{"type": "top"}))
            for xx in range(2):
                editor.placeBlock((x+1+xx,y-1,z+2*zz),Block(w_id))
                editor.placeBlock((x+3+xx,y-2,z+2*zz),Block(w_id))
    def wa4_1(x,y,z):       
        for zz in range(9):
            editor.placeBlock((x,y+1,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x-2,y,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x-4,y-1,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x-6,y-2,z+2*zz),Block(e_id,{"type": "top"}))
            for xx in range(2):
                editor.placeBlock((x-xx,y,z+2*zz),Block(w_id))
            for xx in range(3):
                editor.placeBlock((x-1-xx,y-1,z+2*zz),Block(w_id))
                editor.placeBlock((x-3-xx,y-2,z+2*zz),Block(w_id))
    def wa4_2(x,y,z):
        for zz in range(8):
            editor.placeBlock((x,y,z+2*zz),Block(w_id))
            editor.placeBlock((x-5,y-2,z+2*zz),Block(e_id,{"type": "bottom"}))
            editor.placeBlock((x-6,y-3,z+2*zz),Block(e_id,{"type": "top"}))
            for xx in range(2):
                editor.placeBlock((x-1-xx,y-1,z+2*zz),Block(w_id))
                editor.placeBlock((x-3-xx,y-2,z+2*zz),Block(w_id))
    def feiyan1(x,y,z):
        editor.placeBlock((x,y,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x,y-1,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+2,y,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y-1,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+1,y,z+1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+1,y,z+2),Block(w_id))
        editor.placeBlock((x+1,y,z+3),Block(e_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x,y,z+zz),Block(w_id))
    def feiyan2(x,y,z):
        editor.placeBlock((x,y,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x,y-1,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-2,y,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y-1,z+3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-1,y,z+1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-1,y,z+2),Block(w_id))
        editor.placeBlock((x-1,y,z+3),Block(e_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x,y,z+zz),Block(w_id))
    def feiyan3(x,y,z):
        editor.placeBlock((x,y,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x,y-1,z-3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-2,y,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y-1,z-3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-1,y,z-1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-1,y,z-2),Block(w_id))
        editor.placeBlock((x-1,y,z-3),Block(e_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x,y,z-zz),Block(w_id))
    def feiyan4(x,y,z):
        editor.placeBlock((x,y,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x,y-1,z-3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+2,y,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y-1,z-3),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+1,y,z-1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+1,y,z-2),Block(w_id))
        editor.placeBlock((x+1,y,z-3),Block(e_id,{"type": "bottom"}))
        for zz in range(2):
            editor.placeBlock((x,y,z-zz),Block(w_id))
    def feiyan5(x,y,z):
        editor.placeBlock((x+2,y,z),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+3,y-1,z),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+3,y-1,z-2),Block(e_id,{"type": "top"}))
        for xx in range(2):
            editor.placeBlock((x+xx,y,z),Block(w_id))
        for xx in range(3):
            editor.placeBlock((x+1+xx,y,z-1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y,z-1),Block(w_id))
    def feiyan6(x,y,z):
        editor.placeBlock((x+2,y,z),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+3,y-1,z),Block(e_id,{"type": "top"}))
        editor.placeBlock((x+3,y-1,z+2),Block(e_id,{"type": "top"}))
        for xx in range(2):
            editor.placeBlock((x+xx,y,z),Block(w_id))
        for xx in range(3):
            editor.placeBlock((x+1+xx,y,z+1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x+2,y,z+1),Block(w_id))
    def feiyan7(x,y,z):
        editor.placeBlock((x-2,y,z),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y,z+2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-3,y-1,z),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-3,y-1,z+2),Block(e_id,{"type": "top"}))
        for xx in range(2):
            editor.placeBlock((x-xx,y,z),Block(w_id))
        for xx in range(3):
            editor.placeBlock((x-1-xx,y,z+1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y,z+1),Block(w_id))
    def feiyan7(x,y,z):
        editor.placeBlock((x-2,y,z),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y,z-2),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-3,y-1,z),Block(e_id,{"type": "top"}))
        editor.placeBlock((x-3,y-1,z-2),Block(e_id,{"type": "top"}))
        for xx in range(2):
            editor.placeBlock((x-xx,y,z),Block(w_id))
        for xx in range(3):
            editor.placeBlock((x-1-xx,y,z-1),Block(e_id,{"type": "bottom"}))
        editor.placeBlock((x-2,y,z-1),Block(w_id))
      
    muliang_1(x-11,y+10,z-7)
    muliang_2(x-11,y+10,z+7) 
    muliang_3(x-11,y+10,z-5)
    muliang_4(x+11,y+10,z-5)
    muliang2_1(x-13,y+9,z-9)
    muliang2_2(x-13,y+9,z+9) 
    muliang2_3(x-13,y+9,z-7)
    muliang2_4(x+13,y+9,z-7)
    muliang3_1(x-16,y+8,z-12)
    muliang3_2(x-16,y+8,z+12) 
    muliang3_3(x-16,y+8,z-10)
    muliang3_4(x+16,y+8,z-10)
    qiang(x-9,y+11,z-6)
    wa1_1(x-12,y+11,z-7)
    wa1_2(x-11,y+11,z-7)
    wa2_1(x-12,y+11,z+7)
    wa2_2(x-11,y+11,z+7)
    wa3_1(x+11,y+11,z-8)
    wa3_2(x+11,y+11,z-7)
    wa4_1(x-11,y+11,z-8)
    wa4_2(x-11,y+11,z-7)
    feiyan1(x+13,y+9,z+10)
    feiyan2(x-13,y+9,z+10)
    feiyan3(x-13,y+9,z-10)
    feiyan4(x+13,y+9,z-10)
    feiyan5(x+14,y+9,z-9)
    feiyan6(x+14,y+9,z+9)
    feiyan7(x-14,y+9,z+9)
    feiyan7(x-14,y+9,z-9)

def buildzhuangshi(x,y,z,q_id,w_id,e_id):
    editor.placeBlock((x-9,y+5,z+10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-3,y+5,z+10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+5,z+10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+9,y+5,z+10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+13,y+6,z+10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-13,y+6,z+10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-9,y+5,z+7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-3,y+5,z+7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+5,z+7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+9,y+5,z+7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+13,y+6,z+7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-13,y+6,z+7),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x-9,y+5,z-10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-3,y+5,z-10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+5,z-10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+9,y+5,z-10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+13,y+6,z-10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-13,y+6,z-10),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-9,y+5,z-7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-3,y+5,z-7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+5,z-7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+9,y+5,z-7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+13,y+6,z-7),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-13,y+6,z-7),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x-14,y+5,z-5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-14,y+5,z+5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-14,y+6,z-9),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-14,y+6,z+9),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-11,y+5,z-5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-11,y+5,z+5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-11,y+6,z-9),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-11,y+6,z+9),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x+14,y+5,z-5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+14,y+5,z+5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+14,y+6,z-9),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+14,y+6,z+9),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+11,y+5,z-5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+11,y+5,z+5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+11,y+6,z-9),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+11,y+6,z+9),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x-9,y+13,z+6),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-3,y+13,z+6),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+13,z+6),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+9,y+13,z+6),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x-9,y+13,z-6),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-3,y+13,z-6),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+3,y+13,z-6),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+9,y+13,z-6),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x+10,y+13,z-5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x+10,y+13,z+5),Block(q_id,{"hanging": "true"}))

    editor.placeBlock((x-10,y+13,z-5),Block(q_id,{"hanging": "true"}))
    editor.placeBlock((x-10,y+13,z+5),Block(q_id,{"hanging": "true"}))

    for yy in range(7):
        editor.placeBlock((x-5,y+1+yy,z),Block(w_id))
        editor.placeBlock((x+5,y+1+yy,z),Block(w_id))
    for yy in range(8):
        editor.placeBlock((x-4,y+1+yy,z),Block(e_id,{"facing": "east"}))
        editor.placeBlock((x+4,y+1+yy,z),Block(e_id,{"facing": "west"}))
    for zz in range(14):
        editor.placeBlock((x,y-9,z-14+2*zz),Block(q_id,{"hanging": "true"}))
        editor.placeBlock((x,y-7,z-14+2*zz),Block(q_id))

def wall_r1(x,y,z,q_id,w_id):
    for yy in range(16):
        for xx in range(10):
            for zz in range(10):
                 editor.placeBlock((x+xx,y+yy,z+zz),Block(q_id))
    for yy in range(2):
        for zz in range(5):
            editor.placeBlock((x,y+16+yy,z+1+2*zz),Block(q_id))
        for xx in range(4):
            editor.placeBlock((x+2+2*xx,y+16+yy,z+9),Block(q_id))
    for xx in range(5):
        editor.placeBlock((x+1+2*xx,y+16,z+9),Block(w_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((x,y+16,z+2*zz),Block(w_id,{"type": "top"}))
def wall_r2(x,y,z,q_id,w_id):
    for yy in range(16):
        for xx in range(10):
            for zz in range(10):
                 editor.placeBlock((x+xx,y+yy,z+zz),Block(q_id))
    for yy in range(2):
        for zz in range(5):
            editor.placeBlock((x,y+16+yy,z+2*zz),Block(q_id))
        for xx in range(4):
            editor.placeBlock((x+2+2*xx,y+16+yy,z),Block(q_id))
    for xx in range(5):
        editor.placeBlock((x+1+2*xx,y+16,z),Block(w_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((x,y+16,z+1+2*zz),Block(w_id,{"type": "top"}))
def wall_l1(x,y,z,q_id,w_id):
    for yy in range(16):
        for xx in range(10):
            for zz in range(10):
                 editor.placeBlock((x+xx,y+yy,z+zz),Block(q_id))
    for yy in range(2):
        for zz in range(5):
            editor.placeBlock((x+9,y+16+yy,z+1+2*zz),Block(q_id))
        for xx in range(4):
            editor.placeBlock((x+1+2*xx,y+16+yy,z+9),Block(q_id))
    for xx in range(5):
        editor.placeBlock((x+2*xx,y+16,z+9),Block(w_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((x+9,y+16,z+2*zz),Block(w_id,{"type": "top"}))

def wall_l2(x,y,z,q_id,w_id):
    for yy in range(16):
        for xx in range(10):
            for zz in range(10):
                 editor.placeBlock((x+xx,y+yy,z+zz),Block(q_id))
    for yy in range(2):
        for zz in range(5):
            editor.placeBlock((x+9,y+16+yy,z+2*zz),Block(q_id))
        for xx in range(4):
            editor.placeBlock((x+1+2*xx,y+16+yy,z),Block(q_id))
    for xx in range(5):
        editor.placeBlock((x+2*xx,y+16,z),Block(w_id,{"type": "top"}))
    for zz in range(5):
        editor.placeBlock((x+9,y+16,z+1+2*zz),Block(w_id,{"type": "top"}))
def wall_x(x,y,z,l,q_id,w_id,e_id):
    for yy in range(16):
        for xx in range(l):
            for zz in range(11):
                 editor.placeBlock((x+xx,y+yy,z+zz),Block(q_id))
    for xx in range(0,l,2):
        editor.placeBlock((x+xx,y+18,z),Block(e_id))
        editor.placeBlock((x+xx,y+18,z+10),Block(e_id))
        for yy in range(2):
            editor.placeBlock((x+xx,y+16+yy,z),Block(q_id))
            editor.placeBlock((x+xx,y+16+yy,z+10),Block(q_id))

    for xx in range(1,l,2):
        editor.placeBlock((x+xx,y+16,z),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+xx,y+16,z+10),Block(w_id,{"type": "top"}))
def wall_z(x,y,z,l,q_id,w_id,e_id):
    for yy in range(16):
        for xx in range(11):
            for zz in range(l):
                 editor.placeBlock((x+xx,y+yy,z+zz),Block(q_id))
    for zz in range(0,l,2):
        editor.placeBlock((x,y+18,z+zz),Block(e_id))
        editor.placeBlock((x+10,y+18,z+zz),Block(e_id))
        for yy in range(2):
            editor.placeBlock((x,y+16+yy,z+zz),Block(q_id))
            editor.placeBlock((x+10,y+16+yy,z+zz),Block(q_id))
    for zz in range(1,l,2):
        editor.placeBlock((x,y+16,z+zz),Block(w_id,{"type": "top"}))
        editor.placeBlock((x+10,y+16,z+zz),Block(w_id,{"type": "top"}))


def wall1(x,y,z):
    buildHouse(x, y, z, "stone_bricks", "stripped_acacia_log","acacia_slab","stone_brick_stairs","stone_brick_slab")
    stairs1(x,y,z,"stone_bricks","stone_brick_stairs","stone_brick_slab")
    buildlou(x, y+16, z+14,"stone_bricks","infested_chiseled_stone_bricks","red_concrete")
    buildhen(x, y+16, z+14,"red_concrete","stripped_acacia_wood","stone_bricks")
    buildwa(x, y+36, z+14,"cobblestone","cobblestone_slab","cobblestone_stairs")
    buildfeiyan(x, y+36, z+14,"stone_bricks","stone_brick_slab","stone_brick_stairs","cobblestone_wall")
    buildxiawuding(x, y+16, z+14,"stripped_acacia_wood","cobblestone","cobblestone_slab","cobblestone_stairs")
    buildzhuangshi(x, y+16, z+14,"lantern","stripped_acacia_wood","ladder")
    for xx in range(35):
        for zz in range(8):
            for yy in range(18):
                editor.placeBlock((x-17+xx,y+yy,z+27+zz),Block("air"))
    command = f"summon boat {x+1} {y+1} {z+26}"
    runCommand(command)
    command = f"summon boat {x} {y+1} {z+26}"
    runCommand(command)
    command = f"summon boat {x-1} {y+1} {z+26}"
    runCommand(command)

 
def wall2(x,y,z):      
    buildHouse(x, y, z, "stone_bricks", "stripped_acacia_log","acacia_slab","stone_brick_stairs","stone_brick_slab")
    stairs2(x,y,z,"stone_bricks","stone_brick_stairs","stone_brick_slab")
    buildlou(x, y+16, z+14,"stone_bricks","infested_chiseled_stone_bricks","red_concrete")
    buildhen(x, y+16, z+14,"red_concrete","stripped_acacia_wood","stone_bricks")
    buildwa(x, y+36, z+14,"cobblestone","cobblestone_slab","cobblestone_stairs")
    buildfeiyan(x, y+36, z+14,"stone_bricks","stone_brick_slab","stone_brick_stairs","cobblestone_wall")
    buildxiawuding(x, y+16, z+14,"stripped_acacia_wood","cobblestone","cobblestone_slab","cobblestone_stairs")
    buildzhuangshi(x, y+16, z+14,"lantern","stripped_acacia_wood","ladder")
    for xx in range(35):
        for yy in range(18):
            for zz in range(8):
                editor.placeBlock((x-17+xx,y+yy,z-1-zz),Block("air"))
    command = f"summon boat {x+1} {y+1} {z}"
    runCommand(command)
    command = f"summon boat {x} {y+1} {z}"
    runCommand(command)
    command = f"summon boat {x-1} {y+1} {z}"
    runCommand(command)    
 
 
    
def wall_R1(x,y,z):
    wall_r1(x,y,z,"stone_bricks","stone_brick_slab")
def wall_R2(x,y,z):
    wall_r2(x,y,z,"stone_bricks","stone_brick_slab")
def wall_L1(x,y,z):
    wall_l1(x,y,z,"stone_bricks","stone_brick_slab")
def wall_L2(x,y,z):
    wall_l2(x,y,z,"stone_bricks","stone_brick_slab")
def wall_X(x,y,z,l):
    wall_x(x,y,z,l,"stone_bricks","stone_brick_slab","torch")
def wall_Z(x,y,z,l):
    wall_z(x,y,z,l,"stone_bricks","stone_brick_slab","torch")


def make_wall(height, area): # for example: buildarea = (0, 0, 300 ,300)
    buildarea = (area[0], area[1], area[2]+area[0], area[3]+area[1])
    wall2(buildarea[0]+area[2]//2, height, buildarea[1]-6)
    wall_X(buildarea[0]+area[2]//2+35, height, buildarea[1], (buildarea[0]+area[2]//2)-buildarea[0]-35-10)
    wall_X(buildarea[0]+10, height, buildarea[1], (buildarea[0]+area[2]//2)-buildarea[0]-35-9)


    wall1(buildarea[0]+area[2]//2, height, buildarea[3]-21)
    wall_X(buildarea[0]+area[2]//2+35, height, buildarea[3]-11, (buildarea[0]+area[2]//2)-buildarea[0]-35-10)
    wall_X(buildarea[0]+10, height, buildarea[3]-11, (buildarea[0]+area[2]//2)-buildarea[0]-35-9)

    wall_L1(buildarea[2]-10, height, buildarea[3]-10)
    wall_L2(buildarea[2]-10, height, buildarea[1])
    wall_R1(buildarea[0], height, buildarea[3]-10)
    wall_R2(buildarea[0], height, buildarea[1])
    wall_Z(buildarea[0], height, buildarea[1]+10, buildarea[3]-buildarea[1]-20)
    wall_Z(buildarea[2]-11, height, buildarea[1]+10, buildarea[3]-buildarea[1]-20)
