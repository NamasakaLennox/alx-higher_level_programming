#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
const len = args.length;

if (len <= 1) {
  console.log(0);
} else {
  const arr = args.map(function (num) {
    return (Number(num));
  });
  arr.sort();
  console.log(arr[len - 2]);
}
