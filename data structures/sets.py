"""
Sets
......

Sets are unordered collections of unique elements ie there can only be one representative of the same object

"""

set1 = set() #Create Set
print(set1)

set1.add(1) #Add an item to a set
print(set1)

set1.add(2) #Add an item to a set
print(set1)

set1.add(2) #When you try adding a second "2" into the set, it doesnt. The set remains as it was
print(set1)

list1 = [1,1,1,2,2,3,3,3,3,4,4,4,4,4,4,] #Define a list

print(set(list1)) #Convert the list defined above into a set. Notice it picks only unique values