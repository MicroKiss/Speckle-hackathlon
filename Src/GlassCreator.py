from specklepy.objects import Base
from specklepy.objects.geometry import  Box, Plane
from amulet import Block
from BlockColorDictionary import GetMaterial
from utility import *


class Glass (
    Base
):
    mainGlass: Box = None
    sideGlasses: Base = None


def CreateSideGlass(x: int, y: int, z: int, block: Block) -> Base:
    ret = Base()
    sideWallLength = 7*PIXEL
    sideWallWidth = 2*PIXEL
    sideWallLengthInterval = Interval(start=0, end=sideWallLength)
    sideWallWidthInterval = Interval(start=0, end=sideWallWidth)

    if (block.properties["west"] == "true"):
        westSide = Base()
        plane = Plane.from_list(
            [x - 0.5 + sideWallLength / 2, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=sideWallLengthInterval, ySize=sideWallWidthInterval,
                   zSize=intervalWhole, basePlane=plane)
        side.renderMaterial = GetMaterial(block)

        westSide.side = side
        ret.westSide = westSide

    if (block.properties["east"] == "true"):
        eastSide = Base()
        plane = Plane.from_list(
            [x + 0.5 - sideWallLength / 2, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=sideWallLengthInterval, ySize=sideWallWidthInterval,
                   zSize=intervalWhole, basePlane=plane)
        side.renderMaterial = GetMaterial(block)
        eastSide.side = side
        ret.eastSide = eastSide

    if (block.properties["north"] == "true"):
        southSide = Base()
        plane = Plane.from_list(
            [x, y + 0.5 - sideWallLength / 2, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=sideWallWidthInterval, ySize=sideWallLengthInterval,
                   zSize=intervalWhole, basePlane=plane)
        side.renderMaterial = GetMaterial(block)
        southSide.side = side
        ret.southSide = southSide

    if (block.properties["south"] == "true"):
        northSide = Base()
        plane = Plane.from_list(
            [x, y - 0.5 + sideWallLength / 2, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
        side = Box(xSize=sideWallWidthInterval, ySize=sideWallLengthInterval,
                   zSize=intervalWhole, basePlane=plane)
        side.renderMaterial = GetMaterial(block)
        northSide.side = side
        ret.northSide = northSide

    return ret


def CreateMainGlass(x: int, y: int, z: int, block: Block) -> Base:
    plane = Plane.from_list([x, y, z, 0, 0, 1, 1, 0, 0, 0, 1, 0])
    widthInterval = GetIntervalFromSize(2*PIXEL)
    ret = Box(xSize=widthInterval, ySize=widthInterval,
              zSize=intervalWhole, basePlane=plane)
    ret.renderMaterial = GetMaterial(block)
    return ret


def CreateGlass(x: int, y: int, z: int, block: Block) -> Base:
    if (block.base_name == "stained_glass"):
        pass

    ret = Glass()
    ret.mainGlass = CreateMainGlass(x, y, z, block)
    ret.mainGlass.name = block.base_name
    ret.sideWalls = CreateSideGlass(
        x, y, z, block)
    return ret