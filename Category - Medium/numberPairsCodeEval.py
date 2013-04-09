'''
	numberPairsCodeEval.py - Solution to Problem Number Pairs (Category - Medium)
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

You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers
whose sum is equal to X. Print out only unique pairs and the pairs should be in ascending order

Input sample:

Your program should accept as its first argument a filename. This file will contain a comma 
separated list of sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. 
If no pair exists, print the string NULL 

eg.

	1,2,3,4,6;5
	2,4,5,6,9,11,15;20
	1,2,3,4;50
	
Output sample:

Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed 
in sorted order i.e the first number of each pair should be in ascending order.

e.g.

	1,4;2,3
	5,15;9,11
	NULL

'''

import sys
import itertools

def solution(test_case):
	requiredSum = int(test_case[1])
	nums = filter(lambda x: x <= requiredSum, map(int, test_case[0].split(',')))
	
	validPairs = [i for i in list(itertools.combinations(nums, 2)) if sum(i) == requiredSum] 
	
	if len(validPairs) > 0:
		ans = ';'.join( map(lambda x: ','.join(map(str, x)), validPairs) )
		return ans
	else:
		return 'NULL' 

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [i.split(';') for i in f.read().split('\n') if len(i) > 0]
	
	for test_case in test_cases:
		print solution(test_case)
		
	f.close()