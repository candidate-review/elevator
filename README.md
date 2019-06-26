# The Elevator Problem


## elevator.py
This file is code complete and doesn't require any modifications or edits from you. What's inside is a server that represents the elevator concept. The server provides a dumb interface to use the elevator and retrieve requests from patrons.

### `check_for_elevator_request`
Retrieve requests from patrons to use the elevator.

#### Arguments
None

#### Response
Two-index array of the pick up floor and destination floor.

```
[4, 9] # Someone on floor 4 would like to go to floor 9
```

When there's no new request `false` will be returned

### `service`
Informs the elevator of the request you plan to fulfill

#### Arguments

`request`: Array containing the pick up floor and destination floor

```
service([4, 9])
```

#### Response

`true` when the service request is valid and can be fulfilled

`false` when the request is invalid or the elevator is currently in use

### `pickup`
Used to open the elevator door to allow the patron to enter on the floor they requested pickup from.

### Arguments
None


### Response

`true` when picking up the current service request patron on the requested floor

`false` when used on an invalid floor

### `move`
Move the elevator to a specific floor

#### Arguments
`floor` the floor number to move the elevator to

#### Returns

`true` when the elevator moves to a valid floor

`false` when the elevator is moved to an invalid floor. i.e. if the elevator is on floor 5 it can't move directly to floor 3.

### `dropoff`
Used to drop off a user on the requested floor

### Arguments
None

### Response

`true` when dropping off the current service request patron on the requested floor

`false` when used on an invalid floor

### `reset`
Reset the elevator to the starting state. Clears the current active request queue and returns the elevator to the first floor.

#### Arguments
None

#### Returns
`true`

### `test_mode`
Forces the elevator into test mode where the request queue can be specified.

#### Aruments
`queue` array of arrays representing the request queue

```
# Represents two requests in order
[[1, 4], [7, 9]]
```

#### Returns
The list of requests sent

