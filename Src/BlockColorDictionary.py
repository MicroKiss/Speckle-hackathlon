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


def GetBlockColor (blockName: str)-> int :
    if (blockName in colors.keys()):
        return colors[blockName].hex ()
    elif "brick" in blockName:
        return materials["brick"].hex ()
    elif "anvil" in blockName:
        return materials["brick"].hex ()
    elif "quartz" in blockName:
        return materials["quartz"].hex ()
    elif "diamond" in blockName:
        return rgb (52,235,201).hex ()
    elif "campfire" in blockName:
        return glassColors['brown'].hex ()
    elif "bedrock" in blockName:
        return rgb(49,49,49).hex ()
    elif "gravel" in blockName:
        return rgb(122,116,116).hex ()
    elif "coal" in blockName:
        return rgb(44,44,44).hex ()
    elif "warped_nylium" in blockName:
        return rgb(67,130,98).hex ()
    elif "nylium" in blockName:
        return rgb(148,24,24).hex ()
    elif "deepslate" in blockName:
        return rgb(28,28,28).hex ()
    elif "calcite" in blockName:
        return rgb(175,176,173).hex ()
    elif "tuff" in blockName:
        return rgb(137,137,133).hex ()
    elif "podzol" in blockName:
        return rgb(89,59,34).hex ()
    elif "diorite" in blockName:
        return rgb(148,148,148).hex ()
    elif "granite" in blockName:
        return rgb(153,104,86).hex ()
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
    elif "exposed_copper" in blockName:
        return rgb(91,82,65).hex ()
    elif "weathered_copper" in blockName:
        return rgb(63,97,67).hex ()
    elif "oxidized_copper" in blockName:
        return rgb(90,151,114).hex ()
    elif "copper" in blockName:
        return rgb(205,106,76).hex ()
    elif "netherite" in blockName:
        return rgb(78,71,76).hex ()
    elif "andesite" in blockName:
        return materials["andesite"].hex ()
    elif "plant" in blockName:
        return rgb (0,140,0).hex ()
    else:
        return rgb (165,0,255).hex () # purple

#glassColors['glass'] = rgb (1,2,3)

glassColors['black'] = rgb ( 0,0,0)
glassColors['blue'] = rgb(0, 0, 255)
glassColors['brown'] = 	rgb(139,69,19)
glassColors['cyan'] = rgb (0,255,255)
glassColors['gray'] = rgb(128,128,128)
glassColors['green'] = rgb(0,255,0)
glassColors['light_blue'] = rgb (173, 216, 230)
glassColors['light_gray'] = rgb (200,200,200)
glassColors['lime'] = rgb(191,255,0)
glassColors['magenta'] = rgb(255,0,255)
glassColors['orange'] = rgb  (255, 165, 0)
glassColors['pink'] = rgb(255,105,180)
glassColors['purple'] = rgb(128,0,128)
glassColors['red'] = rgb (255,0,0)
glassColors['white'] = rgb (255,255,255)
glassColors['yellow'] = rgb (255,255,0)

colors['planks']            = rgb (168,139,87)
colors['concrete']            = rgb(199,201,206)
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
materials["stone_brick"] = rgb(125,125,125)
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
materials["polished_blackstone_brick"] = rgb(25,21,25)
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
materials["weathered_cut_copper"] = rgb(84,160,139)
materials["prismarine_brick"] = rgb(88,148,139)
materials["sandstone"] = rgb(214,203,160)
materials["cut_sandstone"] = rgb(214,203,160)


def GetGlassMaterial (color:str):
    try:
        return glassColors[color].hex ()
    except :
        WRITEDEBUG (color)
        return rgb(200,200,200).hex ()

def GetMaterial (block: Block) -> RenderMaterial:
    mat: RenderMaterial = RenderMaterial() 
    if ("glass" in block.base_name ):
        if ('color' in block.properties):
            mat.diffuse = GetGlassMaterial (str (block.properties["color"]))
        else:
            mat.diffuse = rgb(200,200,200).hex ()
        mat.opacity = 0.5
    elif ("leaves" in block.base_name):
        mat.diffuse = rgb(0,200,0).hex ()
        mat.opacity = 0.8
    elif ("water" in block.base_name):
        mat.diffuse = rgb(0,0,240).hex ()
        mat.opacity = 0.5
    elif ("terracotta" in block.base_name):
        if ('color' in block.properties):
            mat.diffuse = GetGlassMaterial (str (block.properties["color"]))
        else:
            mat.diffuse = rgb(200,200,200).hex ()
    elif ("concrete_powder" in block.base_name):
        if ('color' in block.properties):
            mat.diffuse = GetGlassMaterial (str (block.properties["color"]))
        else:
            mat.diffuse = rgb(200,200,200).hex ()
    elif ("wool" in block.base_name):
        if ('color' in block.properties):
            mat.diffuse = GetGlassMaterial (str (block.properties["color"]))
        else:
            mat.diffuse = rgb(200,200,200).hex ()
    elif hasattr(block,'properties') and ("material" in block.properties):
        try:
            mat.diffuse = GetColorFromMaterial(str (block.properties["material"]))
        except:
            WRITEDEBUG (str (block.properties["material"]))
            mat.diffuse = rgb(200,200,200).hex ()
    else:
        name: str = block.base_name
        mat.diffuse=GetBlockColor (str (name))
    
    return mat

def GetColorFromMaterial (mat :str) -> Color:
    return materials[mat].hex ()