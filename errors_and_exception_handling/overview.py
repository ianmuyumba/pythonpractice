"""
-Nobody is perfect - Errors are thus bound to happen
-We can use error handling to attempt to plan for possible errors

-We use three keywords in error and exception handling: 
	- try: Block of code to be attempted (May or may not lead to an error)
	- except: Block of code to be executed in case there is an error in the try block
	- finally: Final block of code to be executed regardless of an error
"""

# try:
# 	#Block of Code to be attempted - May or may not have an error
# 	result = 10 + 10
# except:
# 	print("Looks like you have an error")
# else:
# 	print("All went well")
# 	print(result)
# finally:
# 	pass


#Ask for User input and check for an error

def ask_for_int():
	try:
		integer1 = int(input("Enter an Integer of your choice: "))
	except:
		print("Please enter an integer!!!")
	finally:
		print(f"You have entered Integer: {integer1}")

ask_for_int()



