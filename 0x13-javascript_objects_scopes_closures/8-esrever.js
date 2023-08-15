#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;

  if (len > 0) {
    const list2 = [];
    for (let i = len - 1; i >= 0; i--) {
      list2.push(list[i]);
    }
    return list2;
  }
};
