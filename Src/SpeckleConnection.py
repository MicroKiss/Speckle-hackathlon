import personal as PERSONAL
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_account_from_token


speckleServer = "speckle.xyz"
client = SpeckleClient (host = speckleServer)
account = get_account_from_token ( PERSONAL.api_token, speckleServer)
client.authenticate_with_account (account)
stream = client.stream.list () [0]