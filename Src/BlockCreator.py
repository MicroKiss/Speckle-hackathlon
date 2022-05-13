from specklepy.objects.geometry import Box, Plane
from amulet import Block
from utility import *
from BlockColorDictionary import GetMaterial


def CreateBlock(x: int, y: int, z: int, block: Block) -> Box:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=intervalWhole, ySize=intervalWhole,
              zSize=intervalWhole, basePlane=plane)
    ret.renderMaterial = GetMaterial(block)
    return ret
