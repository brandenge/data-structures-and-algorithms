'use strict';

const { KaryNode, KaryTree } = require('./karyTree');
const Queue = require('./queue');

function fizzBuzz(node) {
  const newNode = new KaryNode('');
  if (node.value % 3 === 0) newNode.value += 'Fizz';
  if (node.value % 5 === 0) newNode.value += 'Buzz';
  if (newNode.value !== 'Fizz' && newNode.value !== 'Buzz' && newNode.value !== 'FizzBuzz') {
    newNode.value = (node.value).toString();
  }
  return newNode;
}

function fizzBuzzTree(karyTree) {
  if (!karyTree.root) return null;
  const newTree = new KaryTree();
  const newRoot = fizzBuzz(karyTree.root);
  newTree.root = newRoot;
  const oldTreeQueue = new Queue();
  const newTreeQueue = new Queue();
  oldTreeQueue.enqueue(karyTree.root);
  newTreeQueue.enqueue(newTree.root);
  while (!oldTreeQueue.isEmpty()) {
    let oldCurrent = oldTreeQueue.dequeue();
    let newCurrent = newTreeQueue.dequeue();
    if (oldCurrent.children.length > 0) {
      newCurrent.children = oldCurrent.children.map(child => {
        const newChild = fizzBuzz(child);
        oldTreeQueue.enqueue(child);
        newTreeQueue.enqueue(newChild);
        return newChild;
      });
    }
  }
  return newTree;
}

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

console.log('KARY TREE:', karyTree.root);
console.log('RESULT TREE', resultTree.root);

module.exports = fizzBuzzTree;
