'use strict';

// Require our linked list implementation
const LinkedList = require('../index');

describe('Linked List', () => {

  it('Instantiates an empty linked list', () => {
    const linkedList = new LinkedList();
    expect(linkedList.head).toEqual(null);
  });

  it('Inserts a new node at the head of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    expect(linkedList.head.value).toEqual(1);
  });

  it('The head property always points to the first node of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    expect(linkedList.head.value).toEqual(2);
  });

  it('Can insert multiple nodes into the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.head.value).toEqual(3);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next.value).toEqual(1);
  });

  it('Will return true when finding a value within the linked list that exists', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.includes(1)).toEqual(true);
    expect(linkedList.includes(2)).toEqual(true);
    expect(linkedList.includes(3)).toEqual(true);
  });

  it('Will return false when searching for a value in the linked list that does not exist', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.includes(4)).toEqual(false);
  });

  it('Can properly return a collection of all the values that exist in the linked list (returned as a string)', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);
    expect(linkedList.toString()).toEqual(`{ 3 } -> { 2 } -> { 1 } -> NULL`);
  });

  it('Can add a node to the end of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.append(1);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(1);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Can add multiple nodes to the end of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.append(1);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.tail.value).toEqual(1);
    linkedList.append(2);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.tail.value).toEqual(2);
    linkedList.append(3);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.next.value).toEqual(3);
    expect(linkedList.tail.value).toEqual(3);
  });

  it('Can insert a node before the first node in the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(2);
    linkedList.insertBefore(2, 1);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(2);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Can insert a node before a node located in the middle of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(3);
    linkedList.insertBefore(3, 1);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(3);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(3);
    expect(linkedList.tail.next).toEqual(null);
    linkedList.insertBefore(3, 2);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next.value).toEqual(3);
    expect(linkedList.head.next.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(3);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Can insert a node after the last node of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insertAfter(1, 2);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(2);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Can insert a node after a node in the middle of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    linkedList.insertAfter(1, 3);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(3);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(3);
    expect(linkedList.tail.next).toEqual(null);
    linkedList.insertAfter(1, 2);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next.value).toEqual(3);
    expect(linkedList.head.next.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(3);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Throws an exception when inserting before a value in an empty linked list', () => {
    const linkedList = new LinkedList();
    const valueNotFound = 1;
    expect(() => linkedList.insertBefore(valueNotFound, 1)).toThrow(`Error in insertBefore() - the beforeValue argument of: ${valueNotFound} is not found in the linked list because the linked list is empty`);
  });

  it('Throws an exception when inserting after a value in an empty linked list', () => {
    const linkedList = new LinkedList();
    const valueNotFound = 1;
    expect(() => linkedList.insertAfter(valueNotFound, 1)).toThrow(`Error in insertAfter() - the afterValue argument of: ${valueNotFound} is not found in the linked list because the linked list is empty`);
  });

  it('Throws an exception when inserting before a value that is not found in the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(2);
    const valueNotFound = 5;
    expect(() => linkedList.insertBefore(valueNotFound, 1)).toThrow(`Error in insertBefore() - the beforeValue argument of: ${valueNotFound} is not found in the linked list`);
  });

  it('Throws an exception when inserting after a value that is not found in the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(1);
    const valueNotFound = 5;
    expect(() => linkedList.insertAfter(valueNotFound, 2)).toThrow(`Error in insertAfter() - the afterValue argument of: ${valueNotFound} is not found in the linked list`);
  });

  it('Can delete a node at the start of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(3);
    linkedList.insert(2);
    linkedList.insert(1);
    linkedList.delete(1);
    expect(linkedList.head.value).toEqual(2);
    expect(linkedList.head.next.value).toEqual(3);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(3);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Can delete a node at the end of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(3);
    linkedList.insert(2);
    linkedList.insert(1);
    linkedList.delete(3);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(2);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(2);
    expect(linkedList.tail.next).toEqual(null);
  });

  it('Can delete a node anywhere in the middle of the linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(3);
    linkedList.insert(2);
    linkedList.insert(1);
    linkedList.delete(2);
    expect(linkedList.head.value).toEqual(1);
    expect(linkedList.head.next.value).toEqual(3);
    expect(linkedList.head.next.next).toEqual(null);
    expect(linkedList.tail.value).toEqual(3);
    expect(linkedList.tail.next).toEqual(null);
  });
});
