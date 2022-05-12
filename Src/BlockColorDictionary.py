from collections import namedtuple
Color = namedtuple('RGB','red, green, blue')

class rgb(Color):
    def hex(self) -> int:
        return int ('{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue),16)

colors:dict= {}

def GetBlockColor (blockName: str)-> int :
    if (blockName in colors.keys()):
        return colors[blockName].hex ()
    else:
        return  rgb(165,0,255).hex () # purple


colors['snow_block']        = rgb (240,240,240)
colors['gold_block']        = rgb (243,225,76)
colors['diamond_block']     = rgb (52,235,201)
colors['iron_block']        = rgb (225,225,225)
colors['cobblestone']       = rgb (108,108,108)
colors['planks']            = rgb (168,139,87)
colors['red_sand']          = rgb (197,73,14)
colors['stone']             = rgb (134,134,134)

