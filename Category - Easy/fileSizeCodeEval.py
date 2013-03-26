'''
	fileSizeCodeEval.py - Solution to Problem File Size (Category - Easy)
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

Print the size of a file in bytes.

Input sample:

Path to a filename. 

e.g. 

	foo.txt
	
Output sample:

Print the size of the file in bytes.

e.g.

	55

'''

import sys
import os

if __name__ == '__main__':
	file_name = sys.argv[1]
	file_size = os.path.getsize(file_name)
	print str(file_size)