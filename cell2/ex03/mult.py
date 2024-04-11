#!/usr/bin/python3

def isneg(num) :
	if num == 0 :
		print("This number is both positive and negative.")
	elif num > 0 :
		print("This number is positive.")
	else :
		print("This number is negative.")

def ft_checknum(n):
	try:
		int(n)
		return (True)
	except:
		return (False)

first = input("Enter the first number:\n")
sec = input("Enter the second number:\n")
if (ft_checknum(first) & ft_checknum(sec)):
	first = int(first)
	sec = int(sec)
	print(first, 'x', sec, "=", first * sec)
	isneg(first*sec)
else
	print("Value Error")
