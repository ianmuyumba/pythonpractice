"""
Equal to - (==)
Not Equal to - (!=)
Greater Than - (>)
Less Than - (<)
Greater Than and Equal to - (>=)
Less Than and Equal to - (<=)
"""

print('Enter Number 1: ')
number1 = int(input())
print('Enter Number 2: ')
number2 = int(input())

if number1 == number2:
	print('' ,number1, 'is equal to ' ,number2)
elif number1 > number2:
	print('' ,number1, 'is Greater than ' ,number2)
elif number1 < number2:
	print('' ,number1, 'is less than ' ,number2)