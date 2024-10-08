#!/usr/bin/python3
"""
0x09-island_perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of an island
    """
    def count_horizontal_edges(matrix):
        """
        return number of edges along horizontal direction
        """
        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i-1]
        return count

    transposed_grid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            transposed_grid[i].append(item)

    return count_horizontal_edges(
            grid) + count_horizontal_edges(transposed_grid)
