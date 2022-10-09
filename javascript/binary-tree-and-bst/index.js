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

  preOrder() {
    const values = [];

    function traverse(current) {
      values.push(current.value);
      if (current.left) traverse(current.left);
      if (current.right) traverse(current.right);
    }
    traverse(this.root);
    return values;
  }

  inOrder() {
    const values = [];

    function traverse(current) {
      if (current.left) traverse(current.left);
      values.push(current.value);
      if (current.right) traverse(current.right);
    }
    traverse(this.root);
    return values;
  }

  postOrder() {
    const values = [];

    function traverse(current) {
      if (current.left) traverse(current.left);
      if (current.right) traverse(current.right);
      values.push(current.value);
    }
    traverse(this.root);
    return values;
  }
}

class BinarySearchTree extends BinaryTree {
  constructor() {
    super();
  }

  add(value) {
    const node = new BinaryNode(value);
    if (this.root === null) {
      this.root = node;
      return;
    }
    function traverse(current) {
      if (value <= current.value) {
        if (current.left) traverse(current.left);
        else current.left = node;
      }
      else if (value > current.value) {
        if (current.right) traverse(current.right);
        else current.right = node;
      }
    }
    traverse(this.root);
  }

  contains(value) {
    if (this.root === null) return false;
    function traverse(current) {
      if (current.value === value) return true;
      else if (value < current.value && current.left) return traverse(current.left);
      else if (value > current.value && current.right) return traverse(current.right);
      else return false;
    }
    return traverse(this.root);
  }
}

class KaryNode {
  constructor(value) {
    this.value = value;
    this.children = [];
  }
}

class KaryTree {
  constructor(k) {
    this.root = null;
    this.k = k;
  }

  preOrder() {
    const values = [];

    function traverse(current) {
      values.push(current.value);
      if (current.children.length > 0) current.children.forEach(child => traverse(child));
    }
    traverse(this.root);
    return values;
  }

  inOrder() {
    const values = [];

    function traverse(current) {
      if (current.children.length > 0) {
        for (let i = 0, len = current.children.length; i < Math.ceil(len / 2); i++) {
          traverse(current.children[i]);
        }
      }
      values.push(current.value);
      if (current.children.length > 0) {
        for (let len = current.children.length, i = Math.ceil(len / 2); i < len; i++) {
          traverse(current.children[i]);
        }
      }
    }
    traverse(this.root);
    return values;
  }

  postOrder() {
    const values = [];

    function traverse(current) {
      if (current.children.length > 0) current.children.forEach(child => traverse(child));
      values.push(current.value);
    }
    traverse(this.root);
    return values;
  }
}

module.exports = { BinaryNode, BinaryTree, BinarySearchTree, KaryNode, KaryTree };
