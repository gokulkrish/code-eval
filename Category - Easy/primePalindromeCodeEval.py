'''
	primepalCodeEval.py - Solution to Problem Prime Palindrome (Category - Easy)
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

Write a program to determine the biggest prime palindrome under 1000.

Input sample:

	None

Output sample:

Your program should print the largest palindrome on stdout. i.e.

	929

'''

from math import sqrt

def isPrime(num):
	
	if num%2 == 0:
		return False
	else:
		for i in xrange(3, int(sqrt(num)), 2):
			if num % i == 0:
				return False
	return True
	
if __name__ == '__main__':

	for num in reversed(xrange(1000)):
		if str(num) == str(num)[::-1] and isPrime(num):
			print num
			break