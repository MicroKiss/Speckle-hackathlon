
from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
import SpeckleConnection
from BlockColorDictionary import GetBlockColor
from AmuletExample import exampleBlockDatas
from FenceCreator import CreateFence
from SlabCreator import CreateSlab
from BlockCreator import CreateBlock
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
        else:
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, GetBlockColor (name))
        parsedBlockData.minecraftName = blockData.block.base_name
        parsedBlockDatas.append (parsedBlockData)
    return parsedBlockDatas

obj = Base()
obj.add_chunkable_attrs (entities = 5000)
entities = []
entities = ParseBlockDatas (exampleBlockDatas)

obj.entities = entities

SpeckleConnection.Send (obj)

