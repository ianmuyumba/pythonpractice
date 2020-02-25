"""
Similar to lists, but have immutability ie once an element is inside a tuple, it cannot be re-assigned.

Defined using parenthesis (1,2,3)

"""

tuple1 = (1,2,3,4,5) #Defining a Tuple
list1 = [1,2,3,4,5] #Defining a List

print(type(tuple1)) #Check type
print(type(list1)) #Check type

print(len(tuple1)) #Check length
print(len(list1)) #Check length

print(tuple1[2])
print(tuple1[2:])
print(tuple1[:2])
print(tuple1[::2])

tuple2 = (10, 10, 20, 30, 40, 40, 50, 60)

print(type(tuple2))
count10 = tuple2.count(10) #the .count() function counts the number of times an object occurs in a tuple
print(count10)

print(tuple2.count(10)) #Alternative to the method above

print(tuple2.index(20)) #the .index() function checks at what index an object occurs in a tuple