#!/usr/bin/ruby
require 'xmlrpc/client'

elevator = XMLRPC::Client.new2('http://localhost:8000')
elevator.call :reset

floor_requests = []

loop do
  req = elevator.call :check_for_elevator_request
  if req
    puts "Someone on floor ##{req[0]} requested to go to floor ##{req[1]}"
    floor_requests << req
  else
    # No new elevator requests
    puts '.'
  end

  sleep 1
end
