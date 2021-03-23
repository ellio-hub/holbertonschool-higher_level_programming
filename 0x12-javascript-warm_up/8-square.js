#!/usr/bin/node
const a = process.argv[2];
let h = '';
let i;
if (!(a / 2)) {
  console.log('Missing size');
} else {
  for (i = 0; i < a; i++) {
    h += 'X';
  }
  for (i = 0; i < a; i++) {
    console.log(h);
  }
}
