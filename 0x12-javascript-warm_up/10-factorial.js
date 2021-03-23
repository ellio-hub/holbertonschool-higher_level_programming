#!/usr/bin/node
function factorialize (num) {
  let c = 1;
  let i;
  for (i = 1; i <= num; i++) {
    c *= i;
  }
  return (c);
}
console.log(factorialize(parseInt(process.argv[2])));
