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

  it('Can find the k-th node from the end of the list when k is a valid positive integer', () => {
    const linkedList = new LinkedList();
    linkedList.insert(5);
    linkedList.insert(4);
    linkedList.insert(3);
    linkedList.insert(2);
    linkedList.insert(1);
    expect(linkedList.kthFromEnd(0)).toEqual(5);
    expect(linkedList.kthFromEnd(1)).toEqual(4);
    expect(linkedList.kthFromEnd(2)).toEqual(3);
    expect(linkedList.kthFromEnd(3)).toEqual(2);
    expect(linkedList.kthFromEnd(4)).toEqual(1);
  });

  it('Throws an error when the k-th node is invalid', () => {
    const linkedList = new LinkedList();
    linkedList.insert(3);
    linkedList.insert(2);
    linkedList.insert(1);
    let k = -1;
    expect(() => linkedList.kthFromEnd(k)).toThrow(`Error in kthFromEnd() - the argument of ${k} must be a positive integer that is less than the total number of nodes in the linked list, which has a current count of: ${linkedList.count}`);
    k = 4;
    expect(() => linkedList.kthFromEnd(k)).toThrow(`Error in kthFromEnd() - the argument of ${k} must be a positive integer that is less than the total number of nodes in the linked list, which has a current count of: ${linkedList.count}`);
    k = linkedList.count;
    expect(() => linkedList.kthFromEnd(k)).toThrow(`Error in kthFromEnd() - the argument of ${k} must be a positive integer that is less than the total number of nodes in the linked list, which has a current count of: ${linkedList.count}`);
  });

  it('Can find the value of the middle node of a linked list', () => {
    const linkedList = new LinkedList();
    linkedList.insert(3);
    expect(linkedList.getMiddleNodeValue()).toEqual(3);
    linkedList.insert(2);
    expect(linkedList.getMiddleNodeValue()).toEqual(2);
    linkedList.insert(1);
    expect(linkedList.getMiddleNodeValue()).toEqual(2);
    linkedList.insert(0);
    expect(linkedList.getMiddleNodeValue()).toEqual(1);
    linkedList.insert(-1);
    expect(linkedList.getMiddleNodeValue()).toEqual(1);
  });

  it('Throws an error when the linked list is empty while it is searching for the middle node', () => {
    const linkedList = new LinkedList();
    expect(() => linkedList.getMiddleNodeValue()).toThrow('Error in getMiddleNodeValue() - the linked list is empty');
  });

  it('Can accurately keep count of the number of nodes ', () => {
    const linkedList = new LinkedList();
    expect(linkedList.count).toEqual(0);
    linkedList.insert(1);
    expect(linkedList.count).toEqual(1);
    linkedList.append(2);
    expect(linkedList.count).toEqual(2);
    linkedList.insertBefore(2, 3);
    expect(linkedList.count).toEqual(3);
    linkedList.insertAfter(3, 4);
    expect(linkedList.count).toEqual(4);
    linkedList.delete(1);
    expect(linkedList.count).toEqual(3);
  });
});
