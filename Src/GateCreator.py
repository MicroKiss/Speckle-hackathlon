from specklepy.objects import Base
from specklepy.objects.geometry import Box, Plane
from amulet import Block
from BlockColorDictionary import GetMaterial
from utility import *


class Gate (
    Base
):
    pieces = None

#North South


def CreateClosedPieces1(x: int, y: int, z: int, block: Block) -> 'list[Box]':
    pieces = []
    left = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
               zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x - 0.5 + PIXEL, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x + 0.5 - PIXEL, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    top = Box(xSize=Interval(start=0, end=12*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
              zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x, y, z + 0.5 - 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottom = Box(xSize=Interval(start=0, end=12*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                 zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x, y, z + 0.5 - 8.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middle = Box(xSize=Interval(start=0, end=4*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                 zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append(left)
    pieces.append(right)
    pieces.append(top)
    pieces.append(bottom)
    pieces.append(middle)
    return pieces
#east west


def CreateClosedPieces2(x: int, y: int, z: int, block: Block) -> 'list[Box]':
    pieces = []
    left = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
               zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x, y - 0.5 + PIXEL, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
                zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x, y + 0.5 - PIXEL, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    top = Box(ySize=Interval(start=0, end=12*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
              zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x, y, z + 0.5 - 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottom = Box(ySize=Interval(start=0, end=12*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
                 zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x, y, z + 0.5 - 8.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middle = Box(ySize=Interval(start=0, end=4*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
                 zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append(left)
    pieces.append(right)
    pieces.append(top)
    pieces.append(bottom)
    pieces.append(middle)
    return pieces


def CreateOpenPieces1(x: int, y: int, z: int, block: Block) -> 'list[Box]':
    pieces = []
    left = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
               zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x - 0.5 + PIXEL, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x + 0.5 - PIXEL, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                  zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x-0.5 + PIXEL, y + 4*PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x-0.5 + PIXEL, y + 4*PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x-0.5 + PIXEL, y + 6*PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                   zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x+0.5 - PIXEL, y + 4*PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x+0.5 - PIXEL, y + 4*PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x+0.5 - PIXEL, y + 6*PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append(left)
    pieces.append(right)
    pieces.append(topLeft)
    pieces.append(bottomLeft)
    pieces.append(middleLeft)
    pieces.append(topRight)
    pieces.append(bottomRight)
    pieces.append(middleRight)
    return pieces


def CreateOpenPieces2(x: int, y: int, z: int, block: Block) -> 'list[Box]':
    pieces = []
    left = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
               zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x - 0.5 + PIXEL, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x + 0.5 - PIXEL, y, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                  zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x-0.5 + PIXEL, y - 4*PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x-0.5 + PIXEL, y - 4*PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x-0.5 + PIXEL, y - 6*PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                   zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x+0.5 - PIXEL, y - 4*PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=6*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x+0.5 - PIXEL, y - 4*PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x+0.5 - PIXEL, y - 6*PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append(left)
    pieces.append(right)
    pieces.append(topLeft)
    pieces.append(bottomLeft)
    pieces.append(middleLeft)
    pieces.append(topRight)
    pieces.append(bottomRight)
    pieces.append(middleRight)
    return pieces


def CreateOpenPieces3(x: int, y: int, z: int, block: Block) -> 'list[Box]':
    pieces = []
    left = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
               zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x, y - 0.5 + PIXEL, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
                zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x, y + 0.5 - PIXEL, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topLeft = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                  zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x - 4*PIXEL, y-0.5 + PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomLeft = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x - 4*PIXEL, y-0.5 + PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x - 6*PIXEL, y - 0.5 + PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topRight = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                   zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x - 4*PIXEL, y+0.5 - PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomRight = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x - 4*PIXEL, y + 0.5 - PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x - 6*PIXEL, y+0.5 - PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append(left)
    pieces.append(right)
    pieces.append(topLeft)
    pieces.append(bottomLeft)
    pieces.append(middleLeft)
    pieces.append(topRight)
    pieces.append(bottomRight)
    pieces.append(middleRight)
    return pieces


def CreateOpenPieces4(x: int, y: int, z: int, block: Block) -> 'list[Box]':
    pieces = []
    left = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
               zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x, y - 0.5 + PIXEL, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    right = Box(ySize=Interval(start=0, end=2*PIXEL), xSize=Interval(start=0, end=2*PIXEL),
                zSize=Interval(start=0, end=11*PIXEL), basePlane=Plane.from_list([x, y + 0.5 - PIXEL, z + 2.5*PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topLeft = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                  zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x + 4*PIXEL, y-0.5 + PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomLeft = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x + 4*PIXEL, y-0.5 + PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleLeft = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                     zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x + 6*PIXEL, y - 0.5 + PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    topRight = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                   zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x + 4*PIXEL, y+0.5 - PIXEL, z + 0.5 - 2.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    bottomRight = Box(xSize=Interval(start=0, end=6*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x + 4*PIXEL, y + 0.5 - PIXEL, z + 0.5 - 8.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    middleRight = Box(xSize=Interval(start=0, end=2*PIXEL), ySize=Interval(start=0, end=2*PIXEL),
                      zSize=Interval(start=0, end=3*PIXEL), basePlane=Plane.from_list([x + 6*PIXEL, y+0.5 - PIXEL, z + 0.5 - 5.5 * PIXEL, 0, 0, 1, 1, 0, 0, 0, 1, 0]))
    pieces.append(left)
    pieces.append(right)
    pieces.append(topLeft)
    pieces.append(bottomLeft)
    pieces.append(middleLeft)
    pieces.append(topRight)
    pieces.append(bottomRight)
    pieces.append(middleRight)
    return pieces


def CreateGate(x: int, y: int, z: int, block: Block) -> Base:
    ret = Gate()
    if (block.properties["open"] == "false"):
        if (block.properties["facing"] == "north" or block.properties["facing"] == "south"):
            ret.pieces = CreateClosedPieces1(x, y, z, block)
        elif (block.properties["facing"] == "east" or block.properties["facing"] == "west"):
            ret.pieces = CreateClosedPieces2(x, y, z, block)
    elif (block.properties["open"] == "true"):
        if (block.properties["facing"] == "north"):
            ret.pieces = CreateOpenPieces1(x, y, z, block)
        elif (block.properties["facing"] == "south"):
            ret.pieces = CreateOpenPieces2(x, y, z, block)
        elif (block.properties["facing"] == "west"):
            ret.pieces = CreateOpenPieces3(x, y, z, block)
        elif (block.properties["facing"] == "east"):
            ret.pieces = CreateOpenPieces4(x, y, z, block)

    for p in ret.pieces:
        p.renderMaterial = GetMaterial(block)
    return ret
