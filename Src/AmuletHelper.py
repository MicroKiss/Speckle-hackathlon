import amulet
from amulet import Block
from amulet.api.level import World
from BlockData import BlockData
import math


def GetBlockAroundPlayer (r : int, worldPath : str) -> 'list[BlockData.BlockData]':
    level = amulet.load_level (worldPath)
    (playerX, playerY, playerZ) = level.get_player ('~local_player').location
    playerX = math.floor (playerX)
    playerY = math.floor (playerY)
    playerZ = math.floor (playerZ)
    return __GetBlocksFromBBox (playerX - r, playerY - r, playerZ - r, playerX + r + 1, playerY + r + 1, playerZ + r + 1, level)


def GetBlockFromBBox (minX : int, minY : int, minZ : int, maxX : int, maxY : int, maxZ : int, worldPath : str) -> 'list[BlockData]':
    level = amulet.load_level (worldPath)
    return __GetBlocksFromBBox (minX, minY, minZ, maxX, maxY, maxZ, level)


FILTERED_BLOCKS : 'list[str]' = ["air"]


def __GetBlocksFromBBox (minX : int, minY : int, minZ : int, maxX : int, maxY : int, maxZ : int, level : World) -> 'list[BlockData]':
    result : list[BlockData] = []
    for x in range (minX, maxX):
        for y in range (minY, maxY):
            for z in range (minZ, maxZ):
                block : Block = level.get_block (x, y, z, "minecraft:overworld")
                if not block.base_name in FILTERED_BLOCKS:
                    result.append (BlockData (x, z, y, block))
    return result
