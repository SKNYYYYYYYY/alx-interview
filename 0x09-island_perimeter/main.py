#!/usr/bin/env python3

island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__=='__main__':
  grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ]
  perimeter = island_perimeter(grid)
  print(perimeter)