'use strict';

const { Queue } = require('../index');

describe('Tests the Queue data structure', () => {
  it('Can successfully enqueue into a queue', () => {
    const queue = new Queue();
    queue.enqueue(1);
    expect(queue.back).not.toEqual(null);
    expect(queue.front).not.toEqual(null);
    expect(queue.back.value).toEqual(1);
    expect(queue.front.value).toEqual(1);
  });

  it('Can successfully enqueue multiple values into a queue', () => {
    const queue = new Queue();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    expect(queue.front.value).toEqual(1);
    expect(queue.front.next.value).toEqual(2);
    expect(queue.front.next.next.value).toEqual(3);
    expect(queue.back.value).toEqual(3);
    expect(queue.back.next).toEqual(null);
  });

  it('Can successfully dequeue out of a queue the expected value', () => {
    const queue = new Queue();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    expect(queue.front.value).toEqual(1);
    expect(queue.back.value).toEqual(3);
    queue.dequeue();
    expect(queue.front.value).toEqual(2);
    queue.dequeue();
    expect(queue.front.value).toEqual(3);
  });

  it('Can successfully peek into a queue, seeing the expected value', () => {
    const queue = new Queue();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    expect(queue.peek()).toEqual(1);
  });

  it('Can successfully empty a queue after multiple dequeues', () => {
    const queue = new Queue();
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.dequeue();
    queue.dequeue();
    queue.dequeue();
    expect(queue.isEmpty()).toEqual(true);
  });

  it('Can successfully instantiate an empty queue', () => {
    const queue = new Queue();
    expect(queue.front).toEqual(null);
  });

  it('Calling dequeue or peek on empty queue raises exception', () => {
    const queue = new Queue();
    expect(() => queue.peek()).toThrow('The queue is empty');
    expect(() => queue.dequeue()).toThrow('The queue is empty');
  });
});
