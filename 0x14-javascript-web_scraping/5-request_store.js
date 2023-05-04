#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const request = require('request');

function writeToFile (filename, data) {
  fs.writeFile(filename, data, 'utf8', (err) => {
    if (err) console.log(err);
  });
}

if (argv.length > 3) {
  request(argv[2], function (err, res, body) {
    if (err) {
      console.log(err);
    } else if (res.statusCode === 200) {
      writeToFile(argv[3], body);
    } else {
      console.log(`code: ${res.statusCode}`);
    }
  });
}
