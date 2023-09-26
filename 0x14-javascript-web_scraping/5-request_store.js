#!/usr/bin/node
/* gets contents of a webpage and stores them in a file */
const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) throw error;

  fs.writeFile(filename, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
