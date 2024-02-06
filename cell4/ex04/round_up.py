#!/usr/bin/python3
def ft_checknum(n):
	try:
		float(n)
		return (True)
	except:
		print("Value Error")
		return (False)

import math

num = input("Give me a number: ")
if(ft_checknum(num)):
	num = float(num)
	print(math.ceil(num))
