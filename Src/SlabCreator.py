from specklepy.objects.geometry import Box, Plane
from utility import *
from amulet import Block
from BlockColorDictionary import GetMaterial
from BlockCreator import CreateBlock


def CreateUpperSlab(x: int, y: int, z: int, block: Block):
    plane = Plane.from_list([x, y, z+0.25, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalWhole, ySize=intervalWhole,
              zSize=intervalHalf, basePlane=plane)
    ret.renderMaterial = GetMaterial (block)
    return ret


def CreateLowerSlab(x: int, y: int, z: int, block: Block):
    plane = Plane.from_list([x, y, z-0.25, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalWhole, ySize=intervalWhole,
              zSize=intervalHalf, basePlane=plane)
    ret.renderMaterial = GetMaterial (block)
    return ret


def CreateSlab(x: int, y: int, z: int, block: Block) -> Box:
    ret: Box = None
    if (block.properties["type"] == "double"):
        ret = CreateBlock(x, y, z, block)
    elif (block.properties["type"] == "top"):
        ret = CreateUpperSlab(x, y, z, block)
    elif (block.properties["type"] == "bottom"):
        ret = CreateLowerSlab(x, y, z, block)
    return ret
