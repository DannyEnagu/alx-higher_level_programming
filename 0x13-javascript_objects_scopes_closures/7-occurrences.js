#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurance = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurance += 1;
    }
  }
  return occurance;
};
