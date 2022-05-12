from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, Point
from AmuletExample import Block
from BlockColorDictionary import GetBlockColor
from utility import *
from SlabCreator import CreateLowerSlab
"""
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
"""


class Stairs (
    Base,
    speckle_type="Stairs"
):
    base: Box = None
    step: Box = None

def CreateStairsStep (x: int, y: int, z: int,block: Block) ->Box:
    if (block.properties["facing"] == "west"):
        plane = Plane.from_list(
            [x - 0.5 + stairsStepWidth / 2, y, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalHalf, ySize=intervalWhole,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step
        
    if (block.properties["facing"] == "east"):
        plane = Plane.from_list(
            [x + 0.5 - stairsStepWidth / 2, y, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalHalf, ySize=intervalWhole,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step
        
    if (block.properties["facing"] == "north"):
        plane = Plane.from_list(
            [x, y - 0.5 + stairsStepWidth / 2, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalWhole, ySize=intervalHalf,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step

    if (block.properties["facing"] == "south"):
        plane = Plane.from_list(
            [x, y + 0.5 - stairsStepWidth / 2, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalWhole, ySize=intervalHalf,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step
        


def SwapStairsElements(stairs: Stairs) ->Base:
    pass



def CreateStairs(x: int, y: int, z: int, block: Block) -> Base:
    ret = Stairs ()
    ret.base = CreateLowerSlab (x, y, z, GetBlockColor (block.base_name))
    ret.step = CreateStairsStep (x, y, z, block)
    if (block.properties["half"] == "top"):
        SwapStairsElements (ret)
    return ret