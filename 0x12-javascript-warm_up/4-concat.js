#!/usr/bin/node
const i = ' is ';
let a = 'undefined';
let b = 'undefined';
process.argv.forEach((val, index) => {
  if (index === 2) {
    a = val;
  }
  if (index === 3) {
    b = val;
  }
});
console.log(a + i + b);
