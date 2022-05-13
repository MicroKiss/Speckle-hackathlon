from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
from amulet import Block
from BlockColorDictionary import GetMaterial
from utility import *


class Wall (
    Base
):
    mainWall: Box = None
    sideWalls: Base = None


def CreateSideWalls(x: int, y: int, z: int, block: Block) -> Base:
    ret = Base()
    if block.properties["up"] == "true":
        sideWallLength = 4*PIXEL
    else:
        sideWallLength = 5*PIXEL
    lengthInterval = GetIntervalFromSize(sideWallLength)
    height = 14*PIXEL
    heightInterval = GetIntervalFromSize(height)

    if (block.properties["west"] == "low"):
        westSide = Base()
        plane = Plane.from_list(
            [x - 0.5 + sideWallLength / 2, y, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=lengthInterval, ySize=interval6Middle,
                   zSize=heightInterval, basePlane=plane)
        side.renderMaterial = GetMaterial(block)

        westSide.side = side
        ret.westSide = westSide

    if (block.properties["east"] == "low"):
        eastSide = Base()
        plane = Plane.from_list(
            [x + 0.5 - sideWallLength / 2, y, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=lengthInterval, ySize=interval6Middle,
                   zSize=heightInterval, basePlane=plane)
        side.renderMaterial = GetMaterial(block)
        eastSide.side = side
        ret.eastSide = eastSide

    if (block.properties["north"] == "low"):
        southSide = Base()
        plane = Plane.from_list(
            [x, y + 0.5 - sideWallLength / 2, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=interval6Middle, ySize=lengthInterval,
                   zSize=heightInterval, basePlane=plane)
        side.renderMaterial = GetMaterial(block)
        southSide.side = side
        ret.southSide = southSide

    if (block.properties["south"] == "low"):
        northSide = Base()
        plane = Plane.from_list(
            [x, y - 0.5 + sideWallLength / 2, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=interval6Middle, ySize=lengthInterval,
                   zSize=heightInterval, basePlane=plane)
        side.renderMaterial = GetMaterial(block)
        northSide.side = side
        ret.northSide = northSide

    return ret


def CreateMainWall(x: int, y: int, z: int, block: Block) -> Base:
    if block.properties["up"] == "true":
        height = 1
        width = 8*PIXEL
    else:
        height = 14*PIXEL
        width = 6*PIXEL
    plane = Plane.from_list([x, y, z - 1 + height, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    widthInterval = GetIntervalFromSize(width)
    ret = Box(xSize=widthInterval, ySize=widthInterval,
              zSize=GetIntervalFromSize(height), basePlane=plane)
    ret.renderMaterial = GetMaterial(block)
    return ret


def CreateWall(x: int, y: int, z: int, block: Block) -> Base:
    ret = Wall()
    ret.mainFence = CreateMainWall(x, y, z, block)
    ret.sideWalls = CreateSideWalls(
        x, y, z, block)
    return ret
