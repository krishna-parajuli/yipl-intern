#! /usr/bin/python

# this code takes any input as full name and treats first word as 
# first name and last word as last name and processes those two words thereafter.
# I thought accounting middle name may change the code out of 
# the scope of specification.

name = raw_input("enter your full name ")

name = name.title()
splitted = name.split()
firstName = splitted[0]
lastName = splitted[-1]
lenfName = len(firstName)
lenlName = len(lastName)
length = lenfName + lenlName
lowfName = firstName.lower()
lowlName = lastName.lower()
hungarian = lowfName+lastName
vowels = ['a','e','i','o','u']
count = 0
vowelless=''

if lenfName == lenlName:
	status = "Good One"
else:
	status = "Not bad though"

for element in lowfName+lowlName:
	if element in vowels:
		count=count+1
	else:
		vowelless=vowelless+element

print "Length (%s %s): %d" % (firstName,lastName,length)

print "Status: %s" % status

print "Hungarian: %s" % hungarian

print "Vowels: %d" % count

print "Vowelless: %s" % vowelless
