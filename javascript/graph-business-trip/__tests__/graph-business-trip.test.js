'use strict';

const businessTrip = require('../index');
const Graph = require('../../graph/index');

describe('Tests for the businessTrip function', () => {

  const graph = new Graph();

  const pandora = graph.addNode('Pandora');
  const arendelle = graph.addNode('Arendelle');
  const metroville = graph.addNode('Metroville');
  const monstropolis = graph.addNode('Monstropolis');
  const narnia = graph.addNode('Narnia');
  const naboo = graph.addNode('Naboo');

  graph.addEdge(pandora, arendelle, 150);
  graph.addEdge(pandora, metroville, 82);
  graph.addEdge(metroville, pandora, 82);
  graph.addEdge(arendelle, metroville, 99);
  graph.addEdge(arendelle, monstropolis, 42);
  graph.addEdge(metroville, narnia, 37);
  graph.addEdge(metroville, naboo, 26);
  graph.addEdge(metroville, monstropolis, 105);
  graph.addEdge(monstropolis, naboo, 73);
  graph.addEdge(narnia, naboo, 250);

  it('Returns null when a trip with a single connection is not possible', () => {
    expect(businessTrip(graph, ['Naboo', 'Pandora'])).toEqual(null);
  });

  it('Returns null when a trip with multiple connections is not possible', () => {
    expect(businessTrip(graph, ['Narnia', 'Arendelle', 'Naboo'])).toEqual(null);
  });

  it('Returns the correct dollar sum for a trip with a single connection', () => {
    expect(businessTrip(graph, ['Metroville', 'Pandora'])).toEqual('$82');
  });

  it('Returns the correct dollar sum for a trip with multiple connections', () => {
    expect(businessTrip(graph, ['Arendelle', 'Monstropolis', 'Naboo'])).toEqual('$115');
  });
});
