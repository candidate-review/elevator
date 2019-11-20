#!/usr/bin/node
var elevator = require('./elevator');

(async () => {
  await elevator.call('test_mode', [[4, 8], [9, 3]]);

  console.log('Someone on floor #4 requested to go to floor #8');
  await elevator.call('service', [4, 8], { id: 1 });
  console.log('Someone on floor #9 requested to go to floor #3');
  await elevator.call('service', [9, 3], { id: 2 });

  await elevator.call('move', 2, { id: 1 })
  await elevator.call('move', 2, { id: 2 })
  await elevator.call('move', 3, { id: 1 })
  await elevator.call('move', 3, { id: 2 })
  await elevator.call('move', 4, { id: 1 })
  await elevator.call('move', 4, { id: 2 })
  await elevator.call('pickup', { id: 1 }) // << pickup on 4
  await elevator.call('move', 5, { id: 1 })
  await elevator.call('move', 5, { id: 2 })
  await elevator.call('move', 6, { id: 1 })
  await elevator.call('move', 6, { id: 2 })
  await elevator.call('move', 7, { id: 1 })
  await elevator.call('move', 7, { id: 2 })
  await elevator.call('move', 8, { id: 1 })
  await elevator.call('move', 8, { id: 2 })
  await elevator.call('dropoff', { id: 1 }) // << drop off on 8
  await elevator.call('move', 9, { id: 2 })
  await elevator.call('pickup', { id: 2 }) // << pickup on 9
  await elevator.call('move', 8, { id: 2 })
  await elevator.call('move', 7, { id: 2 })
  await elevator.call('move', 6, { id: 2 })
  await elevator.call('move', 5, { id: 2 })
  await elevator.call('move', 4, { id: 2 })
  await elevator.call('move', 3, { id: 2 })
  await elevator.call('dropoff', { id: 2 }) // << drop off on 3
})();
