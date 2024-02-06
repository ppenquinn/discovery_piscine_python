#!/usr/bin/python3

def ft_checknum(n):
	try:
		float(n)
		return (True)
	except:
		print("It's not a number")
		return (False)

num = input("Give me a number: ")
if(ft_checknum(num)):
	num = float(num)
	if (num - round(num) == 0):
		print("This number is an integer.")
	else:
		print("This number is a decimal.")

