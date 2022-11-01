'use strict';

function repeatedWord(text) {
  const wordCounts = {};
  const words = text.toLowerCase().replace(/[^a-z ]/g, '').split(' ');
  for (const word of words) {
    if (wordCounts[word]) return word;
    else wordCounts[word] = 1;
  }
  return null;
}

module.exports = repeatedWord;
