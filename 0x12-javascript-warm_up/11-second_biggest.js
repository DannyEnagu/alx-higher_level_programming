#!/usr/bin/node
const argv = process.argv;
let biggest = 0;
let bigger = 0;
let big = 0;
for (let i = 2; i < argv.length; i++) {
  big = Number(argv[i]);
  if (big > biggest) {
    bigger = biggest;
    biggest = big;
  }
  if ((biggest > big) && (bigger < big)) {
    bigger = big;
  }
}
console.log(bigger);
