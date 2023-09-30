'use strict';

const Graph = require('../index');

const graph = new Graph();

const A = graph.addNode('A');
const B = graph.addNode('B');
const C = graph.addNode('C');
const D = graph.addNode('D');
const E = graph.addNode('E');
const F = graph.addNode('F');
const G = graph.addNode('G');
const H = graph.addNode('H');

graph.addEdge(A, B);
graph.addEdge(B, C);
graph.addEdge(A, D);
graph.addEdge(B, D);
graph.addEdge(D, E);
graph.addEdge(D, F);
graph.addEdge(C, G);
graph.addEdge(D, H);
graph.addEdge(F, H);

describe('Tests for the depthFirstTraversal method for the Graph class', () => {

  it('Returns an empty array if no root node is given', () => {
    const emptyGraph = new Graph();
    expect(emptyGraph.depthFirstTraversal()).toEqual([]);
  });

  it('Returns an array of a single node for a graph of a single node, or a disconnected node', () => {
    const singleNodeGraph = new Graph();
    const A = singleNodeGraph.addNode('A');
    expect(singleNodeGraph.depthFirstTraversal(A)).toEqual([A]);
  });

  it('Returns an array of nodes using depth-first pre-ordering', () => {
    const smallGraph = new Graph();
    const A = smallGraph.addNode('A');
    const B = smallGraph.addNode('B');
    const C = smallGraph.addNode('C');

    smallGraph.addEdge(A, B);
    smallGraph.addEdge(A, C);

    expect(smallGraph.depthFirstTraversal(A)).toEqual([A, B, C]);
  });

  it('Returns the correct array of nodes in the proper order for a small graph', () => {
    const smallGraph = new Graph();
    const A = smallGraph.addNode('A');
    const B = smallGraph.addNode('B');
    const C = smallGraph.addNode('C');
    const D = smallGraph.addNode('D');

    smallGraph.addEdge(A, B);
    smallGraph.addEdge(A, C);
    smallGraph.addEdge(B, D);

    expect(smallGraph.depthFirstTraversal(A, console.log)).toEqual([A, B, D, C]);
  });

  it('Returns the correct array of nodes in the proper order for a small cyclical graph', () => {

    const smallGraph = new Graph();
    const A = smallGraph.addNode('A');
    const B = smallGraph.addNode('B');
    const C = smallGraph.addNode('C');
    const D = smallGraph.addNode('D');

    smallGraph.addEdge(A, B);
    smallGraph.addEdge(A, C);
    smallGraph.addEdge(B, D);
    smallGraph.addEdge(D, A);

    expect(smallGraph.depthFirstTraversal(A)).toEqual([A, B, D, C]);
  });

  it('Returns the correct array of nodes in the proper order for a large cyclical graph', () => {
    expect(graph.depthFirstTraversal(A)).toEqual([A, B, C, G, D, E, F, H]);
  });

  it('Calls the callback on each node', () => {
    const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

    graph.depthFirstTraversal(A, console.log);

    expect(consoleSpy).toHaveBeenCalledWith('A');
    expect(consoleSpy).toHaveBeenCalledWith('B');
    expect(consoleSpy).toHaveBeenCalledWith('C');
    expect(consoleSpy).toHaveBeenCalledWith('D');
    expect(consoleSpy).toHaveBeenCalledWith('E');
    expect(consoleSpy).toHaveBeenCalledWith('F');
    expect(consoleSpy).toHaveBeenCalledWith('G');
    expect(consoleSpy).toHaveBeenCalledWith('H');

    consoleSpy.mockRestore();
  });
});
