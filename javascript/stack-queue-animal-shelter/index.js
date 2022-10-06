'use strict';

class Animal {
  constructor(value) {
    this.type = value;
    this.next = null;
  }
}

class AnimalShelter {
  constructor() {
    this.front = null;
    this.back = null;
  }

  enqueue(animal) {
    if (animal.type !== 'cat' && animal.type !== 'dog') return;
    if (!this.back) {
      this.back = animal;
      this.front = animal;
    } else {
      this.back.next = animal;
      this.back = animal;
    }
  }

  dequeue(pref) {
    if (pref !== 'dog' && pref !== 'cat') return null;
    if (!this.front) return null;
    if (this.front.type === pref) {
      const temp = this.front;
      this.front = this.front.next;
      temp.next = null;
      if (this.back === temp) this.back = null;
      return temp;
    }
    if (!this.front.next) return null;
    let prev = this.front;
    let current = this.front.next;
    while (current.type !== pref) {
      if (!current.next) return null;
      current = current.next;
      prev = prev.next;
    }
    prev.next = current.next;
    current.next = null;
    if (this.back === current) this.back = prev;
    return current;
  }
}

module.exports = { Animal, AnimalShelter };
