# Island Perimeter

This Python script calculates the perimeter of an island represented in a 2D grid. The island is made up of `1`s (land), and surrounded by `0`s (water). The grid is fully surrounded by water, and there is exactly one island.

## Usage

Ensure your grid is a list of lists with integers (0s and 1s), like so:

```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output will be the calculated perimeter
