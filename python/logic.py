import time
# import xmlrpclib # Python 2
from xmlrpc import client # Python 3

#elevator = xmlrpclib.ServerProxy('http://localhost:8000') # Python 2
elevator = client.ServerProxy('http://localhost:8000') # Python 3
elevator.reset()

floor_requests = []

while True:
    # seconds = elevator.tick()
    # print("Tick %i" % seconds)

    req = elevator.check_for_elevator_request()
    if req:
        print("Someone on floor #%i requested to go to floor #%i" % (req[0], req[1]))
        floor_requests.append(req)
    else:
        # No new elevator requests
        print('.')

    time.sleep(1)
