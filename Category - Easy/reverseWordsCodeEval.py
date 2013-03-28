'''

	reverseWordsCodeEval.py - Solution to Problem Reverse Words (Category - Easy)
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

Write a program to reverse the words of an input sentence.
Input sample:

The first argument will be a text file containing multiple sentences, one per line. Possibly empty lines too. 

e.g. 

	Hello World
	Hello CodeEval
	
Output sample:

Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. 
Ensure that there are no trailing empty spaces on each line you print. 

e.g.

	World Hello
	CodeEval Hello

'''

import sys

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [i for i in f.read().split('\n') if len(i) > 0]
	
	for test_case in test_cases:
		print ' '.join( reversed( test_case.split(' ') ) )
		
	f.close()