#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from src.Problem1 import Problem1

class TestProblem1(object):
    def test_one(self):
        assert Problem1().calculateMultiplesSum(10) == 23

    def test_two(self):
        assert Problem1().calculateMultiplesSum(1000) == 233168
