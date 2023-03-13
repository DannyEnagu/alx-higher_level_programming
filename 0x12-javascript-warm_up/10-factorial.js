#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]) || 0;
function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return (num * factorial(num - 1));
}
console.log(factorial(number));
