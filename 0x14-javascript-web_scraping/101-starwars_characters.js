#!/usr/bin/node
/* prints all characters of a star wars movie */
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) throw error;

  const characters = JSON.parse(body).characters;
  /* request each character retrived */
  const requests = characters.map((charUrl) => {
    return new Promise((resolve, reject) => {
      request(charUrl, (err, resp, bodyChar) => {
        if (err) { reject(err); }

        resolve(bodyChar);
      });
    });
  });
  Promise.all(requests).then((res) => {
    res.forEach((bodyChar) => {
      if (bodyChar) {
        console.log(JSON.parse(bodyChar).name);
      }
    });
  }).catch((err) => console.log(err));
});
