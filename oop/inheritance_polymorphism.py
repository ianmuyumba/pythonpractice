# """
# Inheritance and Polymorphism
# -Inheritance is a way of forming new classes using classes that have already been defined
# -Benefits:
# 	-Code reuse
# 	-Reduce complexity of a program
# """

# #Base Class
# class Person():
# 	def __init__(self):
# 		print("Person class created")
# 	def legs(self):
# 		print("Has two legs")
# 	def ears(self):
# 		print("Has two ears")
# 	def talk(self):
# 		print("Can Talk")

# # myPerson = Person()
# # print(myPerson)


# # Derived Class
# class Woman(Person):
# 	def __init__(self):
# 		Person.__init__(self) #Inherit the base Class (Person)

# myWoman = Woman()
# #Print out "Has two legs" using the method inherited from Base class
# numberLegs = myWoman.legs()
# print(noLegs)

# # Derived Class - This time we want to overwrite a method from the base class
# class Woman(Person):
# 	def __init__(self):
# 		Person.__init__(self)
# 		# print("Woman class created")
# 	def talk(self): #Make sure to use the same name as the base class
# 		print("Can Talk too much") #Added "too much"

# myWoman = Woman()
# #Print out "Can Talk too much" after overwriting the method from the base class
# womanTalk = myWoman.talk()
# print(womanTalk)


"""
Polymorphism
-The way in which different object classes can share the same method name
-Those methods can then be called from the same place even though a variety of diff objects might be parsed in
"""

class Dog():
	def __init__(self, name = "Simba"):
		self.name = name
	def legs(self):
		print(self.name + " has four legs")
	def ears(self):
		print(self.name + " has two ears")

class Hen():
	def __init__(self, name = "Khasiala"):
		self.name = name
	def legs(self):
		print(self.name + " has two legs")
	def ears(self):
		print(self.name + " has two ears")

dog1 = Dog("Simba")
# print(dog1.lSimbaegs())

hen1 = Hen("Khasiala")
# print(hen1.ears())


#Polymorphism - Two different classes that share the same method name
for pet in [dog1,hen1]:
	type(pet)
	pet.legs()





# # # # # # dog1 = Dog("Simba")
# # # # # # hen1 = Hen("Khasiala")

# # # # # # dog1Legs = dog1.legs()
# # # # # # dog1Ears = dog1.ears("Simba")
# # # # # # dog1Talk = dog1.talk("Simba")


# # # # # My Bad
# # # # My Bad
# # # My Bad
# # My Bad
# My Bad


# # # # # # hen1Legs = dog1.legs("Khasiala")
# # # # # # hen1Ears = dog1.ears("Khasiala")
# # # # # # hen1Talk = dog1.talk("Khasiala")

# # # # # # # print("Dog Attributes")
# # # # # # # print(f"Simba has {dog1Legs} legs")
# # # # # # # print(f"Simba has {dog1Ears} ears")
# # # # # # # print(f"Simba {dog1Talk} talk")

# # # # # # # print(f"Hen Attributes")
# # # # # # # print(f"Khasiala has {hen1Legs} legs")
# # # # # # # print(f"Khasiala has {hen1Ears} ears")
# # # # # # # print(f"Khasiala {hen1Talk} talk")