#!/usr/bin/python3

def array_of_names(persons):
	names = []
	for fname,lname in persons.items() :
		names.append(fname.capitalize() + ' ' + lname.capitalize())
	return(names)

persons = {
	"jean" : "valjean",
	"grace" : "hopper",
	"xavier" : "niel",
	"fifi" : "brindacier"
}

print(array_of_names(persons))
