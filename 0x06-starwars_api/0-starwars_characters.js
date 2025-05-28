#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request({ url, json: true }, (error, response, body) => {
  if (error) console.log(error);
  const characters = body.characters;
  for (const urlChar of characters) {
    request({ url: urlChar, json: true }, (error, response, body) => {
      if (error) console.log(error);
      console.log(body.name);
    });
  }
});
