#!/usr/bin/node
/* prints all characters of a star wars movie */
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) throw error;

  const characters = JSON.parse(body).characters;
  /* request each character retrived */
  characters.forEach((charUrl) => {
    request(charUrl, (err, resp, bodyChar) => {
      if (err) throw err;

      console.log(JSON.parse(bodyChar).name);
    });
  });
});
