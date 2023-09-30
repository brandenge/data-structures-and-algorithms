'use strict';

const LinkedList = require('../linked-list-kth/index');

class HashTable {
  constructor(size) {
    this.size = size;
    this.table = new Array(size);
  }

  set(key, value) {
    let bucket = this.table[this.hash(key)];
    if (bucket === undefined) {
      bucket = new LinkedList();
      this.table[this.hash(key)] = bucket;
    }
    bucket.insert({ [key]: value });
  }

  get(key) {
    const bucket = this.table[this.hash(key)];
    if (bucket) {
      let current = bucket.head;
      while (current) {
        const value = current.value[key];
        if (value !== undefined) return value;
        else current = current.next;
      }
    }
    return null;
  }

  has(key) {
    return this.keys().has(key);
  }

  keys() {
    const keys = new Set();
    this.table.forEach((bucket) => {
      if (bucket) {
        let current = bucket.head;
        while (current) {
          keys.add(Object.keys(current.value)[0]);
          current = current.next;
        }
      }
    });
    return keys;
  }

  hash(str) {
    const asciiSum = str.split('').reduce((sum, char) => sum + (Math.pow(char.charCodeAt(0), 2)), 0);
    return asciiSum * str.length * 86743 % this.size;
  }
}

module.exports = HashTable;
