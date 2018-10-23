#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Problem5:
	lower = 0
	upper = 100
	def __init__( self , lower : int , upper : int ):
		self.lower = lower
		self.upper = upper
	def factors( self , input_i : int ):
		factors = []
		##print( input_i )
		for i in range( self.lower , self.upper+1 ):
			 if( input_i % i == 0 ):
			 	factors.append( i )
		##print(factors)
		return factors
	def smallest_multiple( self , upper_limit : int):
		for i in range( 20 , upper_limit+1 ):
			if( len( self.factors(i) ) == self.upper ):
				return i

if __name__ == "__main__":
    p5 = Problem5(1,20)
    print( p5.smallest_multiple(999999999999) )