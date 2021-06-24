#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (r, response, body) {
  let x = 0;
  if (r) {
    console.log(r);
  }
  const data = JSON.parse(body);
  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      x++;
    }
  }
  console.log(x);
});
