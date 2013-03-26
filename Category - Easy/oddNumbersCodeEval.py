'''
	oddNumbersCodeEval.py - Solution to Problem Odd Numbers (Category - Easy)
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

Print the odd numbers from 1 to 99.

Input sample:

	None

Output sample:

Print the odd numbers from 1 to 99, one number per line.

'''

if __name__ == '__main__':
	for i in xrange(1, 100):
		if i%2 != 0:
			print i
        