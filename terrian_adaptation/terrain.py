from copy import deepcopy
from collections import Counter
import sys
sys.setrecursionlimit(65536)
from gdpc import Editor, Block
from time import *

ED = Editor(buffering=True)



def floodFill(heightMap, minimumArea, exclusion = 0):
    AvailableAreaSize = 16
    tempHM = deepcopy(heightMap)
    maskedHM = [[0 for k in range(len(heightMap[0]))] for j in range(len(heightMap))]
    currentLevel = 999
    currentRegion = 1
    regionDict = {}
    alterDict = {}
    alterHeightDict = {}
    def FF(x, y, area):
        tempHM[x][y] = 999
        area.append([x,y])
        if len(area) <= 3000:
            if ((y - 1) >= (0 + exclusion)):  # go to west
                if tempHM[x][y - 1] == currentLevel:
                    area = FF(x, y - 1, area)
            if ((y + 1) < (len(tempHM[x]) - exclusion)): # go to east
                if tempHM[x][y + 1] == currentLevel:
                    area = FF(x, y + 1, area)
            if ((x + 1) < (len(tempHM) - exclusion)): # go to south
                if tempHM[x + 1][y] == currentLevel:
                    area = FF(x + 1, y, area)
            if ((x - 1) >= (0 + exclusion)): # go to north
                if tempHM[x - 1][y] == currentLevel:
                    area = FF(x - 1, y, area)
        return area
    
    def FFFF (x, y, area):
        area.append([x,y])
        stonks = []
        stonks.append([x,y])
        length = len(stonks)
        tempHM[x][y] = 999
        while length >= 1:
            x = stonks[0][0]
            y = stonks[0][1]
            stonks.pop(0)
            if ((y - 1) >= (0 + exclusion)): # go to west
                if tempHM[x][y - 1] == currentLevel:
                    stonks.append([x, y - 1])
                    area.append([x, y - 1])
                    tempHM[x][y - 1] = 999
            if ((y + 1) < (len(tempHM[x]) - exclusion)): # go to east
                if tempHM[x][y + 1] == currentLevel:
                    stonks.append([x, y + 1])
                    area.append([x, y + 1])
                    tempHM[x][y + 1] = 999
            if ((x + 1) < (len(tempHM) - exclusion)): # go to south
                if tempHM[x + 1][y] == currentLevel:
                    stonks.append([x + 1, y])
                    area.append([x + 1, y])
                    tempHM[x + 1][y] = 999
            if ((x - 1) >= (0 + exclusion)): # go to north
                if tempHM[x - 1][y] == currentLevel:
                    stonks.append([x - 1, y])
                    area.append([x - 1, y])
                    tempHM[x - 1][y] = 999
            length = len(stonks)
        return area
    
    def FFZero(x, y, area, height, surroundingRegion):
        height.append(heightMap[x][y])
        maskedHM[x][y] = 999
        area.append([x,y])
        if len(area) <= 3000:
            if ((x + 1) < (len(maskedHM) - exclusion)): # go to south
                if maskedHM[x + 1][y] == 0:
                    area, height, surroundingRegion  = FFZero(x + 1, y, area, height, surroundingRegion)
                elif maskedHM[x + 1][y] != 0 and maskedHM[x + 1][y] != 999:
                    surroundingRegion.append(maskedHM[x + 1][y])
            if ((y - 1) >= (0 + exclusion)):  # go to west
                if maskedHM[x][y - 1] == 0:
                    area, height, surroundingRegion  = FFZero(x, y - 1, area, height, surroundingRegion)
                elif maskedHM[x][y - 1] != 0 and maskedHM[x][y - 1] != 999:
                    surroundingRegion.append(maskedHM[x][y - 1])
            if ((x - 1) >= (0 + exclusion)): # go to north
                if maskedHM[x - 1][y] == 0:
                    area, height, surroundingRegion  = FFZero(x - 1, y, area, height, surroundingRegion)
                elif maskedHM[x - 1][y] != 0 and maskedHM[x - 1][y] != 999:
                    surroundingRegion.append(maskedHM[x - 1][y])
            if ((y + 1) < (len(maskedHM[x]) - exclusion)): # go to east
                if maskedHM[x][y + 1] == 0:
                    area, height, surroundingRegion  = FFZero(x, y + 1, area, height, surroundingRegion)
                elif maskedHM[x][y + 1] != 0 and maskedHM[x][y + 1] != 999:
                    surroundingRegion.append(maskedHM[x][y + 1])
        return area, height, surroundingRegion
    
    def FFFFZero (x, y, area, height, surroundingRegion):
        height.append(heightMap[x][y])
        area.append([x,y])
        maskedHM[x][y] = 999
        stonks = []
        stonks.append([x,y])
        length = len(stonks)
        while length >= 1:
            x = stonks[0][0]
            y = stonks[0][1]
            stonks.pop(0)
            height.append(heightMap[x][y])
            maskedHM[x][y] = 999
            area.append([x,y])
            if ((x + 1) < (len(maskedHM) - exclusion)): # go to west
                if maskedHM[x + 1][y] == 0:
                    stonks.append([x + 1, y])
                    maskedHM[x + 1][y] = 999
                elif maskedHM[x + 1][y] != 0 and maskedHM[x + 1][y] != 999:
                    surroundingRegion.append(maskedHM[x + 1][y])
            if ((y - 1) >= (0 + exclusion)): # go to east
                if maskedHM[x][y - 1] == 0:
                    stonks.append([x, y - 1])
                    maskedHM[x][y - 1] = 999
                elif maskedHM[x][y - 1] != 0 and maskedHM[x][y - 1] != 999:
                    surroundingRegion.append(maskedHM[x][y - 1])
            if ((x - 1) >= (0 + exclusion)): # go to south
                if maskedHM[x - 1][y] == 0:
                    stonks.append([x - 1, y])
                    maskedHM[x - 1][y] = 999
                elif maskedHM[x - 1][y] != 0 and maskedHM[x - 1][y] != 999:
                    surroundingRegion.append(maskedHM[x - 1][y])
            if ((y + 1) < (len(maskedHM[x]) - exclusion)): # go to north
                if maskedHM[x][y + 1] == 0:
                    stonks.append([x, y + 1])
                    maskedHM[x][y + 1] = 999
                elif maskedHM[x][y + 1] != 0 and maskedHM[x][y + 1] != 999:
                    surroundingRegion.append(maskedHM[x][y + 1])
            length = len(stonks)
        return area, height, surroundingRegion
    
    print("Calucating Region")
    for x in range(exclusion, (len(tempHM) - exclusion)):
        for y in range(exclusion, (len(tempHM[0]) - exclusion)):
            if tempHM[x][y] < 257 and tempHM[x][y] >= -20:
                currentLevel = tempHM[x][y]
                area = FFFF(x, y, [])
                if len(area) >= minimumArea:
                    valid = False
                    for cell in area:
                        if cell[0] + AvailableAreaSize < len(heightMap) and cell[1] + AvailableAreaSize < len(heightMap[0]):
                            plotArea = list([heightMap[i][k] for i in range(cell[0], cell[0] + AvailableAreaSize) for k in range(cell[1], cell[1] + AvailableAreaSize)])
                            if len(set(plotArea)) == 1 and list(set(plotArea))[0] == currentLevel:
                                valid = True
                                break
                    if valid:
                        for blocks in area:
                            maskedHM[blocks[0]][blocks[1]] = currentRegion
                        regionDict[currentRegion] = currentLevel
                        currentRegion = currentRegion + 1
    
    print("Calucating Non-Region")
    for x in range(exclusion, (len(maskedHM) - exclusion)):
           for y in range(exclusion, (len(maskedHM[0]) - exclusion)):
               if maskedHM[x][y] == 0:
                   area, height, surroundingRegion = FFFFZero(x, y, [], [], [])
                   region = None
                   if len(surroundingRegion) > 0:
                       region = max(set(surroundingRegion), key=surroundingRegion.count)
                   if region != None and len(area) <= (minimumArea * 4): #if non-assigned area is bordered with an assigned area
                       for item in area: # Assign assigned area to non-assigned area
                               alterDict[item[0],item[1]] = regionDict.get(int(region)) - heightMap[item[0]][item[1]]
                               alterHeightDict[item[0],item[1]] = heightMap[item[0]][item[1]]
                               maskedHM[item[0]][item[1]] = region
                               
                   else: #if non-assigned area not bordered with an assigned area
                       tempHeight = deepcopy(height) # remove top and bottom section to make way for buildable area
                       tempHeight.sort()
                       tempHeight = [i for i in tempHeight if i > 0]
                       if len(tempHeight) > 1:
                           upperRemoval = tempHeight[int(len(tempHeight) * 0.75):len(tempHeight)]
                           upperRemoval = list(set(upperRemoval))
                           lowerRemoval = tempHeight[0:int(len(tempHeight) * 0.1)]
                           lowerRemoval = list(set(lowerRemoval))
                           if len([i for i in list(set(tempHeight)) if i not in upperRemoval]) > 1:
                               targetHeight = max([i for i in list(set(tempHeight)) if i not in upperRemoval])
                               if len(tempHeight[int(len(tempHeight) * 0.75):len(tempHeight)]) > 1:
                                   for i in range(len(height)):
                                       if height[i] in upperRemoval and height[i] > 0 and targetHeight > 0:
                                           alterDict[area[i][0], area[i][1]] = targetHeight - height[i]
                                           alterHeightDict[area[i][0], area[i][1]] = height[i]
    return alterDict,alterHeightDict

