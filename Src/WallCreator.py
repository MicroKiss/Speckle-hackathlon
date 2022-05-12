from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, Point
from amulet import Block
from BlockColorDictionary import GetBlockColor
from utility import *

class Wall (
    Base
):
    mainWall: Box = None
    sideWalls: Base = None

def CreateSideWalls(x: int, y: int, z: int, mat: int, properties: dict) -> Base:
    ret = Base()
    if properties["up"] == "true":
        sideWallLength = 4*PIXEL
    else:
        sideWallLength = 5*PIXEL
    lengthInterval = GetIntervalFromSize(sideWallLength)
    height = 14*PIXEL
    heightInterval = GetIntervalFromSize(height)
    
    if (properties["west"] == "low"):
        westSide = Base()
        plane = Plane.from_list(
            [x - (8*PIXEL/sideWallLength) + sideWallLength, y, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=lengthInterval, ySize=interval6Middle,
                    zSize=heightInterval, basePlane=plane)
        side.renderMaterial = RenderMaterial(diffuse=mat)

        westSide.side = side
        ret.westSide = westSide

    if (properties["east"] == "low"):
        eastSide = Base()
        plane = Plane.from_list(
            [x + (8*PIXEL/sideWallLength) - sideWallLength, y, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=lengthInterval, ySize=interval6Middle,
                    zSize=heightInterval, basePlane=plane)
        side.renderMaterial = RenderMaterial(diffuse=mat)
        eastSide.side = side
        ret.eastSide = eastSide

    if (properties["north"] == "low"):
        southSide = Base()
        plane = Plane.from_list(
            [x, y + (8*PIXEL/sideWallLength) - sideWallLength, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=interval6Middle, ySize=lengthInterval,
                    zSize=heightInterval, basePlane=plane)
        side.renderMaterial = RenderMaterial(diffuse=mat)
        southSide.side = side
        ret.southSide = southSide

    if (properties["south"] == "low"):
        northSide = Base()
        plane = Plane.from_list(
            [x, y - (8*PIXEL/sideWallLength) + sideWallLength, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=interval6Middle, ySize=lengthInterval,
                    zSize=heightInterval, basePlane=plane)
        side.renderMaterial = RenderMaterial(diffuse=mat)
        northSide.side = side
        ret.northSide = northSide

    return ret


def CreateMainWall(x: int, y: int, z: int, mat: int, properties: dict) -> Box:
    if properties["up"] == "true":
        height = 1
        width = 8*PIXEL
    else:
        height = 14*PIXEL
        width = 6*PIXEL
    plane = Plane.from_list([x, y, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    widthInterval = GetIntervalFromSize(width)
    ret = Box(xSize=widthInterval, ySize=widthInterval,
              zSize=GetIntervalFromSize(height), basePlane=plane)
    ret.renderMaterial = RenderMaterial(diffuse=mat)
    return ret


def CreateWall(x: int, y: int, z: int, block: Block) -> Base:
    ret = Wall()
    ret.mainFence = CreateMainWall(x, y, z, GetBlockColor(block.base_name), block.properties)
    ret.sideWalls = CreateSideWalls(
        x, y, z, GetBlockColor(block.base_name), block.properties)
    return ret
