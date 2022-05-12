from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
from utility import *
from AmuletExample import Block
from BlockColorDictionary import GetBlockColor
from BlockCreator import CreateBlock
def CreateSlab (x: int, y: int, z: int, block: Block) -> Box:
    ret : Box = None
    mat = GetBlockColor(block.base_name)
    if (block.properties["type"] == "double"):
        ret = CreateBlock (x,y,z,mat)
    elif (block.properties["type"] == "top"):
        plane = Plane.from_list([x,y,z+0.25,0,0,1,1,0,0,0,1,0])
        ret = Box(xSize = intervalWhole, ySize = intervalWhole, zSize = intervalHalf, basePlane = plane)
        ret.renderMaterial = RenderMaterial (diffuse=mat)
    elif (block.properties["type"] == "bottom"):
        plane = Plane.from_list([x,y,z-0.25,0,0,1,1,0,0,0,1,0])
        ret = Box(xSize = intervalWhole, ySize = intervalWhole, zSize = intervalHalf, basePlane = plane)
        ret.renderMaterial = RenderMaterial (diffuse=mat)
    return ret