def FindMountain(alterDict, heightmap):
    print("Finding mountains")
    MountainMap = [[0 for k in range(len(heightmap[0]))] for j in range(len(heightmap))]
    tempHM = deepcopy(heightmap)
    for key, value in alterDict:
        x = key
        y = value
        if alterDict[x,y]<=-10:
            MountainMap[x][y] = 1
    for x in range(len(tempHM)):
        for y in range(len(tempHM[0])):
            if tempHM[x][y] != 999 and MountainMap[x][y] == 1:
                stonks = []
                stonks.append([x,y])
                length = len(stonks)
                tempHM[x][y] = 999
                while length >= 1:
                    x = stonks[0][0]
                    y = stonks[0][1]
                    stonks.pop(0)
                    if (y - 1) >= 0: # go to west
                        if tempHM[x][y - 1] != 999 and MountainMap[x][y - 1] == 0 and (x, y - 1) in alterDict:
                            if alterDict[x, y - 1] != alterDict[x, y] or alterDict[x, y - 1]<=-2:
                                stonks.append([x, y - 1])
                                MountainMap[x][y - 1] = 1 
                                tempHM[x][y - 1] = 999
                    if (y + 1) < len(tempHM[x]): # go to east
                        if tempHM[x][y + 1] != 999 and MountainMap[x][y + 1] == 0 and (x, y + 1) in alterDict:
                            if alterDict[x, y + 1] != alterDict[x, y] or alterDict[x, y + 1]<=-2:
                                stonks.append([x, y + 1])
                                MountainMap[x][y + 1] = 1 
                                tempHM[x][y + 1] = 999
                    if (x + 1) < len(tempHM): # go to south
                        if tempHM[x + 1][y] != 999 and MountainMap[x + 1][y] == 0 and (x + 1, y) in alterDict:
                            if alterDict[x + 1, y] != alterDict[x, y] or alterDict[x + 1, y]<=-2:
                                stonks.append([x + 1, y])
                                MountainMap[x + 1][y] = 1 
                                tempHM[x + 1][y] = 999
                    if (x - 1) >= 0: # go to north
                        if tempHM[x - 1][y] != 999 and MountainMap[x - 1][y] == 0 and (x - 1, y) in alterDict:
                            if alterDict[x - 1, y] != alterDict[x, y] or alterDict[x - 1, y]<=-2:
                                stonks.append([x - 1, y])
                                MountainMap[x - 1][y] = 1 
                                tempHM[x - 1][y] = 999
                    length = len(stonks)
    return MountainMap

