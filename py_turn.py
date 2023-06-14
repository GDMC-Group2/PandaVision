__all__ = []
# __version__

import re
from interfaceUtils import getBlock
import interfaceUtils



##################

#入力されたpythonファイル上の建築物の向きを変更
#変化させたファイルを生成する
#座標情報の取得
#取得した座標のx,zの後ろ(相対座標からのズレ)を変化
#blockdataを変更
#editor.placeBlock((x+xx,y,z+zz),Block("campfire",{"facing":"west","lit":"false"}))
#editor.PlaceBlock(())

#ブロック設置以外の座標変化は自力で行う事


def e_z(l): #erase_zero,l=length
    if(l==0):#始点に対してずれがない場合 (+0になる場合)
        return ''
    elif("-" in l):#マイナスになる場合
        return str(l)
    else:
        return "+"+str(l)

def rotate_change(states,rotate): #ブロック情報の向きを変える
    facing=["east","south","west","north","east","south","west"]
    if("east" in states): #0番
        states=states.replace("east",facing[0+rotate])
    elif("south" in states): #1番
        states=states.replace("south",facing[1+rotate])
    elif("west" in states): #2番
        states=states.replace("west",facing[2+rotate])
    elif("north" in states): #3番
        states=states.replace("north",facing[3+rotate])
    print(states)
    return states

#x+xx,z+zzの回転
#x-zz z+xx
#x-xx,z-zz
#x+zz,z-xx


def py_turn(r_name,w_name,rotate):
    r=open(r_name,'r',encoding="utf-8") #読み取り
    w=open(w_name,'w') #ファイル読み込み
    for line in r: #列の回数分だけ実行. lineが文章
        if("editor.placeBlock" in line): #\editorblock関数を探す
            for i in line: #空白(インデント)を挿入
                if(i==' '):
                    w.write(' ')
                else:
                    break
            spl_line=line.split(',',3)
            #余計なデータを削除する
            spl_line[0]=spl_line[0].replace("editor.placeBlock((","")
            spl_line[0]=spl_line[0].lstrip()
            spl_line[2]=spl_line[2].replace(")","")
            x=spl_line[0].lstrip("x") #x,y,zの後ろの値を取得
            y=spl_line[1].lstrip("y")
            z=spl_line[2].lstrip("z")      
            #+と-を反転させる
            if(rotate==0):
                pass
            elif(rotate==1):
                xl=z.translate(str.maketrans("+-","-+"))
                zl=x
            elif(rotate==2):
                xl=x.translate(str.maketrans("+-","-+"))
                zl=z.translate(str.maketrans("+-","-+"))
            elif(rotate==3):
                xl=z
                zl=x.translate(str.maketrans("+-","-+"))
            w.write("editor.placeBlock(("+"x"+xl+","+"y"+y+","+"z"+zl+"),") #座標情報を書き込む
            block=spl_line[3]    
            if("facing" in block):
                block=rotate_change(block,rotate)
            w.write(block)
        else:
            w.write(line)
    w.close()
    r.close()






py_turn("bracksmith.py","bracksmith_1.py",1)
py_turn("bracksmith.py","bracksmith_2.py",2)
py_turn("bracksmith.py","bracksmith_3.py",3)
#############################





def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True






