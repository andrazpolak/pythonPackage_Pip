from example_package.example import *

import unittest


class TestExample(unittest.TestCase):
    def test_first(self):
        self.assertAlmostEqual(add_one(2), 3)
        # self.assertAlmostEqual(add_one(2), 4)
