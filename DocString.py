'''
In Python, a docstring is a special type of string used to document modules, classes, functions, or methods
It provides a way to describe what a particular piece of code does, its parameters, return values, 
and any other relevant information.

Docstrings are typically placed as the first statement inside a module, class, or function definition

The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method or function declaration. 
All functions should have a docstring.


### DocString always be declared just after function declaration. Otherwise it wpn't be accessed

'''
def add(a, b):
    """
    This function takes two arguments, 'a' and 'b', and returns their sum.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of 'a' and 'b'.
    """
    return a + b
  

print(add.__doc__) # This will print the docstring declared above
  