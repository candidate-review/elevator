from collections import defaultdict
from platform import system as system_name
from os import system as system_call
from random import randint
from sys import version_info

if version_info.major == 2:
    from SimpleXMLRPCServer import SimpleXMLRPCServer # Python 2
else:
    from xmlrpc.server import SimpleXMLRPCServer # Python 3

def print_warn(string, elevator_id=None):
    elevator_id_str = '' if not elevator_id else '(%s) ' % elevator_id
    print("\x1b[6;37;41m%s%s\x1b[0m" % (elevator_id_str, string))

def print_success(string, elevator_id=None):
    elevator_id_str = '' if not elevator_id else '(%s) ' % elevator_id
    print("\x1b[5;30;42m%s%s\x1b[0m" % (elevator_id_str, string))

def print_status(string, elevator_id=None):
    elevator_id_str = '' if not elevator_id else '(%s) ' % elevator_id
    print("\x1b[5;30;47m%s%s\x1b[0m" % (elevator_id_str, string))

def print_status1(string, elevator_id=None):
    elevator_id_str = '' if not elevator_id else '(%s) ' % elevator_id
    print("\x1b[1;37;44m%s%s\x1b[0m" % (elevator_id_str, string))

class Elevator():
    MAX_FLOOR = 10

    def __init__(self):
        # Initlaied in #reset
        self.current_floor = None
        self.requests = None
        self.active = None

        self.server = SimpleXMLRPCServer(("localhost", 8000), logRequests=False)
        self.register_rpc_handlers()

        self.reset()
        self.server.serve_forever()

    def register_rpc_handlers(self):
        self.server.register_function(self.check_for_elevator_request)
        self.server.register_function(self.move)
        self.server.register_function(self.service)
        self.server.register_function(self.pickup)
        self.server.register_function(self.dropoff)
        self.server.register_function(self.reset)
        self.server.register_function(self.test_mode)

    def check_for_elevator_request(self):
        from_floor = randint(1, self.MAX_FLOOR)
        to_floor = randint(1, self.MAX_FLOOR)
        if randint(0, 10) > 8 and from_floor != to_floor:
            print_status("Someone on floor #%i requested to go to floor #%i" % (from_floor, to_floor))
            self.requests.append([from_floor, to_floor])
            return (from_floor, to_floor)

        return []

    def move(self, floor, opts={}):
        elevator_id = opts.get('id')

        valid_direction = (self.current_floor[elevator_id] == floor \
                           or floor == self.current_floor[elevator_id] + 1 or \
                           floor == self.current_floor[elevator_id] - 1) \
                           and (floor >= 1 and floor <= self.MAX_FLOOR)

        if (valid_direction):
            print_success('Moved from floor %s to %s' % (self.current_floor[elevator_id], floor), elevator_id)
            self.current_floor[elevator_id] = floor
            return True
        else:
            print_warn('Invalid move to floor %s, elevator is currently on floor %s' \
                       % (floor, self.current_floor[elevator_id]), elevator_id)
            return False

    def service(self, req, opts = {}):
        elevator_id = opts.get('id')

        if self.active[elevator_id]:
            print_warn('Unable to service another request. Currently servicing %s.' % self.active[elevator_id], elevator_id)
            return False
        if self.requests[0] != req:
            print_warn('Invalid service request. Next request in the queue is %s.' % self.requests[0], elevator_id)
            return False

        print_status1("Servicing a request to pickup a passenger on floor #%i and drop them on floor #%i" % (req[0], req[1]), elevator_id)
        self.active[elevator_id].extend(self.requests[0])
        del self.requests[0]

        return True

    def pickup(self, opts = {}):
        elevator_id = opts.get('id')

        if not self.active[elevator_id]:
            print_warn('No active requests to pickup. Make sure you called #service to start fulfilling a request.', elevator_id)
            return False
        elif self.active[elevator_id][0] == self.current_floor[elevator_id] and len(self.active[elevator_id]) == 2:
            print_success('Picked up a passenger on floor #' + str(self.current_floor[elevator_id]), elevator_id)
            del self.active[elevator_id][0]
            return True
        else:
            if len(self.active[elevator_id]) == 1:
                print_warn("Passenger was already picked up. Drop them off on floor #%s" % self.active[elevator_id][0], elevator_id)
            else:
                print_warn("Invalid pick up floor. Current pick up request is for floor #%s." % (self.active[elevator_id][0]), elevator_id)
            return False

    def dropoff(self, opts = {}):
        elevator_id = opts.get('id')

        if not self.active[elevator_id]:
            print_warn('No active requests to drop off. Make sure you called #service to start fulfilling a request.', elevator_id)
            return False
        elif self.active[elevator_id][0] == self.current_floor[elevator_id] and len(self.active[elevator_id]) == 1:
            print_success("Dropped off a passenger on floor #%s. Request complete." % self.current_floor[elevator_id], elevator_id)
            self.active[elevator_id] = []
            return True
        else:
            if len(self.active[elevator_id]) == 1:
                print_warn("Invalid drop off floor. Current drop off request is for floor #%s." % self.active[elevator_id][0], elevator_id)
            else:
                print_warn("You need to pick up the passenger on floor #%s before you drop them off" % self.active[elevator_id][0], elevator_id)
            return False

    def clear_screen(self):
        command = "-cls" if system_name().lower()=="windows" else "clear"
        system_call(command)

    def reset(self):
        self.current_floor = defaultdict(lambda : 1)
        self.requests = []
        self.active = defaultdict(lambda : [])

        self.clear_screen()
        print_status('Elevator is ready for service!')

        return True

    def test_mode(self, queue):
        self.reset()

        self.requests = queue

        print_status('Entering test mode')
        print_status('Request queue: ' + str(queue))
        print('')

        return self.requests

Elevator()
