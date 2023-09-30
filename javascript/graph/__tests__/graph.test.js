'use strict';

const Graph = require('../index');

describe('Tests for the Graph class', () => {
  const graph = new Graph();

  const A = graph.addNode('A');
  const B = graph.addNode('B');
  const C = graph.addNode('C');
  const D = graph.addNode('D');
  const E = graph.addNode('E');
  const F = graph.addNode('F');

  const AtoC = graph.addEdge(A, C, 1);
  const BtoC = graph.addEdge(B, C, 2);
  const BtoF = graph.addEdge(B, F, 3);
  const CtoE = graph.addEdge(C, E, 4);
  const DtoA = graph.addEdge(D, A, 5);
  const DtoE = graph.addEdge(D, E, 6);
  const EtoC = graph.addEdge(E, C, 7);
  const EtoF = graph.addEdge(E, F, 8);

  test('A node can be successfully be added to the graph', () => {
    expect(graph.adjacencyList.has(A)).toBe(true);
    expect(graph.adjacencyList.has(B)).toBe(true);
    expect(graph.adjacencyList.has(C)).toBe(true);
    expect(graph.adjacencyList.has(D)).toBe(true);
    expect(graph.adjacencyList.has(E)).toBe(true);
    expect(graph.adjacencyList.has(F)).toBe(true);
  });

  test('An edge can be successfully added to the graph', () => {
    expect(graph.adjacencyList.get(A)).toEqual([AtoC]);
    expect(graph.adjacencyList.get(B)).toEqual([BtoC, BtoF]);
    expect(graph.adjacencyList.get(C)).toEqual([CtoE]);
    expect(graph.adjacencyList.get(D)).toEqual([DtoA, DtoE]);
    expect(graph.adjacencyList.get(E)).toEqual([EtoC, EtoF]);
    expect(graph.adjacencyList.get(F)).toEqual([]);
  });

  test('A collection of all nodes can be properly retrieved from the graph', () => {
    expect(graph.getNodes()).toEqual([A, B, C, D, E, F]);
  });

  test('All appropriate neighbors can be retrieved from the graph', () => {
    expect(graph.getNeighbors(A)).toEqual([AtoC]);
    expect(graph.getNeighbors(B)).toEqual([BtoC, BtoF]);
    expect(graph.getNeighbors(C)).toEqual([CtoE]);
    expect(graph.getNeighbors(D)).toEqual([DtoA, DtoE]);
    expect(graph.getNeighbors(E)).toEqual([EtoC, EtoF]);
    expect(graph.getNeighbors(F)).toEqual([]);
  });

  test('Neighbors are returned with the weight between nodes included', () => {
    expect(graph.getNeighbors(A)[0].weight).toEqual(1);
    expect(graph.getNeighbors(B)[0].weight).toEqual(2);
    expect(graph.getNeighbors(B)[1].weight).toEqual(3);
    expect(graph.getNeighbors(C)[0].weight).toEqual(4);
    expect(graph.getNeighbors(D)[0].weight).toEqual(5);
    expect(graph.getNeighbors(D)[1].weight).toEqual(6);
    expect(graph.getNeighbors(E)[0].weight).toEqual(7);
    expect(graph.getNeighbors(E)[1].weight).toEqual(8);
  });

  test('The proper size is returned, representing the number of nodes in the graph', () => {
    expect(graph.size()).toEqual(6);
  });

  test('A graph with only one node and edge can be properly returned', () => {
    const smallGraph = new Graph();
    const G = smallGraph.addNode('first node');
    expect(smallGraph.adjacencyList.has(G)).toBe(true);
    expect(smallGraph.size()).toEqual(1);
    const H = smallGraph.addNode('second node');
    const GtoH = smallGraph.addEdge(G, H, 9);
    expect(smallGraph.adjacencyList.get(G)).toEqual[GtoH];
  });
});
