#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let c = '';
    let i;
    for (i = 0; i < this.width; i++) {
      c += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(c);
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
