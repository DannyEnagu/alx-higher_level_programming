#!/usr/bin/nodeconst
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c = 'X') {
    const size = this.height;

    if (size) {
      for (let i = 0; i < size; i++) {
        let rows = '';
        for (let j = 0; j < size; j++) {
          rows += c;
        }
        console.log(rows);
      }
    }
  }
}
module.exports = Square;
