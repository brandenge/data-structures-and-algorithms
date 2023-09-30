'use strict';

const { BinarySearchTree } = require('../index');

const bst = new BinarySearchTree();
bst.add(2);
bst.add(3);
bst.add(1);

describe('Tests for the BinarySearchTree class', () => {
  it('Can successfully add a left child and right child properly to a node', () => {
    expect(bst.root.value).toEqual(2);
    expect(bst.root.left.value).toEqual(1);
    expect(bst.root.right.value).toEqual(3);
    expect(bst.inOrder()).toEqual([1, 2, 3]);
  });

  it('Returns true for the contains method when given an existing node value', () => {
    expect(bst.contains(3)).toEqual(true);
  });

  it('Returns false for the contains method when given a non-existing node value', () => {
    expect(bst.contains(4)).toEqual(false);
  });
});
