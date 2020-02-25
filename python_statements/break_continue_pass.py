"""

Break - Breaks out of the current closest enclosing loop
Continue - Goes to the top of the closest enclosing loop
pass - Does nothing at all (Used as a placeholder)

"""

#Pass

x = 0
while x < 5:
	#A comment alone is not enough to fill this space
	pass

#Continue

mystring = "Ian Muyumba"

for letter in mystring:
	if letter == 'a':
		continue
	print(letter)

# Break

for letter in mystring:
	if letter == 'n':
		break
	print(letter)