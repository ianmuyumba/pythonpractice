"""
While loops continue to execute a block of code while some condition remains true
Syntax
	
	while some_boolean_condition:
		#do something

	while some_boolean_condition:
		#do something
	else
		#do something different
"""

x = 0

while x < 5:
	print(f"The current value of x is {x}")
	x = x + 1
	# x +=1 
else:
	print(f"{x} is not less than 5")