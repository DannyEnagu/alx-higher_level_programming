#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

if (argv.length === 5) {
    const fileDataA = fileData(argv[2]);
    const fileDataB = fileData(argv[3]);
    const writeStream = fs.createWriteStream(argv[4]);
    console.log(fileDataA, fileDataB);
    writeStream.write(`${fileDataA}\n${fileDataB}`);
    writeStream.end();
}

function writeToFile (filename) {
    try {
      fs.readFile(filename, 'utf8', (err, data) => {
        if (err) throw err;
 
      });
    } catch (error) {
     console.error(error);
    }
    return await fileData;
}
