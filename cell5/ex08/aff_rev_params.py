#!/usr/bin/python3

import sys

if len((sys.argv)) <= 2 :
	print("none")
else:
	i = len(sys.argv) - 1
	while (i >= 1):
		print(sys.argv[i])
		i -= 1
