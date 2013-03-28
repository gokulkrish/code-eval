'''

	hexToDecimalCodeEval.py - Solution to Problem Hex to Decimal (Category - Easy)
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

You will be given a hexadecimal(base 16) number. Convert it into decimal (base 10)

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file 
contains a hex number. You may assume that the hex number does not have the leading 'Ox'. 
Also all alpha characters(e.g. a through f) in the input will be in lowercase 

e.g.

	9f
	11
	
Output sample:

Print out the equivalent decimal number 

e.g.

	159
	17

'''

import sys

def convertToInt(num):
	s = '0x' + num
	
	return int(s, 16)

if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	test_cases = [i for i in f.read().split('\n') if len(i) > 0]
	
	for test_case in test_cases:
		print convertToInt(test_case)
		
	f.close()