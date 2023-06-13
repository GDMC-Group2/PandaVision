from winreg import REG_EXPAND_SZ
import interfaceUtils

USE_BATCHING = True

def setBlock(x, y, z, block):
    """Place blocks or add them to batch."""
    if USE_BATCHING:
        # add block to buffer, send once buffer has 100 items in it
        interfaceUtils.placeBlockBatched(x, y, z, block, 100)
    else:
        interfaceUtils.setBlock(x, y, z, block)


class RoadGenerator():
    # 初期化
    def __init__(self, area, heightmap, new_array, area_with_border):
        self.area_with_border = area_with_border
        self.area = area
        self.heightmap = heightmap # heightmap
        self.new_array = new_array
        self.flag1 = True
        self.flag2 = True
        self.x_dif = 0 # ｘ difference
        self.z_dif = 0 # ｚ difference
        self.block_box = "stone_bricks" # block of road
        self.direction = 0 # direction (0 or 1)
        self.width = 3 # width

    # 道の生成
    def find_real_start_end(self, start, end):
        previous = (start[0], start[1]) # position in array
        ss = 0
        r = []


        # Calculate difference between start and end
        self.x_dif = end[0]-start[0] # x座標
        if self.x_dif > 0:
            self.flag1 = True
        else:
            self.flag1 = False

        self.z_dif = end[1]-start[1] # z座標
        if self.z_dif > 0:
            self.flag2 = True
        else:
            self.flag2 = False

        if self.z_dif!=0: # z
            if self.flag2: # +
                for zz in range(abs(self.z_dif)):
                    if previous[0]>0 and previous[0]<self.area[2]-1 and previous[1]+zz>0 and previous[1]+zz<self.area[3]-1:
                        if self.area_with_border[previous[0], previous[1]+zz] >-2:
                            r.append((previous[0], previous[1]+zz))
                    ss = zz

                previous = (previous[0], previous[1]+ss)
            else: # -
                for zz in range(abs(self.z_dif)):
                    if previous[0]>0 and previous[0]<self.area[2]-1 and previous[1]-zz>0 and previous[1]-zz<self.area[3]-1:
                        if self.area_with_border[previous[0], previous[1]-zz] >-2:
                            r.append((previous[0], previous[1]-zz))
                    ss = zz

                previous = (previous[0], previous[1]-ss)

        if self.x_dif!=0: # x
            if self.flag1: # +
                for xx in range(abs(self.x_dif)):
                    if previous[0]+xx>0 and previous[0]+xx<self.area[2]-1 and previous[1]>0 and previous[1]<self.area[3]-1:
                        if self.area_with_border[previous[0]+xx, previous[1]] >-2:
                            r.append((previous[0]+xx, previous[1]))
            else: # -
                for xx in range(abs(self.x_dif)):
                    if previous[0]-xx>0 and previous[0]-xx<self.area[2]-1 and previous[1]>0 and previous[1]<self.area[3]-1:
                        if self.area_with_border[previous[0]-xx, previous[1]] >-2:
                            r.append((previous[0]-xx, previous[1]))
        if r!=[]:
            r_start = r[0]
            r_end = r[-1]
            return r_start, r_end
        else:
            return start, end

    # def illumination(self, cnt, x, y, z):
    #     if cnt%4==1:
    #         setBlock(x,y-1,z, "sea_lantern")

    def generate(self, path_list):
        i = 0
        for one_p in path_list:
            x = one_p[0]
            z = one_p[1]
            r_x = one_p[0] + self.area[0]
            r_z = one_p[1] + self.area[1]
            
            for x_w in range(x-self.width//2, x + self.width//2+1):
                if x_w < 0 or x_w > self.heightmap.shape[0] or x_w == x:
                    continue
                if i % 4 == 1 or i % 4 == 2:
                    setBlock(x_w + self.area[0], self.heightmap[x_w][z]-1, r_z, 'sea_lantern')
                else:
                    setBlock(x_w + self.area[0], self.heightmap[x_w][z]-1, r_z, 'stone_bricks')
            for z_w in range(z-self.width//2, z + self.width//2+1):
                if z_w < 0 or z_w > self.heightmap.shape[1] or z_w == z:
                    continue
                if i % 4 == 1 or i % 4 == 2:
                    setBlock(r_x, self.heightmap[x][z_w]-1, z_w + self.area[1], 'sea_lantern')
                else:
                    setBlock(r_x, self.heightmap[x][z_w]-1, z_w + self.area[1], 'stone_bricks')
            if i%4==1:
                setBlock(r_x, self.heightmap[one_p[0]][one_p[1]]-1, r_z, 'sea_lantern')
            else:
                setBlock(r_x, self.heightmap[one_p[0]][one_p[1]]-1, r_z, 'stone_bricks')
            i += 1
            # for i in range(self.width):
            #     for j in range(self.width):
            #         if one_p[0] + self.area[0]-2+i<self.area[2]-1 and one_p[0] + self.area[0]-2+i>0 and one_p[1] + self.area[1]-2+j<self.area[3]-1 and one_p[1] + self.area[1]-2+j>0:
            #             setBlock(one_p[0] + self.area[0]-1+i, self.heightmap[one_p[0]-1+i][one_p[1]-1+j]-1, one_p[1] + self.area[1]-1+j, 'stone_bricks')
            #     self.illumination(i, one_p[0] + self.area[0], self.heightmap[one_p[0]][one_p[1]]-1, one_p[1] + self.area[1])
        interfaceUtils.sendBlocks()
def rectanglesOverlap(r1, r2):
    """Check that r1 and r2 do not overlap."""
    if (r1 >= r2 + r2[2]) or (r1 + r1[2] <= r2) or (r1 + r1 <= r2) or (r1 >= r2 + r2):
        return False
    else:
        return True
