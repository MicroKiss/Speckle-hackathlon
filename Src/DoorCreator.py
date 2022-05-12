from specklepy.objects.other import RenderMaterial
from specklepy.objects import Base
from specklepy.objects.geometry import Box, Plane, Interval
from utility import *
from amulet import Block
from BlockColorDictionary import GetBlockColor
from BlockCreator import CreateBlock

doorWidth = 3*PIXEL
intervalDoorWidth = Interval(start=0, end=doorWidth)

def CreateUpperDoor1(x: int, y: int, z: int, block: Block):
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalWhole, ySize=intervalDoorWidth,
              zSize=intervalWhole, basePlane=plane)
    return ret
def CreateUpperDoor2(x: int, y: int, z: int, block: Block):
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalDoorWidth, ySize=intervalWhole,
              zSize=intervalWhole, basePlane=plane)
    return ret


def CreateLowerDoor1(x: int, y: int, z: int, block: Block):
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalWhole, ySize=intervalDoorWidth,
              zSize=intervalWhole, basePlane=plane)
    return ret
def CreateLowerDoor2(x: int, y: int, z: int, block: Block):
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalDoorWidth, ySize=intervalWhole,
              zSize=intervalWhole, basePlane=plane)
    return ret


def CreateDoor(x: int, y: int, z: int, block: Block) -> Base:
    ret: Box = None
    mat = GetBlockColor(block.base_name)
    #if (block.properties["half"] == "upper"):
    #elif (block.properties["half"] == "lower"):
    if (((block.properties["facing"] == "west" or block.properties["facing"] == "east" ) and block.properties["open"] == "true")
    or ((block.properties["facing"] == "north" or block.properties["facing"] == "south" ) and block.properties["open"] == "false")):
        ret = CreateUpperDoor1(x, y, z, block)
    else:
        ret = CreateUpperDoor2(x, y, z, block)

    ret.info = block.properties["facing"]  + block.properties["open"] 
    return ret
