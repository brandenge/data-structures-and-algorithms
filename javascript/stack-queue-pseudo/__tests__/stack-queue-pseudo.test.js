'use strict';

const PseudoQueue = require('../index');

describe('Testing the pseudoQueue class', () => {
  it('Can successfully instantiate', () => {
    const pseudoQueue = new PseudoQueue();
    expect(pseudoQueue.front).toEqual(null);
    expect(pseudoQueue.back).toEqual(null);
  });

  it('Can successfully enqueue 1 value', () => {
    const pseudoQueue = new PseudoQueue();
    pseudoQueue.enqueue(1);
    expect(pseudoQueue.front.value).toEqual(1);
    expect(pseudoQueue.back.value).toEqual(1);
    expect(pseudoQueue.front.next).toEqual(null);
    expect(pseudoQueue.back.next).toEqual(null);
  });

  it('Can successfully enqueue 2 values', () => {
    const pseudoQueue = new PseudoQueue();
    pseudoQueue.enqueue(1);
    pseudoQueue.enqueue(2);
    expect(pseudoQueue.front.value).toEqual(1);
    expect(pseudoQueue.back.value).toEqual(2);
    expect(pseudoQueue.front.next).toEqual(null);
    expect(pseudoQueue.back.next.value).toEqual(1);
  });

  it('Can successfully enqueue more than 2 values', () => {
    const pseudoQueue = new PseudoQueue();
    pseudoQueue.enqueue(1);
    pseudoQueue.enqueue(2);
    pseudoQueue.enqueue(3);
    expect(pseudoQueue.front.value).toEqual(1);
    expect(pseudoQueue.back.value).toEqual(3);
    expect(pseudoQueue.front.next).toEqual(null);
    expect(pseudoQueue.back.next.value).toEqual(2);
    expect(pseudoQueue.back.next.next.value).toEqual(1);
  });

  it('Does not throw an error when dequeueing an empty pseudoQueue', () => {
    const pseudoQueue = new PseudoQueue();
    expect(() => pseudoQueue.dequeue()).not.toThrow(expect.anything());
  });

  it('Can successfully dequeue 1 value', () => {
    const pseudoQueue = new PseudoQueue();
    pseudoQueue.enqueue(1);
    expect(pseudoQueue.dequeue()).toEqual(1);
    expect(pseudoQueue.front).toEqual(null);
    expect(pseudoQueue.back).toEqual(null);
  });

  it('Can successfully dequeue 2 values', () => {
    const pseudoQueue = new PseudoQueue();
    pseudoQueue.enqueue(1);
    pseudoQueue.enqueue(2);
    expect(pseudoQueue.dequeue()).toEqual(1);
    expect(pseudoQueue.front.value).toEqual(2);
    expect(pseudoQueue.back.value).toEqual(2);
    expect(pseudoQueue.front.next).toEqual(null);
    expect(pseudoQueue.back.next).toEqual(null);
    expect(pseudoQueue.dequeue()).toEqual(2);
    expect(pseudoQueue.front).toEqual(null);
    expect(pseudoQueue.back).toEqual(null);
  });

  it('Can successfully dequeue more than 2 values', () => {
    const pseudoQueue = new PseudoQueue();
    pseudoQueue.enqueue(1);
    pseudoQueue.enqueue(2);
    pseudoQueue.enqueue(3);
    expect(pseudoQueue.dequeue()).toEqual(1);
    expect(pseudoQueue.front.value).toEqual(2);
    expect(pseudoQueue.back.value).toEqual(3);
    expect(pseudoQueue.front.next).toEqual(null);
    expect(pseudoQueue.back.next.value).toEqual(2);
    expect(pseudoQueue.back.next.next).toEqual(null);
    expect(pseudoQueue.dequeue()).toEqual(2);
    expect(pseudoQueue.front.value).toEqual(3);
    expect(pseudoQueue.back.value).toEqual(3);
    expect(pseudoQueue.front.next).toEqual(null);
    expect(pseudoQueue.back.next).toEqual(null);
    expect(pseudoQueue.dequeue()).toEqual(3);
    expect(pseudoQueue.front).toEqual(null);
    expect(pseudoQueue.back).toEqual(null);
  });
});
