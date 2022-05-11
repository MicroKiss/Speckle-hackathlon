
from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, GEOMETRY
import SpeckleConnection as SC
from color_constants import colors
from BlockData import BlockData, GetDummyBlockDatas
import random


def GetColorFromBlockID (id:int) -> int:
    return random.choice (list (colors.values ())).hex ()

def CreateBlock (x:int, y:int, z:int, mat:int = colors["midnightblue"].hex ()):
    plane = Plane.from_list([x,y,z,0,0,1,1,0,0,0,1,0])
    interval = Interval (start= 0, end= 1)
    ret = Box(xSize = interval, ySize = interval, zSize = interval, basePlane = plane)
    ret.renderMaterial = RenderMaterial (diffuse=mat)
    return ret

def CreateBlockFromBlockData (blockData: BlockData):
    return CreateBlock (blockData.x, blockData.y, blockData.z, GetColorFromBlockID (blockData.id))


def ParseBlockDatas (blockDatas: BlockData)-> list:
    parsedDatas = []
    for blockData in blockDatas:
        parsedDatas.append (CreateBlockFromBlockData (blockData))
    return parsedDatas

obj = Base()
obj.add_chunkable_attrs (entities = 5000)
obj.entities = ParseBlockDatas (GetDummyBlockDatas ())

SC.Send (obj)

