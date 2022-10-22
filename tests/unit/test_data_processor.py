"""
    Functional and unit tests for the utils.py module developed in hw 3.
    This script will test the linear and binary search functions and the
    list indexing function.
"""
import os
import sys
import unittest
import numpy as np
import csv
sys.path.append('src')
import data_processor as dp  # nopep8


class TestUtils(unittest.TestCase):
    """Class to test the three functions in the utils.py script
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass to include all of the needed random data to test the
        different functions
        """
        cls.num_rows = np.random.randint(low=1, high=10, size=1,
                                         dtype=int)
        cls.num_columns = np.random.randint(low=1, high=10, size=1,
                                            dtype=int)
        np.random.seed(1)
        cls.rand_matrix = np.random.rand(int(cls.num_rows),
                                         int(cls.num_columns))
        cls.rand_int = np.random.randint(low=1, high=10, size=1, dtype=int)
        cls.csv_file = 'test.csv'
        cls.rows = [['0', '1', '2'], ['3', '4', '5']]
        with open(cls.csv_file, 'w', newline='') as cls.csv_file:
            writer = csv.writer(cls.csv_file, dialect='excel')
            writer.writerows(cls.rows)

    @classmethod
    def tearDownClass(cls):
        """tearDownClass to remove all of the data that was setup in the
        setUpClass function
        """
        cls.num_rows = None
        cls.num_columns = None
        cls.rand_matrix = None
        cls.rand_int = None
        os.remove('test.csv')

    def test_get_random_matrix(self):
        """Tests for the get random matrix function. AssertAlmostEqual to
        check the matrix is being created properly. AssertRaises to make sure
        the inputs are > 0. AssertTrue check the shape of each matrix
        """
        self.assertAlmostEqual(
            dp.get_random_matrix(int(self.num_rows),
                                 int(self.num_columns)).all(),
            self.rand_matrix.all(), places=4)
        self.assertTrue(
            dp.get_random_matrix(int(self.num_rows),
                                 int(self.num_columns)).shape,
            self.rand_matrix.shape)
        with self.assertRaises(TypeError):
            dp.get_random_matrix(self.rand_int, self.rand_int)
            dp.get_random_matrix(-1*(self.rand_int), -1*(self.rand_int))

    def test_get_file_dimensions(self):
        """Tests for the get_file_dimensions function. AssertEqual to check
        that the csv file's dimensions are being calculated correctly.
        AssertRaises to make sure that the datafile is populated.
        """
        csv_file = np.loadtxt('test.csv', delimiter=',')
        self.assertTrue(dp.get_file_dimensions('test.csv'), csv_file.shape)


if __name__ == '__main__':
    unittest.main()
