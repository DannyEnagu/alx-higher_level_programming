#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes the square value of all intergers of a matrix

       Args:
        @matrix: A 2D array of integer

       Return:
        A new metrix of integers
    """
    new_matrix = []

    for i in range(0, len(matrix)):
        sub_arr = []
        for j in range(0, len(matrix[i])):
            sub_arr.append(matrix[i][j] ** 2)
        new_matrix.append(sub_arr)

    return new_matrix
