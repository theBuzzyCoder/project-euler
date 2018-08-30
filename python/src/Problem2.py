#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from utils.PyNumberSeries import PyNumberSeries
from utils.NumericUtils import isEven


class Problem2(object):

    def getEvenFibonacciSeries(self, maxLimit: int):
        fibonacciSeries = PyNumberSeries().getFibonacciSeriesUpto(maxLimit)
        return filter(isEven, fibonacciSeries)

    def getSum(self, maxLimit: int):
        return sum(self.getEvenFibonacciSeries(maxLimit))

if __name__ == "__main__":
    p2 = Problem2()
    print(p2.getSum(4000000))
