#!/usr/bin/python3

"""
 function that returns a list of lists of  integers;
 representing the Pascal's triangle of (n)

 if n <= 0 return  an empty list
 Assume n will always be an integer



"""


def pascal_triangle(n):
    """
    return a list of lists of integers representing the pascal's triangle
    if n <= 0 return an empty list

    """
    if n <= 0:
        return []
    else:

        triangle = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
    return triangle
