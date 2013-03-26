'''
	rfindCodeEval.py - Solution to Problem Rightmost Char (Category - Easy)
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

You are given a string 'S' and a character 't'. 
Print out the position of the rightmost occurrence of 't'(case matters) in 'S' or -1 if there is none. 
The position to be printed out is zero based.

Input sample:

The first argument is a file, containing a string and a character, comma delimited, one per line.
Ignore all empty lines in the input file.

e.g. 

	Hello World,r
	Hello CodeEval,E

Output sample:

Print out the zero based position of the character 't' in string 'S', one per line. 
Do NOT print out empty lines between your output.

e.g.

	8
	10

'''

import sys

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [tuple(i.split(',')) for i in f.read().split('\n') if len(i) > 0]
	
	for test_case in test_cases:
		print test_case[0].rfind(test_case[1])