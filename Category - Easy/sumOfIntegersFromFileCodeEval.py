'''
	sumintsCodeEval.py - Solution to Problem Sum of Integers from File (Category - Easy)
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

Print out the sum of integers read from a file.

Input sample:

The first argument to the program will be a text file containing a positive integer, one per line. 

e.g. 

	5
	12
	
NOTE: For solutions in JavaScript, assume that there are 7 lines of input

Output sample:

Print out the sum of all the integers read from the file. 

e.g.

	17

'''

import sys

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = f.read().split('\n')
	
	print sum( [int(i) for i in test_cases if len(i) > 0] )