import unittest
import pandas as pd
from app.io.input import read_file_builtin, read_file_pandas

class TestInputFunctions(unittest.TestCase):

# successfull test (reading from a file .txt that exists)
    def test_read_file_builtin_success(self):
        content = read_file_builtin('test_builtin.txt')
        self.assertEqual(content, 'I love NaUKMA <3')

# test for a file that does not exist
    def test_read_file_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_builtin('non_existent_file.txt')

# test for an empty file
    def test_read_file_builtin_empty_file(self):
        content = read_file_builtin('empty_builtin.txt')
        self.assertEqual(content, '')

# successfull test (reading from a file .csv that exists)
    def test_read_file_pandas_success(self):
        content = read_file_pandas('test_pandas.csv')
        expected_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        actual_df = pd.read_csv('test_pandas.csv')
        pd.testing.assert_frame_equal(actual_df, expected_df)

# test for a file that does not exist
    def test_read_file_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas('non_existent_file.csv')

# test for an empty file
    def test_read_file_pandas_empty_file(self):
        content = read_file_pandas('empty.csv')
        self.assertEqual(content.strip(), 'Empty DataFrame\nColumns: []\nIndex: []')

if __name__ == '__main__':
    unittest.main()