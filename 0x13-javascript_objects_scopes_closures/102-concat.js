#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

const writeStream = fs.createWriteStream(argv[4]);
if (argv.length === 5) {
  readAndWriteToFile(argv[2]);
  readAndWriteToFile(argv[3]);
}

function readAndWriteToFile (filename) {
  try {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) throw err;
      if (filename === argv[2]) { writeStream.write(data); }
      if (filename === argv[3]) {
        writeStream.write(data);
        writeStream.end();
      }
    });
  } catch (error) {
    console.error(error);
  }
}
