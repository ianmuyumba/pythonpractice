"""
Strings
"""
string1 = 'Ian Muyumba' #Single Quote
string2 = "Ian Mandela" #Double Quote
string3 = "I'm Ian Muyumba" #Quotation mark inside double quote
string4 = "My first name is Ian\nMy second name is Muyumba" #Line break (\n)
string5 = "My first name is Ian\tMy second name is Muyumba" #Tabbed Content

print(string1)
print(string2)
print(string3)
print(string4)
print(string5)

print(len(string5)) #Print length of a string
print(string1[0]) #Print a character from a string (Indexing)
print(string1[10]) #Print a character from a string (Indexing)
print(string1[-1]) #Print a character from a string (Reverse Indexing)
print(string1[-9]) #Print a character from a string (Reverse Indexing)
print(string5[4:]) #Print from specific character to the end (Slicing)
print(string5[:4]) #Print from the start to a specific character (Slicing - up to but not including)
print(string5[4:20]) #Print from specific character to specific character (Slicing)
print(string5[::2]) #Print in Step Size
print(string5[::-1]) #Reverse a string in step size

string6 = string1[3:]
print(string6)
string7 = 'Mandela' + string6 #Concatenating a string 
print(string7)
string8 = y*10 #Concatenating a string by multiplication
print(string8)



"""
String Methods
"""
upperString1 = string1.upper() #Make a string UpperCase
print(upperString1)
lowerString1 = string1.lower() #Make a string LowerCase
print(lowerString1)
splitString1 = string1.split() #Split a string into a list
print(splitString1)



"""
String Interpolation
- Useful when injecting a variable into a string for printing
-There are multiple ways to format strings for printing variables in them among them:
	1. .format()
	2. fstrings	
"""
firstName = "Ian"
lastName = "Muyumba"
print("My name is Ian " + lastName +".")

# .format() syntax - 'string here {} then also {}' .format('something1','something2')

print("My name is Ian {}".format("MUYUMBA")) #.format() function to display basic text
print("My name is {2} {1} {0}".format("Ian", "Muyumba", "Mandela")) #.format() function using indexes
print("My name is {firstName} {middleName} {lastName}".format(firstName="Ian", middleName="Mandela", lastName="Muyumba")) #.format() function using variable assignments

# fstrings syntax - print(f"Hello, my name is {fullname}")
print(f"My name is {firstName} {lastName}")
