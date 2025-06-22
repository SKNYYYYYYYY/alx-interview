#!/usr/bin/python3
"""2d matrix
"""


def island_perimeter(grid):
    """calculate perimetr of the land"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2
    return perimeter
