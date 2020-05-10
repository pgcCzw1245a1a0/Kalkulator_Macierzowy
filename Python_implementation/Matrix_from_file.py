import numpy as np


def check_data_type(matrix):    #checking if matrix include float type number or only int
    for rows in matrix:
        for col in rows:
            if col.find('.') != -1:
                return True

    return False


def read_matrix(file):
    temp_matrix = open(file).read()
    matrix = [item.split() for item in temp_matrix.split("\n")[:-1]]   #read as strings

    if check_data_type(matrix) == True:  #type conversion from string --> int/float
        result = [list(map(float, i)) for i in matrix]
    else:
        result = [list(map(int, i)) for i in matrix]

    file.close(file)
    return result


def close_file(file):
    file.close()



