"""
Lambda Expressions are a way to quickly create anonnymous functions ie One
time expressions that you may not reference again

"""

#Map
''''''
def square(number1):
	return number1**2

myNumbers1 = [1,2,3,4,5]

#Find Square of each number in the above list
for item in map(square,myNumbers1):
	print(item)


#Find the Square of each number in the list, append to a list
print(list(map(square,myNumbers1)))


#Filter
''''''
def checkEven(num):
	return num%2==0

myNumbers2 = [10,15,20,25,30]

print(list(filter(checkEven,myNumbers2)))

for n in filter(checkEven,myNumbers2):
	print(n)


""" Lambda """

def square(num):
	resultSquare = num**2
	return resultSquare

print(square(3))

# The above expression can be simplified as below

myNumbers3 = [10,20,30,40,50]

print(list(map(lambda num:num**2,myNumbers3)))

#Pick only the first letters of given names in a list

myName = ["Ian", "Muyumba", "Mandela"]

print(list(map(lambda firstLetter:firstLetter [0], myName)))