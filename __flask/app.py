"""
1. Installation on Windows

-To install flask, you first need Python installed on your machine - the latest edition, preferably
-You then need to install a virtual environment:
	-change directory to your prefered installation folder
	-install a virtual environment: py -m venv enviroment_name 
	-activate virtual environment: enviroment_name\Scripts\activate (Take note of case)
-Finally install flask: pip install flask

-Create Flask App
	-create a simple.py file: app.py
	-set an environment variable: set FLASK_APP=app.py (Allows flask to know what file to look for
	when it wants to run run)
	-

"""
# First import flask
# The First flask is lowercase (the library) while thesecond is uppercase (the class)
from flask import Flask

# Instantiate the class
app = Flask(__name__)

# Create route (URL Endpoint)
@app.route('/') #Decorator
# Define a function
def index():
	return '<h1>My name is Ian Muyumba Mandela</>'

# Now run the flask app: flask run (Runs the file you specified under set FLASK_APP=app.py)
# It serves a browser URL through which you can view your app
# To quit, press CTRL+C



#Modification that allows for user input in browser
from flask import Flask

app = Flask(__name__)


@app.route('/<name>') #<name> is a placeholder
def index(name): #You have to serve any placeholder as a parameter in the function
	return '<h1>My name is {}</>'.format(name)

#In the browser, input a parameter after the base url: /Ian


# Get out of the virtual environment: deactivate


"""
Ways to run your flask app running

Method 1: if __name__ = '__main__':
			app.run()
	#This allows you to run the file directly: python app.py

Method 2: flask run command
"""




