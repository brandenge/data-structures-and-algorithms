'use strict';

const HashTable = require("../index");

describe('Tests for the HashTable class', () => {
  test('Setting a key/value to your hashtable results in the value being in the data structure', () => {
    const hashTable = new HashTable(5);
    hashTable.set('a', 1);
    expect(hashTable.table[hashTable.hash('a')].head.value['a']).toEqual(1);
    expect(hashTable.has('a')).toEqual(true);
  });

  test('Retrieving based on a key returns the value stored', () => {
    const hashTable = new HashTable(5);
    hashTable.set('a', 1);
    expect(hashTable.get('a')).toEqual(1);
  });

  test('Successfully returns null for a key that does not exist in the hashtable', () => {
    const hashTable = new HashTable(5);
    hashTable.set('a', 1);
    expect(hashTable.get('b')).toEqual(null);
  });

  test('Successfully returns a list of all unique keys that exist in the hashtable', () => {
    const hashTable = new HashTable(5);
    hashTable.set('a', 1);
    expect(hashTable.get('b')).toEqual(null);
  });

  test('Successfully handle a collision within the hashtable', () => {
    const hashTable = new HashTable(1);
    hashTable.set('a', 1);
    hashTable.set('b', 2);
    expect(hashTable.keys().has('b')).toEqual(true);
  });

  test('Successfully retrieve a value from a bucket within the hashtable that has a collision', () => {
    const hashTable = new HashTable(1);
    hashTable.set('a', 1);
    hashTable.set('b', 2);
    expect(hashTable.get('b')).toEqual(2);
  });

  test('Successfully hash a key to an in-range value', () => {
    const hashTable = new HashTable(5);
    expect(hashTable.hash('a')).toBeGreaterThan(-1);
    expect(hashTable.hash('a')).toBeLessThan(5);
  });
});
