'use strict';

const { KaryNode, KaryTree } = require('../index');

describe('Tests for the KaryTree (K-ary Tree) class', () => {
  it('Can successfully instantiate an empty tree', () => {
    const karyTree = new KaryTree();
    expect(karyTree.root).toEqual(null);
  });

  it('Can successfully instantiate a tree with a single root node', () => {
    const karyTree = new KaryTree(3);
    const node = new KaryNode(1);
    karyTree.root = node;
    karyTree.k = 3;
    expect(karyTree.root.value).toEqual(1);
    expect(karyTree.k).toEqual(3);
    expect(karyTree.root.children.length).toEqual(0);
    expect(karyTree.preOrder()).toEqual([1]);
    expect(karyTree.inOrder()).toEqual([1]);
    expect(karyTree.postOrder()).toEqual([1]);
  });

  const karyTree = new KaryTree();
  const nodes = [];
  for (let i = 0; i <= 10; i++) {
    nodes.push(new KaryNode(i));
  }
  karyTree.root = nodes[2];
  karyTree.root.children.push(nodes[1]);
  karyTree.root.children.push(nodes[3]);

  console.log('preorder', karyTree.preOrder());
  console.log('inorder', karyTree.inOrder());
  console.log('postorder', karyTree.postOrder());

  it('Can successfully return a small collection from a preorder traversal', () => {
    expect(karyTree.preOrder()).toEqual([2, 1, 3]);
  });

  it('Can successfully return a small collection from an inorder traversal', () => {
    expect(karyTree.inOrder()).toEqual([1, 2, 3]);
  });

  it('Can successfully return a small collection from a postorder traversal', () => {
    expect(karyTree.postOrder()).toEqual([1, 3, 2]);
  });

  it('Can successfully return a large collection from a preorder traversal', () => {
    karyTree.root.children[0].children.push(nodes[4], nodes[5], nodes[6]);
    karyTree.root.children[1].children.push(nodes[7], nodes[8], nodes[9]);
    expect(karyTree.preOrder()).toEqual([2, 1, 4, 5, 6, 3, 7, 8, 9]);
  });

  it('Can successfully return a large collection from an inorder traversal', () => {
    expect(karyTree.inOrder()).toEqual([4, 5, 1, 6, 2, 7, 8, 3, 9]);
  });

  it('Can successfully return a large collection from a postorder traversal', () => {
    expect(karyTree.postOrder()).toEqual([4, 5, 6, 1, 7, 8, 9, 3, 2]);
  });
});
