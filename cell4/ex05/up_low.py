#!/usr/bin/python3

str = input()
for c in str:
	if(c.isupper()):
		print(c.lower(),end='')
	else:
		print(c.upper(),end='')
print()
