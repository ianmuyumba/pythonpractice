"""
-Allow for us to create a block of code that we may need to execute many times
-In this case, you only have to call the function, rather than copypasting the entire block of code

	Syntax
		def name_of_function():
			# Comment explaining the function
			print("Hello")

-Functions can also take in parameters

	Syntax
		def name_of_function(name):
			'''
			DOCSTRING: Comment explaining the function
			'''
			print("Hello"+name)

"""

# def functionName():
# 	print("Hello World")

# def functionName(name):
# 	print("Hello World"+name)

"""
-The return keyword is used to send back the result of the function in a method, rather than printing it out.
-It allows us to assign the output of the function to a new variable
"""

#Ask for user input and use a function to calculate the sum

# print("Enter Number 1: ")
# number1 = int(input())
# print("Enter Number 2: ")
# number2 = int(input())


# def addFunction(number1,number2):
# 	'''
# 	Function to find the sum of two given variables
# 	'''
# 	return number1+number2


# result = addFunction(number1,number2)


# print(f"The sum of Number 1 and Number 2 is: {result}")

# # help(addFunction) #Displays the DOCSTRING (Documentation that was defined in the function with triple quotes)



# #Function with default parameter

# def addFunction(name1 = " Ian"):
# 	# Function to find the sum of two given variables
# 	print("hello"+name1)

# addFunction()

#Check for a word in a given string

print("Check for a letter in your name")

print("Enter your full name")
myString1 = input()

print("Enter the letter to check")
myString2 = input()


def stringCheck():
	if myString2 in myString1:
		print(True)
	else:
		print(False)

stringCheck()