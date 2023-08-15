#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;
  const temp = [];
  for (let i = len; i >= 0; i--) {
    temp.push(list[i]);
  }
  return (list = temp);
};
