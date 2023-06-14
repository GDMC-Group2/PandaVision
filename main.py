from gdpc import Editor
from ExisitingSettlement import SearchBuildarea as SBA
from time import *
from terrian_adaptation import terrain, building_placement, city_planning, surface_reconstruction
from Building import hotel
from tools import getEnv
import interfaceUtils


# import sys
# x1 = int(sys.argv[1])
# z1 = int(sys.argv[2])
# x2 = int(sys.argv[3])
# z2 = int(sys.argv[4])
# area = (x1, z1, x2, z2)
# print(f"Build area is at position {area[0]}, {area[1]} with size {area[2]}, {area[3]}")



def main():
    #sとgの仕様
    #sが原点
    #gがベクトル値
    ED = Editor(buffering=True)
    #s=start x,y,z g=goal x,y,z
    #s=[-292,-60,-49]
    #g=[~111,255,~104]
    #command=f"setbuildarea {s[0]} {s[1]} {s[2]} {g[0]} {g[1]} {g[2]}"
    #ED.runCommand(command)

    # print("Build area")
    # Here we read start and end coordinates of our build area
    BUILD_AREA = ED.getBuildArea()  # BUILDAREA
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

    if flag:
        search_area = [(0, 0, 300, 300)]
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
        height = terrain.setSameHeight(HM_Area, ActualArea, env)
        buildingMap, buildingDict = city_planning.executeCityPlanning(Area,isMaxArea)
        building_placement.placeCity(buildingMap, buildingDict, ActualArea, height, isMaxArea)
        if isMaxArea == 1:
            x = ActualArea[0] + int(ActualArea[2]/2)
            y = height
            z = ActualArea[1] + int(ActualArea[3]/2)
        isMaxArea = 0
    #if 'x' in locals() and 'y' in locals() and 'z' in locals():
        #hotel.hotel3(x,y,z)
# setbuildarea 0 40 0 400 100 400

begin_time = time()
main()
end_time = time()
print("run time:", end_time-begin_time)
