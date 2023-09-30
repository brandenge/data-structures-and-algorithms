'use strict';

const { Animal, AnimalShelter } = require('../index');

describe('Tests the AnimalShelter enqueue method', () => {
  it('Successfully initializes an empty AnimalShelter', () => {
    const animalShelter = new AnimalShelter();
    expect(animalShelter.front === null);
    expect(animalShelter.back === null);
  });

  it('Successfully enqueues a node to an empty queue', () => {
    const animalShelter = new AnimalShelter();
    const animal = new Animal('cat');
    animalShelter.enqueue(animal);
    expect(animalShelter.front.type === 'cat');
    expect(animalShelter.back.type === 'cat');
    expect(animalShelter.front.next === null);
    expect(animalShelter.back.next === null);
  });

  it('Successfully enqueues a node to the back of a queue with only 1 node in it', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    const animal2 = new Animal('dog');
    animalShelter.enqueue(animal1);
    animalShelter.enqueue(animal2);
    expect(animalShelter.front.type === 'cat');
    expect(animalShelter.back.type === 'dog');
    expect(animalShelter.front.next === 'dog');
    expect(animalShelter.back.next === null);
  });

  it('Successfully enqueues a node to the back of a queue with 2 or more nodes in it', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    const animal2 = new Animal('dog');
    const animal3 = new Animal('cat');
    animalShelter.enqueue(animal1);
    animalShelter.enqueue(animal2);
    animalShelter.enqueue(animal3);
    expect(animalShelter.front.type === 'cat');
    expect(animalShelter.back.type === 'cat');
    expect(animalShelter.front.next.type === 'dog');
    expect(animalShelter.front.next.next.type === 'cat');
    expect(animalShelter.back.next === null);
  });

  it('Does not throw an error when dequeueing an empty queue', () => {
    const animalShelter = new AnimalShelter();
    expect(() => animalShelter.dequeue('cat')).not.toThrow(expect.anything());
  });

  it('Returns null when dequeueing an empty queue', () => {
    const animalShelter = new AnimalShelter();
    expect(animalShelter.dequeue()).toEqual(null);
    expect(animalShelter.front).toEqual(null);
    expect(animalShelter.back).toEqual(null);
  });

  it('Returns null without any side effects if the animal argument provided to dequeue is not a cat or dog', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    animalShelter.enqueue(animal1);
    expect(animalShelter.front.type).toEqual('cat');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next).toEqual(null);
    expect(animalShelter.back.next).toEqual(null);
    expect(animalShelter.dequeue('turtle')).toEqual(null);
    expect(animalShelter.front.type).toEqual('cat');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next).toEqual(null);
    expect(animalShelter.back.next).toEqual(null);
  });

  it('Successfully dequeues a node from the front of a queue with only 1 node in it', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    animalShelter.enqueue(animal1);
    expect(animalShelter.dequeue('cat').type).toEqual('cat');
    expect(animalShelter.front).toEqual(null);
    expect(animalShelter.back).toEqual(null);
  });

  it('Returns null when dequeueing a dog without any dogs within the queue', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    animalShelter.enqueue(animal1);
    expect(animalShelter.dequeue('dog')).toEqual(null);
    expect(animalShelter.front.type).toEqual('cat');
    expect(animalShelter.back.type).toEqual('cat');
  });

  it('Successfully dequeues a node from the front of a queue with 2 or more nodes in it', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    const animal2 = new Animal('dog');
    const animal3 = new Animal('cat');
    animalShelter.enqueue(animal1);
    animalShelter.enqueue(animal2);
    animalShelter.enqueue(animal3);
    animalShelter.dequeue('cat');
    animalShelter.dequeue('dog');
    expect(animalShelter.front.type).toEqual('cat');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next).toEqual(null);
    expect(animalShelter.back.next).toEqual(null);
  });

  it('Successfully dequeues only the oldest node of the given preference argument, even if it is not at the front', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    const animal2 = new Animal('dog');
    const animal3 = new Animal('cat');
    animalShelter.enqueue(animal1);
    animalShelter.enqueue(animal2);
    animalShelter.enqueue(animal3);
    expect(animalShelter.dequeue('dog').type).toEqual('dog');
    expect(animalShelter.front.type).toEqual('cat');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next.type).toEqual('cat');
    expect(animalShelter.back.next).toEqual(null);
  });

  it('Successfully enqueues and dequeues multiple times with the same number of times each', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    const animal2 = new Animal('dog');
    const animal3 = new Animal('cat');
    animalShelter.enqueue(animal1);
    animalShelter.enqueue(animal2);
    animalShelter.enqueue(animal3);
    animalShelter.dequeue('cat');
    expect(animalShelter.front.type).toEqual('dog');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next.type).toEqual('cat');
    expect(animalShelter.back.next).toEqual(null);
    animalShelter.dequeue('dog');
    expect(animalShelter.front.type).toEqual('cat');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next).toEqual(null);
    expect(animalShelter.back.next).toEqual(null);
    animalShelter.dequeue('cat');
    expect(animalShelter.front).toEqual(null);
    expect(animalShelter.back).toEqual(null);
  });

  it('Successfully enqueues and dequeues multiple times each, but a different number of times', () => {
    const animalShelter = new AnimalShelter();
    const animal1 = new Animal('cat');
    const animal2 = new Animal('dog');
    const animal3 = new Animal('cat');
    animalShelter.enqueue(animal1);
    animalShelter.enqueue(animal2);
    animalShelter.enqueue(animal3);
    animalShelter.dequeue('cat');
    expect(animalShelter.front.type).toEqual('dog');
    expect(animalShelter.back.type).toEqual('cat');
    expect(animalShelter.front.next.type).toEqual('cat');
    expect(animalShelter.back.next).toEqual(null);
    animalShelter.dequeue('cat');
    expect(animalShelter.front.type).toEqual('dog');
    expect(animalShelter.back.type).toEqual('dog');
    expect(animalShelter.front.next).toEqual(null);
    expect(animalShelter.back.next).toEqual(null);
  });
});
