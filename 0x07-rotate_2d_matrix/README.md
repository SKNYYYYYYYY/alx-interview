
# Rotate 2D Matrix

This Python module provides a function to rotate a 2D matrix 90 degrees clockwise **in-place**, meaning it modifies the original matrix without using extra space for another matrix.

## Function

```python
rotate_2d_matrix(matrix)
```

### Parameters:

* `matrix` (list of list of ints): A square 2D matrix (NxN) to be rotated.

### Description:

* The function first transposes the matrix (swapping rows with columns).
* Then, it reverses each row to complete the 90-degree clockwise rotation.

### Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

# Result:
# matrix becomes:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
```

## Usage

Run the script or import the function in another Python file:

