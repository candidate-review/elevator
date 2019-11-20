#!/usr/bin/node
var elevator = require('./elevator');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    await elevator.call('reset');

    const floorRequests = [];

    while(true) {
       const req = await elevator.call('check_for_elevator_request');

        if (req.length === 0) {
            console.log('.');
        } else {
            console.log(`Someone on floor ${req[0]} requested to go to floor ${req[1]}`);
            floorRequests.push(req);
        }

        await sleep(1000);
    }
})();
