package main

import (
	"fmt"
	"time"

	"github.com/nilshell/xmlrpc"
)

func main() {
	var boolRes interface{}
	var floor_requests [][2]int64
	var res []interface{}

	client, _ := xmlrpc.NewClient("http://localhost:8000", nil)
	client.Call("reset", nil, &boolRes)

	for {
		client.Call("check_for_elevator_request", nil, &res)

		if len(res) == 2 {
			floor_request := [2]int64{}
			for i := range res {
				floor_request[i] = res[i].(int64)
			}

			floor_requests = append(floor_requests, floor_request)
			fmt.Printf("Someone on floor #%d requested to go to floor #%d\n", floor_request[0], floor_request[1])
		} else {
			// No new elevator requests
			fmt.Println(".")
		}

		time.Sleep(1 * time.Second)
	}
}
