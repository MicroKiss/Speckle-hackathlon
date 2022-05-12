from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, Point
from AmuletExample import Block
from BlockColorDictionary import GetBlockColor
from utility import *

upperSideFenceZdiff = -PIXEL + 0.5 - sideFenceHeight / 2
lowerSideFenceZdiff = - 3/2*PIXEL + sideFenceHeight / 2


def CreateSideFences(x: int, y: int, z: int, mat: int, properties: dict) -> Base:
    ret = Base()
    if (properties["west"] == "true"):
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
        ret.westSide = westSide

    if (properties["east"] == "true"):
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
        ret.eastSide = eastSide

    if (properties["south"] == "true"):
        southSide = Base()
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
        southSide.lower = lower
        southSide.upper = upper
        ret.southSide = southSide

    if (properties["north"] == "true"):
        northSide = Base()
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
        northSide.lower = lower
        northSide.upper = upper
        ret.northSide = northSide

    return ret


def CreateMainFence(x: int, y: int, z: int, mat: int) -> Box:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    ret = Box(xSize=interval4Middle, ySize=interval4Middle,
              zSize=intervalWhole, basePlane=plane)
    ret.renderMaterial = RenderMaterial(diffuse=mat)
    return ret


class Fence (
    Base,
    speckle_type="Fence"
):
    mainFence: Box = None
    sideFences: Base = None


def CreateFence(x: int, y: int, z: int, block: Block) -> Base:
    ret = Fence()
    ret.mainFence = CreateMainFence(x, y, z, GetBlockColor(block.base_name))
    ret.sideFences = CreateSideFences(
        x, y, z, GetBlockColor(block.base_name), block.properties)
    return ret
