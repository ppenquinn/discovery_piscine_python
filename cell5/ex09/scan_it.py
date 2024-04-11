#!/usr/bin/python3

import sys

if len((sys.argv)) != 3 :
	print("none")
else:
	scan = sys.argv[2].count(sys.argv[1])
	if (scan > 0):
		print(scan)
	else:
		print("none")
