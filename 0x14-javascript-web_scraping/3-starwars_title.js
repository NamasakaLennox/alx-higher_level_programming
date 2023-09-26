#!/usr/bin/node
/* prints the title of a Star Wars movie given an episode number */
const argv = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) throw error;

  const title = JSON.parse(body).title;
  console.log(title);
});
