'use strict';

const { KaryNode, KaryTree } = require('./karyTree');
const Queue = require('./queue');

function fizzBuzz(node) {
  const newNode = new KaryNode('');
  if (node.value % 3 === 0) newNode.value += 'Fizz';
  if (node.value % 5 === 0) newNode.value += 'Buzz';
  else newNode.value = (node.value).toString();
  return newNode;
}

function fizzBuzzTree(karyTree) {
  if (!karyTree.root) return null;
  const newTree = new KaryTree();
  const newRoot = fizzBuzz(karyTree.root);
  newTree.root = newRoot;
  if (karyTree.children.length === 0) return newTree;
  const queue = new Queue();
  let current = karyTree.root;
  queue.enqueue(current);
  while(queue.front) {
    let current = queue.dequeue();
    if (current.children.length > 0) {
      current.children.forEach(child => {
        current.children.push(fizzBuzz(child));
        queue.enqueue(child);
      });
    }
  }
  return newTree;
}


module.exports = fizzBuzzTree;
