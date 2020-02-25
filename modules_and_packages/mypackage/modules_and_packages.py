"""
-Modules are .py scripts that you call in another .py script
-Packages are a collection of modules
-There, however, is a key .py script, __init__.py, that needs to be placed inside the folder
to let python know that the collection of .py scripts should be treated as a package
"""

from modules_and_packagesTest import myName

myName() #Executes the function from another .py file (modules_and_packagesTest)