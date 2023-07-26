'''
Error in Python can be of two types i.e. Syntax errors and Exceptions. 
In Python, there are several built-in exceptions that can be raised when an error occurs during the execution of a program.

SyntaxError
TypeError
NameError
IndexError
KeyError
ValueError
AttributeError
IOError
ZeroDivisionError
ImportError

Error Handling can be done suing 'Try Except' Block

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

x = 5
y = "hello"
try:
    z = x + y
except Exception as e:
    print(e)

print('Hello World')

print('-------------------------1-------------------------------')

# Catch error explicitly
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str") 

# Finally block:
try:
   print('code that may/may not produce errors')

except:
   print('when error arises, then this block of code exceutes')

else:
   print('when error doesnot arise, then this block of code exceutes')

finally:
   print('This block will exceute whether error occurs or not.')







