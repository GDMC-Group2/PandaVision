from gdpc import Editor
from ExisitingSettlement import SearchBuildarea as SBA
from time import *
from terrian_adaptation import terrain, building_placement, city_planning, surface_reconstruction
from Building import hotel
from tools import getEnv
import interfaceUtils
from basement import Basement as bs
from air import Air as ar
from searchBlockinfo import SearchBlocks
from box import Box
import sys

# x1 = int(sys.argv[1])
# z1 = int(sys.argv[2])
# x2 = int(sys.argv[3])
# z2 = int(sys.argv[4])
# area = (x1, z1, x2, z2)
# print(f"Build area is at position {area[0]}, {area[1]} with size {area[2]}, {area[3]}")
# command=f'setbuildarea {area[0]} 0 {area[1]} {area[2]} 255 {area[3]}'
# ED = Editor(buffering=True)
# ED.runCommand(command)


def main():
    #sとgの仕様
    #sが原点
    #gがベクトル値
    ED = Editor(buffering=True)
    #s=start x,y,z g=goal x,y,z
    # s=[args[0], args[1]]
    # g=[args[2], args[3]]
    # command=f"setbuildarea {s[0]} 0 {s[1]} {g[0]} 255 {area[1]}"
    # ED.runCommand(command)

    # print("Build area")
    # Here we read start and end coordinates of our build area
    BUILD_AREA = ED.getBuildArea()  # BUILDAREA
    # BUILD_AREA = Box((area[0], 0, area[1]), (area[2], 255, area[3]))
    # print(BUILD_AREA)
    # print("world slice")
    WORLDSLICE = ED.loadWorldSlice(BUILD_AREA.toRect(), cache=True)  # this takes a while
    worldSlice = WORLDSLICE
    print(worldSlice)
    

    # print("heights")
    #heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
    area = [worldSlice.rect.offset[0],worldSlice.rect.offset[1],worldSlice.rect.size[0],worldSlice.rect.size[1]]

    print(f"Build area is at position {area[0]}, {area[1]} with size {area[2]}, {area[3]}")
    command="gamerule doMobSpawning false"
    ED.runCommand(command)
    # ------------------------------------
    if area[2] * area[3] >= 360000:
        new_area = []
        new_area.append(area[0] + area[2] // 5)
        new_area.append(area[1] + area[3] // 5)
        new_area.append(area[2] - area[2] // 5 * 2)
        new_area.append(area[3] - area[3] // 5 * 2)
        area = new_area
    # ------------------------------------

    


    #heightmap = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

    heightmap, env, flag = getEnv.calcGoodHeightmap(worldSlice)
    #test用 先に木を切ってしまう場合用
    #surface_reconstruction.RemoveTrees(heightmap,area)    
    #ED.updateWorldSlice()
    #heightmap, env, flag = getEnv.calcGoodHeightmap(worldSlice)
    #test完了

    ar(area[0]+area[2]//2, heightmap[area[0]+area[2]//2][area[1]+area[3]//2], area[1]+area[3]//2)
    bs(area[0]+area[2]//2, heightmap[area[0]+area[2]//2][area[1]+area[3]//2], area[1]+area[3]//2)
        
    if flag:
        search_area = [(area[0], area[1], area[2], area[3])]
        print("flag!")
    else:
        search_BuildArea = SBA.SearchBuildArea(area=area, heightmap=heightmap, env=env, worldSlice=worldSlice)
        search_area = search_BuildArea.output() # tuple in list
        print(search_area)
    isMaxArea = 1
    for Area in search_area:
        HM_Area = heightmap[Area[0]:Area[0]+Area[2],Area[1]:Area[1]+Area[3]]
        ActualArea = [area[0]+Area[0],area[1]+Area[1],Area[2],Area[3]]
        surface_reconstruction.RemoveTrees(HM_Area, ActualArea)
        SB = SearchBlocks(worldSlice, Area)
        block_id = SB.run()
        height = terrain.setSameHeight(HM_Area, ActualArea, block_id)
        print("Surface BlockID: ", block_id)
        buildingMap, buildingDict = city_planning.executeCityPlanning(Area,isMaxArea)
        building_placement.placeCity(buildingMap, buildingDict, ActualArea, height, block_id, isMaxArea)
        if isMaxArea == 1:
            x = ActualArea[0] + int(ActualArea[2]/2)
            y = height
            z = ActualArea[1] + int(ActualArea[3]/2)
        isMaxArea = 0
    #if 'x' in locals() and 'y' in locals() and 'z' in locals():
        #hotel.hotel3(x,y,z)
# setbuildarea -500 40 -500 500 100 500
# setbuildarea 0 -70 0 200 200 200

# 0 0 0 to 1000 255 1000
# setbuildarea 0 0 0 1000 255 1000

# -12654 0 5046 to -12398 255 5302
# setbuildarea -12654 0 5046 256 255 256

# -12606 0 115 to -12350 255 371
# setbuildarea -12606 0 115 256 255 256

# -5273 0 2582 to -5017 255 2838
# setbuildarea -5273 0 2582 256 255 256

# 1509 0 -2910 to 1765 255 -2654
# setbuildarea 1509 0 -2910 256 255 256

# python main.py 0 0 400 400
if __name__ == "__main__":
    begin_time = time()
    main()
    end_time = time()
    print("run time:", end_time-begin_time)
