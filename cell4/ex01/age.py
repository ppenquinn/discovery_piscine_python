#!/usr/bin/python3

def ft_checknum(n):
	try:
		int(n)
		return (True)
	except:
		print("Value Error")
		return (False)

age = input("Please tell me your age: ")
if (ft_checknum(age)):
	age = int(age)
	print("You are currently %d years old." %age)
	for x in [10, 20, 30]:
		print("In %d years, you'll be %d years old." %(x, x + age))


