#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .PyNumber import PyNumber

class PyNumberSeries(object):

    fibonacciSeries = []

    @classmethod
    def loopFibonacci(cls, first: PyNumber = PyNumber(0), second: PyNumber = PyNumber(1)) -> list:
        """
        Fibonacci is a number series which is evaluated using below algorithm
        Fibonacci(0th item) is 0
        Fibonacci(1st item) is 1
        Fibonacci(nth item) is Fibonacci((n-1)th item) + Fibonacci((n-2)th item)

        This particular function doesn't have a limit for the number iterations.
        The loop limiter should be the caller rather than the callee.

        By default the start point is from 0, 1. However this can be changed based on the needs.

        >>> fibonacciGenerator = PyNumberSeries.loopFibonacci(); [next(fibonacciGenerator) for i in range(5)]
        [0, 1, 1, 2, 3]

        >>> fibonacciGenerator = PyNumberSeries.loopFibonacci(); [next(fibonacciGenerator) for i in range(8)]
        [0, 1, 1, 2, 3, 5, 8, 13]

        >>> fibonacciGenerator = PyNumberSeries.loopFibonacci(); [next(fibonacciGenerator) for i in range(10)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        """
        i = 0
        cls.fibonacciSeries.append(first)
        yield first  # This is to yield the 0th item
        while True:
            # When the loop begins, it will yield the second item and as the loop proceeds
            # it will yield the next items
            cls.fibonacciSeries.append(second)
            yield second
            first, second = second, first + second

    def getNthFibonacci(self, nthLimiter: int) -> PyNumber:
        """
        Returns the nth Fibonacci number

        >>> PyNumberSeries().getNthFibonacci(5)
        3
        >>> PyNumberSeries().getNthFibonacci(10)
        34
        >>> PyNumberSeries().getNthFibonacci(8)
        13
        >>> PyNumberSeries.fibonacciSeries
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        """
        try:
            return self.fibonacciSeries[(nthLimiter - 1)]
        except IndexError:
            pass

        if self.fibonacciSeries:
            start = len(self.fibonacciSeries) - 2
            second = self.fibonacciSeries.pop()
            first = self.fibonacciSeries.pop()
            fibonacciGenerator = self.loopFibonacci(first=first, second=second)
        else:
            start = 0
            fibonacciGenerator = self.loopFibonacci()

        nthElement = PyNumber(0)
        assert start < nthLimiter
        for i in range(start, nthLimiter):
            nthElement = next(fibonacciGenerator)
        assert nthElement != 0
        return nthElement

    def getFibonacciSeriesUpto(self, maxValue: int, first: int = 0, second: int = 1) -> list:
        if self.fibonacciSeries:
            if (self.fibonacciSeries[-1] > maxValue):
                return filter(lambda number: number < maxValue, self.fibonacciSeries)
            start = len(self.fibonacciSeries) - 2
            second = self.fibonacciSeries.pop()
            first = self.fibonacciSeries.pop()
            fibonacciGenerator = self.loopFibonacci(first=first, second=second)
        else:
            start = 0
            first, second = PyNumber(first), PyNumber(second)
            fibonacciGenerator = self.loopFibonacci(first, second)

        while (next(fibonacciGenerator) < maxValue):
            pass
        return iter(self.fibonacciSeries)
