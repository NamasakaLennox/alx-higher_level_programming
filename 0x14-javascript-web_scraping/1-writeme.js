#!/usr/bin/node
/* writes a text into a file */
const argv = process.argv;
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) throw err;
});
