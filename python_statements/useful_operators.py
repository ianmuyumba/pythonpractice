"""
Range function - range is a generator function
"""

# Find the numbers from one to ten but not including 10, then cast them onto a list

numbers1 = range(10)
list1 = [*numbers1]
print(list1)


for numbers1 in range(10): # Print Numbers but not including 10
	print(numbers1)

for numbers1 in range(4,10): # Print Numbers starting at 4
	print(numbers1)

for numbers1 in range(4,10,2): # Step size - Print while skipping a number
	print(numbers1)	



"""
Enumerate
"""

# Case Study 1

index_count1 = 0
for letter1 in "abcdefghijklmnop":
	print("At index {} the letter is {}." .format(index_count1,letter1))
	index_count1 += 1

# Case Study 2

index_count2 = 0
word1 = "abcdefghijklmnop"

for letter2 in word1:
	print(f"At index {index_count2} the letter is {word1[index_count2]}")
	print(word1[index_count2])
	index_count2 += 1

# The enumerate function simplifies the above two case studies - basically to enumerate a given variable

word2 = "abcdefg"

for letters in enumerate(word2):
	print(type(letters))

for index,letter in enumerate(word2):
	print(index)
	print(letter)
	print('\n')


"""
zip function - used in zipping together two or more items

"""

mylist1 = ["a", "b", "c"]
mylist2 = [1,2,3]
mylist3 = [1000,2000,3000]

for items in zip(mylist1, mylist2, mylist3):
	print(items)

# Unpack the above tuples

mylist1 = ["a", "b", "c"]
mylist2 = [1,2,3]
mylist3 = [1000,2000,3000]

for a,b,c in zip(mylist1, mylist2, mylist3):
	print(f"Student {a} is at number {b} with {c} marks")


"""
in function - used to check if a given item is in a string, list or tuple

"""
string1 = "abcdefghijklmnop"
list2 = [1,2,3,4,5]
dictionary1 = {"Key1":"Ian Muyumba", "Key2":1000}


if "a" in string1: #Returns True
	print("True")
else:
	print("False")


if "Key2" in dictionary1: #Returns True
	print("True")
else:
	print("False")


# Check if an item is among the values in dictionary (in function)

if 1000 in dictionary1.values():
	print("True")
else:
	print("False")


# Check if an item is among the keys in dictionary (in function)

if 1000 in dictionary1.keys():
	print("True")
else:
	print("False")


# Seek user input and check if its in the list

print("Enter the number to check in the list")
number1 = int(input())

if number1 in list2: #Returns False
	print("True")
else:
	print("False")

"""
Mathematical Functions - Min and Max
"""

list3 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
dictionary2 = {"Key1":"Ian Muyumba", "Key2":1000, "Key3":"Brian Mandela", "Key4":2000}

print(min(list3)) #Minimum value in the list
print(max(list3)) #Maximum value in the list

print(min(tuple1)) #Minimum value in the tuple
print(max(tuple1)) #Maximum value in the tuple

print(max(dictionary2))
print(min(dictionary2))

"""
Random Library

Shufle function - Shufles a list
				- You have to import the function from the random library

Random Int Function - Grab a random integer from a list or tuple
"""

from random import shuffle

print(f"Before shuffling, the list is as follows: {list3} " )
shuffle(list3)
print(f"After shuffling, the list is as follows: {list3} " )


from random import randint

#Print a random integer from a given range

randomInteger = randint(0,100)
print(randomInteger)

#Print random value from a list

import random

list4 = [1,2,3,4,5,6,7,8,9]

print(random.choice(list3)) #Print value from list

print(secrets.choice(foo)) #Pick secure random choices (e.g. generating a passphrase from a wordlist)