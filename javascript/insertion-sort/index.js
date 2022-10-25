'use strict';

function insertionSort(arr) {
  for (let i = 1, len = arr.length; i < len; i++) {
    let j = i - 1;
    let temp = arr[i];
    while (j >= 0 && temp < arr[j]) {
      arr[j + 1] = arr[j];
      j -= 1;
    }
    arr[j + 1] = temp;
  }
}

module.exports = insertionSort;
