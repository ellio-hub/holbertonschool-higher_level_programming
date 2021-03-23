#!/usr/bin/node
const a = process.argv[2];
if (!(a / 2)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < a; i++) {
    console.log('C is fun');
  }
}
