#!/usr/bin/python3
"""2D Matrix Rotation"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix"""
    matrix.reverse()
    matrix_len = len(matrix)
    for i in range(matrix_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
