#!/usr/bin/python3

import sys

def shrink(txt):
	print(txt[0:8])

def enlarge(txt):
	while (len(txt) <= 8):
		txt += 'Z'
	print(txt)

if len(sys.argv) < 2 :
	print("none")
else:
	for x in sys.argv[1 :]:
		if len(x) >= 8:
			shrink(x)
		else:
			enlarge(x)
