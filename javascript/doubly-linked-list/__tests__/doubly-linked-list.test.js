'use strict';

// Require our linked list implementation
const DoublyLinkedList = require('../index');

describe('Doubly Linked List', () => {

  it('Instantiates an empty linked list', () => {
    const doublyLinkedList = new DoublyLinkedList();
    expect(doublyLinkedList.head).toEqual(null);
  });

  it('Inserts a new node at the head of the linked list.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    expect(doublyLinkedList.head.value).toEqual(1);
  });

  it('The head property always points to the first node of the linked list.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    doublyLinkedList.insert(2);
    expect(doublyLinkedList.head.value).toEqual(2);
  });

  it('Can insert multiple nodes into the linked list.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    doublyLinkedList.insert(2);
    doublyLinkedList.insert(3);
    expect(doublyLinkedList.head.value).toEqual(3);
    expect(doublyLinkedList.head.next.value).toEqual(2);
    expect(doublyLinkedList.head.next.next.value).toEqual(1);
  });

  it('It can traverse in reverse through the doubly linked list.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    doublyLinkedList.insert(2);
    doublyLinkedList.insert(3);
    expect(doublyLinkedList.head.next.next.prev.prev.value).toEqual(3);
  });

  it('It will not create a circular linked list.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    expect(doublyLinkedList.head.prev).toEqual(null);
    expect(doublyLinkedList.head.next).toEqual(null);
    doublyLinkedList.insert(2);
    expect(doublyLinkedList.head.prev).toEqual(null);
    expect(doublyLinkedList.head.next.next).toEqual(null);
    doublyLinkedList.insert(3);
    expect(doublyLinkedList.head.prev).toEqual(null);
    expect(doublyLinkedList.head.next.next.next).toEqual(null);
  });

  it('Will return true when finding a value within the linked list that exists.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    doublyLinkedList.insert(2);
    doublyLinkedList.insert(3);
    expect(doublyLinkedList.includes(1)).toEqual(true);
    expect(doublyLinkedList.includes(2)).toEqual(true);
    expect(doublyLinkedList.includes(3)).toEqual(true);
  });

  it('Will return false when searching for a value in the linked list that does not exist.', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    doublyLinkedList.insert(2);
    doublyLinkedList.insert(3);
    expect(doublyLinkedList.includes(4)).toEqual(false);
  });

  it('Can properly return a collection of all the values that exist in the linked list (returned as a string).', () => {
    const doublyLinkedList = new DoublyLinkedList();
    doublyLinkedList.insert(1);
    doublyLinkedList.insert(2);
    doublyLinkedList.insert(3);
    expect(doublyLinkedList.toString()).toEqual(`NULL <- { 3 } ->  <- { 2 } ->  <- { 1 } -> NULL`);
  });
});
