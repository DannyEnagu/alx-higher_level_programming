#!/usr/bin/node
const argv = process.argv;
const xTimes = Number(argv[2]);
if (xTimes) {
  for (let i = 0; i < xTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
