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
}

class PseudoQueue {
  constructor() {
    this.front = null;
    this.back = null;
  }

  enqueue(value) {
    const stack = new Stack();
    if (this.back) {
      stack.top = this.back;
      stack.push(value);
      this.back = stack.top;
    } else {
      this.back = new Node(value);
      this.front = this.back;
    }
  }

  dequeue() {
    if (!this.back) return;
    const stack = new Stack();
    const tempStack = new Stack();
    stack.top = this.back;
    while (stack.top) {
      tempStack.push(stack.pop());
    }
    const popped = tempStack.pop();
    this.front = tempStack.top;
    while (tempStack.top) {
      stack.push(tempStack.pop());
    }
    this.back = stack.top;
    return popped;
  }
}

module.exports = PseudoQueue;
