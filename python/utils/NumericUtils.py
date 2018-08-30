#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To run doctest's unittest use
python3 -m doctest NumericUtils.py -v
"""

def isDivisible(dividend: int, divisor: int) -> bool:
    """
    Checks if the number is divisible by the divisor.

    >>> isDivisible(4, 5)
    False
    >>> isDivisible(15, 5)
    True
    """
    assert divisor != 0
    return ((dividend % divisor) == 0)


def isEven(number: int) -> bool:
    """
    Checks if the given number is even or odd.

    >>> isEven(4)
    True
    >>> isEven(3)
    False
    >>> not isEven(3)
    True
    """
    return ((number % 2) == 0)
