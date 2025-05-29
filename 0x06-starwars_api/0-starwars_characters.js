// #!/usr/bin/node

// const request = require('request');

// function requestCharacter (urlChar) {
//   return new Promise((resolve, reject) => {
//     request({ url: urlChar, json: true }, (error, response, body) => {
//       if (error) reject(error);
//       resolve(body);
//     });
//   });
// }

// const movieId = process.argv[2];
// const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// request({ url, json: true }, async (error, response, body) => {
//   if (error) console.log(error);
//   const film = body;
//   const characters = film.characters;
//   for (const urlChar of characters) {
//     try {
//       const charName = await requestCharacter(urlChar);
//       console.log(charName.name);
//     } catch (error) { console.log('Error fetching : ', error); }
//   }
// });
