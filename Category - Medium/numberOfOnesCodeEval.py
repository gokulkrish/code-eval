'''
	numberOfOnesCodeEval.py - Solution to Problem Number of Ones (Category - Medium)
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

Write a program to determine the number of 1 bits in the internal representation 
of a given integer.

Input sample:

The first argument will be a text file containing an integer, one per line. 

e.g. 

	10
	22
	56
	
Output sample:

Print to stdout, the number of ones in the binary form of each number.

e.g.

	2
	3
	3

'''

import sys
	
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = (int(i) for i in f.read().split('\n') if len(i) > 0)
	
	for test_case in test_cases:
		print bin(test_case)[2:].count('1')
	
	f.close()