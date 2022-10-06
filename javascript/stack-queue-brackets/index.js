'use strict';

function validateBrackets(str) {
  if (str.length === 0 || !/[[\](){}]/.test(str)) return false;
  let square = 0;
  let round = 0;
  let curly = 0;
  str = str.replace(/[^[\]{}()]/g, '');
  for (let i = 0, len = str.length; i < len; i++) {
    if (str[i] === '[') square++;
    else if (str[i] === '(') round++;
    else if (str[i] === '{') curly++;
    else if (str[i] === ']') square--;
    else if (str[i] === ')') round--;
    else if (str[i] === '}') curly--;
    if (square < 0 || round < 0 || curly < 0) return false;
  }
  if (square > 0 || round > 0 || curly > 0) return false;
  return true;
}

module.exports = validateBrackets;
