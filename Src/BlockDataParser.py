
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
from pathlib import Path
import os

skippedElements = ["air", "chain","flower_pot","head","carpet","scaffolding","lantern","barrel","chest","bookshelf","wall_head","cobweb","fletching_table"]

def ParseBlockDatas (blockDatas: list)-> list:
    parsedBlockDatas = []
    for blockData in blockDatas:
        parsedBlockData = None
        name: str =  blockData.block.base_name
        if name in skippedElements:
            continue
        elif "fence" == name:
            parsedBlockData = CreateFence (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "fence_gate" == name:
            parsedBlockData = CreateGate (blockData.x, blockData.y, blockData.z, blockData.block)
        elif "glass_pane" in name or "iron_bars" == name:
            parsedBlockData = CreateGlass (blockData.x, blockData.y, blockData.z, blockData.block)
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
        parsedBlockData.minecraftName = name
        if (parsedBlockData!= None):
            parsedBlockDatas.append (parsedBlockData)
    return parsedBlockDatas

from AmuletHelper import GetBlockAroundPlayer
import SpeckleConnection as SC
if __name__ == "__main__":
    obj = Base()
    obj.add_chunkable_attrs (entities = 100)
    obj.entities = ParseBlockDatas (GetBlockAroundPlayer (50,Path(os.getenv('APPDATA'), '.minecraft', 'saves','Neo-GothicPalace_by_NevasBuildings')))
    print (len (obj.entities))
    SC.Send (obj)