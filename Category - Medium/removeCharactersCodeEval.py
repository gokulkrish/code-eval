'''
	removeCharactersCodeEval.py - Solution to Problem Remove Characters (Category - Medium)
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

Write a program to remove specific characters from a string.

Input sample:

The first argument will be a text file containing an input string followed by a comma and 
then the characters that need to be scrubbed. 

e.g. 

	how are you, abc
	hello world, def
	
Output sample:

Print to stdout, the scrubbed strings, one per line. Trim out any leading/trailing whitespaces if they occur. 

e.g.

	how re you
	hllo worl

'''

import sys

def solution(test_case):
	text = test_case[0]
	chars = (i for i in test_case[1])
	ans = text
	
	for char in chars:
		ans = ans.replace(char, '')
		
	return ans
	
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = (tuple(i.split(', ')) for i in f.read().split('\n') if len(i) > 0)
	
	for test_case in test_cases:
		print solution(test_case)
	
	f.close()