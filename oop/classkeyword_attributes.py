"""
Class Keyword
Creating Attributes
"""

#Simple Class Initialization
class MyClass():
	pass

sampleClass = MyClass()

print(type(sampleClass))


class DogClass():
	def __init__(self,breed,name,spots):
		#Attributes
		#Take in  the argument and asign it using self.attribute_name
		self.breed = breed
		self.name = name
		self.spots = spots
		
#output attributes of the dog class
mydog = DogClass(breed = "German Shepherd", name = "Simba", spots = True)

dogBreed = mydog.breed
dogName = mydog.name
dogSpots = mydog.spots

print(f"My dog's Attributes")
print(f"Name: {dogName}")
print(f"Breed: {dogBreed}")
print(f"Spots: {dogSpots}")
