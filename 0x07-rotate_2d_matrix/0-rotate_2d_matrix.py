#!/usr/bin/python3
"""module to rotate a matrix"""


def rotate_2d_matrix(matrix):
    """rotates 90 degrees clockwise"""
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    # reverse
    for row in matrix:
        row.reverse()
    return matrix
