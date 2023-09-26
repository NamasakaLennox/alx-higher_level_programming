#!/usr/bin/node
/* displays the status code of a get request */
const argv = process.argv;
const request = require('request');

request(argv[2], (err, resp, body) => {
  if (err) throw err;

  console.log('code: ' + resp.statusCode);
});