def editTerrainFF(alterDict, alterHeightDict, heightmap, buildArea, env, ClearMountain):
    MountainMap = FindMountain(alterDict, heightmap)
    print("Editing terrain")
    def FindAdjacentType(x, y):
        tempHM = deepcopy(heightmap)
        stonks = []
        stonks.append([x,y])
        length = len(stonks)
        tempHM[x][y] = 999
        while length >= 1:
            x = stonks[0][0]
            y = stonks[0][1]
            stonks.pop(0)
            if ((y - 1) >= 0):  # go to west
                if tempHM[x][y - 1] != 999:
                    if env[x][y - 1] in [1,2,3]:
                        return env[x][y - 1]
                    else:
                        stonks.append([x, y - 1])
                        tempHM[x][y - 1] = 999
            if ((y + 1) < buildArea[2]): # go to east
                if tempHM[x][y + 1] != 999:
                    if env[x][y + 1] in [1,2,3]:
                        return env[x][y + 1]
                    else:
                        stonks.append([x, y + 1])
                        tempHM[x][y + 1] = 999
            if ((x + 1) < buildArea[3]): # go to south
                if tempHM[x + 1][y] != 999:
                    if env[x + 1][y] in [1,2,3]:
                        return env[x + 1][y]
                    else:
                        stonks.append([x + 1, y])
                        tempHM[x + 1][y] = 999
            if ((x - 1) >= 0): # go to north
                if tempHM[x - 1][y] != 999:
                    if env[x - 1][y] in [1,2,3]:
                        return env[x - 1][y]
                    else:
                        stonks.append([x - 1, y])
                        tempHM[x - 1][y] = 999
            length = len(stonks)
        return -1
    for key, value in alterDict:
        x = key
        z = value
        diff = alterDict[x,z]
        if env[x][z] != 0 and (MountainMap[x][z] == 0 or ClearMountain):
            if env[x][z] == 1:
                blockType = 'grass_block'
            elif env[x][z] == 2:
                blockType = 'sand'
            elif env[x][z] == 3:
                blockType = 'stone'
            elif env[x][z] == 4:
                blockID = FindAdjacentType(x, z)
                if blockID == 1:
                    blockType = 'grass_block'
                elif blockID == 2:
                    blockType = 'sand'
                elif blockID == 3:
                    blockType = 'stone'
                else:
                    blockType = 'grass_block'
            if diff > 0:
                for i in range(diff):
                    ED.placeBlock((buildArea[0]+x, alterHeightDict[x,z]+i, buildArea[1]+z), Block(blockType))
            elif diff < 0:
                for i in range(-diff):
                    ED.placeBlock((buildArea[0]+x, alterHeightDict[x,z]-1-i, buildArea[1]+z), Block('air'))
                ED.placeBlock((buildArea[0]+x, alterHeightDict[x,z]-1+diff, buildArea[1]+z), Block(blockType))

