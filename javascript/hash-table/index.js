'use strict';

const LinkedList = require('../linked-list-kth/index');

class HashTable {
  constructor(size) {
    this.size = size;
    this.table = [];
  }

  set(key, value) {
    const index = this.hash(key);
    if (this.table[index] === null) {
      const newBucket = new LinkedList();
      newBucket.head = { key: value };
      this.table[index] = newBucket;
    }
  }

  get(key) {

  }

  has(key) {

  }

  keys() {

  }

  hash(str) {
    str.split('').map((char, i) => char )
  }
}
