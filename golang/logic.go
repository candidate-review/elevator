package main

import (
	"fmt"
	"time"

	"github.com/kolo/xmlrpc"
)

func main() {
	var boolRes bool
	var floor_requests [][]int
	var res []int

	client, _ := xmlrpc.NewClient("http://localhost:8000", nil)
	client.Call("reset", nil, &boolRes)

	for {
		client.Call("check_for_elevator_request", nil, &res)

		if len(res) == 2 {
			floor_requests = append(floor_requests, res)
			fmt.Printf("Someone on floor #%d requested to go to floor #%d\n", res[0], res[1])
		} else {
			// No new elevator requests
			fmt.Println(".")
		}

		res = nil
		time.Sleep(1 * time.Second)
	}
}
