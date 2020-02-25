"""
Variable Names in python are stored in namespaces, and have a scope, which
determines the visibility of the variable name to other parts of the code

Variables can be: (LEGB Rule)
	-Local
	-Enclosing function locals
	-Global (module)
	-Built-in (Python)
"""

#num, below, is a Local Variable (It is local to the Lambda function)
lambda num:num**2

#name, below in the greetings function, is an Enclosing function local Variable
name1 = "Muyumba" #Global Variable

def greetings():
	name1 = "Mandela" #Enclosing function local Variable
	#When the above line is commented out, the Global Variable will be picked, instead
	def hello():
		name1 = "Ian" #Local Variables
		#When the above line is commented out, the Enclosing local Variable will be picked, instead
		print(f"Hello {name1}")
	hello()

greetings()

#The scope of the local and enclosing local is just within the function, as illustrated below
print(f"The Global Variable still remains {name1}")

#The global keyword is used when you need to reassign a global variable locally, as below

x = 100

def globalVar():
	global x
	print(f"The value of X is {x}")

	#Local reassignment on a global variable
	x = 200
	print(f"We have reassigned X to {x}")

globalVar()
print(x) #Prints out 200, the value of the new reassignment
