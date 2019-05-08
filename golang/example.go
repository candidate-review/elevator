package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

func main() {
	var result [][]int
	var boolRes bool

	client, _ := xmlrpc.NewClient("http://localhost:8000", nil)
	client.Call("test_mode", [][]int{{4, 8}, {9, 3}}, &result)

	fmt.Printf("Someone on floor #4 requested to go to floor #8\n")
	client.Call("service", []int{4, 8}, &boolRes)
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
	client.Call("service", []int{9, 3}, &boolRes)
	client.Call("move", 9, &boolRes)
	client.Call("pickup", nil, &boolRes)
	client.Call("move", 8, &boolRes)
	client.Call("move", 7, &boolRes)
	client.Call("move", 6, &boolRes)
	client.Call("move", 5, &boolRes)
	client.Call("move", 4, &boolRes)
	client.Call("move", 3, &boolRes)
	client.Call("dropoff", nil, &boolRes)

	// Invalid jump from floor 3 to 1
	client.Call("move", 1, &boolRes)
}
