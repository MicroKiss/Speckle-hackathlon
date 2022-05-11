
from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane
import SpeckleConnection
from color_constants import colors
from AmuletExample import exampleBlockDatas
import BlockData


def CreateBlock (x:int, y:int, z:int, mat:int = colors["purple"].hex ()) -> Box:
    plane = Plane.from_list([x,y,z,0,0,1,1,0,0,0,1,0])
    interval = Interval (start= 0, end= 1)
    ret = Box(xSize = interval, ySize = interval, zSize = interval, basePlane = plane)
    ret.renderMaterial = RenderMaterial (diffuse=mat)
    return ret

"""

gold_block
iron_block
cobblestone
"""

def ParseBlockDatas (blockDatas: list)-> list:
    parsedBlockDatas = []
    for blockData in blockDatas:
        if blockData.block.base_name == "air":
            continue
        elif blockData.block.base_name == "diamond_block":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["aqua"].hex ())
        elif blockData.block.base_name == "stone":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["darkgray"].hex ())
        elif blockData.block.base_name == "red_sand":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["darkorange2"].hex ())
        elif blockData.block.base_name == "planks":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["goldenrod1"].hex ())
        elif blockData.block.base_name == "snow_block":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["white"].hex ())
        elif blockData.block.base_name == "gold_block":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["floralwhite"].hex ())
        elif blockData.block.base_name == "iron_block":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["gray89"].hex ())
        elif blockData.block.base_name == "cobblestone":
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, colors["gray40"].hex ())
        else:
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z) 
        parsedBlockDatas.append (parsedBlockData)
    return parsedBlockDatas

obj = Base()
obj.add_chunkable_attrs (entities = 5000)
obj.entities = ParseBlockDatas (exampleBlockDatas)

SpeckleConnection.Send (obj)

