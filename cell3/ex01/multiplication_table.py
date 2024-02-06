#!/usr/bin/python3

def ft_checknum(n):
	try:
		int(n)
		return (True)
	except:
		print("Value Error")
		return (False)


num = input("Enter a number\n")
if (ft_checknum(num)):
	num = int(num)
	for i in range(10) :
		print(i, "x", num, "=", i * num)
