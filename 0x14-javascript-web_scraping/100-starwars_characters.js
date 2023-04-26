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
      casts.forEach(cast => {
        // Get Cast details
        request(cast, function (error, resp, body) {
          if (error) {
            console.log(error);
          } else if (resp.statusCode === 200) {
            console.log(JSON.parse(body).name);
          } else {
            console.log(`code: ${resp.statusCode}`);
          }
        });
      });
    } else {
      console.log(`code: ${res.statusCode}`);
    }
  });
}

getCastsByFilmID(url);
