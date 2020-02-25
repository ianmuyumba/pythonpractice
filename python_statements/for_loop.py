"""

For Loops are used in iteration - Many items in Python, lists, strings, dictionaries, sets, are iterable

Syntax
	my_iterable = [1,2,3,4]
	for item_name in my_iterable:
		#Execute Code

"""
'''.........................................................................'''


list1 = [1,2,3,4,5,6,7,8,9,10] #Define a list

for number1 in list1:
	print(number1) #Print each number in the list

for evenNumbers in list1: 
	if evenNumbers % 2 == 0:
		print('Even Number: ' ,evenNumbers) #Print out even numbers in the list
	else:
		print(f'Odd Number: {evenNumbers}') #Print out odd numbers in the list


'''.........................................................................'''


listSum = 0

for numbersList in list1:
	listSum = listSum + numbersList
	print(listSum) #Print Sum of all items in the list, step by step

print(listSum) #Print Sum of all items in the list


'''.........................................................................'''


string1 = "Ian Muyumba"

for letter1 in string1:
	print(letter1)


'''.........................................................................'''


tuple1 = (1,2,3,4,5)

for items in tuple1:
	print(items)

'''.........................................................................'''

list2 = [(1,2,3), (4,5,6), (7,8,9)] #Tuple Unpacking

for (a,b,c) in list2:
	print(a)

for (a,b,c) in list2:
	print(b)

for (a,b,c) in list2:
	print(c)


'''.........................................................................'''

dictionary1 = {"key1":1, "key2":2, "key3":3}

for keys,values in dictionary1.items(): #Using Tuple unpacking principals to unpack a dictionary
	print(values)