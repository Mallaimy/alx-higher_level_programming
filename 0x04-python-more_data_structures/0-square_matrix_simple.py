#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), i)) for i in matrix]
