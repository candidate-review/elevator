package main

import (
	"fmt"
	"github.com/kolo/xmlrpc"
)

type Shaft struct {
	id int
}

func main() {
	var result [][]int
	var boolRes bool
	client, _ := xmlrpc.NewClient("http://localhost:8000", nil)
	client.Call("test_mode", [][]int{{4, 8}, {9, 3}}, &result)

	fmt.Printf("Someone on floor #4 requested to go to floor #8\n")
	client.Call("service", []interface{}{[]int{4, 8}, Shaft{1}}, &boolRes)
	fmt.Printf("Someone on floor #9 requested to go to floor #3\n")
	client.Call("service", []interface{}{[]int{9, 3}, Shaft{2}}, &boolRes)

	client.Call("move", []interface{}{2, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{2, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{3, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{3, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{4, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{4, Shaft{2}}, &boolRes)
	client.Call("pickup", []interface{}{Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{5, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{5, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{6, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{6, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{7, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{7, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{8, Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{8, Shaft{2}}, &boolRes)
	client.Call("dropoff", []interface{}{Shaft{1}}, &boolRes)
	client.Call("move", []interface{}{9, Shaft{2}}, &boolRes)
	client.Call("pickup", []interface{}{Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{8, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{7, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{6, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{5, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{4, Shaft{2}}, &boolRes)
	client.Call("move", []interface{}{3, Shaft{2}}, &boolRes)
	client.Call("dropoff", []interface{}{Shaft{2}}, &boolRes)

	// Invalid jump from floor 3 to floor 1
	client.Call("move", []interface{}{1, Shaft{2}}, &boolRes)

	// Invalid jump from floor 8 to floor 1
	client.Call("move", []interface{}{1, Shaft{1}}, &boolRes)
}
