import SpeckleConnection as SC
from datetime import datetime

from specklepy.objects import Base
from specklepy.objects.other import RenderMaterial
from specklepy.objects.geometry import Interval, Box, Plane, GEOMETRY


from specklepy.transports.server import ServerTransport
from specklepy.api import operations

from color_constants import colors

def GetColorFromMinecraftBlockId(asd:int):
    re

def CreateBlock (x:int, y:int, z:int):
    plane = Plane.from_list([x,y,z,0,0,1,1,0,0,0,1,0])
    interval = Interval (start= 0, end= 1)
    ret = Box(xSize = interval, ySize = interval, zSize = interval, basePlane = plane)
    ret.renderMaterial = RenderMaterial (diffuse=colors["midnightblue"].hex ())
    return ret


blocks = []
blocks.append(CreateBlock(0,0,0))
blocks.append(CreateBlock(1,0,0))
blocks.append(CreateBlock(2,0,0))
blocks.append(CreateBlock(3,0,0))
blocks.append(CreateBlock(4,0,0))
blocks.append(CreateBlock(2,1,0))
blocks.append(CreateBlock(2,2,0))
blocks.append(CreateBlock(2,1,1))

# next create a server transport - this is the vehicle through which you will send and receive
transport = ServerTransport(client=SC.client, stream_id=SC.stream.id)

# this serialises the block and sends it to the transport

base_obj = Base()
base_obj.entities = blocks
base_obj.add_chunkable_attrs (entities = 5000)

hash = operations.send(base=base_obj, transports=[transport])

# you can now create a commit on your stream with this object
now = datetime.now().strftime("%H:%M:%S")
commid_id = SC.client.commit.create(
    stream_id=SC.stream.id, 
    object_id=hash, 
    message="time: "+ now,
    )

