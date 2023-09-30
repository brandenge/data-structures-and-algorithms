'use strict';

const { BinaryNode, BinaryTree } = require('../index');

describe('Tests for the BinaryTree class', () => {
  it('Can successfully instantiate an empty tree', () => {
    const binaryTree = new BinaryTree();
    expect(binaryTree.root).toEqual(null);
  });

  it('Can successfully instantiate a tree with a single root node', () => {
    const binaryTree = new BinaryTree();
    const node = new BinaryNode(1);
    binaryTree.root = node;
    expect(binaryTree.root.value).toEqual(1);
    expect(binaryTree.root.left).toEqual(null);
    expect(binaryTree.root.right).toEqual(null);
    expect(binaryTree.preOrder()).toEqual([1]);
    expect(binaryTree.inOrder()).toEqual([1]);
    expect(binaryTree.postOrder()).toEqual([1]);
  });

  const binaryTree = new BinaryTree();
  const node1 = new BinaryNode(1);
  const node2 = new BinaryNode(2);
  const node3 = new BinaryNode(3);
  node2.left = node1;
  node2.right = node3;
  binaryTree.root = node2;

  it('Can successfully return a collection from a preorder traversal', () => {
    expect(binaryTree.preOrder()).toEqual([2, 1, 3]);
  });

  it('Can successfully return a collection from an inorder traversal', () => {
    expect(binaryTree.inOrder()).toEqual([1, 2, 3]);
  });

  it('Can successfully return a collection from a postorder traversal', () => {
    expect(binaryTree.postOrder()).toEqual([1, 3, 2]);
  });
});
