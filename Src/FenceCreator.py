from specklepy.objects import Base
from specklepy.objects.geometry import  Box, Plane
from amulet import Block
from BlockColorDictionary import GetMaterial
from utility import *

upperSideFenceZdiff = -PIXEL + 0.5 - sideFenceHeight / 2
lowerSideFenceZdiff = - 3/2*PIXEL + sideFenceHeight / 2

class Fence (
    Base
):
    mainFence: Box = None
    sideFences: Base = None



def CreateWestSide (x: int, y: int, z: int, block: Block) -> Base:
    westSide = Base()
    planeLower = Plane.from_list(
        [x - 0.5 + sideFenceLength / 2, y, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = GetMaterial (block)

    westSide.lower = lower
    planeUpper = Plane.from_list(
        [x - 0.5 + sideFenceLength / 2, y, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = GetMaterial (block)
    westSide.upper = upper
    return westSide

def CreateEastSide (x: int, y: int, z: int, block: Block) -> Base:
    eastSide = Base()
    planeLower = Plane.from_list(
        [x + 0.5 - sideFenceLength / 2, y, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = GetMaterial (block)
    eastSide.lower = lower
    planeUpper = Plane.from_list(
        [x + 0.5 - sideFenceLength / 2, y, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = GetMaterial (block)
    eastSide.upper = upper
    return eastSide

def CreateNorthSide (x: int, y: int, z: int, block: Block) -> Base:
    northSide = Base()
    planeUpper = Plane.from_list(
        [x, y + 0.5 - sideFenceLength / 2, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = GetMaterial (block)
    planeLower = Plane.from_list(
        [x, y + 0.5 - sideFenceLength / 2, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = GetMaterial (block)
    northSide.lower = lower
    northSide.upper = upper
    return northSide

def CreateSouthSide (x: int, y: int, z: int, block: Block) -> Base:
    southSide = Base()
    planeUpper = Plane.from_list(
        [x, y - 0.5 + sideFenceLength / 2, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = GetMaterial (block)
    planeLower = Plane.from_list(
        [x, y - 0.5 + sideFenceLength / 2, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = GetMaterial (block)
    southSide.lower = lower
    southSide.upper = upper
    return southSide

def CreateSideFences(x: int, y: int, z: int, block: Block) -> Base:
    ret = Base()
    if (block.properties["west"] == "true"):
        ret.westSide = CreateWestSide (x,y,z,block)
    if (block.properties["east"] == "true"):
        ret.eastSide = CreateEastSide (x,y,z,block)
    if (block.properties["north"] == "true"):
        ret.northSide = CreateNorthSide (x,y,z,block)
    if (block.properties["south"] == "true"):
        ret.southSide = CreateSouthSide (x,y,z,block)
    return ret


def CreateMainFence(x: int, y: int, z: int, block: Block) -> Box:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=interval4Middle, ySize=interval4Middle,
              zSize=intervalWhole, basePlane=plane)
    ret.renderMaterial = GetMaterial (block)
    return ret


def CreateFence(x: int, y: int, z: int, block: Block) -> Base:
    ret = Fence()
    ret.mainFence = CreateMainFence(x, y, z, block)
    ret.sideFences = CreateSideFences(
        x, y, z, block)
    return ret
