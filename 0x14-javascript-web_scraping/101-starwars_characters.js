#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const url = api + process.argv[2];

function getCastsByFilmID (url) {
  // Get film details
  request(url, function (err, res, body) {
    if (err) {
      console.log(err);
    } else if (res.statusCode === 200) {
      const casts = JSON.parse(body).characters;
      let j = 0;
      const sortedCasts = [];
      for (const i in casts) {
        // Get Cast details
        request(casts[i], function (error, resp, body) {
          if (error) {
            console.log(error);
          } else if (resp.statusCode === 200) {
            sortedCasts.push({ name: JSON.parse(body).name, index: i });
            sortedCasts.sort((a, b) => a.index - b.index);
            if (j === casts.length - 1) {
              sortedCasts.forEach((v) => { console.log(v.name); });
            }
            j++;
          } else {
            console.log(`code: ${resp.statusCode}`);
          }
        });
      }
    } else {
      console.log(`code: ${res.statusCode}`);
    }
  });
}

getCastsByFilmID(url);
