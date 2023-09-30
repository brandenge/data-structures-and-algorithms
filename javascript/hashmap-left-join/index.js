'use strict';

const hashMapLeftJoin = (hashMap1, hashMap2) => {
  return Array.from(hashMap1.keys()).map(key => {
    return [key, hashMap1.get(key), hashMap2.get(key)];
  });
};

module.exports = hashMapLeftJoin;
