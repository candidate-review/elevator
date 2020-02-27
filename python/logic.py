import time
from sys import version_info

if version_info.major == 2:
  import xmlrpclib # Python 2
  elevator = xmlrpclib.ServerProxy('http://localhost:8000') # Python 2
else:
  from xmlrpc import client # Python 3
  elevator = client.ServerProxy('http://localhost:8000') # Python 3

elevator.reset()

floor_requests = []

while True:
    req = elevator.check_for_elevator_request()
    if req:
        print("Someone on floor #%i requested to go to floor #%i" % (req[0], req[1]))
        floor_requests.append(req)
    else:
        # No new elevator requests
        print('.')

    time.sleep(1)
