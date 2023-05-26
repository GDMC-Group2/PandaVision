__all__ = []
# __version__

import re
from interfaceUtils import getBlock
import interfaceUtils



##################

#ある範囲の建築物を記憶,textデータに起こす.
#textデータからは手動でpythonファイルに変換

def e_z(l): #erase_zero,l=length
    if(l==0):#始点に対してずれがない場合 (+0になる場合)
        return ''
    elif(l<0):#マイナスになる場合
        return str(l)
    else:
        return "+"+str(l)

def rotate_change(states,rotate): #ブロック情報の向きを変える
    facing=["east","south","west","north","east","south","west"]
    if("east" in states): #0番
        states=states.replace("east",facing[0+rotate])
    elif("north" in states): #1番
        states=states.replace("north",facing[1+rotate])
    elif("west" in states): #2番
        states=states.replace("west",facing[2+rotate])
    elif("south" in states): #3番
        states=states.replace("south",facing[3+rotate])
    print(states)
    return states



def build_text(x,y,z,xl,yl,zl,filename,rotate): #x,y,z...始点,xl,yl,zl...長さ,始点は-から+方向に向かう方向に設定する.
    #探査はx,y,zが増加する方向に進む
    f=open(filename,'w') #ファイルを作成
    for yy in range(yl):
        for xx in range(xl):
            for zz in range(zl):
                vec=[[xx,zz],[-zz,xx],[-xx,-zz],[zz,-xx]]
                block=getBlock(x+xx,y+yy,z+zz) #ブロック情報を取得
                if("minecraft:air" not in block): #空気ブロックは無視
                    block=block.replace('minecraft:','')
                    state=block.split(",",4)
                    id=state[0].split(":")
                    block_name=id[1]
                    state[4]=state[4].replace("}]","")
                    states=re.findall("(?<={).+?(?=})",state[4])
                    states=''.join(states)
                    f.write("editor.placeBlock((" + "x" + e_z(vec[rotate][0]) + "," + "y" + e_z(yy) + "," + "z" + e_z(vec[rotate][1])+"),") #座標情報
                    f.write("Block("+block_name)
                    if(len(states)!=0): #文字があったら
                        #rotateを変化させる
                        if ("facing" in states and rotate!=0):
                            states=rotate_change(states,rotate)
                        f.write(",{"+states+"}")
                    else:
                        pass
                    f.write("))\n")
                else:
                    pass
    f.close()


build_text(-40,3,0,10,8,8,"blacksmith",0)

#############################



#x+xx,z+zzの回転
#x-zz z+xx
#x-xx,z-zz
#x+zz,z-xx
#時計回りになる
#



def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True






