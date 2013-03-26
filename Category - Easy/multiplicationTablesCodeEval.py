'''
	tableCodeEval.py - Solution to Problem Multiplication Tables (Category - Easy)
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

Print out the grade school multiplication table upto 12 X 12.

Input sample:

	None

Output sample:

Print out the table in a matrix like fashion, each number formatted to a width of 4 
(The numbers are right-aligned and strip out leading/trailing spaces on each line). The first 3 line will look like: 

e.g.

	1   2   3   4   5   6   7   8   9  10  11  12
	2   4   6   8  10  12  14  16  18  20  22  24
	3   6   9  12  15  18  21  24  27  30  33  36

'''

if __name__ == '__main__':
	for i in xrange(1, 13):
		tmp = []
		for j in xrange(1, 13):
			tmp.append( '%4d' % (i * j))
		print (''.join(tmp)).lstrip()
    