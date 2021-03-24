#!/usr/bin/node
exports.converter = function (base) {
  function myconverter (x) {
    return x.toString(base);
  }
  return myconverter;
};
