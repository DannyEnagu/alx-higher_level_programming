#!/usr/bin/node
const argv = process.argv;
if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  let biggest = 0;
  let bigger = 0;
  for (let i = 2; i < argv.length; i++) {
    const big = Number(argv[i]);
    if (big > biggest) {
      bigger = biggest;
      biggest = big;
    }
  }
  console.log(bigger);
}
