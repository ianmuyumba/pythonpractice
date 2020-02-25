"""
List Comprehension
"""

#Append values in a string onto a list

mystring1 = "Ian Muyumba" #Define String
mylist1 = [] #Define empty list

for letters in mystring1:
	mylist1.append(letters)
print(mylist1)

#Efficient alternative for the above operation

mylist2 = [letters for letters in mystring1]
print(mylist2)

mylist2 = [letters for letters in "Muyumba"]
print(mylist2)



# Range of numbers into a list

mylist3 = []

for numbers1 in range(1,10):
	mylist3.append(numbers1)
print(mylist3)

#Efficient alternative for the above operation

mylist4 = [numbers for numbers in range(0,10)]
print(mylist4)

#Square of each of the numbers, and append them onto a list

mylist4 = [numbers**2 for numbers in range(0,10)]
print(mylist4)

#Take out only even numbers only and append them onto the list

mylist5 = [numbers2 for numbers2 in range(0,10) if numbers2%2 == 0]
print(mylist5)



#Perform arithmetic operations, then append onto a list e.g convert from degrees to farenheit

celcious = [20, 30, 40, 45, 53]
farenheit = []

for temperature in celcious:
	farenheit.append(((9/5)*temperature + 32))
print(farenheit)

#Efficient alternative for the above operation

farenheit1 = [((9/5)*temperature + 32) for temperature in celcious]
print(farenheit1)
