"""
    Functional and unit tests for the utils.py module developed in hw 3.
    This script will test the linear and binary search functions and the
    list indexing function.
"""
import os
import sys
import csv
import unittest
import numpy as np
import pandas as pd
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
        cls.empty_file = 'empty.csv'
        cls.matrix_file_name = 'test_matrix.csv'
        cls.rows = [['0', '1', '2'], ['3', '4', '5']]
        with open(cls.csv_file, 'w', newline='',
                  encoding='utf-8') as cls.csv_file:
            writer = csv.writer(cls.csv_file, dialect='excel')
            writer.writerows(cls.rows)
        with open('empty.csv', 'w', encoding='utf-8') as cls.empty_file:
            pass
        cls.matrix_data = pd.DataFrame(cls.rand_matrix)
        cls.matrix_file = cls.matrix_data.to_csv(cls.matrix_file_name)

    @classmethod
    def tearDownClass(cls):
        """tearDownClass to remove all of the data that was setup in the
        setUpClass function
        """
        cls.num_rows = None
        cls.num_columns = None
        cls.rand_matrix = None
        cls.rand_int = None
        cls.matrix_data = None
        cls.matrix_file = None
        os.remove('test.csv')
        os.remove('empty.csv')
        os.remove('test_matrix.csv')
        os.remove('matrix.csv')
        os.remove('file3.csv')

    def test_get_random_matrix_equals(self):
        """Tests for the get random matrix function. AssertAlmostEqual to
        check the matrix is being created properly. AssertEqual check the shape
        of each matrix
        """
        self.assertAlmostEqual(
            dp.get_random_matrix(int(self.num_rows),
                                 int(self.num_columns)).all(),
            self.rand_matrix.all(), places=4)
        self.assertEqual(
            dp.get_random_matrix(int(self.num_rows),
                                 int(self.num_columns)).shape,
            self.rand_matrix.shape)

    def test_get_random_matrix_raises(self):
        """Tests for the get random matrix function. AssertRaises to make sure
        the inputs are > 0.
        """
        with self.assertRaises(TypeError):
            dp.get_random_matrix(self.rand_int, self.rand_int)
            dp.get_random_matrix(-1*(self.rand_int), -1*(self.rand_int))
            dp.get_random_matrix()

    def test_get_file_dimensions_equals(self):
        """Tests for the get_file_dimensions function. AssertEqual to check
        that the csv file's dimensions are being calculated correctly.
        """
        csv_file = np.loadtxt('test.csv', delimiter=',')
        self.assertEqual(dp.get_file_dimensions('test.csv'), csv_file.shape)

    def test_get_file_dimensions_raises(self):
        """Tests for the get_file_dimensions function. AssertRaises to make
        sure that the datafile is populated. AssertRaises ValueError to check
        that an error is raised for an empty file
        """
        with self.assertRaises(ValueError):
            dp.get_file_dimensions(self.empty_file)
        with self.assertRaises(TypeError):
            dp.get_file_dimensions()

    def test_write_matrix_to_file_check_contents(self):
        """Tests for the write_matrix_to_file function to check that the
        matrix is created correctly. Check that the file is populated with
        information.
        """
        write_matrix_to_file = dp.write_matrix_to_file(int(self.num_rows),
                                                       int(self.num_columns),
                                                       'matrix.csv')
        with open('matrix.csv', 'r') as f1, open('test_matrix.csv', 'r') as f2:
            fileone = pd.read_csv('matrix.csv')
            filetwo = pd.read_csv('test_matrix.csv')

        with open('file3.csv', 'w') as outFile:
            for line in fileone:
                if line not in filetwo:
                    raise Exception("The produced files aren't the same")

    def test_write_matrix_to_file_raises(self):
        """Tests for the write_matrix_to_file function. AssertRaises for
        different TypeErrors
        """
        with self.assertRaises(TypeError):
            dp.write_matrix_to_file()
            dp.write_matrix_to_file(None, None, 'fake.csv')
            dp.write_matrix_to_file('a', 'd', 'fake.csv')


if __name__ == '__main__':
    unittest.main()
