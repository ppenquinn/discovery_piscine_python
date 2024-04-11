#!/usr/bin/python3

def greetings(txt = "noble stranger"):
	if isinstance(txt, str):
		print("Hello, " + txt + '.')
	else:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
