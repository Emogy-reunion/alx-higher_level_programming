#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        temp = [1]
        for i in range(len(tria) - 1):
            temp.append(tria[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
