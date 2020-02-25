"""

If Statements are used to check if a certain condition is true, and thereafter execute a block of code to that effect
With the Elif statement, you can parse in several conditions and execute several blocks of code
The Else statement provides recourse if all the conditions are not true

"""
print("100 is our Standard Measure")

print("Enter your number of choice")

number1 = int(input())

if number1 == 100:
	print(number1, " is equal to 100")
elif number1 > 100:
	print(number1, " is greater than 100")
else:
	print(number1, " is less than 100")