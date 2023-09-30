'use strict';

function zipLists(list1, list2) {
  if ((!list1.head && !list2.head) || (list1.head && !list2.head)) return;
  else if (!list1.head) {
    list1.head = list2.head;
    return;
  }
  if (!list1.head.next) {
    list1.head.next = list2.head;
    return;
  } else if (!list2.head.next) {
    list2.head.next = list1.head.next;
    list1.head.next = list2.head;
    return;
  }
  let current1 = list1.head;
  let current2 = list2.head;
  while (current1.next || current2.next) {
    if (current1.next && current2.next) {
      const next1 = current1.next;
      const next2 = current2.next;
      current1.next = current2;
      current2.next = next1;
      current1 = next1;
      current2 = next2;
    } else if (!current1.next) {
      current1.next = current2;
      return;
    } else if (!current2.next) {
      current2.next = current1.next;
      break;
    }
  }
  current1.next = current2;
}

module.exports = { zipLists };
