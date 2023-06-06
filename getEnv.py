import numpy as np
from gdpc import Editor
ED = Editor(buffering=False)

def calcGoodHeightmap(worldSlice, heightmapType = "MOTION_BLOCKING_NO_LEAVES"):
    hm_mbnl = worldSlice.heightmaps[heightmapType]
    heightmap = hm_mbnl[:]
    area0 = worldSlice._rect
    area = (area0.begin[0], area0.begin[1], area0.end[0]-area0.begin[0], area0.end[1]-area0.begin[1])
    print(area)
    chikeyi=[[0 for i in range(area[3])]for j in range(area[2])]
    cnt = 0
    flag = True
    for x in range(area[2]):
        for z in range(area[3]):
            while True:
                y = heightmap[x, z]
                block_info = ED.getBlock((area[0] + x, y - 1, area[1] + z))
                block = block_info.id
                if 'water' in block:
                    chikeyi[x][z]= 0
                    cnt += 1
                elif 'grass_block' in block:
                    chikeyi[x][z]= 1
                elif 'sand' in block:
                    chikeyi[x][z]= 2
                elif 'stone' in block:
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