'use strict';

function businessTrip(graph, cityNames) {
  let sum = 0;
  const nodes = graph.getNodes();
  const cityNodes = cityNames.map(name => {
    const index = nodes.findIndex(node => node.value === name);
    return nodes[index];
  });

  for (let i = 0, len = cityNames.length - 1; i < len; i++) {
    const edges = graph.getNeighbors(cityNodes[i]);
    const edgeIndex = edges.findIndex(edge => edge.node.value === cityNames[i + 1]);
    if (edgeIndex === -1) return null;
    else sum += edges[edgeIndex].weight;
  }
  if (sum === 0) return null;
  return `$${sum}`;
}

module.exports = businessTrip;
