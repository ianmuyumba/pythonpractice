"""
OOP allows us to create our own objects that have methods and attributes
-It allows us to create code that is repeatable and organized
-Objects in python are also  called classes

Syntax

	class NameOfClass(): #The name of the class is in CamelCase - first letter capitalized
		
		def __init__(self,parameter1,parameter2):
			self.parameter1 = parameter1
			self.parameter2 = parameter2
		
		#Various other method calls
		def method1(self): #The self keyword lets python know that its a method connected to the class
			#Perform some action
			print(self.parameter1)

"""