#!/usr/bin/python3

""" This module defines a function island_perimeter
that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    function that returns the perimeter of the island in grid

    Args:
        grid: A list of two integers, 0 and 1, 0 represents water
              1 represents land

        each cell is square, with a side liength of 1
        cells are connected horizontally/vertically not (diagonally)
        grid is rectangular with its width and height not exceeding 100
    """
    rows = len(grid)
    col = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(col):
            if grid[i][j] == 1:
                # Check each side
                if i == 0 or grid[i - 1][j] == 0:  # Top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == col - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1
    return perimeter
