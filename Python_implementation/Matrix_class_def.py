#TODO

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def dim(self):  #return dimention of matrix [rows x columns]
        dimention = []
        dimention.append(len(self.matrix))
        dimention.append(len(self.matrix[0]))

        return dimention
