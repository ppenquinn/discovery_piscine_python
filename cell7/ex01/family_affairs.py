#!/usr/bin/python3

def find_the_redheads(family):
	names = []
	for name in family.keys():
		if family[name] == "red":
			names.append(name)
	return (names)
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
