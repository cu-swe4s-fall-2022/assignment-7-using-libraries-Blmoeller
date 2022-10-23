"""A set 3 functions: get_random_matrix, get_file_dimensions, and
get_file_dimensions that complete various operations for creating a random
matrix, calculating the dimensions of a csv file, and creating a csv file that
contains a matrix of random values
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

    Raises:
        TypeError: For variable num_rows  -- Sorry No numbers below zero
        TypeError: For variable num_rows  -- Sorry, no floats allowed.
        Must be an integer
        TypeError: For variable num_columns  -- Sorry No numbers below zero
        TypeError: For variable num_columns -- Sorry, no floats
        allowed. Must be an integer

    Returns:
        List: A random matrix of floats from the range of (0, 1]
    """
    if num_rows < 0:
        raise TypeError("Sorry, no numbers below zero")
    if num_rows == float:
        raise TypeError("Sorry, no floats allowed. Must be an integer")
    if num_columns < 0:
        raise TypeError("Sorry, no numbers below zero")
    if num_columns == float:
        raise TypeError("Sorry, no floats allowed. Must be an integer")
    np.random.seed(1)
    rand_matrix = np.random.rand(num_rows, num_columns)
    return rand_matrix


def get_file_dimensions(file_name):
    """Function to calculate the dimensions of a specified csv file

    Args:
        file_name (str): The file name (or path) for a certain file

    Returns:
        list: Returns an array with the dimensions of the file
    """
    csv_file = pd.read_csv(file_name, sep=',', header=None)
    file_dim = csv_file.shape
    return file_dim


def write_matrix_to_file(num_rows, num_columns, file_name):
    """Creates a random matrix of floats from the range of (0, 1] with the
    number of rows and columns as input parameters

    Args:
        num_rows (int): number of rows, integer > 0
        num_columns (int): number of columns, integer > 0
        file_name (str): The name of the file that you would like to output

    Raises:
        TypeError: For variable num_rows  -- Sorry No numbers below zero
        TypeError: For variable num_rows  -- Sorry, no floats allowed.
        Must be an integer
        TypeError: For variable num_columns  -- Sorry No numbers below zero
        TypeError: For variable num_columns -- Sorry, no floats
        allowed. Must be an integer

    Returns:
        List: A random matrix of floats from the range of (0, 1] and writes
        this matrix to a csv file
    """
    if num_rows < 0:
        raise TypeError("Sorry, no numbers below zero")
    if num_rows == float:
        raise TypeError("Sorry, no floats allowed. Must be integer")
    if num_columns < 0:
        raise TypeError("Sorry, no numbers below zero")
    if num_columns == float:
        raise TypeError("Sorry, no floats allowed. Must be integer")
    np.random.seed(1)
    rand_matrix = np.random.rand(num_rows, num_columns)
    rand_matrix = pd.DataFrame(rand_matrix)
    rand_matrix.to_csv(file_name)
    return rand_matrix
