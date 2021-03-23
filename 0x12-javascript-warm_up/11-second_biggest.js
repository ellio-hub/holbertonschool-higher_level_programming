#!/usr/bin/node
function secbig (arr) {
  let b = 0;
  let res = 0;
  for (const value of arr) {
    const n = Number(value);
    if (n > b) {
      [res, b] = [b, n];
    } else if (n < b && n > res) {
      res = n;
    }
  }
  return res;
}
console.log(secbig(process.argv));
