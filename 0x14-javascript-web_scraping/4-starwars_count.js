#!/usr/bin/node
/* Write a script that prints the number of movies where the character
   “Wedge Antilles” is present. */
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) throw error;

  const results = JSON.parse(body).results;
  let count = 0;
  results.forEach((result) => {
    const characters = result.characters;
    characters.forEach((character) => {
      if (character.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
