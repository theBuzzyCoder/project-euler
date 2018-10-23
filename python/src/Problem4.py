#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Problem4:
	def test_for_palindrome(self , string_input : str ):
		return string_input == string_input[::-1]
	def process_pre_palindrome( self , integer_input: int ):
		return self.test_for_palindrome( str(integer_input) )
	def get_products( self , min : int , max : int):
		products = []
		for i in range( min , max+1 ):
			for j in range( min , max+1 ):
				products.append( i * j )
		return products
	def Largest_palindrome_product(self , min : int , max : int):
		list_of_products = self.get_products(min,max)
		list_of_palindromes = list( filter( self.process_pre_palindrome , list_of_products ) )
		return list_of_palindromes

if __name__ == "__main__":
    p4 = Problem4()
    ##print( p4.test_for_palindrome("malayalam") )
    ##print( p4.get_products(100,999) )
    print( max( p4.Largest_palindrome_product(100,999) ) )