#!/usr/bin/env python3
"""
A function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    topRow = [1]
    pascal = []
    y = [0]
    for x in range(n):
        pascal.append(topRow)
        topRow=[left+right for left,right in zip(topRow+y, y+topRow)]
    return pascal
