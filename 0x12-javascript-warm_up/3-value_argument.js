#!/usr/bin/node

const process = require('process');
const len = process.argv.length;

if (len <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
