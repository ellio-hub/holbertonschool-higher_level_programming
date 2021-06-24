#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (r, response, body) {
  if (r) {
    console.log(r);
  } else {
    const p = JSON.parse(body);
    const completed = {};
    for (const x of p) {
      if (x.completed === true) {
        if (x.userId in completed) {
          completed[x.userId]++;
        } else {
          completed[x.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
