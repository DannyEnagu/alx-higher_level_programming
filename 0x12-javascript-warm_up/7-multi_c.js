#!/usr/bin/node
const argv = process.argv;
let xTimes = Number(argv[2]);
if (xTimes) {
  for (; xTimes >= 0; xTimes--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
