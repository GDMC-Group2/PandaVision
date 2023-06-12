import numpy as np
from gdpc import Editor
ED = Editor(buffering=True)

def calcGoodHeightmap(worldSlice):
    area=[]
    hm_mbnl = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
    heightmap = hm_mbnl[:]
    wS_area = worldSlice.rect
    #areaを変換
    area.append(wS_area.offset[0])
    area.append(wS_area.offset[1])
    area.append(wS_area.size[0])
    area.append(wS_area.size[1])

    print(area)
    test=0
    chikeyi=[[0 for i in range(area[3])]for j in range(area[2])]
    cnt = 0
    flag = True
    for x in range(area[2]):
        for z in range(area[3]):
            while True:
                y = heightmap[x, z]
                block_info= worldSlice.getBlock((area[0] + x, y - 1, area[1] + z))
                block = block_info.id
                if 'water' in block:
                    chikeyi[x][z]= 0
                    cnt += 1
                elif 'grass_block' in block:
                    chikeyi[x][z]= 1
                elif 'sand' in block:
                    chikeyi[x][z]= 2
                elif 'stone' in block and block!="cobblestone":
                    chikeyi[x][z]= 3
                else:
                    chikeyi[x][z]= 4
                if block[-4:] == '_log':
                    heightmap[x, z] -= 1
                else:
                    break
    if (cnt/(area[2]*area[3]))<0.6:
        flag = False
    return np.array(np.minimum(hm_mbnl, heightmap)),chikeyi,flag