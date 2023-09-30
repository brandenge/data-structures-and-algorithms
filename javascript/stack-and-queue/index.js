'use strict';

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
  }

  push(value) {
    const node = new Node(value);
    node.next = this.top;
    this.top = node;
  }

  pop() {
    if (!this.top) throw new Error('The stack is empty');
    const temp = this.top;
    this.top = this.top.next;
    temp.next = null;
    return temp.value;
  }

  peek() {
    if (!this.top) throw new Error('The stack is empty');
    return this.top.value;
  }

  isEmpty() {
    return !this.top;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.back = null;
  }

  enqueue(value) {
    const node = new Node(value);
    if (!this.back) this.back = node;
    else {
      this.back.next = node;
      this.back = node;
    }
    if (!this.front) this.front = node;
  }

  dequeue() {
    if (!this.front) throw new Error('The queue is empty');
    const temp = this.front;
    this.front = this.front.next;
    if (this.front === null) this.back = null;
    temp.next = null;
    return temp.value;
  }

  peek() {
    if (!this.front) throw new Error('The queue is empty');
    return this.front.value;
  }

  isEmpty() {
    return this.front === null;
  }
}

module.exports = { Stack, Queue };
