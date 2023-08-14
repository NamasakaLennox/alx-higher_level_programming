#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  console.log(a + b);
}

add(parseInt(args[2]), parseInt(args[3]));
