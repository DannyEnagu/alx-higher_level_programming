#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]);
number
  ? console.log('My number: ' + number)
  : console.log('Not a number');
