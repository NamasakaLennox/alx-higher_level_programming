#!/usr/bin/node
/* computes the number of tasks completed by a user */
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) throw error;

  const content = JSON.parse(body);
  const dict = {};
  for (let id = 1; id <= 10; id++) {
    let count = 0;
    content.forEach((item) => {
      if (item.userId === id && item.completed) {
        count++;
      }
    });
    if (count > 0) {
      dict[id] = count;
    }
  }
  console.log(dict);
});
