import amulet

# load the level
level = amulet.load_level("C:\\Users\\Peti\\AppData\\Roaming\\.minecraft\\saves\\1_18_2")

block = level.get_block(0, -60, 0, "minecraft:overworld")
print(block.base_name)