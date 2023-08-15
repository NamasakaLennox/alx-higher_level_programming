#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let nb = 0;

  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      nb++;
    }
  }
  return nb;
};
