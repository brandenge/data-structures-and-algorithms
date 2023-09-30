'use strict';

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.count = 0;
  }

  insert(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    if (this.tail === null) this.tail = newNode;
    this.count += 1;
  }

  append(value) {
    const newNode = new Node(value);
    if (this.tail !== null) {
      this.tail.next = newNode;
    } else {
      this.head = newNode;
    }
    this.tail = newNode;
    this.count += 1;
  }

  insertBefore(beforeValue, insertValue) {
    const newNode = new Node(insertValue);
    if (this.head === null) {
      throw new Error(`Error in insertBefore() - the beforeValue argument of: ${beforeValue} is not found in the linked list because the linked list is empty`);
    }
    if (this.head.value === beforeValue) {
      newNode.next = this.head;
      this.head = newNode;
      this.count += 1;
      return;
    }
    let current = this.head;
    while (current.next !== null) {
      if (current.next.value === beforeValue) {
        newNode.next = current.next;
        current.next = newNode;
        this.count += 1;
        return;
      } else {
        current = current.next;
      }
    }
    throw new Error(`Error in insertBefore() - the beforeValue argument of: ${beforeValue} is not found in the linked list`);
  }

  insertAfter(afterValue, insertValue) {
    const newNode = new Node(insertValue);
    if (this.head === null) {
      throw new Error(`Error in insertAfter() - the afterValue argument of: ${afterValue} is not found in the linked list because the linked list is empty`);
    }
    if (this.head.value === afterValue) {
      newNode.next = this.head.next;
      this.head.next = newNode;
      if (newNode.next === null) this.tail = newNode;
      this.count += 1;
      return;
    }
    let current = this.head;
    while (current.next !== null) {
      if (current.value === afterValue) {
        newNode.next = current.next;
        current.next = newNode;
        this.count += 1;
        return;
      } else {
        current = current.next;
      }
    }
    if (current.value === afterValue) {
      current.next = newNode;
      this.tail = newNode;
    } else {
      throw new Error(`Error in insertAfter() - the afterValue argument of: ${afterValue} is not found in the linked list`);
    }
  }

  delete(value) {
    if (this.head === null) return;
    if (this.head.value === value) {
      if (this.tail === this.head) this.tail = this.head.next;
      this.head = this.head.next;
      this.count -= 1;
      return;
    }
    let current = this.head;
    while (current.next !== null) {
      if (current.next.value === value) {
        current.next = current.next.next;
        if (current.next === null) this.tail = current;
        this.count -= 1;
        return;
      } else {
        current = current.next;
      }
    }
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
    let output = '';
    while (currentNode !== null) {
      output += `{ ${currentNode.value} } -> `;
      currentNode = currentNode.next;
    }
    output += 'NULL';
    return output;
  }

  kthFromEnd(k) {
    if (k >= this.count || k < 0) {
      throw new Error(`Error in kthFromEnd() - the argument of ${k} must be a positive integer that is less than the total number of nodes in the linked list, which has a current count of: ${this.count}`);
    }
    let currentNode = this.head;
    for (let i = 1, count = this.count - k; i < count; i++) {
      currentNode = currentNode.next;
    }
    return currentNode.value;
  }

  getMiddleNodeValue() {
    if (this.head === null) {
      throw new Error('Error in getMiddleNodeValue() - the linked list is empty');
    }
    let currentNode = this.head;
    for (let i = 1, count = Math.ceil(this.count / 2); i < count; i++) {
      currentNode = currentNode.next;
    }
    return currentNode.value;
  }
}

module.exports = LinkedList;
