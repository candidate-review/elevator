from sys import version_info

if version_info.major == 2:
  import xmlrpclib # Python 2
  elevator = xmlrpclib.ServerProxy('http://localhost:8000') # Python 2
else:
  from xmlrpc import client # Python 3
  elevator = client.ServerProxy('http://localhost:8000') # Python 3

elevator.test_mode([(4, 8), (9, 3)])

print("Someone on floor #4 requested to go to floor #8")
elevator.service([4, 8], { 'id': 1 })
print("Someone on floor #9 requested to go to floor #3")
elevator.service([9, 3], { 'id': 2 })

elevator.move(2, { 'id': 1 })
elevator.move(2, { 'id': 2 })
elevator.move(3, { 'id': 1 })
elevator.move(3, { 'id': 2 })
elevator.move(4, { 'id': 1 })
elevator.move(4, { 'id': 2 })
elevator.pickup({ 'id': 1 }) # << pickup on 4
elevator.move(5, { 'id': 1 })
elevator.move(5, { 'id': 2 })
elevator.move(6, { 'id': 1 })
elevator.move(6, { 'id': 2 })
elevator.move(7, { 'id': 1 })
elevator.move(7, { 'id': 2 })
elevator.move(8, { 'id': 1 })
elevator.move(8, { 'id': 2 })
elevator.dropoff({ 'id': 1 }) # << drop off on 8
elevator.move(9, { 'id': 2 })
elevator.pickup({ 'id': 2 }) # << pickup on 9
elevator.move(8, { 'id': 2 })
elevator.move(7, { 'id': 2 })
elevator.move(6, { 'id': 2 })
elevator.move(5, { 'id': 2 })
elevator.move(4, { 'id': 2 })
elevator.move(3, { 'id': 2 })
elevator.dropoff({ 'id': 2 }) # << drop off on 3

# Invalid jump from floor 3 to floor 1
elevator.move(1, { 'id' : 2 })
# Invalid jump from floor 8 to floor 1
elevator.move(1, { 'id' : 1 })
