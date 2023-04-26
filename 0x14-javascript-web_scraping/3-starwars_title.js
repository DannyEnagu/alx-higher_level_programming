#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const url = api + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const fromJson = JSON.parse(body);
    console.log(fromJson.title);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
