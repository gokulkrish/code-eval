'''
	multiplesOfANumberCodeEval.py - Solution to Problem Multiples of a Number (Category - Easy)
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

Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater 
than or equal to x. Do not use division or modulo operator.

Input sample:

The first argument will be a text file containing a comma separated list of two integers, one list per line. 

e.g. 

	13,8
	17,16
	
Output sample:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line.

e.g.

	16
	32

'''

import sys

def solution(test_case):
	x, n = int(test_case[0]), int(test_case[1])
	ans = 0
	i = 1
	
	while True:
		ans = n * i
		if ans >= x:
			break
		i += 1
	
	return ans

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [ tuple( i.split(',') ) for i in f.read().split('\n') if len(i) > 0 ]
	
	for test_case in test_cases:
		print solution(test_case)
	
	f.close()