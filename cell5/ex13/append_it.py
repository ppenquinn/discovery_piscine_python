#!/usr/bin/python3

import sys

if len(sys.argv) < 2 :
	print("none")
else:
	for i in sys.argv[1 :] :
		if i[-3 :] != "ism" :
			print("%sism" %i)
