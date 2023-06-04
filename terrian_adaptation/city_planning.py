import random
import seaborn as sns; sns.set()
from copy import deepcopy
from building_lists import *

buildingTypes = [7,13,6,2,1,3,6,12,8]

def decideAreas(area, exclusion):
    x_len = area[2]
    y_len = area[3]
    wall_width = 11
    areaMap = [[0 for k in range(y_len)] for j in range(x_len)]
    areaDict = {}
    x_middle = int(x_len/2)
    y_middle = int(y_len/2)
    x_road = int((x_middle-44-wall_width)/2)
    y_road = int((y_middle-44-wall_width)/2)
    for i in range(-44-exclusion,45+exclusion):
        for j in range(-44-exclusion,45+exclusion):
            areaMap[x_middle+i][y_middle+j] = -1
    for i in range(x_len):
        for j in range(wall_width+6):
            areaMap[i][j] = -1
            areaMap[i][y_len-1-j] = -1
    for i in range(wall_width):
        for j in range(y_len):
            areaMap[i][j] = -1
            areaMap[x_len-1-i][j] = -1
    for i in range(x_len):
        for j in range(-5-exclusion,6+exclusion):
            areaMap[i][y_middle+j] = -1
    for i in range(-34,35):
        for j in range(27):
            areaMap[x_middle+i][j] = -1
            areaMap[x_middle+i][y_len-1-j] = -1
    areaDict[1] = (wall_width, wall_width, x_middle-x_road-48, y_middle-y_road-48)
    areaDict[2] = (wall_width, y_middle-y_road-39, x_middle-x_road-48, y_middle+y_road+40)
    areaDict[3] = (wall_width, y_middle+y_road+49, x_middle-x_road-48, y_len-wall_width)
    areaDict[4] = (x_middle-x_road-39, wall_width, x_middle+x_road+40, y_middle-y_road-48)
    areaDict[5] = (x_middle-x_road-39, y_middle-y_road-39, x_middle+x_road+40, y_middle+y_road+40)
    areaDict[6] = (x_middle-x_road-39, y_middle+y_road+49, x_middle+x_road+40, y_len-wall_width)
    areaDict[7] = (x_middle+x_road+49, wall_width, x_len-wall_width, y_middle-y_road-48)
    areaDict[8] = (x_middle+x_road+49, y_middle-y_road-39, x_len-wall_width, y_middle+y_road+40)
    areaDict[9] = (x_middle+x_road+49, y_middle+y_road+49, x_len-wall_width, y_len-wall_width)
    for num, buildArea in areaDict.items():
        for i in range(buildArea[0],buildArea[2]):
            for j in range(buildArea[1],buildArea[3]):
                if areaMap[i][j] == 0:
                    areaMap[i][j] = num
    return areaMap, areaDict

def decideHouseArea(area, exclusion):
    x_len = area[2]
    y_len = area[3]
    wall_width = 11
    areaMap = [[1 for k in range(y_len)] for j in range(x_len)]
    areaDict = {}
    x_middle = int(x_len/2)
    y_middle = int(y_len/2)
    for i in range(-44-exclusion,45+exclusion):
        for j in range(-44-exclusion,45+exclusion):
            areaMap[x_middle+i][y_middle+j] = -1
    for i in range(x_len):
        for j in range(wall_width+6):
            areaMap[i][j] = -1
            areaMap[i][y_len-1-j] = -1
    for i in range(wall_width):
        for j in range(y_len):
            areaMap[i][j] = -1
            areaMap[x_len-1-i][j] = -1
    for i in range(-34,35):
        for j in range(27):
            areaMap[x_middle+i][j] = -1
            areaMap[x_middle+i][y_len-1-j] = -1
    areaDict[1] = (wall_width, wall_width, x_len-wall_width, y_len-wall_width)
    return areaMap, areaDict

def decideBuildings(num, area, buildingMap, buildingDict, buildingType, exclusion, intervalDistance = 2):
    BuildingRemainNum = deepcopy(BuildingMaxNum)
    BuildingSizeList = BuildingSizeLists[buildingType]
    for x in range(area[0] + exclusion, (area[2] - exclusion)):
        for y in range(area[1] + exclusion, (area[3] - exclusion)):
            if buildingMap[x][y] == num:
                buildingList = []
                for building, size in BuildingSizeList.items():
                    for name in BuildingRemainNum:
                        if name in building:
                            if BuildingRemainNum[name] != 0:
                                if x + size[0] < (area[2] - exclusion) and y + size[1] < (area[3] - exclusion):
                                    plotArea = list([buildingMap[i][k] for i in range(x, x + size[0]) for k in range(y, y + size[1])])
                                    if len(set(plotArea)) == 1 and list(set(plotArea))[0] == num:
                                        buildingList.append(building)
                if buildingList:
                    selectedBuilding = random.choice(buildingList)
                    buildingDict[(x,y)] = selectedBuilding
                    for name in BuildingRemainNum:
                        if name in selectedBuilding:
                            BuildingRemainNum[name] = BuildingRemainNum[name] - 1
                    for i in range(-intervalDistance, BuildingSizeList[selectedBuilding][0]+intervalDistance):
                        for j in range(-intervalDistance, BuildingSizeList[selectedBuilding][1]+intervalDistance):
                            if x+i >= exclusion and x+i < (area[2]-exclusion) and y+j >= exclusion and y+j < (area[3]-exclusion):
                                if i in range(BuildingSizeList[selectedBuilding][0]) and j in range(BuildingSizeList[selectedBuilding][1]):
                                    buildingMap[x+i][y+j] = selectedBuilding
                                else:
                                    buildingMap[x+i][y+j] = -1
    return buildingMap, buildingDict

def executeCityPlanning(area, isMaxArea = 0, exclusion = 2):
    x_len = area[2]
    y_len = area[3]
    buildArea = x_len*y_len
    if isMaxArea == 1:
        if buildArea >= 60000 and x_len >= 250 and y_len >= 250:
            buildingMap, areaDict = decideAreas(area, exclusion)
            buildingDict = {}
            for num, buildingArea in areaDict.items():
                buildingMap, buildingDict = decideBuildings(num, buildingArea, buildingMap, buildingDict, buildingTypes[num-1], exclusion)
        elif buildArea > 16900 and x_len > 130 and y_len > 130:
            buildingDict = {}
            buildingMap, areaDict = decideHouseArea(area, exclusion)
            buildingMap, buildingDict = decideBuildings(1, areaDict[1], buildingMap, buildingDict, 1, exclusion)
        else:
            return [[0 for k in range(area[3])] for j in range(area[2])], {}
    else:
        buildingArea = (0, 0, x_len, y_len)
        buildingMap = [[1 for k in range(y_len)] for j in range(x_len)]
        buildingDict = {}
        if buildArea >= 1000:
            buildingMap, buildingDict = decideBuildings(1, buildingArea, buildingMap, buildingDict, 0, exclusion, 4)
        else:
            buildingMap, buildingDict = decideBuildings(1, buildingArea, buildingMap, buildingDict, 14, exclusion)
    return buildingMap, buildingDict
