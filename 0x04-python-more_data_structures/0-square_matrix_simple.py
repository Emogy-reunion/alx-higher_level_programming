#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    square_matrix = [[y ** 2 for y in row] for row in matrix]
    return square_matrix
