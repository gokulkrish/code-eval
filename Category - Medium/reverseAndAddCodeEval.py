'''
	reverseAndAddCodeEval.py - Solution to Problem Reverse and Add (Category - Medium)
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

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum 
is not a palindrome (which means, it is not the same number from left to right and right to left), 
repeat this procedure. 

eg.

	195 (initial number) + 591 (reverse of initial number) = 786

	786 + 687 = 1473

	1473 + 3741 = 5214

	5214 + 4125 = 9339 (palindrome)
	
In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to 
palindromes in a few step for almost all of the integers. But there are interesting exceptions. 
196 is the first number for which no palindrome has been found. It is not proven though, 
that there is no such a palindrome.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is 
one test case. Each test case will contain an integer n < 4,294,967,295. Assume each test case will 
always have an answer and that it is computable with less than 1000 iterations (additions)

Output sample:

For each line of input, generate a line of output which is the number of iterations (additions) to 
compute the palindrome and the resulting palindrome. (they should be on one line and separated by 
a single space character)

'''

import sys

def solution(num):
	num_of_iters = 0
	ans = num
	
	while True:
		num_of_iters += 1
		ans = ans + int(str(ans)[::-1])
		if ans == int(str(ans)[::-1]):
			break
	
	return ' '.join([str(num_of_iters), str(ans)])
	
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [int(i) for i in f.read().split('\n') if len(i) > 0]
	
	for test_case in test_cases:
		print solution(test_case)
	
	f.close()