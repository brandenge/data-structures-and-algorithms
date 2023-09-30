# Hash Map Left Join

This is an implementation of a function that takes 2 hash maps as arguments and LEFT JOINs them into a single data structure.

[Link to Code](./index.js)

## Challenge

- Write a function called left join
- Arguments: two hash maps
- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Approach & Efficiency

Time Complexity:

- Linear - O(n) - the more keys there are in the hash, the more we must iterate through. And all the operations within each iteration are constant time.

Space Complexity:

- Linear - O(n) - the more keys there are in the hash, the proportionally bigger the constructed two-dimensional array that is being returned will be

## Solution / Whiteboard

![Code Challenge 33 Whiteboard](./code-challenge-33.png)
