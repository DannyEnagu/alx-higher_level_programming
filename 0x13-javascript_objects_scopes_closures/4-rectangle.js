#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const height = this.height;
    const width = this.width;

    if (height && width) {
      for (let i = 0; i < height; i++) {
        let rows = '';
        for (let j = 0; j < width; j++) {
          rows += 'X';
        }
        console.log(rows);
      }
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
module.exports = Rectangle;
