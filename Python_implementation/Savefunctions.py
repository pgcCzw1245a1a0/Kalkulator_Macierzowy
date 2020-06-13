#!/usr/bin/python
# -*- coding: utf-8 -*-

#IMPORTANT - Counter has to start from 1  (NOT 0!!!)
import json, os, path
import numpy as np


def save_operation(matrix1, matrix2, sign, result, counter):                         #operacja zapisywania, przyjmuje macierze, działanie, macierz wynikową i licznik)
    prepare_memory(counter)
    operation_dict = {"mat1": matrix1.tolist(),                                      #tworzenie słownika
                      "mat2": matrix2.tolist(),
                      "sign": sign,
                      "res": result.tolist()}
    filename = "./memory/operation_memory_{}.json".format(counter)                   #zamiana słownika na json_dict
    json_dict = json.dumps(operation_dict)
    with open(filename,"w") as file:
        file.write(json_dict)


def load_operation(cnt):    #funkcja otrzymuje licznik, ktory okresla ktora macierz chcemy wczytac
    filename = "./memory/operation_memory_{}.json".format(cnt)   #koncowka (cnt) okresla ktora macierz chcemy zaladowac
    with open(filename, "r") as file:
        file_content = file.read()                                                  #wczytanie pliku
        op_dict = json.loads(file_content)                                          #zamienienie jsona na format do odczytu
        return op_dict


def prepare_memory(counter):
    if not os.path.exists("./memory"):                                              #przy pierwszym zadaniu tworzy folder memory
        os.mkdir("./memory")                                                        #^^^^
    if counter > 10:
        os.remove("./memory/operation_memory_{}.json".format(counter - 10))         #Jeśli jest więcej niż 10 zadań to usuwane jest najstarsze


def delete_operation(id):                                                           #funkcja usuwa zadanie o podanym ID
    if os.path.exists("./memory"):
        os.remove("./memory/operation_memory_{}.json".format(id))
    else:
        print("File does not exist!")


# mat1 = np.array([[2,2], [2,3]])
# mat2 = np.array([[2,2], [2,4]])
# result = mat1 @ mat2
# save_operation(mat1, mat2, "@", result, 1)
# load_operation(1)

# test for i in range(2,14):
#     save_operation(mat1, mat2, "@", result, i)
#     load_operation(i)




