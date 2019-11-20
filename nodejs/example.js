#!/usr/bin/node
var elevator = require('./elevator');

(async () => {
  await elevator.call('test_mode', [[4, 8], [9, 3]]);

  console.log('Someone on floor #4 requested to go to floor #8');
  await elevator.call('service', [4, 8]);
  await elevator.call('move', 2);
  await elevator.call('move', 3);
  await elevator.call('move', 4);
  await elevator.call('pickup');
  await elevator.call('move', 5);
  await elevator.call('move', 6);
  await elevator.call('move', 7);
  await elevator.call('move', 8);
  await elevator.call('dropoff');

  console.log('Someone on floor #9 requested to go to floor #3');
  await elevator.call('service', [9, 3]);
  await elevator.call('move', 9);
  await elevator.call('pickup');
  await elevator.call('move', 8);
  await elevator.call('move', 7);
  await elevator.call('move', 6);
  await elevator.call('move', 5);
  await elevator.call('move', 4);
  await elevator.call('move', 3);
  await elevator.call('dropoff');

  // Invalid jump from floor 3 to floor 1
  await elevator.call('move', 1);
})();
