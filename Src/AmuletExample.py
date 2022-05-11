import amulet
from amulet import Block
from BlockData import BlockData
import types
# load the level
level = amulet.load_level("D:\\Speckle-hackathlon\\testFiles\\New World")
#-1 -60 -1 től 1 -60 1 ig


exampleBlockDatas = []
for i in range(-6, 9):
    for j in range(1, 4):
        block:Block = level.get_block(i, -60, j, "minecraft:overworld")
        blockData: BlockData = BlockData(i, j, -60, block)
        exampleBlockDatas.append(blockData)
        if __name__ == "__main__":
            print (block.base_name)

