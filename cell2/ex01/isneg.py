#!/usr/bin/python3

def ft_isnum(n) :
	try :
		float(n)
		return (True)
	except :
		return (False)

num = input()
if (ft_isnum(num)) :
	num = float(num)
	if num == 0 :
		print("This number is both positive and negative.")
	elif num > 0 :
		print("This number is positive.")
	else :
		print("This number is negative.")
