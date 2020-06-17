#TODO
from numpy import *
from typing import TypeVar


class Matrix:

    def __init__(self, matrix):
        super.__init__(*args, **kwargs)
        self.matrix = array(matrix)


    def dim(self):  #return dimention of matrix [rows x columns]
        return self.matrix.shape

    def transpose(self): #return transposed matrix
        return self.matrix.transpose()

Matrix = TypeVar("Matrix", bound= Matrix)


def multiplication(matrix_1: Matrix, matrix_2: Matrix)-> Matrix:
    try
    _, c1 = matrix_1.dim
    r2, _ = matrix_2.dim
    if(c1 != r2):
        raise ValueError("Wrong size of matrix")
    except ValueError("Wrong size of matrix")

    return matrix_1 @ matrix_2


def addition(matrix_1: Matrix, matrix_2: Matrix)-> Matrix: #TO DO check if matrix is nxn
    try
    r1, c1 = matrix_1.dim
    r2, c2 = matrix_2.dim
    if(c1 != c2 and r1 != r2):
        raise ValueError("Wrong size of matrix")
    except ValueError("Wrong size of matrix")

    return matrix_1 + matrix_2


def subrtaction(matrix_1: Matrix, matrix_2: Matrix)-> Matrix: #TO DO check if matrix is nxn
    try
    r1, c1 = matrix_1.dim
    r2, c2 = matrix_2.dim
    if(c1 != c2 and r1 != r2):
        raise ValueError("Wrong size of matrix")
    except ValueError("Wrong size of matrix")

    return matrix_1 - matrix_2