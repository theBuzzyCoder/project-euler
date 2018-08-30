#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from src.Problem2 import Problem2


class TestProblem2(unittest.TestCase):

    def setUp(self):
        self.problem2 = Problem2()

    def test_one(self):
        self.assertEqual(self.problem2.getSum(89), 44)

    def test_two(self):
        self.assertEqual(self.problem2.getSum(4000000), 4613732)

    def tearDown(self):
        del self.problem2


if __name__ == '__main__':
    unittest.main()
