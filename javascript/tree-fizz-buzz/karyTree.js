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

module.exports = { KaryNode, KaryTree };
