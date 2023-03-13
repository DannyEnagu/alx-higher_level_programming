#!/usr/bin/node
const argv = process.argv;
const squareSize = Number(argv[2]);
if (squareSize) {
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
