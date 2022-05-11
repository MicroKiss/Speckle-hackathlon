from amulet import Block

class BlockData:
  def __init__(self, x:int, y:int, z:int, block: Block):
    self.x = x
    self.y = y
    self.z = z
    self.block = block

"""
def GetDummyBlockDatas () ->list :
  blocks = []
  blocks.append(BlockData(0,-3,-2,1))
  blocks.append(BlockData(1,0,2,2))
  blocks.append(BlockData(2,0,0,3))
  blocks.append(BlockData(3,0,0,4))
  blocks.append(BlockData(4,0,0,5))
  blocks.append(BlockData(5,2,0,6))
  blocks.append(BlockData(4,2,4,7))
  blocks.append(BlockData(3,1,1,8))
  return blocks
"""