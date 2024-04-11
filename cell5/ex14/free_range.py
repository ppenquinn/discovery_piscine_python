#!/usr/bin/python3

import sys

def ft_isnum(n) :
	try :
		float(n)
		return (True)
	except :
		return (False)

if len(sys.argv) != 3 :
	print("none")
else:
	if (ft_isnum(sys.argv[1]) & ft_isnum(sys.argv[2])):
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[2])
		ans = []
		for i in range(num1,num2 + 1):
			ans.append(i)
		print(ans)
	else:
		print("Value Error")
