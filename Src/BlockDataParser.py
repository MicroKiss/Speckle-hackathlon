
from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
import SpeckleConnection
from BlockColorDictionary import GetBlockColor
from AmuletExample import exampleBlockDatas, Block
from FenceCreator import CreateFence
from SlabCreator import CreateSlab
from BlockCreator import CreateBlock
from StairsCreator import CreateStairs, GetInnerStairs
from utility import *



def ParseBlockDatas (blockDatas: list)-> list:
    parsedBlockDatas = []
    for blockData in blockDatas:
        name: str =  blockData.block.base_name
        if name == "air":
            continue
        elif "fence" in name:
            parsedBlockData = CreateFence (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "slab" in name:
            parsedBlockData = CreateSlab (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "stairs" in name:
            parsedBlockData = CreateStairs (blockData.x, blockData.y, blockData.z, blockData.block)
        else:
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, GetBlockColor (name))
        parsedBlockData.minecraftName = blockData.block.base_name
        parsedBlockDatas.append (parsedBlockData)
    return parsedBlockDatas

if (__name__ == "__main__"):
    entities = []
    entities = ParseBlockDatas (exampleBlockDatas)
    entities.append (GetInnerStairsLeft (3,3,-55,Block(namespace = "dummy", base_name="dummyname")))
    entities.append (GetInnerStairsRight (3,4,-55,Block(namespace = "dummy", base_name="dummyname")))

    obj = Base()
    obj.add_chunkable_attrs (entities = 5000)
    obj.entities = entities
    SpeckleConnection.Send (obj)

