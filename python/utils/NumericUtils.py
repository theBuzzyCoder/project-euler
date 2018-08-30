#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To run doctest's unittest use
python3 -m doctest NumericUtils.py -v
"""
from functools import reduce


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


def factorial(number: int) -> int:
    """
    In the first loop, x is 2 the first element and the second element i.e 3 is y.
    Second loop onwards, x is the result of lambda function and y is the next elements
    that come after the current y value.
    Execution order for [1, 2, 3, 4, 5]
    ((((1 * 2) * 3) * 4) * 5)

    >>> factorial(5)
    120
    >>> factorial(4)
    24
    """
    return reduce(lambda x, y: x * y, range(1, number + 1))

def isPrime(number: int) -> bool:
    """
    Wilsons theorm for checking prime numbers states that
    any number(n) is a prime only when
    (n - 1)! == (-1 % n)

    >>> isPrime(4)
    False
    >>> isPrime(2)
    True
    >>> isPrime(101)
    True
    """
    return (factorial(number - 1) % number) == (-1 % number)
