"""
and - both conditions must be true
or - either condition must be true

not - Asks for an opposite boolean to the one that could have been achieved
"""
print("To pass through Gate A, you must have at least ten Mangoes AND ten oranges")
print("To pass through Gate B, you must have at least ten Mangoes OR ten oranges")

print('How many mangoes do you have?: ')
mangoes = int(input())
print('How many oranges do you have?: ')
oranges = int(input())

if mangoes >= 10 and oranges >= 10:
	print("You can pass through Gate A")
elif mangoes >= 10 or oranges >= 10:
	print("You can pass through Gate B")
else:
	print("You do not have enough Mangoes and Oranges to pass through Gate A or Gate B")