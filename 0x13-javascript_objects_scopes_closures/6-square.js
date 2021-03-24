#!/usr/bin/node
const x = require('./5-square');
module.exports = class Square extends x {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    let x ='';
    if (c === undefined) {
      c = 'X';
    }
    for(let i = 0; i < this.width; i++){
      x += c;
    }
    for(let i = 0; i < this.width; i++){
      console.log(x);
    }
  }
};
