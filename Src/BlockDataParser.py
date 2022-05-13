
from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
from amulet import Block
from FenceCreator import CreateFence
from SlabCreator import CreateSlab
from BlockCreator import CreateBlock
from StairsCreator import CreateStairs
from DoorCreator import CreateDoor
from WallCreator import CreateWall
from GateCreator import CreateGate
from GlassCreator import CreateGlass
from utility import *

skippedElements = ["air", "chain"]

def ParseBlockDatas (blockDatas: list)-> list:
    parsedBlockDatas = []
    for blockData in blockDatas:
        name: str =  blockData.block.base_name
        if name in skippedElements:
            continue
        elif "fence" == name:
            parsedBlockData = CreateFence (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "fence_gate" == name:
            parsedBlockData = CreateGate (blockData.x, blockData.y, blockData.z, blockData.block)
        #elif "glass_pane" == name:
        #    parsedBlockData = CreateGlass (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "slab" == name:
            parsedBlockData = CreateSlab (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "stairs" == name:
            parsedBlockData = CreateStairs (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "door" == name:
            parsedBlockData = CreateDoor (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "wall" == name:
            parsedBlockData = CreateWall (blockData.x, blockData.y, blockData.z, blockData.block)
        else:
            parsedBlockData = CreateBlock (blockData.x, blockData.y, blockData.z, blockData.block)
        
        parsedBlockDatas.append (parsedBlockData)
    return parsedBlockDatas

from AmuletExample import exampleBlockDatas
import SpeckleConnection as SC
if __name__ == "__main__":
    obj = Base()
    obj.add_chunkable_attrs (entities = 5000)
    obj.entities = ParseBlockDatas (exampleBlockDatas)
    SC.Send (obj)