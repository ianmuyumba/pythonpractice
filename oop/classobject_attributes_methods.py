class DogClass():
	#Class Object Attributes - They are the same for any instance of the class
	species = "Mammal"


	def __init__(self,breed,name,spots):
		#Attributes
		#Take in  the argument and asign it using self.attribute_name
		self.breed = breed
		self.name = name
		self.spots = spots
		
#output attributes of the dog class
mydog = DogClass(breed = "German Shepherd", name = "Simba", spots = True)

dogSpecies = mydog.species #Class Attribute
dogBreed = mydog.breed
dogName = mydog.name
dogSpots = mydog.spots

print(f"My dog's Attributes")
print(f"\nSpecies: {dogSpecies}")
print(f"Name: {dogName}")
print(f"Breed: {dogBreed}")
print(f"Spots: {dogSpots}")



"""
Methods
-Methods are functions defined inside the body of a class.
-The are used to perform operations that sometimes utilise the attributes of the object defined in the class
"""

#Operations/Actions (Our fist method (Function inside a class))

class DogClass():
	#Class Object Attribute
	species = "Mammal"

	def __init__(self,breed,name):
		#Attributes
		self.breed = breed
		self.name = name
	#Method
	def bark(self):
		print("Woof! My name is {}".format(self.name))

mydog = DogClass(breed = "German Shepherd", name = "Simba")
print(mydog.bark())


#Get the circumference of a circle

print("Enter the radius of your circle: ")
radius = int(input())

class Circle():
	#Class Object Attribute
	pi = 3.14
	def __init__(self,radius=1):
		#Attributes of the circle
		self.radius = radius
	#Get Circumference method
	def getCircumference(self):
		return self.radius*self.pi*2

myCircle = Circle(radius)
finalCircumference = myCircle.getCircumference()

print("The radius of your circle is {} and the circumference is {}".format(radius,finalCircumference))



#Area of a Square

print("Find the Area of a given rectangle")
print("Enter the length: ")
length = int(input())
print("Enter the width: ")
width = int(input())

class Rectangle():
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def getArea(self):
		return length*width
		
myRectangle = Rectangle(length,width)
areaRectangle = myRectangle.getArea()

print(f"length: {length}")
print(f"width: {width}")
print(f"Area: {areaRectangle}")


#Area of a Triangle

print("Find the area of a Triangle")
print("Enter length: ")
lengthTriangle = int(input())
print("Enter width: ")
widthTriangle = int(input())


class MyTriangle():
	#Get area of a triangle
	def __init__(self, lengthTriangle,widthTriangle):
		self.lengthTriangle = lengthTriangle
		self.widthTriangle = widthTriangle
	#Get area of triangle method
	def triangleArea(self):
		return (lengthTriangle*0.5)*widthTriangle

triangle1 = MyTriangle(lengthTriangle,widthTriangle)
areaTriangle = triangle1.triangleArea()

print("Length: {}".format(lengthTriangle))
print("Width: {}".format(widthTriangle))
print("Area: {}".format(areaTriangle))
