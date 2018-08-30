#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.PyNumber import PyNumber

class Problem1(object):
    def calculateMultiplesSum(self, uptoNumber: int):
        """
        If we list all the natural numbers below 10
        that are multiples of 3 or 5, we get 3, 5, 6 and 9.
        The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.
        """
        total = 0
        for i in range(uptoNumber):
            if PyNumber.isDivisible(i, 3) or PyNumber.isDivisible(i, 5):
                total += i
        return total


if __name__ == '__main__':
    print(Problem1().calculateMultiplesSum(1000))
