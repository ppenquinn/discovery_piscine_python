#!/usr/bin/python3

import sys

if len((sys.argv)) != 2 :
	print("none")
else:
	if (input("What was the parameter? ") == sys.argv[1]):
		print("Good job!")
	else:
		print("Nope, sorry...")
