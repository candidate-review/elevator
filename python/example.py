# import xmlrpclib # Python 2
from xmlrpc import client # Python 3

#elevator = xmlrpclib.ServerProxy('http://localhost:8000') # Python 2
elevator = client.ServerProxy('http://localhost:8000') # Python 3
elevator.test_mode([(4, 8), (9, 3)])

print("Someone on floor #4 requested to go to floor #8")
elevator.service([4, 8])
elevator.move(2)
elevator.move(3)
elevator.move(4)
elevator.pickup() # << pickup on 4
elevator.move(5)
elevator.move(6)
elevator.move(7)
elevator.move(8)
elevator.dropoff() # << drop off on 8

print("Someone on floor #9 requested to go to floor #3")
elevator.service([9, 3])
elevator.move(9)
elevator.pickup() # << pickup on 9
elevator.move(8)
elevator.move(7)
elevator.move(6)
elevator.move(5)
elevator.move(4)
elevator.move(3)
elevator.dropoff() # << drop off on 3

# Invalid jump from floor 3 to floor 1
elevator.move(1)
