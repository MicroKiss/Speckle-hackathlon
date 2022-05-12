from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, Point
from amulet import Block
from BlockColorDictionary import GetBlockColor
from utility import *

upperSideFenceZdiff = -PIXEL + 0.5 - sideFenceHeight / 2
lowerSideFenceZdiff = - 3/2*PIXEL + sideFenceHeight / 2

class Fence (
    Base
):
    mainFence: Box = None
    sideFences: Base = None



def CreateWestSide (x: int, y: int, z: int, mat:int) -> Base:
    westSide = Base()
    planeLower = Plane.from_list(
        [x - 0.5 + sideFenceLength / 2, y, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = RenderMaterial(diffuse=mat)

    westSide.lower = lower
    planeUpper = Plane.from_list(
        [x - 0.5 + sideFenceLength / 2, y, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = RenderMaterial(diffuse=mat)
    westSide.upper = upper
    return westSide

def CreateEastSide (x: int, y: int, z: int, mat:int) -> Base:
    eastSide = Base()
    planeLower = Plane.from_list(
        [x + 0.5 - sideFenceLength / 2, y, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = RenderMaterial(diffuse=mat)
    eastSide.lower = lower
    planeUpper = Plane.from_list(
        [x + 0.5 - sideFenceLength / 2, y, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=intervalSideFence, ySize=interval2Middle,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = RenderMaterial(diffuse=mat)
    eastSide.upper = upper
    return eastSide

def CreateNorthSide (x: int, y: int, z: int, mat:int) -> Base:
    northSide = Base()
    planeUpper = Plane.from_list(
        [x, y + 0.5 - sideFenceLength / 2, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = RenderMaterial(diffuse=mat)
    planeLower = Plane.from_list(
        [x, y + 0.5 - sideFenceLength / 2, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = RenderMaterial(diffuse=mat)
    northSide.lower = lower
    northSide.upper = upper
    return northSide

def CreateSouthSide (x: int, y: int, z: int, mat:int) -> Base:
    southSide = Base()
    planeUpper = Plane.from_list(
        [x, y - 0.5 + sideFenceLength / 2, z + upperSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    upper = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeUpper)
    upper.renderMaterial = RenderMaterial(diffuse=mat)
    planeLower = Plane.from_list(
        [x, y - 0.5 + sideFenceLength / 2, z + lowerSideFenceZdiff, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    lower = Box(xSize=interval2Middle, ySize=intervalSideFence,
                zSize=intervalLowerSideFenceHeight, basePlane=planeLower)
    lower.renderMaterial = RenderMaterial(diffuse=mat)
    southSide.lower = lower
    southSide.upper = upper
    return southSide

def CreateSideFences(x: int, y: int, z: int, mat: int, properties: dict) -> Base:
    ret = Base()
    if (properties["west"] == "true"):
        ret.westSide = CreateWestSide (x,y,z,mat)
    if (properties["east"] == "true"):
        ret.eastSide = CreateEastSide (x,y,z,mat)
    if (properties["north"] == "true"):
        ret.northSide = CreateNorthSide (x,y,z,mat)
    if (properties["south"] == "true"):
        ret.southSide = CreateSouthSide (x,y,z,mat)
    return ret


def CreateMainFence(x: int, y: int, z: int, mat: int) -> Box:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=interval4Middle, ySize=interval4Middle,
              zSize=intervalWhole, basePlane=plane)
    ret.renderMaterial = RenderMaterial(diffuse=mat)
    return ret


def CreateFence(x: int, y: int, z: int, block: Block) -> Base:
    ret = Fence()
    ret.mainFence = CreateMainFence(x, y, z, GetBlockColor(block.base_name))
    ret.sideFences = CreateSideFences(
        x, y, z, GetBlockColor(block.base_name), block.properties)
    return ret
