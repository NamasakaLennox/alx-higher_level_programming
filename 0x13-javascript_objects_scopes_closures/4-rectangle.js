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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
