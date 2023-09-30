'use strict';

const LinkedList = require('../../linked-list-kth');
const { zipLists } = require('../index');

describe('Tests for zipList function', () => {

  it('Returns the 1st list if both lists are empty', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('NULL');
  });

  it('Returns the 1st list if the 2nd list is empty', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list1.append(1);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> NULL');
  });

  it('Reassigns the 1st list to the 2nd list and then returns the 1st list if the 1st list starts empty', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list2.append(1);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> NULL');
  });

  it('Correctly zips 2 lists with the 1st list having more than one node and the 2nd list having only 1 node', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list1.append(1);
    list1.append(2);
    list2.append(3);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> { 3 } -> { 2 } -> NULL');
  });

  it('Correctly zips 2 lists with the 2nd list having more than one node and the 1st list having only 1 node', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list1.append(1);
    list2.append(2);
    list2.append(3);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> { 2 } -> { 3 } -> NULL');
  });

  it('Correctly zips 2 lists of equal length', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list1.append(1);
    list1.append(3);
    list1.append(5);
    list2.append(2);
    list2.append(4);
    list2.append(6);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NULL');
  });

  it('Correctly zips 2 lists with the 1st list having more nodes than the 2nd list', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list1.append(1);
    list1.append(3);
    list1.append(5);
    list1.append(7);
    list1.append(9);
    list2.append(2);
    list2.append(4);
    list2.append(6);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 9 } -> NULL');
  });

  it('Correctly zips 2 lists with the 1st list having less nodes than the 2nd list', () => {
    const list1 = new LinkedList();
    const list2 = new LinkedList();
    list1.append(1);
    list1.append(3);
    list1.append(5);
    list2.append(2);
    list2.append(4);
    list2.append(6);
    list2.append(8);
    list2.append(10);
    zipLists(list1, list2);
    expect(list1.toString()).toEqual('{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 8 } -> { 10 } -> NULL');
  });
});
