'use strict';

// Require our linked list implementation
const LinkedList = require('../index');

describe('Linked List', () => {

  it('Instantiates an empty linked list', () => {
    const linkedList = new LinkedList();
    expect(linkedList.head).toEqual(null);
  });

  it('Inserts a new node at the head of the linked list.', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    expect(linkedList.head.value).toEqual(1);
  });

  it('The head property always points to the first node of the linked list.', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    expect(linkedList.head.value).toEqual(2);
  });

  it('Can insert multiple nodes into the linked list.', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.head.value).toEqual(3);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next.value).toEqual(1);
  });

  it('Will return true when finding a value within the linked list that exists.', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.includes(1)).toEqual(true);
    expect(linkedList.includes(2)).toEqual(true);
    expect(linkedList.includes(3)).toEqual(true);
  });

  it('Will return false when searching for a value in the linked list that does not exist.', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.includes(4)).toEqual(false);
  });

  it('Can properly return a collection of all the values that exist in the linked list (returned as a string).', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.toString()).toEqual(`{ 3 } -> { 2 } -> { 1 } -> NULL`);
  });
});
