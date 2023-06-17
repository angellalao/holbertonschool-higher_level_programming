#!/usr/bin/python3

"""
Module contains a function to perform division on a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a number.

    Arguments:
    - matrix: A matrix (list of lists) containing integers or floats.
    - div: A number (integer or float) to divide the matrix elements by.

    Returns:
    - A new matrix with each element divided by the given number,
      rounded to two decimal places.

    Raises:
    - TypeError: If the matrix is not a valid matrix (list of lists)
                 containing integers or floats, or if the div is not a number.
    - ZeroDivisionError: If the div is zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    row_size = len(matrix[0])
    if type(matrix) != list:
        raise TypeError(error_msg)
    for row in matrix:
        if type(row) != list:
            raise TypeError(error_msg)
        for num in row:
            if type(num) != int and type(num) != float:
                raise TypeError(error_msg)
    for row in matrix[1:]:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero ")

    for row in matrix:
        new_row = []
        for num in row:
            new_num = round(num / div, 2)
            new_row.append(new_num)
        new_matrix.append(new_row)
    return new_matrix
