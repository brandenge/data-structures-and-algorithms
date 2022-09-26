'use strict';

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
  }

  insert(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    if (this.head !== null) this.head.prev = newNode;
    this.head = newNode;
  }

  includes(value) {
    let currentNode = this.head;
    while (currentNode !== null) {
      if (currentNode.value === value) return true;
      currentNode = currentNode.next;
    }
    return false;
  }

  toString() {
    let currentNode = this.head;
    let output = 'NULL';
    while (currentNode !== null) {
      output += ` <- { ${currentNode.value} } -> `;
      currentNode = currentNode.next;
    }
    output += 'NULL';
    return output;
  }
}

module.exports = DoublyLinkedList;
