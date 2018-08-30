#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from src.Problem1 import Problem1


class TestProblem1(unittest.TestCase):

    def setUp(self):
        self.problem1 = Problem1()

    def test_one(self):
        self.assertEqual(self.problem1.calculateMultiplesSum(10), 23)

    def test_two(self):
        self.assertEqual(self.problem1.calculateMultiplesSum(1000), 233168)

    def tearDown(self):
        del self.problem1


if __name__ == '__main__':
    unittest.main()
