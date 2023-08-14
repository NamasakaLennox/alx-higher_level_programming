#!/usr/bin/node

const process = require('process');
let num = parseInt(process.argv[2]);

if (!num) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
