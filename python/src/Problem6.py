#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Problem6:
	def sum_squares( self , input_list : list ):
		return sum([ i ** 2 for i in input_list ])
	def sum_square_difference( self , limit : int):
		input_list = range( limit+1 )
		sum_list = sum( input_list ) ** 2
		##print( sum_list )
		sum_squares = self.sum_squares( input_list )
		##print( sum_squares )
		return abs( sum_squares - sum_list )

if __name__ == "__main__":
    p6 = Problem6()
    print( p6.sum_square_difference(100) )