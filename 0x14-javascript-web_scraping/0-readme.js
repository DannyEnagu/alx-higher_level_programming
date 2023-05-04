#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

function readFromFile (filename) {
  fs.readFile(filename, 'utf8', (err, data) => {
    try {
      if (err) throw err;
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  });
}

if (argv.length > 2) {
  const pathToFile = argv[2];
  readFromFile(pathToFile);
}
