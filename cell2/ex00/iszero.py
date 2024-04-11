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
		print("This number is equal to zero.")
	else :
		print("This number is different from zero.")
