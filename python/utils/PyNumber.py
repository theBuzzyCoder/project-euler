#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PyNumber(object):
    """
    Custom numbers class that provides mathematical functionalities of a number.
    """

    def __init__(self, number: int):
        self.theNumber = number

    @staticmethod
    def isDivisible(dividend: int, divisor: int) -> bool:
        """
        Checks if the number is divisible by the divisor.
        """
        assert divisor != 0
        return (dividend % divisor == 0)
