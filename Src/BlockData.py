from amulet import Block

class BlockData:
  def __init__(self, x:int, y:int, z:int, block: Block):
    self.x = x
    self.y = y
    self.z = z
    self.block = block