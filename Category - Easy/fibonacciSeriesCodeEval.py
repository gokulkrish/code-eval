'''
	fibonacciSeriesCodeEval.py - Solution to Problem Fibonacci Series (Category - Easy)
	Copyright (C) 2013, Shubham Verma

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

'''

Description:

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1;. 
Given a positive integer 'n', print out the F(n).

Input sample:

The first argument will be a text file containing a positive integer, one per line. 

e.g. 

	5
	12
	
Output sample:

Print to stdout, the fibonacci number, F(n).

e.g.

	5
	144

'''

import sys

fib_dict = {0: 0, 1: 1}

def fib(num):
	if num in fib_dict.keys():
		return fib_dict[num]
	else:
		fib_dict[num] = fib(num - 1) + fib(num - 2)
		return fib_dict[num]
		
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [ int(i) for i in f.read().split('\n') if len(i) > 0 ]
	
	for test_case in test_cases:
		print fib(test_case)
	
	f.close()