from collections import namedtuple
Color = namedtuple('rgb','red, green, blue')

class rgb(Color):
    def hex(self) -> int:
        return int ('{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue),16)

colors:dict= {}

def GetBlockColor (blockName: str)-> int :
    if (blockName in colors.keys()):
        return colors[blockName].hex ()
    elif "diamon" in blockName:
        return rgb (52,235,201).hex ()
    elif "grass" in blockName:
        return rgb (46,109,29).hex ()
    elif "dirt" in blockName:
        return rgb (151,108,74).hex ()
    elif "cobblestone" in blockName:
        return rgb (108,108,108).hex ()
    elif "stone" in blockName:
        return rgb (134,134,134).hex ()
    elif "snow" in blockName:
        return rgb (240,240,240).hex ()
    elif "iron" in blockName:
        return rgb (225,225,225).hex ()
    elif "gold" in blockName:
        return rgb (243,225,76).hex ()
    else:
        return rgb (165,0,255).hex () # purple

colors['planks']            = rgb (168,139,87)
colors['stairs']          = rgb (168,139,87)
colors['slab']          = rgb (168,139,87)
colors['fence']          = rgb (168,139,87)
colors['door']          = rgb (168,139,87)
colors['red_sand']          = rgb (197,73,14)

