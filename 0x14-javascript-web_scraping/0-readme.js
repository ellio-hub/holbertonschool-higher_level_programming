#!/usr/bin/node
const fs = require('fs');
const FileName = process.argv[2];
fs.readFile(FileName, 'utf8', function (r, l) {
  if (r) {
    console.log(r);
  } else {
    console.log(l);
  }
});
