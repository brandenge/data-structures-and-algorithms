'use strict';

const repeatedWord = require('../index');

describe('Tests for the repeatedWord function', () => {
  it('Should return a single letter word from a partial sentence text', () => {
    const text = 'Once upon a time, there was a brave princess who...';
    expect(repeatedWord(text)).toEqual('a');
  });

  it('Should be case insensitive as to what counts as a repeated word', () => {
    const text = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...';
    expect(repeatedWord(text)).toEqual('it');
  });

  it('Should return a longer word from a text', () => {
    const text = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...';
    expect(repeatedWord(text)).toEqual('summer');
  });

  it('Should return null if there are no repeated words', () => {
    const text = 'It is a New Age today';
    expect(repeatedWord(text)).toEqual(null);
  });
});
