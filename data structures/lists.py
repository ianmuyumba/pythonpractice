"""
- Lists are ordered sequences that can hold a variety of object types (Collection of variables. Could be of different datatypes)
- Denoted by square brackets [] and Commas , to separate items in the list
	[1,3,3,4,5]
	[Ian,Muyumba,Mandela]
- Lists support indexing and slicing.
- Lists can be nested, ie a List inside another List
- There are a variety of useful methods that can also be called on Lists

"""

list1 = [1,2,3,4,5]
print(type(list1))
print(len(list1))
print(list1)

list2 = ["Ian", "Muyumba", "Mandela"]
print(type(list2))
print(len(list2))
print(list2)


list3 = ["Ian", "Muyumba", "Mandela", 10000, 15000, 20000]
print(type(list3))
print(len(list3))
print(list3)

print(list1[2])
print(list1[2:])
print(list1[:2])

list4 = list1 + list2 #Concatenating lists
print(list4)

list1[0] = 100 #Changing an item in a list
print(list1)

list1.append(6) #Add an item at the end of a list
print(list1)

list1.pop(5) #Remove an item from the list at the index provided
print(list1)

poppedList = list1.pop(4) #Remove an item from the list at the index provided and save in new variable
print(poppedList)

numberList = [2,5,7,9,3,4,6]
letterList = ["a","e","h","m","y","o",]

numberList.sort() #Sort the list in ascending order
print(numberList)

letterList.sort() #Sort the list in alphabetical order
print(letterList)

numberList.reverse() #Reverse List
print(numberList)

letterList.reverse() #Reverse List
print(letterList)