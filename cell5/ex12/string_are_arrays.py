#!/usr/bin/python3

import sys

if len(sys.argv) != 2 :
	print("none")
else:
	cnt = 0
	for i in sys.argv[1] :
		if i == 'z' :
			print("z", end='')
			cnt += 1
	if cnt == 0 :
		print("none")
	else :
		print()
