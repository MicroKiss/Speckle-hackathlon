import amulet
from amulet import Block
from BlockData import BlockData
import types
# load the level
level = amulet.load_level("D:\\Speckle-hackathlon\\testFiles\\New World")
#-1 -60 -1 től 1 -60 1 ig


exampleBlockDatas = []
for x in range(-10, 40):
    for y in range(-20, 20):
        for z in range (-61,-50):
            block:Block = level.get_block(x, z, y, "minecraft:overworld")
            blockData: BlockData = BlockData(x, y, z, block)
            exampleBlockDatas.append(blockData)
            if __name__ == "__main__":
                print (block.base_name)

