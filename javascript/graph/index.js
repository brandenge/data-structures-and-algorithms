'use strict';

class Node {
  constructor(value) {
    this.value = value;
  }
}

class Edge {
  constructor(node, weight = 0) {
    this.node = node;
    this.weight = weight;
  }
}

class Graph {
  constructor() {
    this.adjacencyList = new Map();
  }

  addNode(value) {
    const node = new Node(value);
    this.adjacencyList.set(node, []);
    return node;
  }

  addEdge(startNode, endNode, weight = 0) {
    const neighbors = this.adjacencyList.get(startNode);
    const edge = new Edge(endNode, weight);
    neighbors.push(edge);
    return edge;
  }

  getNodes() {
    return [...this.adjacencyList.keys()];
  }

  getNeighbors(node) {
    return [...this.adjacencyList.get(node)];
  }

  size() {
    return this.adjacencyList.size;
  }

  breadthFirstTraversal(root, callback) {
    if (!root) return [];
    const queue = [root];
    const visited = new Set();
    let current;

    while (queue.length) {
      current = queue.pop();
      visited.add(current);
      if (callback) callback(current.value);
      const neighbors = this.getNeighbors(current);
      for (let edge of neighbors) {
        if (!visited.has(edge.node)) {
          queue.unshift(edge.node);
        }
      }
    }
    return [...visited];
  }

  depthFirstTraversal(root, callback) {
    if (!root) return [];
    const stack = [root];
    const visited = new Set();
    let current;

    while (stack.length) {
      current = stack.pop();
      visited.add(current);
      if (callback) callback(current.value);
      const neighbors = this.getNeighbors(current);
      for (let edge of neighbors) {
        if (!visited.has(edge.node)) {
          stack.push(edge.node);
        }
      }
    }
    return [...visited];
  }

  areConnected(node1, node2) {
    return this.depthFirstTraversal(node1).includes(node2);
  }
}

module.exports = Graph;
