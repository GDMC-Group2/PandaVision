from Building import hotel, hotel2, house1, house2, house3, Farm, Tower, Pavilion, store, well, wall, river, bridge,blacksmith,honey_farm
from gdpc import Editor, Block

ED = Editor(buffering=True)

CoverList = [
    'store1_n',
    'store1_s',
    'store1_e',
    'store1_w',
    'store2_n',
    'store2_s',
    'store2_e',
    'store2_w',
    'store3_n',
    'store3_s',
    'store3_e',
    'store3_w',
    'pavilion_n',
    'pavilion_s',
    'pavilion_e',
    'pavilion_w'
 ]


def placeBuildings(buildingDict, area, height):
    for location, building in buildingDict.items():
        if building == 'tower':
            Tower.buildTower(area[0]+location[0]+15, height, area[1]+location[1]+15, 7)
        if building == 'farm':
            Farm.buildFarm(area[0]+location[0]+21, height, area[1]+location[1]+21)
        if building == 'house1_n':
            house1.house1(area[0]+location[0]+6, height, area[1]+location[1]+2,'n')
        if building == 'house1_s':
            house1.house1(area[0]+location[0]+6, height, area[1]+location[1]+13,'s')
        if building == 'house1_e':
            house1.house1(area[0]+location[0]+13, height, area[1]+location[1]+6,'e')
        if building == 'house1_w':
            house1.house1(area[0]+location[0]+2, height, area[1]+location[1]+6,'w')
        if building == 'house2_n':
            house2.house2(area[0]+location[0]+15, height, area[1]+location[1]+17,'n')
        if building == 'house2_s':
            house2.house2(area[0]+location[0]+15, height, area[1]+location[1]+12,'s')
        if building == 'house2_e':
            house2.house2(area[0]+location[0]+12, height, area[1]+location[1]+15,'e')
        if building == 'house2_w':
            house2.house2(area[0]+location[0]+17, height, area[1]+location[1]+15,'w')
        if building == 'house3_n':
            house3.house3(area[0]+location[0]+1, height, area[1]+location[1]+13,'n')
        if building == 'house3_s':
            house3.house3(area[0]+location[0]+1, height, area[1]+location[1]+9,'s')
        if building == 'house3_e':
            house3.house3(area[0]+location[0]+9, height, area[1]+location[1]+1,'e')
        if building == 'house3_w':
            house3.house3(area[0]+location[0]+13, height, area[1]+location[1]+1,'w')
        if building == 'store1_n':
            store.store1(area[0]+location[0], height, area[1]+location[1]+10,'n')
        if building == 'store1_s':
            store.store1(area[0]+location[0], height, area[1]+location[1]+1,'s')
        if building == 'store1_e':
            store.store1(area[0]+location[0]+1, height, area[1]+location[1],'e')
        if building == 'store1_w':
            store.store1(area[0]+location[0]+10, height, area[1]+location[1],'w')
        if building == 'store2_n':
            store.store2(area[0]+location[0], height, area[1]+location[1]+10,'n')
        if building == 'store2_s':
            store.store2(area[0]+location[0], height, area[1]+location[1]+1,'s')
        if building == 'store2_e':
            store.store2(area[0]+location[0]+1, height, area[1]+location[1],'e')
        if building == 'store2_w':
            store.store2(area[0]+location[0]+10, height, area[1]+location[1],'w')
        if building == 'store3_n':
            store.store3(area[0]+location[0], height, area[1]+location[1]+10,'n')
        if building == 'store3_s':
            store.store3(area[0]+location[0], height, area[1]+location[1]+1,'s')
        if building == 'store3_e':
            store.store3(area[0]+location[0]+1, height, area[1]+location[1],'e')
        if building == 'store3_w':
            store.store3(area[0]+location[0]+10, height, area[1]+location[1],'w')
        if building == 'pavilion_n':
            Pavilion.buildPavilion(area[0]+location[0]+8, height, area[1]+location[1]+8,'n')
        if building == 'pavilion_s':
            Pavilion.buildPavilion(area[0]+location[0]+8, height, area[1]+location[1]+9,'s')
        if building == 'pavilion_e':
            Pavilion.buildPavilion(area[0]+location[0]+9, height, area[1]+location[1]+8,'e')
        if building == 'pavilion_w':
            Pavilion.buildPavilion(area[0]+location[0]+8, height, area[1]+location[1]+8,'w')
        if building == 'well':
            well.Wells(area[0]+location[0]+1, height, area[1]+location[1]+1)
        if building == 'blacksmith_n':
            blacksmith.blacksmith_main(area[0]+location[0]+9, height, area[1]+location[1]+7,'n')
        if building == 'blacksmith_s':
            blacksmith.blacksmith_main(area[0]+location[0], height, area[1]+location[1],'s')
        if building == 'blacksmith_e':
            blacksmith.blacksmith_main(area[0]+location[0]+7, height, area[1]+location[1],'e')
        if building == 'blacksmith_w':
            blacksmith.blacksmith_main(area[0]+location[0], height, area[1]+location[1]+9,'w')
        if building == 'honey_farm_n':
            honey_farm.honey_farm(area[0]+location[0],height,area[1]+location[1],'n')
        if building == 'honey_farm_e':
            honey_farm.honey_farm(area[0]+location[0],height,area[1]+location[1],'e')
