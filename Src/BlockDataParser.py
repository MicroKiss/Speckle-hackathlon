
from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
import SpeckleConnection
from BlockColorDictionary import GetBlockColor
from amulet import Block
from FenceCreator import CreateFence
from SlabCreator import CreateSlab
from BlockCreator import CreateBlock
from StairsCreator import CreateStairs
from WallCreator import CreateWall
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
        elif "wall" in name:
            parsedBlockData = CreateWall (blockData.x, blockData.y, blockData.z, blockData.block)
        else:
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, GetBlockColor (name))
        parsedBlockData.minecraftName = blockData.block.base_name
        parsedBlockDatas.append (parsedBlockData)
    return parsedBlockDatas
