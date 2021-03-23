#!/usr/bin/node
let i;
process.argv.forEach((val, index) => {
  i = index;
  if (index === 2) {
    console.log(`${val}`);
  }
});
if (i < 2) {
  console.log('No argument');
}
