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
}

module.exports = { KaryNode, KaryTree };
