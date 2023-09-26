#!/usr/bin/node
/* reads contents of a file and displays them */
const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) throw err;

  console.log(data.toString());
});
