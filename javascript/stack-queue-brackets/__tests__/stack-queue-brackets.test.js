'use strict';

const validateBrackets = require('../index');

describe('tests the validatesBrackets function', () => {
  it('returns false when given an empty string', () => {
    expect(validateBrackets('')).toEqual(false);
  });

  it('returns false when given a string with no brackets', () => {
    expect(validateBrackets('abcde')).toEqual(false);
  });

  it('returns true when given a string with a single set of balanced brackets', () => {
    expect(validateBrackets('[]')).toEqual(true);
  });

  it('correctly tests all 3 types of brackets - square, round, and curly', () => {
    expect(validateBrackets('[]{}()')).toEqual(true);
  });

  it('returns true when given a string with a single set of balanced brackets and other characters mixed in', () => {
    expect(validateBrackets('1[2]3(a)b{c}!')).toEqual(true);
  });

  it('returns true when given a string with a single set of balanced brackets and other characters mixed in', () => {
    expect(validateBrackets('1[2]3(a)b{c}!')).toEqual(true);
  });

  it('returns false when given a string with a different number of opening and closing brackets', () => {
    expect(validateBrackets('[[[]]')).toEqual(false);
  });

  it('returns false when given a string with the same number of opening and closing brackets, but in the incorrect order (i.e. with improper nesting)', () => {
    expect(validateBrackets('[[]]][')).toEqual(false);
  });
});
