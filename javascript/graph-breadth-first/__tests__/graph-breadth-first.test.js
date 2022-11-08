'use strict';

const Graph = require('../index');

describe('Tests for the breadthFirstTraversal method for the Graph class', () => {
  it('Returns an empty array if no root node is given', () => {
    const graph = new Graph();
    expect(graph.breadthFirstTraversal()).toEqual([]);
  });

  it('Returns an array of a single node for a graph of a single node, or a disconnected node', () => {
    const graph = new Graph();
    const A = graph.addNode('A');
    expect(graph.breadthFirstTraversal(A)).toEqual([A]);
  });

  it('Returns the correct array of nodes in the proper order for a cyclical graph', () => {
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

    expect(graph.breadthFirstTraversal(pandora)).toEqual([pandora, arendelle, metroville, monstropolis, narnia, naboo]);
  });

  it('Calls the callback on each node in the proper order', () => {
    const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

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

    graph.breadthFirstTraversal(pandora, console.log);

    expect(consoleSpy).toHaveBeenCalledWith('Pandora');
    expect(consoleSpy).toHaveBeenCalledWith('Arendelle');
    expect(consoleSpy).toHaveBeenCalledWith('Metroville');
    expect(consoleSpy).toHaveBeenCalledWith('Monstropolis');
    expect(consoleSpy).toHaveBeenCalledWith('Narnia');
    expect(consoleSpy).toHaveBeenCalledWith('Naboo');

    console.log.mockRestore();
  });
});
