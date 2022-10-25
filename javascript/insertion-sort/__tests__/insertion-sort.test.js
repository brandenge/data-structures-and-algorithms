'use strict';

const insertionSort = require('../index');

describe('Tests for insertion sort, sorting input arrays in-place in ascending order', () => {

  it('Sorts an unsorted array', () => {
    const arr = [8, 4, 23, 42, 16, 15];
    insertionSort(arr);
    expect(arr).toEqual([4, 8, 15, 16, 23, 42]);
  });

  it('Sorts a reverse-sorted array', () => {
    const arr = [20, 18, 12, 8, 5, -2];
    insertionSort(arr);
    expect(arr).toEqual([-2, 5, 8, 12, 18, 20]);
  });

  it('Sorts an array with duplicate values', () => {
    const arr = [5, 12, 7, 5, 5, 7];
    insertionSort(arr);
    expect(arr).toEqual([5, 5, 5, 7, 7, 12]);
  });

  it('Sorts a nearly sorted array', () => {
    const arr = [2, 3, 5, 7, 13, 11];
    insertionSort(arr);
    expect(arr).toEqual([2, 3, 5, 7, 11, 13]);
  });

  it('Sorts an already sorted array', () => {
    const arr = [2, 3, 5, 7, 11, 13];
    insertionSort(arr);
    expect(arr).toEqual([2, 3, 5, 7, 11, 13]);
  });
});
