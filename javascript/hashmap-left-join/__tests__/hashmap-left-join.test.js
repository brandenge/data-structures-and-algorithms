'use strict';

const HashMap = require('../../hash-table/index');
const hashMapLeftJoin = require('../index');

describe('Tests for the function hashMapLeftJoin', () => {
  const hashMap1 = new HashMap(1024);
  hashMap1.set('diligent', 'employed');
  hashMap1.set('fond', 'enamored');
  hashMap1.set('guide', 'usher');
  hashMap1.set('outfit', 'garb');
  hashMap1.set('wrath', 'anger');

  const hashMap2 = new HashMap(1024);
  hashMap2.set('diligent', 'idle');
  hashMap2.set('fond', 'averse');
  hashMap2.set('guide', 'follow');
  hashMap2.set('flow', 'jam');
  hashMap2.set('wrath', 'delight');

  const emptyHashMap = new HashMap(1024);

  it('Returns an empty array if the first hashmap is empty', () => {
    const actual = hashMapLeftJoin(emptyHashMap, hashMap2);
    const expected = [];
    console.log('actual1', actual);
    expect(actual).toEqual(expected);
  });

  it('Returns the first hashMap key and values with null appended to the end if the second hashMap is empty', () => {
    const actual = hashMapLeftJoin(hashMap1, emptyHashMap);
    const expected = [
      ['wrath', 'anger', null],
      ['diligent', 'employed', null],
      ['guide', 'usher', null],
      ['outfit', 'garb', null],
      ['fond', 'enamored', null],
    ];
    console.log('actual2', actual);
    expect(actual).toEqual(expected);
  });

  it('Returns the correct left join when the first hashMap and second hashMap have different keys', () => {
    const actual = hashMapLeftJoin(hashMap1, hashMap2);
    const expected = [
      ['wrath', 'anger', 'delight'],
      ['diligent', 'employed', 'idle'],
      ['guide', 'usher', 'follow'],
      ['outfit', 'garb', null],
      ['fond', 'enamored', 'averse'],
    ];
    console.log('actual3', actual);
    expect(actual).toEqual(expected);
  });
});
