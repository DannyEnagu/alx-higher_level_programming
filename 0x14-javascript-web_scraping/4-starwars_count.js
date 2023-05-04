#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let idCounter = 0;
    movies.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes('18')) idCounter++;
      });
    });
    console.log(idCounter);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
