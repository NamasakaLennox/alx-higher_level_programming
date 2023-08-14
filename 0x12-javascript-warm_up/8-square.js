#!/usr/bin/node

const process = require('process');
const num = parseInt(process.argv[2]);

if (!num) {
  console.log('Missing size');
} else {
  let str = '';
  for (let j = num; j > 0; j--) {
    str += 'X';
  }
  for (let i = num; i > 0; i--) {
    console.log(str);
  }
}
