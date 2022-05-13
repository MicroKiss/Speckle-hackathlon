from specklepy.objects import Base
from specklepy.objects.geometry import  Box, Plane
from amulet import Block
from BlockColorDictionary import GetMaterial
from utility import *


class Glass (
    Base
):
    mainGlass: Box = None
    sideGlasses: Base = None


def CreateGlass(x: int, y: int, z: int, block: Block) -> Block:
    pass