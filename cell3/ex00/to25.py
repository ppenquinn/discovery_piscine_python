#!/usr/bin/python3

def ft_checknum(n):
	try:
		int(n)
		return (True)
	except:
		return (False)

num = input("Enter a number less than 25\n")
if (ft_checknum(num)):
	num = int(num)
	if (num > 25):
		print("Error")
	else:
		while num <= 25:
			print("Inside the loop, my variable is" ,num)
			num += 1
else:
	print("Error")
