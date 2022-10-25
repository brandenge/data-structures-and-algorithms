# Insertion Sort


## Pseudo Code

```pseudocode
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace


## Efficiency

Time Complexity: Quadratic - O(n ^ 2)
Space Complexity: Constant - O(1), because the input array is being mutated in-place (i.e. it is a destructive operation) and not copied.

Pseudocode Source: Code Fellows
