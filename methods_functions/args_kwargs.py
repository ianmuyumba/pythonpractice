"""
*args (Arguments) and **kwargs (Keyword Arguments)
-These two Functional Parameters allow us to accept an arbitrary number
 of parameters without having to define a bunch of parameters in your function calls
"""

#Function with only two parameters
def argsExample(a,b):
	#Returns 5% of the sum of a and b
	return sum((a,b)) * 0.05

print("Enter Number A: ")
a = int(input())

print("Enter Number B: ")
b = int(input())

print(argsExample(a,b))



#Function with more than two parameters. *args allows us to parse the parameters in the function
def Args1(*args):
	#Returns 5% of the sum of a and b
	return sum(args) * 0.05

print(Args1(10,10,10,10,10))



#For Loop in the function
def Args2(*args):
	for item in args:
		print(item)




#The Kwargs (Keyword Arguments) returns back a dictionary with key value pairs
def kwargsExample(**kwargs):
	if "fruit" in kwargs:
		print("My fruit of choice is {}".format(kwargs["fruit"]))
	else:
		print("I did not find any fruit")

kwargsExample(fruit="Apple") #Prints "My fruit of choice is apple"


#Args and Kwargs in the same function
def argsKwargs(*args,**kwargs):
	print(args)
	print(kwargs)
	print("I would like {} {}".format(args[0],kwargs["food"]))

argsKwargs(10,20,30,fruit="orange",food="eggs", animal="dog")