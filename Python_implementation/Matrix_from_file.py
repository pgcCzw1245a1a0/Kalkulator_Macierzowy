import numpy as np

def check_data_type(matrix):    #checking if matrix include float type number or only int
    for rows in matrix:
        for col in rows:
            if col.find('.') != -1:
                return True
            else:
                continue
    return False


def read_matrix(file):
    temp_matrix = open(file).read()
    matrix = [item.split() for item in temp_matrix.split("\n")[:-1]]   #read as strings

    if check_data_type(matrix) == True:  #type conversion from string --> int/float
        result = [list(map(float, i)) for i in matrix]
    else:
        result = [list(map(int, i)) for i in matrix]

    return result


def close_file(file):
    file.close()


matrix = read_matrix('macierz.txt')
print(matrix)
print(matrix[3][4] * matrix[2][1])

