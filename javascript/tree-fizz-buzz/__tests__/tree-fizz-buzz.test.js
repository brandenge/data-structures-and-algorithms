'use strict';

const { KaryNode, KaryTree } = require('../karyTree');
const fizzBuzzTree = require('../index');

describe('Tests for fizzBuzzTree function', () => {
  it('returns null when passed an empty tree', () => {
    const karyTree = new KaryTree();
    expect(fizzBuzzTree(karyTree)).toEqual(null);
  });

  it('it returns the correctly modified copy of the k-ary tree when passed a k-ary tree with only 1 node in it', () => {
    const karyTree1 = new KaryTree();
    const karyTree2 = new KaryTree();
    const karyTree3 = new KaryTree();
    const karyTree4 = new KaryTree();
    const karyTree5 = new KaryTree();
    const karyTree6 = new KaryTree();
    const karyTree7 = new KaryTree();
    const karyTree8 = new KaryTree();
    const node1 = new KaryNode(2);
    const node2 = new KaryNode(9);
    const node3 = new KaryNode(10);
    const node4 = new KaryNode(15);
    const node5 = new KaryNode(-2);
    const node6 = new KaryNode(-9);
    const node7 = new KaryNode(-10);
    const node8 = new KaryNode(-15);
    karyTree1.root = node1;
    karyTree2.root = node2;
    karyTree3.root = node3;
    karyTree4.root = node4;
    karyTree5.root = node5;
    karyTree6.root = node6;
    karyTree7.root = node7;
    karyTree8.root = node8;
    expect(fizzBuzzTree(karyTree1).root.value).toEqual('2');
    expect(fizzBuzzTree(karyTree3).root.value).toEqual('Buzz');
    expect(fizzBuzzTree(karyTree2).root.value).toEqual('Fizz');
    expect(fizzBuzzTree(karyTree4).root.value).toEqual('FizzBuzz');
    expect(fizzBuzzTree(karyTree5).root.value).toEqual('-2');
    expect(fizzBuzzTree(karyTree6).root.value).toEqual('Fizz');
    expect(fizzBuzzTree(karyTree7).root.value).toEqual('Buzz');
    expect(fizzBuzzTree(karyTree8).root.value).toEqual('FizzBuzz');
  });

  it('it returns the correctly modified copy of the k-ary tree when passed a small k-ary tree', () => {
    const karyTree = new KaryTree();
    const node1 = new KaryNode(2);
    const node2 = new KaryNode(9);
    const node3 = new KaryNode(10);
    const node4 = new KaryNode(15);
    karyTree.root = node1;
    karyTree.root.children = [node2, node3, node4];
    const resultTree = fizzBuzzTree(karyTree);
    expect(resultTree.root.value).toEqual('2');
    expect(resultTree.root.children[0].value).toEqual('Fizz');
    expect(resultTree.root.children[1].value).toEqual('Buzz');
    expect(resultTree.root.children[2].value).toEqual('FizzBuzz');
    expect(karyTree.root.value).toEqual(2);
    expect(karyTree.root.children[0].value).toEqual(9);
    expect(karyTree.root.children[1].value).toEqual(10);
    expect(karyTree.root.children[2].value).toEqual(15);
  });

  it('it returns the correctly modified copy of the k-ary tree when passed a large k-ary tree', () => {
    const karyTree = new KaryTree();
    const node1 = new KaryNode(22);
    const node2 = new KaryNode(33);
    const node3 = new KaryNode(100);
    const node4 = new KaryNode(150);
    const node5 = new KaryNode(-22);
    const node6 = new KaryNode(-9);
    const node7 = new KaryNode(-10);
    const node8 = new KaryNode(-15);
    karyTree.root = node1;
    karyTree.root.children = [node2, node3, node4];
    karyTree.root.children[2].children = [node5, node6, node7, node8];
    const resultTree = fizzBuzzTree(karyTree);
    expect(resultTree.root.value).toEqual('22');
    expect(resultTree.root.children[0].value).toEqual('Fizz');
    expect(resultTree.root.children[1].value).toEqual('Buzz');
    expect(resultTree.root.children[2].value).toEqual('FizzBuzz');
    expect(resultTree.root.children[2].children[0].value).toEqual('-22');
    expect(resultTree.root.children[2].children[1].value).toEqual('Fizz');
    expect(resultTree.root.children[2].children[2].value).toEqual('Buzz');
    expect(resultTree.root.children[2].children[3].value).toEqual('FizzBuzz');
    expect(karyTree.root.value).toEqual(22);
    expect(karyTree.root.children[0].value).toEqual(33);
    expect(karyTree.root.children[1].value).toEqual(100);
    expect(karyTree.root.children[2].value).toEqual(150);
    expect(karyTree.root.children[2].children[0].value).toEqual(-22);
    expect(karyTree.root.children[2].children[1].value).toEqual(-9);
    expect(karyTree.root.children[2].children[2].value).toEqual(-10);
    expect(karyTree.root.children[2].children[3].value).toEqual(-15);
  });
});
