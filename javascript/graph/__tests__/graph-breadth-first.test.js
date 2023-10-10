'use strict';

const Graph = require('../index');

const graph = new Graph();

const pandora = graph.addNode('Pandora');
const arendelle = graph.addNode('Arendelle');
const metroville = graph.addNode('Metroville');
const monstropolis = graph.addNode('Monstropolis');
const narnia = graph.addNode('Narnia');
const naboo = graph.addNode('Naboo');

graph.addEdge(pandora, arendelle);
graph.addEdge(arendelle, metroville);
graph.addEdge(arendelle, monstropolis);
graph.addEdge(metroville, narnia);
graph.addEdge(metroville, naboo);
graph.addEdge(metroville, monstropolis);
graph.addEdge(monstropolis, naboo);
graph.addEdge(narnia, naboo);

describe('Tests for the breadthFirstTraversal method for the Graph class', () => {

  it('Returns an empty array if no root node is given', () => {
    const emptyGraph = new Graph();
    expect(emptyGraph.breadthFirstTraversal()).toEqual([]);
  });

  it('Returns an array of a single node for a graph of a single node, or a disconnected node', () => {
    const smallGraph = new Graph();
    const A = smallGraph.addNode('A');
    expect(smallGraph.breadthFirstTraversal(A)).toEqual([A]);
  });

  it('Returns the correct array of nodes in the proper order for a cyclical graph', () => {

    expect(graph.breadthFirstTraversal(pandora)).toEqual([pandora, arendelle, metroville, monstropolis, narnia, naboo]);
  });

  it('Calls the callback on each node in the proper order', () => {
    const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

    graph.breadthFirstTraversal(pandora, console.log);

    expect(consoleSpy).toHaveBeenCalledWith('Pandora');
    expect(consoleSpy).toHaveBeenCalledWith('Arendelle');
    expect(consoleSpy).toHaveBeenCalledWith('Metroville');
    expect(consoleSpy).toHaveBeenCalledWith('Monstropolis');
    expect(consoleSpy).toHaveBeenCalledWith('Narnia');
    expect(consoleSpy).toHaveBeenCalledWith('Naboo');

    consoleSpy.mockRestore();
  });
});

describe('Test for the areConnected method', () => {
  it('Returns false when the 2 nodes are not connected in the graph', () => {
    const islandNode = graph.addNode('node');
    expect(graph.areConnected(pandora, islandNode)).toEqual(false);
  });

  it('Returns true when the 2 nodes are connected in the graph', () => {
    expect(graph.areConnected(pandora, narnia)).toEqual(true);
  });
});
