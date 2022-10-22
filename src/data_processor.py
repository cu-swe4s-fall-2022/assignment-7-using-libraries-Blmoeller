"""

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
"""
import sys
import pandas as pd
import numpy as np
sys.path.append('..')


def get_random_matrix(num_rows, num_columns):
    """Creates a random matrix of floats from the range of (0, 1] with the
    number of rows and columns as input parameters

    Args:
        num_rows (int): number of rows, integer > 0
        num_columns (int): number of columns, integer > 0

    Returns:
        List: A random matrix of floats from the range of (0, 1]
    """
    if num_rows < 0:
        raise TypeError
    if num_rows == float:
        raise TypeError
    if num_columns < 0:
        raise TypeError
    if num_columns == float:
        raise TypeError

    np.random.seed(1)
    rand_matrix = np.random.rand(num_rows, num_columns)
    return rand_matrix


def get_file_dimensions(file_name):
    csv_file = pd.read_csv('iris.data', sep=',' , header=None)
    file_dim = csv_file.shape
    return file_dim


def write_matrix_to_file(num_rows, num_columns, file_name):
    return None
