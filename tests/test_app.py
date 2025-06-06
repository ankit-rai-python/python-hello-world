import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app import say_hello

class TestApp(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello("Ankit"), "Hello, Ankit!")

if __name__ == "__main__":
    unittest.main()
