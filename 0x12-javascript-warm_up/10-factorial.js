#!/usr/bin/node

const process = require('process');
const num = parseInt(process.argv[2]);

function factorial (a) {
  if ((!a) || (a < 2)) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(num));
