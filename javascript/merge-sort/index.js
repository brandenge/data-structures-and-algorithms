'use strict';

function mergeSort(arr) {
  const n = arr.length;

  if (n > 1) {
    const mid = Math.ceil(n / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
    mergeSort(left);
    mergeSort(right);
    return merge(left, right, arr);
  }
}

function merge(left, right, arr) {
  let i = 0, j = 0, k = 0;
  const leftLen = left.length, rightLen = right.length;

  while (i < leftLen && j < rightLen) {
    if (left[i] <= right[j]) {
      arr[k] = left[i];
      i++;
    } else {
      arr[k] = right[j];
      j++;
    }
    k++;
  }

  while (i < leftLen) {
    arr[k] = left[i];
    i++;
    k++;
  }
  while (j < rightLen) {
    arr[k] = right[j];
    j++;
    k++;
  }
  return arr;
}

module.exports = mergeSort;
