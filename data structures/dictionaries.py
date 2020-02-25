"""
Dictionaries
	- Unordered mappings for storing objects - They are, instead, stored in Key-Value pairs
	- You can thus grab an object using its key, without neccesarily needing to know an index location

Syntax - {'key1':'value1','key2':'value2'}

Can be nested - Can contain other dictionaries, as well as lists

N/B - Keys should always be strings
"""

dictionary1 = {"firstName":"Ian", "middleName":"Mandela", "lastName":"Muyumba"}
print(type(dictionary1))
print(dictionary1)
print(dictionary1["firstName"]) #Using the key to access the value from a dictionary

dictionary2 = {"fullName":"Ian Muyumba", "details":{"age":23, "Gender":"Male"}, "bankAccounts":["Coop", "Equity","KCB"]} #A dictionary containing a string, List and another dictionary

#Checking the type of each item in the dictionary
print(type(dictionary2["fullName"]))
print(type(dictionary2["details"])) 
print(type(dictionary2["bankAccounts"]))

print(dictionary2)

print(dictionary2["details"]["age"]) #Print the value of the item in the nested dictionary
print(dictionary2["bankAccounts"][0]) #Print the value of the first item in the list

letterUpper = dictionary2["bankAccounts"][0].upper() #Assign a variable to the value of the first item in the list and make it uppercase
print(letterUpper)

print(dictionary2.keys()) #Return the keys from a list
print(dictionary2.values()) #Return the values from a dictionary
print(dictionary2.items()) #Return the keys from a list