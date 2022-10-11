'use strict';

const { BinaryNode, BinaryTree } = require('../index');

describe('Tests the findMax method of the BinaryTree class', () => {
  it('Returns null when used on an empty tree', () => {
    const binaryTree = new BinaryTree();
    expect(binaryTree.findMax()).toEqual(null);
  });

  it('Returns the value of the root node when there is only 1 node in the tree', () => {
    const node = new BinaryNode(5);
    const binaryTree = new BinaryTree();
    binaryTree.root = node;
    expect(binaryTree.findMax()).toEqual(binaryTree.root.value);
  });

  it('Returns the max value of a small tree', () => {
    const node1 = new BinaryNode(1);
    const node2 = new BinaryNode(2);
    const node3 = new BinaryNode(3);
    node1.left = node2;
    node1.right = node3;

    const binaryTree = new BinaryTree();
    binaryTree.root = node1;

    expect(binaryTree.findMax()).toEqual(3);
  });

  it('Returns the max value of a larger tree', () => {
    const node1 = new BinaryNode(1);
    const node2 = new BinaryNode(2);
    const node3 = new BinaryNode(3);
    const node4 = new BinaryNode(4);
    const node5 = new BinaryNode(5);
    const node6 = new BinaryNode(6);
    const node7 = new BinaryNode(7);
    const node8 = new BinaryNode(8);
    const node9 = new BinaryNode(9);
    node1.left = node2;
    node1.right = node3;
    node2.left = node4;
    node2.right = node5;
    node3.left = node6;
    node3.right = node7;
    node7.right = node8;
    node8.right = node9;

    const binaryTree = new BinaryTree();
    binaryTree.root = node1;

    expect(binaryTree.findMax()).toEqual(9);
  });

  it('Returns the max value of a tree with all negative values', () => {
    const node1 = new BinaryNode(-100);
    const node2 = new BinaryNode(-1000);
    const node3 = new BinaryNode(-10000);
    node1.left = node2;
    node1.right = node3;
    const binaryTree = new BinaryTree();
    binaryTree.root = node1;
    expect(binaryTree.findMax()).toEqual(-100);
  });
});
