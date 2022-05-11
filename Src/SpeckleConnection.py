import personal as PERSONAL
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_account_from_token
from specklepy.transports.server import ServerTransport
from specklepy.api import operations
from datetime import datetime
from specklepy.objects import Base


speckleServer = "speckle.xyz"
client = SpeckleClient (host = speckleServer)
account = get_account_from_token ( PERSONAL.api_token, speckleServer)
client.authenticate_with_account (account)
stream = client.stream.list () [0]
transport = ServerTransport (client=client, stream_id=stream.id)



def Send (obj:Base):
    hash = operations.send(base=obj, transports=[transport])
    now = datetime.now().strftime("%H:%M:%S")
    commid_id = client.commit.create(
        stream_id=stream.id, 
        object_id=hash, 
        message="New commit at : "+ now,
        )