#!/usr/bin/python3

import sys

if len(sys.argv) < 2 :
	print("none")
else:
	print("parameters:", len(sys.argv) - 1)
	for i in sys.argv[1:] :
		print("%s: %d" %(i, len(i)))

