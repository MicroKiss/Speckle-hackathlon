from specklepy.objects.other import RenderMaterial
from amulet import Block
from specklepy.objects import Base
from specklepy.objects.geometry import Box, Plane, Interval
from utility import *
from BlockColorDictionary import GetMaterial

doorWidth = 3*PIXEL
intervalDoorWidth = Interval(start=0, end=doorWidth)
threePixel = Interval(start=0, end=3*PIXEL)

# West & South
def CreateUpperDoor1(x: int, y: int, z: int, block: Block) -> Base:
    ret = Base()
    pieces : 'list[Box]' = []
    left = Box(xSize=threePixel, ySize=intervalDoorWidth,
                   zSize=intervalWhole, basePlane=Plane.from_list([x - 0.5 + 1.5*PIXEL, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(xSize=threePixel, ySize=intervalDoorWidth,
                   zSize=intervalWhole, basePlane=Plane.from_list([x + 0.5 - 1.5*PIXEL, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    top = Box(xSize=Interval(start=0, end=10*PIXEL), ySize=intervalDoorWidth,
                   zSize=threePixel, basePlane=Plane.from_list([x, y , z+ 0.5 - 1.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottom = Box(xSize=Interval(start=0, end=10*PIXEL), ySize=intervalDoorWidth,
                   zSize=threePixel, basePlane=Plane.from_list([x, y , z- 0.5 + 1.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middle = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=intervalDoorWidth,
                   zSize=Interval(start=0, end=10*PIXEL), basePlane=Plane.from_list([x, y , z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleRight = Box(xSize=Interval(start=0, end=4*PIXEL), ySize=intervalDoorWidth,
                   zSize=Interval(start=0, end=2*PIXEL), basePlane=Plane.from_list([x + 3 * PIXEL, y , z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleLeft = Box(xSize=Interval(start=0, end=4*PIXEL), ySize=intervalDoorWidth,
                   zSize=Interval(start=0, end=2*PIXEL), basePlane=Plane.from_list([x - 3 * PIXEL, y , z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append (left)                
    pieces.append (right)               
    pieces.append (top)              
    pieces.append (bottom)                
    pieces.append (middle)       
    pieces.append (middleRight)     
    pieces.append (middleLeft) 
    ret.pieces = pieces
    return ret

# North & East
def CreateUpperDoor2(x: int, y: int, z: int, block: Block) ->Base:
    ret = Base()
    pieces : 'list[Box]' = []
    left = Box(ySize=threePixel, xSize=intervalDoorWidth,
                   zSize=intervalWhole, basePlane=Plane.from_list([x, y - 0.5 + 1.5*PIXEL, z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(ySize=threePixel, xSize=intervalDoorWidth,
                   zSize=intervalWhole, basePlane=Plane.from_list([x, y + 0.5 - 1.5*PIXEL, z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    top = Box(ySize=Interval(start=0, end=10*PIXEL), xSize=intervalDoorWidth,
                   zSize=threePixel, basePlane=Plane.from_list([x, y , z+ 0.5 - 1.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottom = Box(ySize=Interval(start=0, end=10*PIXEL), xSize=intervalDoorWidth,
                    zSize=threePixel, basePlane=Plane.from_list([x, y , z- 0.5 + 1.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middle = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=intervalDoorWidth,
                    zSize=Interval(start=0, end=10*PIXEL), basePlane=Plane.from_list([x, y , z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleRight = Box(ySize=Interval(start=0, end=4*PIXEL), xSize=intervalDoorWidth,
                   zSize=Interval(start=0, end=2*PIXEL), basePlane=Plane.from_list([x , y + 3 * PIXEL, z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleLeft = Box(ySize=Interval(start=0, end=4*PIXEL), xSize=intervalDoorWidth,
                   zSize=Interval(start=0, end=2*PIXEL), basePlane=Plane.from_list([x, y  - 3 * PIXEL, z, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append (left)                
    pieces.append (right)               
    pieces.append (top)              
    pieces.append (bottom)                
    pieces.append (middle)       
    pieces.append (middleRight)     
    pieces.append (middleLeft) 

    ret.pieces = pieces
    return ret


def CreateLowerDoor1(x: int, y: int, z: int, block: Block) -> Box:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalWhole, ySize=intervalDoorWidth,
              zSize=intervalWhole, basePlane=plane)
    return ret


def CreateLowerDoor2(x: int, y: int, z: int, block: Block) -> Box:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalDoorWidth, ySize=intervalWhole,
              zSize=intervalWhole, basePlane=plane)
    return ret


def CreateDoor(x: int, y: int, z: int, block: Block) -> Base:
    ret: Base = None
    if (block.properties["half"] == "upper"):
        if (((block.properties["facing"] == "west" or block.properties["facing"] == "east") and block.properties["open"] == "true")
                or ((block.properties["facing"] == "north" or block.properties["facing"] == "south") and block.properties["open"] == "false")):
            ret = CreateUpperDoor1(x, y, z, block)
        else:
            ret = CreateUpperDoor2(x, y, z, block)
        for p in ret.pieces:
            p.renderMaterial = GetMaterial(block)
    elif (block.properties["half"] == "lower"):
        if (((block.properties["facing"] == "west" or block.properties["facing"] == "east") and block.properties["open"] == "true")
                or ((block.properties["facing"] == "north" or block.properties["facing"] == "south") and block.properties["open"] == "false")):
            ret = CreateLowerDoor1(x, y, z, block)
        else:
            ret = CreateLowerDoor2(x, y, z, block)
        ret.renderMaterial = GetMaterial (block)

    ret.info = block.properties["facing"] + block.properties["open"]
    return ret
