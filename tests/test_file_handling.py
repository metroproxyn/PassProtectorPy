import os
import unittest
from src.file_handling import FileHandling

class TestFileHandling(unittest.TestCase):

    def setup(self):
        self.test_file = 'test.txt'
        self.file_handling = FileHandling()
    
    def tearDown(self):
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)
    
    def test_write_to_file(self):
        #TODO: add more functionality
        content = "Test content"
    
    def test_read_to_file(self):
        #TODO: add more functionality
        content = "Test content"
    
    def test_file_exists(self):
        #TODO: add more functionality

if __name__ == '__main__':
    unittest.main()