'''
	sumprimeCodeEval.py - Solution to Problem Sum of Primes (Category - Easy)
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

Write a program to determine the sum of the first 1000 prime numbers.

Input sample:

	None

Output sample:

Your program should print the sum on stdout.i.e.

	3682913

'''

from math import sqrt

def isPrime(num):
	if num == 1:
		return False
	if num == 2:
		return True
	if num%2 == 0:
		return False
	else:
		for i in xrange(3, int(sqrt(num))+1, 2):
			if num%i==0:
				return False

	return True
	
if __name__ == '__main__':

	primes = []
	i = 1
	
	while True:
		if len(primes) == 1000:
			break
		if isPrime(i):
			primes.append(i)
		i += 1
	
	print sum(primes)