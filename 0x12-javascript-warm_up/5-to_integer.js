#!/usr/bin/node
let a = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    a = val;
  }
});
if (!(a / 2)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(a));
}
