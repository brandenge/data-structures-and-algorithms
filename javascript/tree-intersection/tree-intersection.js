'use strict';

const HashMap = require('../hash-table/index');

function treeIntersection(tree1, tree2) {
  if (!tree1.root || !tree2.root) return [];
  const hashMap = treeToHashMap(tree1.root, new HashMap(1024));
  return getCommonValues(tree2.root, hashMap, []);
}

function treeToHashMap(current, hashMap) {
  if (current.left) treeToHashMap(current.left, hashMap);
  hashMap.set((current.value).toString(), 1);
  if (current.right) treeToHashMap(current.right, hashMap);
  return hashMap;
}

function getCommonValues(current, hashMap, results) {
  if (current.left) getCommonValues(current.left, hashMap, results);
  if (hashMap.has((current.value).toString())) results.push(current.value);
  if (current.right) getCommonValues(current.right, hashMap, results);
  return results;
}

module.exports = { treeIntersection, treeToHashMap, getCommonValues };
