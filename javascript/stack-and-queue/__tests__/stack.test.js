'use strict';

const { Stack } = require('../index');

describe('Tests the Stack data structure', () => {
  it('Can successfully push onto a stack', () => {
    const stack = new Stack();
    stack.push(3);
    expect(stack.top.value).toEqual(3);
  });

  it('Can successfully push multiple values onto a stack', () => {
    const stack = new Stack();
    stack.push(3);
    stack.push(2);
    stack.push(1);
    expect(stack.top.value).toEqual(1);
    expect(stack.top.next.value).toEqual(2);
    expect(stack.top.next.next.value).toEqual(3);
  });

  it('Can successfully pop off the stack', () => {
    const stack = new Stack();
    stack.push(3);
    stack.push(2);
    stack.push(1);
    stack.pop();
    expect(stack.top.value).toEqual(2);
    expect(stack.top.next.value).toEqual(3);
    expect(stack.top.next.next).toEqual(null);
  });

  it('Can successfully empty a stack after multiple pops', () => {
    const stack = new Stack();
    stack.push(3);
    stack.push(2);
    stack.push(1);
    stack.pop();
    stack.pop();
    stack.pop();
    expect(stack.top).toEqual(null);
  });

  it('Can successfully peek the next item on the stack', () => {
    const stack = new Stack();
    stack.push(3);
    stack.push(2);
    stack.push(1);
    expect(stack.peek()).toEqual(1);
    expect(stack.top.value).toEqual(1);
    expect(stack.top.next.value).toEqual(2);
    expect(stack.top.next.next.value).toEqual(3);
    expect(stack.top.next.next.next).toEqual(null);
  });

  it('Can successfully instantiate an empty stack', () => {
    const stack = new Stack();
    expect(stack.top).toEqual(null);
  });

  it('Calling pop or peek on empty stack raises exception', () => {
    const stack = new Stack();
    expect(() => stack.peek()).toThrow('The stack is empty');
    expect(() => stack.pop()).toThrow('The stack is empty');
  });
});
