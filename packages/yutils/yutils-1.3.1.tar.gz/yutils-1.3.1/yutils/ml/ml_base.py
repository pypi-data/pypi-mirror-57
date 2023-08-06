#!%PYTHON_HOME%\python.exe
# coding: utf-8
# version: python37

import numpy as np

from yutils.base import InputChecker
from yutils.tools.numpy_tools import to_array, is_matrix


class MLObject(InputChecker):
    def _verbose_print(self, message):
        if self.verbose:
            print(message)

    @staticmethod
    def _add_ones(array):
        if is_matrix(array):
            column_of_ones = np.ones(shape=(array.shape[0], 1))
            return np.append(column_of_ones, array, axis=1)
        if len(array.shape) == 1:
            return np.append([1], array)
        return np.append([[1]], array, axis=0)



def create_data_from_text_file(path):
    data = [line.split(',') for line in open(path, 'r').read().splitlines()]
    features = to_array([line[:-1] for line in data], turn_str_items_to_numeric=True)
    results = to_array([line[-1] for line in data], turn_str_items_to_numeric=True)
    return features, results
