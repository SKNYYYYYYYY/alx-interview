#!/usr/bin/python3
"""
Module for generating Pascal's Triangle up to a given number of rows
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Trianlge of n rows
    Args:
			n: Number of rows in the triangle
    Returns:
			list: Pascal's Triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
