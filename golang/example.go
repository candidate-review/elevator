package main

import (
	"fmt"
	"github.com/nilshell/xmlrpc"
)

func main() {
	client, _ := xmlrpc.NewClient("http://localhost:8000", nil)
	result := []interface{}{}
	client.Call("test_mode", [2][2]int{{4, 8}, {9, 3}}, &result)

	var boolRes interface{}

	fmt.Printf("Someone on floor #4 requested to go to floor #8\n")
	client.Call("service", [2]int{4, 8}, &boolRes)
	client.Call("move", 2, &boolRes)
	client.Call("move", 3, &boolRes)
	client.Call("move", 4, &boolRes)
	client.Call("pickup", nil, &boolRes)
	client.Call("move", 5, &boolRes)
	client.Call("move", 6, &boolRes)
	client.Call("move", 7, &boolRes)
	client.Call("move", 8, &boolRes)
	client.Call("dropoff", nil, &boolRes)

	fmt.Printf("Someone on floor #9 requested to go to floor #3\n")
	client.Call("service", [2]int{9, 3}, &boolRes)
	client.Call("move", 9, &boolRes)
	client.Call("pickup", nil, &boolRes)
	client.Call("move", 8, &boolRes)
	client.Call("move", 7, &boolRes)
	client.Call("move", 6, &boolRes)
	client.Call("move", 5, &boolRes)
	client.Call("move", 4, &boolRes)
	client.Call("move", 3, &boolRes)
	client.Call("dropoff", nil, &boolRes)

	// Invalid jump fro floor 3 to 1
	client.Call("move", 1, &boolRes)
}
