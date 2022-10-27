# Sort and Comparator Functions

This is an implementation of using comparator functions with the sort method to sort nested data structures by any property.

[Link to Code](./sort.js)

## Challenge

- Implement the functions sortYear, sortTitle, and inGenre in the file sort.ts.
  - Execute your tests while developing using npm run watch
  - Execute your tests in CI using npm test
- Functions:
  - sortYear
    - Arguments: movies array
    - Sorts the input array by year, in ascending order.
  - sortTitle
    - Arguments: movies array
    - Sorts the input array by title, ignoring "The " at the beginning of titles.
  - inGenre
    - Arguments: movies array, genre string
    - Filters the input array, returning only those movies who include genre.

## Approach & Efficiency

sortYear

- Time Complexity: linear O(n)
- Space Complexity: constant O(1)

sortTitle

- Time Complexity: linear O(n)
- Space Complexity: constant O(1)

inGenre

- Time Complexity: linear O(n)
- Space Complexity: constant O(1)
