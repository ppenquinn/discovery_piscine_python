#!/usr/bin/python3

def ft_checknum(n):
	try:
		int(n)
		return (True)
	except:
		return (False)

num1 = input("Give me the first number: ")
num2 = input("Give me the second number: ")
symbol = ['+', '-', '/', '*']
print("Thank you")
if(ft_checknum(num1) & ft_checknum(num2)) :
	num1 = int(num1)
	num2 = int(num2)
	if (num2 != 0):
		ans = [num1 + num2, num1 - num2, round(num1 / num2), num1 * num2]
	else:
		ans = [num1 + num2, num1 - num2, "Not a number", num1 * num2]
	for x in symbol:
		print(num1,x,num2,"=",ans[symbol.index(x)])