def executeFF(heightMap, buildArea, env, minimumArea, exclusion = 0, ClearMountain = 0):
    alterDict, alterHeightDict = floodFill(heightMap, minimumArea, exclusion)
    editTerrainFF(alterDict, alterHeightDict, heightMap, buildArea, env, ClearMountain)

def setSameHeight(heightmap, buildArea, block_id):
    print('setSameHeight')
    begin_time=time()
    heightlist = [h2 for h1 in heightmap for h2 in h1]
    maxH = Counter(heightlist).most_common(1)[0][0]
    for x in range(len(heightmap)):
        for y in range(len(heightmap[0])):
            diff = maxH - heightmap[x][y]
            if diff > 0:
                for i in range(diff):
                    # print(buildArea[0]+x, heightmap[x][y]+i, buildArea[1]+y)
                    ED.placeBlock((buildArea[0]+x, heightmap[x][y]+i, buildArea[1]+y), Block(block_id))
            elif diff <= 0:
                for i in range(-diff):
                    # print(buildArea[0]+x, heightmap[x][y]+i, buildArea[1]+y)
                    ED.placeBlock((buildArea[0]+x, heightmap[x][y]-1-i, buildArea[1]+y), Block('air'))
                ED.placeBlock((buildArea[0]+x, heightmap[x][y]-1+diff, buildArea[1]+y), Block(block_id))

    end_time=time()
    print('setSameHeight done')
    print("time:",end_time-begin_time)
    return maxH
