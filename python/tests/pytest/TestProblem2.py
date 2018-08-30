#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from src.Problem2 import Problem2

class TestProblem2object):
    def test_one(self):
        assert Problem2().getSum(89) == 44

    def test_two(self):
        assert Problem2().getSum(4000000) == 4613732
