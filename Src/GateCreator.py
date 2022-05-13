from specklepy.objects import Base
from specklepy.objects.geometry import  Box, Plane
from amulet import Block
from BlockColorDictionary import GetMaterial
from utility import *


class Gate (
    Base
):
    leftSide: Base = None
    rightSide: Base = None


def CreateGate(x: int, y: int, z: int, block: Block) -> Block:
    pass