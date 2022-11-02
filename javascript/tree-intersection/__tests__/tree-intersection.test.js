'use strict';

const { treeIntersection, treeToHashMap, getCommonValues } = require('../tree-intersection');
const { BinaryNode, BinaryTree } = require('../../binary-tree-and-bst');
const HashMap = require('../../hash-table/index');

const smallTree1 = new BinaryTree();
smallTree1.root = new BinaryNode(2);
smallTree1.root.left = new BinaryNode(1);
smallTree1.root.right = new BinaryNode(3);

const smallTree2 = new BinaryTree();
smallTree2.root = new BinaryNode(4);
smallTree2.root.left = new BinaryNode(5);
smallTree2.root.right = new BinaryNode(1);

const largeTree1 = new BinaryTree();
largeTree1.root = new BinaryNode(150);
largeTree1.root.left = new BinaryNode(100);
largeTree1.root.right = new BinaryNode(250);
largeTree1.root.left.left = new BinaryNode(75);
largeTree1.root.left.right = new BinaryNode(160);
largeTree1.root.left.right.left = new BinaryNode(125);
largeTree1.root.left.right.right = new BinaryNode(175);
largeTree1.root.right.left = new BinaryNode(200);
largeTree1.root.right.right = new BinaryNode(350);
largeTree1.root.right.right.left = new BinaryNode(300);
largeTree1.root.right.right.right = new BinaryNode(500);

const largeTree2 = new BinaryTree();
largeTree2.root = new BinaryNode(42);
largeTree2.root.left = new BinaryNode(100);
largeTree2.root.right = new BinaryNode(600);
largeTree2.root.left.left = new BinaryNode(15);
largeTree2.root.left.right = new BinaryNode(160);
largeTree2.root.left.right.left = new BinaryNode(125);
largeTree2.root.left.right.right = new BinaryNode(175);
largeTree2.root.right.left = new BinaryNode(200);
largeTree2.root.right.right = new BinaryNode(350);
largeTree2.root.right.right.left = new BinaryNode(4);
largeTree2.root.right.right.right = new BinaryNode(500);

describe('Tests for the treeIntersection function', () => {
  it('Returns an empty array when there are no common values', () => {
    expect(treeIntersection(new BinaryTree(), new BinaryTree())).toEqual([]);
  });

  it('Gets common values between two small trees', () => {
    expect(treeIntersection(smallTree1, smallTree2)).toEqual([1]);
  });

  it('Gets common values between two large trees', () => {
    expect(treeIntersection(largeTree1, largeTree2)).toEqual([100, 125, 160, 175, 200, 350, 500]);
  });
});

describe('Tests for the treeToHashMap function', () => {
  it('Inserts only a single key into the HashMap when given a node with no children', () => {
    const hashMap = treeToHashMap(new BinaryNode(4), new HashMap(1024));
    expect(hashMap.keys().has('4')).toEqual(true);
  });

  it('Correctly populates a hashMap with the values from a small tree', () => {
    const hashMap = treeToHashMap(smallTree1.root, new HashMap(1024));
    expect(Array.from(hashMap.keys())).toEqual(['3', '1', '2']);
  });

  it('Correctly populates a hashMap with the values from a large tree', () => {
    const hashMap = treeToHashMap(largeTree1.root, new HashMap(1024));
    const actual = Array.from(hashMap.keys()).map((val) => +val).sort((a, b) => a - b);
    const expected = ['75', '100', '125', '160', '175', '150', '200', '250', '300', '350', '500'].map((val) => +val).sort((a, b) => a - b);
    expect(actual).toEqual(expected);
  });
});

describe('Tests for the getCommonValues function', () => {
  it('Returns an empty array when there are no common values', () => {
    const hashMap = treeToHashMap(new BinaryNode(10), new HashMap(1024));
    const actual = getCommonValues(new BinaryNode(4), hashMap, []);
    expect(actual).toEqual([]);
  });

  it('Gets common values between two small trees', () => {
    const hashMap = treeToHashMap(smallTree1.root, new HashMap(1024));
    const actual = getCommonValues(smallTree2.root, hashMap, []);
    expect(actual).toEqual([1]);
  });

  it('Gets common values between two large trees', () => {
    const hashMap = treeToHashMap(largeTree1.root, new HashMap(1024));
    const actual = getCommonValues(largeTree2.root, hashMap, []);
    expect(actual).toEqual([100, 125, 160, 175, 200, 350, 500]);
  });
});
