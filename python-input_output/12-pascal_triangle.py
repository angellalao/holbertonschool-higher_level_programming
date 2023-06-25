#!/usr/bin/python3
"""
module with function that returns pascals triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists representing pascals triangle of n """
    list = []
    if n <= 0:
        return list

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]

        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)

        triangle.append(row)
    return triangle
