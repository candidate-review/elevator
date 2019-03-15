#!/usr/bin/ruby
require 'xmlrpc/client'

elevator = XMLRPC::Client.new2('http://localhost:8000')
elevator.call :test_mode, [[4, 8], [9, 3]]

puts 'Someone on floor #4 requested to go to floor #8'
elevator.call(:service, [4, 8])
elevator.call(:move, 2)
elevator.call(:move, 3)
elevator.call(:move, 4)
elevator.call(:pickup) # << pickup on 4
elevator.call(:move, 5)
elevator.call(:move, 6)
elevator.call(:move, 7)
elevator.call(:move, 8)
elevator.call(:dropoff) # << drop off on 8

puts 'Someone on floor #9 requested to go to floor #3'
elevator.call(:service, [9, 3])
elevator.call(:move, 9)
elevator.call(:pickup) # << pickup on 9
elevator.call(:move, 8)
elevator.call(:move, 7)
elevator.call(:move, 6)
elevator.call(:move, 5)
elevator.call(:move, 4)
elevator.call(:move, 3)
elevator.call(:dropoff) # << drop off on 3

# Invalid jump from floor 3 to floor 1
elevator.call(:move, 1)
