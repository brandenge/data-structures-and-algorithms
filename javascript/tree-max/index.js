'use strict';

class BinaryNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
  }

  findMax() {
    if (!this.root) return null;
    let max = -Infinity;

    function traverse(current) {
      if (current.left) traverse(current.left);
      if (max < current.value) max = current.value;
      if (current.right) traverse(current.right);
    }
    traverse(this.root);
    return max;
  }
}

module.exports = { BinaryNode, BinaryTree };
