from gdpc import Block, Editor

ED = Editor(buffering=True)

def make_roof(ED, x1, x2, orientation='x'):
    x1, y1, z1 = x1[0], x1[1], x1[2]
    x2, y2, z2 = x2[0], x2[1], x2[2]
    a = Block('minecraft:nether_bricks')
    b = Block('minecraft:nether_brick_slab', {'type':'bottom'})
    c = Block('minecraft:nether_brick_wall',{'up':'true'})
    if orientation == 'x':
        for x in range(x1, x1+5):
            ED.placeBlock((x, y1, z1), a)
        for x in range(x2-4, x2+1):
            ED.placeBlock((x, y1, z1), a)
        for x in range(x1+4, x2-3):
            ED.placeBlock((x, y1, z1), b)
        ED.placeBlock((x1, y1 + 1, z1), c)
        ED.placeBlock((x2, y1 + 1, z1), c)
        ED.placeBlock((x1+2, y1 + 1, z1), a)
        ED.placeBlock((x2-2, y1 + 1, z1), a)
        ED.placeBlock((x1 + 2, y1 + 2, z1), Block("minecraft:dragon_head", {"rotation":4}))
        ED.placeBlock((x2 - 2, y1 + 2, z1), Block("minecraft:dragon_head", {"rotation":12}))
        ED.placeBlock((x1 + 3, y1 + 1, z1), b)
        ED.placeBlock((x2 - 3, y1 + 1, z1), b)
        ED.placeBlock((x1, y1+2, z1), Block("minecraft:lantern"))
        ED.placeBlock((x2, y1+2, z1), Block("minecraft:lantern"))
    else:
        for z in range(z1, z1 + 5):
            ED.placeBlock((x1, y1, z), a)
        for z in range(z2 - 4, z2 + 1):
            ED.placeBlock((x1, y1, z), a)
        for z in range(z1 + 4, z2 - 3):
            ED.placeBlock((x1, y1, z), b)
        ED.placeBlock((x1, y1 + 1, z1), c)
        ED.placeBlock((x2, y1 + 1, z2), c)
        ED.placeBlock((x1, y1 + 1, z1 + 2), a)
        ED.placeBlock((x1, y1 + 1, z2 - 2), a)
        ED.placeBlock((x1, y1 + 2, z1 + 2), Block("minecraft:dragon_head", {"rotation":8}))
        ED.placeBlock((x1, y1 + 2, z2 - 2), Block("minecraft:dragon_head", {"rotation":0}))
        ED.placeBlock((x1, y1 + 1, z1 + 3), b)
        ED.placeBlock((x1, y1 + 1, z2 - 3), b)
        ED.placeBlock((x1, y1+2, z1), Block("minecraft:lantern"))
        ED.placeBlock((x1, y1+2, z2), Block("minecraft:lantern"))