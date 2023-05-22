

def make_roof(interface, x1, x2, orientation='x'):
    x1, y1, z1 = x1[0], x1[1], x1[2]
    x2, y2, z2 = x2[0], x2[1], x2[2]
    a = 'minecraft:nether_bricks'
    b = 'minecraft:nether_brick_slab[type=bottom]'
    c = 'minecraft:nether_brick_wall[up=true]'
    if orientation == 'x':
        for x in range(x1, x1+5):
            interface.placeBlock(x, y1, z1, a)
        for x in range(x2-4, x2+1):
            interface.placeBlock(x, y1, z1, a)
        for x in range(x1+4, x2-3):
            interface.placeBlock(x, y1, z1, b)
        interface.placeBlock(x1, y1 + 1, z1, c)
        interface.placeBlock(x2, y1 + 1, z1, c)
        interface.placeBlock(x1+2, y1 + 1, z1, a)
        interface.placeBlock(x2-2, y1 + 1, z1, a)
        interface.placeBlock(x1 + 2, y1 + 2, z1, "dragon_head[rotation=4]")
        interface.placeBlock(x2 - 2, y1 + 2, z1, "dragon_head[rotation=12]")
        interface.placeBlock(x1 + 3, y1 + 1, z1, b)
        interface.placeBlock(x2 - 3, y1 + 1, z1, b)
        interface.placeBlock(x1, y1+2, z1, "lantern")
        interface.placeBlock(x2, y1+2, z1, "lantern")
    else:
        for z in range(z1, z1 + 5):
            interface.placeBlock(x1, y1, z, a)
        for z in range(z2 - 4, z2 + 1):
            interface.placeBlock(x1, y1, z, a)
        for z in range(z1 + 4, z2 - 3):
            interface.placeBlock(x1, y1, z, b)
        interface.placeBlock(x1, y1 + 1, z1, c)
        interface.placeBlock(x2, y1 + 1, z2, c)
        interface.placeBlock(x1, y1 + 1, z1 + 2, a)
        interface.placeBlock(x1, y1 + 1, z2 - 2, a)
        interface.placeBlock(x1, y1 + 2, z1 + 2, "dragon_head[rotation=8]")
        interface.placeBlock(x1, y1 + 2, z2 - 2, "dragon_head[rotation=0]")
        interface.placeBlock(x1, y1 + 1, z1 + 3, b)
        interface.placeBlock(x1, y1 + 1, z2 - 3, b)
        interface.placeBlock(x1, y1+2, z1, "lantern")
        interface.placeBlock(x1, y1+2, z2, "lantern")