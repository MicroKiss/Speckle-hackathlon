from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Box, Plane
from utility import *

def CreateBlock (x:int, y:int, z:int, mat:int ) -> Box:
    plane = Plane.from_list([x,y,z,0,0,1,1,0,0,0,1,0])
    ret = Box(xSize = intervalWhole, ySize = intervalWhole, zSize = intervalWhole, basePlane = plane)
    ret.renderMaterial = RenderMaterial (diffuse=mat)
    return ret