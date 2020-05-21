#!/usr/bin/python
# -*- coding: utf-8 -*-

#IMPORTANT - Counter has to start from 1  (NOT 0!!!)
import json, os, path
import numpy as np


def save_operation(matrix1, matrix2, sign, result, counter):
    prepare_memory(counter)
    operation_dict = {"mat1": matrix1.tolist(),
                      "mat2": matrix2.tolist(),
                      "sign": sign,
                      "res": result.tolist()}
    filename = "./memory/operation_memory_{}.json".format(counter)
    json_dict = json.dumps(operation_dict)
    with open(filename,"w") as file:
        file.write(json_dict)



