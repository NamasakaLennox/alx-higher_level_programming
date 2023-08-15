#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  /* prints the rectangle to the console */
  print () {
    let string = '';
    for (let i = 0; i < this.width; i++) {
      string += 'X';
    }

    for (let j = 0; j < this.height; j++) {
      console.log(string);
    }
  }
}

module.exports = Rectangle;
