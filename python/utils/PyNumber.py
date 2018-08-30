#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PyNumber(int):
    """
    Custom numbers class that provides mathematical functionalities of a number.
    """

    def __init__(self, number: int):
        self.__theNumber = number

    # I overloaded operators before inheriting the int as parent class.
    # def __int__(self):
    #     """
    #     >>> int(PyNumber(4))
    #     4
    #     """
    #     return self.__theNumber
    #
    # def __float__(self):
    #     """
    #     >>> float(PyNumber(4))
    #     4.0
    #     """
    #     return self.__theNumber * 1.0
    # def __add__(self, obj: PyNumber) -> PyNumber:
    #     return PyNumber(self.__theNumber + int(obj))
    #
    # def __sub__(self, obj: PyNumber) -> PyNumber:
    #     return PyNumber(self.__theNumber - int(obj))
    #
    # def __mul__(self, obj: PyNumber) -> PyNumber:
    #     return PyNumber(self.__theNumber * float(obj))
    #
    # def __truediv__(self, obj: PyNumber) -> PyNumber:
    #     assert int(obj) != 0
    #     return PyNumber(self.__theNumber / float(obj))
    #
    # def __floordiv__(self, obj: PyNumber) -> PyNumber:
    #     assert int(obj) != 0
    #     return PyNumber(self.__theNumber // float(obj))
