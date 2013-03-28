'''
	sumdigitsCodeEval.py - Solution to Problem Lowercase (Category - Easy)
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

Given a positive integer, find the sum of its constituent digits.

Input sample:

The first argument will be a text file containing positive integers, one per line. 

e.g. 

	23
	496
	
Output sample:

Print to stdout, the sum of the numbers that make up the integer, one per line.

e.g.

	5
	19

'''

import sys

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = f.read().split('\n')	
	for test_case in test_cases:
		print sum( map(int, test_case) )
		
	f.close()