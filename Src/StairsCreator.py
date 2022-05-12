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
    steps = None



def CreateHalfBlock (x,y,z)->Box :
    plane = Plane.from_list(
    [x,y,z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    return  Box(xSize=intervalHalf, ySize=intervalHalf,
            zSize=intervalHalf, basePlane=plane)



def NorthWestCoords (x,y,z):
    return (x - 0.5 + stairsStepWidth / 2, y - 0.5 + stairsStepWidth / 2, z + 0.25)
def NorthEastCoords (x,y,z):
    return (x + 0.5 - stairsStepWidth / 2, y - 0.5 + stairsStepWidth / 2, z + 0.25)
def SouthWestCoords (x,y,z):
    return (x - 0.5 + stairsStepWidth / 2, y + 0.5 - stairsStepWidth / 2, z + 0.25)
def SouthEastCoords (x,y,z):
    return (x + 0.5 - stairsStepWidth / 2, y + 0.5 - stairsStepWidth / 2, z + 0.25)


def GetStraightStairs (x: int, y: int, z: int, block: Block) -> Stairs:
    ret = Stairs ()
    ret.base = CreateLowerSlab (x, y, z, GetBlockColor (block.base_name))
    steps = list ()
    steps.append(CreateStairsStep (x, y, z, block))
    ret.steps = steps
    return ret

#NorthWest
def GetInnerStairs1(x: int, y: int, z: int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*NorthWestCoords(x,y,z))
    steps.append(step1)
    step2 = CreateHalfBlock(*NorthEastCoords(x,y,z))
    steps.append(step2)
    step3 = CreateHalfBlock(*SouthWestCoords(x,y,z))
    steps.append(step3)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#NorthEast
def GetInnerStairs2(x: int, y: int, z: int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*NorthWestCoords(x,y,z))
    steps.append(step1)
    step2 = CreateHalfBlock(*NorthEastCoords(x,y,z))
    steps.append(step2)
    step3 = CreateHalfBlock(*SouthEastCoords(x,y,z))
    steps.append(step3)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#SouthWest
def GetInnerStairs3(x: int, y: int, z: int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*NorthWestCoords(x,y,z))
    steps.append(step1)
    step2 = CreateHalfBlock(*SouthEastCoords(x,y,z))
    steps.append(step2)
    step3 = CreateHalfBlock(*SouthWestCoords(x,y,z))
    steps.append(step3)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#SouthEast
def GetInnerStairs4(x: int, y: int, z: int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*NorthEastCoords(x,y,z))
    steps.append(step1)
    step2 = CreateHalfBlock(*SouthEastCoords(x,y,z))
    steps.append(step2)
    step3 = CreateHalfBlock(*SouthWestCoords(x,y,z))
    steps.append(step3)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#SouthEast
def GetOuterStairs1(x: int, y: int, z:int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*SouthEastCoords(x,y,z))
    steps.append(step1)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#SouthWest
def GetOuterStairs2(x: int, y: int, z:int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*SouthWestCoords(x,y,z))
    steps.append(step1)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#NorthWest
def GetOuterStairs3(x: int, y: int, z:int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*NorthWestCoords(x,y,z))
    steps.append(step1)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret
#NorthEast
def GetOuterStairs4(x: int, y: int, z:int, block: Block) -> Stairs:
    base = CreateLowerSlab(x, y, z, GetBlockColor(block.base_name))
    steps = []
    step1 = CreateHalfBlock(*NorthEastCoords(x,y,z))
    steps.append(step1)
    ret = Stairs()
    ret.base = base
    ret.steps = steps
    return ret

def CreateStairsStep (x: int, y: int, z: int,block: Block) ->Stairs:
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
    originBaseZ = stairs.base.basePlane.origin.z
    originStepZ = stairs.steps[0].basePlane.origin.z

    stairs.base.basePlane.origin.z = originStepZ
    for i in stairs.steps:
        i.basePlane.origin.z = originBaseZ


def CreateStairs(x: int, y: int, z: int, block: Block) -> Stairs:

    if (block.properties["shape"] == "inner_right" and  block.properties["facing"] == "west"
    or block.properties["shape"] == "inner_left" and block.properties["facing"] == "north"):
        ret = GetInnerStairs1 (x,y,z,block)
    elif (block.properties["shape"] == "inner_right" and  block.properties["facing"] == "north"
    or block.properties["shape"] == "inner_left" and block.properties["facing"] == "east"):
        ret = GetInnerStairs2 (x,y,z,block)
    elif (block.properties["shape"] == "inner_right" and  block.properties["facing"] == "south"
    or block.properties["shape"] == "inner_left" and block.properties["facing"] == "west"):
        ret = GetInnerStairs3 (x,y,z,block)
    elif (block.properties["shape"] == "inner_right" and  block.properties["facing"] == "east"
    or block.properties["shape"] == "inner_left" and block.properties["facing"] == "south"):
        ret = GetInnerStairs4 (x,y,z,block)
    elif (block.properties["shape"] == "outer_right" and  block.properties["facing"] == "east"
    or block.properties["shape"] == "outer_left" and block.properties["facing"] == "south"):
        ret = GetOuterStairs1 (x,y,z,block)
    elif (block.properties["shape"] == "outer_right" and  block.properties["facing"] == "south"
    or block.properties["shape"] == "outer_left" and block.properties["facing"] == "west"):
        ret = GetOuterStairs2 (x,y,z,block)
    elif (block.properties["shape"] == "outer_right" and  block.properties["facing"] == "west"
    or block.properties["shape"] == "outer_left" and block.properties["facing"] == "north"):
        ret = GetOuterStairs3 (x,y,z,block)
    elif (block.properties["shape"] == "outer_right" and  block.properties["facing"] == "north"
    or block.properties["shape"] == "outer_left" and block.properties["facing"] == "east"):
        ret = GetOuterStairs4 (x,y,z,block)
    else: 
        ret = GetStraightStairs (x,y,z,block)

    mat = GetBlockColor(block.base_name)
    ret.base.renderMaterial = RenderMaterial(diffuse=mat)
    ret.base["info"] = block.properties["facing" ] + block.properties["shape"]
    for s in ret.steps:
        s.renderMaterial = RenderMaterial(diffuse=mat)

    if (block.properties["half"] == "top"):
        SwapStairsElements (ret)
    return ret