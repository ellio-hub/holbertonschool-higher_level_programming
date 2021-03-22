#!/usr/bin/node
let i;
process.argv.forEach((val, index) => {
  i = index;
});
if (i <= 1) {
  console.log('No argument');
} else if (i === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
