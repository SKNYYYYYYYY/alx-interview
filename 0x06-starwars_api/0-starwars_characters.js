#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./get_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request({ url, json: true }, (err, res, body) => {
      if (err) return reject(err);
      resolve(body.name);
    });
  });
}

request({ url: filmUrl, json: true }, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = body.characters;

  for (const url of characters) {
    try {
      const name = await fetchCharacter(url);
      console.log(name);
    } catch (err) {
      console.error('Failed to fetch character:', err);
    }
  }
});
