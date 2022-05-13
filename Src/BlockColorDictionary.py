from collections import namedtuple
Color = namedtuple('rgb','red, green, blue')
from specklepy.objects.other import RenderMaterial
from amulet import Block
from utility import *

materials:dict= {}
colors:dict= {}
glassColors: dict= {}

class rgb(Color):
    def hex(self) -> int:
        return int ('{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue),16)


def GetGlassColorKey (blockName : str)-> str :
    if (blockName == "glass" or blockName == "glass_pane"):
        return blockName
    elif ("tinted" in blockName):
        return "tinted"
    elif ("stained_glass_pane" in blockName):
        return blockName[:-19]
    else:
        return blockName[:14]


def GetBlockColor (blockName: str)-> int :
    if (blockName in colors.keys()):
        return colors[blockName].hex ()
    elif "diamond" in blockName:
        return rgb (52,235,201).hex ()
    elif "grass" in blockName:
        return rgb (46,109,29).hex ()
    elif "dirt" in blockName:
        return rgb (151,108,74).hex ()
    elif "cobblestone" in blockName:
        return materials["cobblestone"].hex ()
    elif "sandstone" in blockName:
        return materials["sandstone"].hex ()
    elif "stone" in blockName:
        return materials["stone"].hex ()
    elif "snow" in blockName:
        return rgb (240,240,240).hex ()
    elif "iron" in blockName:
        return materials["iron"].hex ()
    elif "gold" in blockName:
        return rgb (243,225,76).hex ()
    elif "sand" in blockName:
        return rgb (233,226,203).hex ()
    elif "andesite" in blockName:
        return materials["andesite"].hex ()
    elif "glass" in blockName:
        return glassColors[GetGlassColorKey(blockName)].hex ()
    else:
        return rgb (165,0,255).hex () # purple

# TODO actual colors
glassColors['glass'] = rgb (1,2,3)
glassColors['tinted'] = rgb (1,2,3)
glassColors['white'] = rgb (1,2,3)
glassColors['orange'] = rgb (1,2,3)
glassColors['magenta'] = rgb (1,2,3)
glassColors['light_blue'] = rgb (1,2,3)
glassColors['yellow'] = rgb (1,2,3)
glassColors['lime'] = rgb (1,2,3)
glassColors['pink'] = rgb (1,2,3)
glassColors['gray'] = rgb (1,2,3)
glassColors['light_grey'] = rgb (1,2,3)
glassColors['cyan'] = rgb (1,2,3)
glassColors['purple'] = rgb (1,2,3)
glassColors['blue'] = rgb (1,2,3)
glassColors['brown'] = rgb (1,2,3)
glassColors['green'] = rgb (1,2,3)
glassColors['red'] = rgb (1,2,3)
glassColors['black'] = rgb (1,2,3)

colors['planks']            = rgb (168,139,87)
colors['stairs']          = rgb (168,139,87)
colors['slab']          = rgb (168,139,87)
colors['fence']          = rgb (168,139,87)
colors['door']          = rgb (168,139,87)
colors['red_sand']          = rgb (197,73,14)
colors['wall']          = rgb (108,108,108)

materials["stone"] = rgb(173,173,173)
materials["acacia"] = rgb(173,93,50)
materials["andesite"] = rgb(192,192,192)
materials["birch"] = rgb(201,189,131)
materials["blackstone"] = rgb(18,14,15)
materials["brick"] = rgb(152,85,64)
materials["cobbled_deepslate"] = rgb(60,60,66)
materials["cobblestone"] = rgb(108,108,108)
materials["crimson"] = rgb(134,62,90)
materials["cut_copper"] = rgb(226,130,108)
materials["dark_oak"] = rgb(39,25,12)
materials["dark_prismarine"] = rgb(41,80,64)
materials["deepslate_brick"] = rgb(52,52,52)
materials["deepslate_tile"] = rgb(34,34,34)
materials["diorite"] = rgb(203,202,205)
materials["end_stone_brick"] = rgb(223,233,172)
materials["exposed_cut_copper"] = rgb(137,97,81)
materials["granite"] = rgb(189,133,114)
materials["iron"] = rgb(162,162,162)
materials["jungle"] = rgb(160,121,82)
materials["mossy_cobblestone"] = materials['cobblestone']
materials["mossy_stone_brick"] = materials['stone']
materials["nether_brick"] = rgb(102,16,14)
materials["oak"] = rgb(178,144,91)
materials["oxidized_cut_copper"] = rgb(80,152,128)
materials["polished_andesite"] = rgb(119,121,120)
materials["polished_blackstone"] = rgb(25,21,25)
materials["polished_deepslate"] = rgb(51,51,51)
materials["polished_diorite"] = rgb(200,200,200)
materials["polished_granite"] = rgb(145,98,84)
materials["prismarine"] = rgb(138,184,162)
materials["purpur"] = rgb(166,119,165)
materials["quartz"] = rgb(218,212,204)
materials["red_nether_brick"] = rgb(73,9,9)
materials["red_sandstone"] = rgb(157,80,28)
materials["smooth_quartz"] = rgb(220,217,211)
materials["smooth_red_sandstone"] = rgb(171,91,30)
materials["smooth_sandstone"] = rgb(209,198,160)
materials["spruce"] = rgb(99,74,46)
materials["_brick"] = materials['brick']
materials["warped"] = rgb(60,131,133)
materials["waxed_cut_copper"] = rgb(157,84,62)
materials["waxed_exposed_cut_copper"] = rgb(155,113,97)
materials["waxed_oxidized_cut_copper"] = rgb(74,143,114)
materials["waxed_weathered_cut_copper"] = rgb(158,114,106)
materials["prismarine_brick"] = rgb(88,148,139)
materials["sandstone"] = rgb(214,203,160)


def GetMaterial (block: Block) -> RenderMaterial:
    mat = RenderMaterial() #diffuse=mat
    if hasattr(block,'properties') and ("material" in block.properties):
        try:
            mat.diffuse = GetColorFromMaterial(block.properties["material"])
        except:
            WRITEDEBUG (str (block.properties["material"]))
    else:
        name: str = block.base_name
        mat.diffuse=GetBlockColor (name)
    return mat

def GetColorFromMaterial (mat :str) -> Color:
    return materials[str (mat)].hex ()