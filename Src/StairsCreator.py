from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, Point
from AmuletExample import Block
from BlockColorDictionary import GetBlockColor
from utility import *
from SlabCreator import CreateLowerSlab

class Stairs (
    Base,
):
    base: Box = None
    step: Box = None


def GetInnerStairs(x: int, y: int, z: int, block: Block) -> Base:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    plane1 = Plane.from_list(
        [x - 0.5 + stairsStepWidth / 2, y - 0.5 + stairsStepWidth / 2, z + 0.25, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    step1 = Box(xSize=intervalHalf, ySize=intervalHalf,
                zSize=intervalHalf, basePlane=plane1)
    steps.append(step1)
    plane2 = Plane.from_list(
        [x + 0.5 - stairsStepWidth / 2, y - 0.5 + stairsStepWidth / 2, z + 0.25, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    step2 = Box(xSize=intervalHalf, ySize=intervalHalf,
                zSize=intervalHalf, basePlane=plane2)
    steps.append(step2)

    plane3 = Plane.from_list(
        [x - 0.5 + stairsStepWidth / 2, y + 0.5 - stairsStepWidth / 2, z + 0.25, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    step3 = Box(xSize=intervalHalf, ySize=intervalHalf,
                zSize=intervalHalf, basePlane=plane3)
    steps.append(step3)

    ret = Base()
    ret.base = base
    ret.steps = steps
    return ret


def CreateStairsStep (x: int, y: int, z: int,block: Block) ->Base:
    if (block.properties["facing"] == "west"):
        plane = Plane.from_list(
            [x - 0.5 + stairsStepWidth / 2, y, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalHalf, ySize=intervalWhole,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step
    elif (block.properties["facing"] == "east"):
        plane = Plane.from_list(
            [x + 0.5 - stairsStepWidth / 2, y, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalHalf, ySize=intervalWhole,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step
    elif (block.properties["facing"] == "north"):
        plane = Plane.from_list(
            [x, y - 0.5 + stairsStepWidth / 2, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalWhole, ySize=intervalHalf,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step
    elif (block.properties["facing"] == "south"):
        plane = Plane.from_list(
            [x, y + 0.5 - stairsStepWidth / 2, z + 0.25 , 0, 0, 1, 1, 0, 0, 0, 1, 0])
        step = Box(xSize=intervalWhole, ySize=intervalHalf,
                    zSize=intervalHalf, basePlane=plane)
        step.renderMaterial = RenderMaterial(diffuse=GetBlockColor(block.base_name))
        return step


def SwapStairsElements(stairs: Stairs):
    stairs.base.basePlane.origin.z, stairs.step.basePlane.origin.z = stairs.step.basePlane.origin.z, stairs.base.basePlane.origin.z


def CreateStairs(x: int, y: int, z: int, block: Block) -> Base:
    ret = Stairs ()
    ret.base = CreateLowerSlab (x, y, z, GetBlockColor (block.base_name))
    ret.step = CreateStairsStep (x, y, z, block)
    if (block.properties["half"] == "top"):
        SwapStairsElements (ret)
    return ret