#!/usr/bin/ruby
require 'xmlrpc/client'

elevator = XMLRPC::Client.new2('http://localhost:8000')
elevator.call :test_mode, [[4, 8], [9, 3]]

puts 'Someone on floor #4 requested to go to floor #8'
elevator.call(:service, [4, 8], { id: 1 })
puts 'Someone on floor #9 requested to go to floor #3'
elevator.call(:service, [9, 3], { id: 2 })

elevator.call(:move, 2, { id: 1 })
elevator.call(:move, 2, { id: 2 })
elevator.call(:move, 3, { id: 1 })
elevator.call(:move, 3, { id: 2 })
elevator.call(:move, 4, { id: 1 })
elevator.call(:move, 4, { id: 2 })
elevator.call(:pickup, { id: 1 }) # << pickup on 4
elevator.call(:move, 5, { id: 1 })
elevator.call(:move, 5, { id: 2 })
elevator.call(:move, 6, { id: 1 })
elevator.call(:move, 6, { id: 2 })
elevator.call(:move, 7, { id: 1 })
elevator.call(:move, 7, { id: 2 })
elevator.call(:move, 8, { id: 1 })
elevator.call(:move, 8, { id: 2 })
elevator.call(:dropoff, { id: 1 }) # << drop off on 8
elevator.call(:move, 9, { id: 2 })
elevator.call(:pickup, { id: 2 }) # << pickup on 9
elevator.call(:move, 8, { id: 2 })
elevator.call(:move, 7, { id: 2 })
elevator.call(:move, 6, { id: 2 })
elevator.call(:move, 5, { id: 2 })
elevator.call(:move, 4, { id: 2 })
elevator.call(:move, 3, { id: 2 })
elevator.call(:dropoff, { id: 2 }) # << drop off on 3

# Invalid jump from floor 3 to floor 1
elevator.call(:move, 1, { id: 2 }) 
# Invalid jump from floor 8 to floor 1
elevator.call(:move, 1, { id: 1 }) 
