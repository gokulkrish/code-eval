'''
	happyNumbersCodeEval.py - Solution to Problem Happy Numbers (Category - Easy)
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

A happy number is defined by the following process. Starting with any positive integer, replace the number 
by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are 
happy numbers, while those that do not end in 1 are unhappy numbers.

Input sample:

The first argument is the pathname to a file which contains test data, one test case per line. Each 
line contains a positive integer. Each line is in the format: N i.e. a positive integer 

eg.

	1
	7
	22
	
Output sample:

If the number is a happy number, print out a 1. If not, print out a 0 

eg.

	1
	1
	0
	
For the curious, here's why 7 is a happy number: 7->49->97->130->10->1. 
Here's why 22 is NOT a happy number: 22->8->64->52->29->85->89->145->42->20->4->16->37->58->89 ...

'''

import sys

def isHappyNum(num):
	tmp = []
	num_copy = num
	while num_copy != 1:
		num_copy = sum([int(i) * int(i) for i in str(num_copy)])
		if num_copy in tmp:
			return 0
		else:
			tmp.append(num_copy)
	
	return 1
	
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [int(i) for i in f.read().split('\n') if len(i) > 0]

	for test_case in test_cases:
		print isHappyNum(test_case)