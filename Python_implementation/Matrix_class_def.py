#TODO
from numpy import *


class Matrix:

    def __init__(self, matrix):
        self.matrix = array(matrix)

    def dim(self):  #return dimention of matrix [rows x columns]
        return self.matrix.shape

    def transpose(self): #return transposed matrix
        return self.matrix.transpose()


def multiplication(matrix_1, matrix_2):
    return matrix_1 @ matrix_2


def addition(matrix_1, matrix_2): #TO DO check if matrix is nxn
    return matrix_1 + matrix_2


def subrtaction(matrix_1, matrix_2): #TO DO check if matrix is nxn
    return matrix_1 - matrix_2