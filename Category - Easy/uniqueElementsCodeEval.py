'''
	uniqueElementsCodeEval.py - Solution to Problem Unique Elements (Category - Easy)
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

You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

Input sample:

File containing a list of sorted integers, comma delimited, one per line. 

e.g. 

	1,1,1,2,2,3,3,4,4
	2,3,4,5,5

Output sample:

Print out the sorted list with duplicates removed, one per line

e.g.

	1,2,3,4
	2,3,4,5

'''

import sys

def extractUnique(nums):
	
	nums_list = nums.split(',')
	tmp = []
	
	for num in nums_list:
		if num not in tmp:
			tmp.append(num)

	return ','.join(tmp)
		
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [i for i in f.read().split('\n') if len(i) > 0]
	
	for test_case in test_cases:
		print extractUnique(test_case)
	
	f.close()