def placeMainRoad(x,y,z,l,f):
    y = y-1
    if f == 'x':
        for i in range(-l,l+1):
            for j in range(-1,2):
                ED.placeBlock((x+i,y,z+j), Block('polished_andesite'))
            ED.placeBlock((x+i,y,z+2), Block('smooth_stone'))
            ED.placeBlock((x+i,y,z-2), Block('smooth_stone'))
            ED.placeBlock((x+i,y,z+3), Block('polished_andesite'))
            ED.placeBlock((x+i,y,z-3), Block('polished_andesite'))
            ED.placeBlock((x+i,y,z+4), Block('chiseled_stone_bricks'))
            ED.placeBlock((x+i,y,z-4), Block('chiseled_stone_bricks'))
    if f == 'z':
        for j in range(-l,l+1):
            for i in range(-1,2):
                ED.placeBlock((x+i,y,z+j), Block('polished_andesite'))
            ED.placeBlock((x+2,y,z+j), Block('smooth_stone'))
            ED.placeBlock((x-2,y,z+j), Block('smooth_stone'))
            ED.placeBlock((x+3,y,z+j), Block('polished_andesite'))
            ED.placeBlock((x-3,y,z+j), Block('polished_andesite'))
            ED.placeBlock((x+4,y,z+j), Block('chiseled_stone_bricks'))
            ED.placeBlock((x-4,y,z+j), Block('chiseled_stone_bricks'))

def setSurface(buildingMap, area, height, BlockType):
    for x in range(area[2]):
        for y in range(area[3]):
            if type(buildingMap[x][y]) == int or buildingMap[x][y] in CoverList:
                ED.placeBlock((area[0]+x,height-1,area[1]+y),Block(BlockType))

def placeCity(buildingMap, buildingDict, area, height, q_id,isMaxArea = 0):
    wall_width = 11
    x_len = area[2]
    y_len = area[3]
    buildArea = x_len*y_len
    x_middle = int(x_len/2)
    y_middle = int(y_len/2)
    print(buildingDict)
    if isMaxArea == 1:
        if buildArea >= 60000 and x_len >= 250 and y_len >= 250:
            x_road = int((x_middle-44-wall_width)/2)
            y_road = int((y_middle-44-wall_width)/2)
            setSurface(buildingMap, area, height, q_id)
            wall.make_wall(height, area)
            placeMainRoad(area[0]+x_middle,height,area[1]+y_middle-y_road-44,x_middle-1,'x')
            placeMainRoad(area[0]+x_middle,height,area[1]+y_middle+y_road+44,x_middle-1,'x')
            placeMainRoad(area[0]+x_middle-x_road-44,height,area[1]+y_middle,y_middle-1,'z')
            placeMainRoad(area[0]+x_middle+x_road+44,height,area[1]+y_middle,y_middle-1,'z')
            river.river(area[0]+x_middle,height,area[1]+y_middle,x_middle-wall_width+1)
            bridge.Bridge(area[0]+x_middle-x_road-44,height,area[1]+y_middle)
            bridge.Bridge(area[0]+x_middle+x_road+44,height,area[1]+y_middle)
            hotel.hotel(area[0]+x_middle,height,area[1]+y_middle)
            placeBuildings(buildingDict, area, height)
        elif buildArea > 16900 and x_len > 130 and y_len > 130:
            setSurface(buildingMap, area, height, q_id)
            wall.make_wall(height, area)
            hotel.hotel(area[0]+x_middle,height,area[1]+y_middle)
            placeBuildings(buildingDict, area, height)
        else:
            setSurface(buildingMap, area, height, q_id)
            hotel2.hotel(area[0]+x_middle,height,area[1]+y_middle)
            placeMainRoad(area[0]+x_middle,height,area[1]+y_middle,x_middle,'x')
    else:
        if buildArea >= 1000:
            setSurface(buildingMap, area, height, q_id)
        placeBuildings(buildingDict, area, height)
