# Graphs

This is an implementation of a graph data structure.

[Link to Code](index.js)

## Challenge

Implement your own Graph. The graph should be represented as an adjacency list, and should include methods for the following actions:

- add node
- add edge
- get nodes
- get neighbors
- size

Write tests to prove the following functionality:

- Node can be successfully added to the graph
- An edge can be successfully added to the graph
- A collection of all nodes can be properly retrieved from the graph
- All appropriate neighbors can be retrieved from the graph
- Neighbors are returned with the weight between nodes included
- The proper size is returned, representing the number of nodes in the graph
- A graph with only one node and edge can be properly returned

## Approach & Efficiency

addNode

Time Complexity: Constant O(1)
Space Complexity: Constant O(1)

addEdge

Time Complexity: Constant O(1)
Space Complexity: Constant O(1)

getNodes

Time Complexity: Linear O(n)
Space Complexity: Linear O(n)

getNeighbors

Time Complexity: Linear O(n) - although the map key lookup is constant, we are then iterating over the keys to create an array with them
Space Complexity: Linear O(n) - a new array is being returned

size

Time Complexity: Constant O(1) - size is a property of the adjacency list map
Space Complexity: Constant O(1)

Bonus methods:

breadthFirstTraversal

Time Complexity: Quadratic O(n^2)
Space Complexity: Linear O(n)

depthFirstTraversal

Time Complexity: Quadratic O(n^2)
Space Complexity: Linear O(n)

## API

addNode

- Arguments: value
- Returns: The added node
- Adds a node to the graph

addEdge

- Arguments: 2 nodes to be connected by the edge, weight (optional)
- Returns: nothing
- Adds a new edge between two nodes in the graph
- If specified, assign a weight to the edge
- Both nodes should already be in the Graph

getNodes

- Arguments: none
- Returns all of the nodes in the graph as a collection (set, list, or similar)
- Empty collection returned if there are no nodes

getNeighbors

- Arguments: node
- Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- Empty collection returns if there are no nodes

size

- Arguments: none
- Returns the total number of nodes in the graph
- 0 if there are none

Credits:

- [Code Fellows Demo Code](https://github.com/codefellows/seattle-code-javascript-401d48/blob/main/class-35/inclass-demo/index.js)
