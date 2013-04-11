'''
	longestLinesCodeEval.py - Solution to Problem Unique Elements (Category - Medium)
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

Write a program to read a multiple line text file and write the 'N' longest lines to stdout.
Where the file to be read is specified on the command line.

Input sample:

Your program should read an input file (the first argument to your program). The first line 
contains the value of the number 'N' followed by multiple lines. You may assume that the input 
file is formatted correctly and the number on the first line i.e. 'N' is a valid positive integer.

e.g.

	2
	Hello World
	
	CodeEval
	Quick Fox
	A
	San Francisco
	
NOTE: For solutions in JavaScript, assume that there are 8 lines of input (i.e. line 1 will be N and the next
	  7 lines will be the input lines

Output sample:

The 'N' longest lines, newline delimited. Do NOT print out empty lines. Ignore all empty lines in the input. 
Ensure that there are no trailing empty spaces on each line you print. Also ensure that the lines are printed 
out in decreasing order of length i.e. the output should be sorted based on their length 

e.g.

	San Francisco
	Hello World

'''

import sys

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	text = [i.rstrip() for i in f.read().split('\n') if len(i) > 0]
	
	requiredTests = int(text[0])
	testCases = filter(lambda x: len(x) > 0, text[1:])
	
	sortedTestCases = sorted(testCases, key=len, reverse=True)
	
	for item in sortedTestCases[:requiredTests]:
		print item
	
	f.close()