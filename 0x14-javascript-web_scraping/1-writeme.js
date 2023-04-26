#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

function writeToFile (filename, data) {
  fs.writeFile(filename, data, 'utf8', (err) => {
    if (err) console.log(err);
  });
}

if (argv.length > 3) {
  writeToFile(argv[2], argv[3]);
}
