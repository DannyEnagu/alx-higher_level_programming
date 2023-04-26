#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

function writeToFile (filename, data) {
  fs.writeFile(filename, data, 'utf8', (err) => {
    try {
      if (err) throw err;
    } catch (error) {
      console.log(error);
    }
  });
}

if (argv.length > 3) {
  const fileContent = `${argv[3]}\n`;
  writeToFile(argv[2], fileContent);
}
