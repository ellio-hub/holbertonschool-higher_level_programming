#!/usr/bin/node
/* using API to print the title film  */
const request = require('request');
const url = process.argv[2];
request.get(url, (error, res, body) => {
  if (error) console.log(error);
  const result = JSON.parse(res.body);
  const nbFound = result.results.reduce((x, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? x + 1
      : x;
  }, 0);
  console.log(nbFound);
});
