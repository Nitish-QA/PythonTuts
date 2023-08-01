'''
In Python, decorators are a powerful concept that allows you to modify the behavior of functions or methods. 
They are a form of metaprogramming, which means they enable you to add extra functionality to functions 
without changing their code directly.

***At a high level, a decorator is a function that takes another function as an argument, 
adds some functionality to it, and returns the modified function. 
You use the @ symbol followed by the decorator's name before the function you want to decorate.

Python decorators allow you to change the behavior of a function without modifying the function itself.

You'll use a decorator when you need to change the behavior of a function without modifying the function 
itself. A few good examples are 
when you want to add logging, test performance, perform caching, verify permissions, and so on.

To get a better understanding of how decorators work, you should understand a few concepts first.

1. A function is an object. Because of that, a function can be assigned to a variable. 
The function can be accessed from that variable.
'''
def my_function():

    print('I am a function.')

# Assign the function to a variable without parenthesis. We don't want to execute the function.

description = my_function

# Accessing the function from the variable I assigned it to.

print(description())

# Output

'I am a function.'


# 2.  A function can be nested within another function.

def outer_function():

    def inner_function():

        print('I came from the inner function.')

    # Executing the inner function inside the outer function.
    inner_function()

outer_function()

# Output: I came from the inner function.
'''
NOTE that the inner_function is not available outside the outer_function. 
If I try to execute the inner_function outside of the outer_function I receive a NameError exception.

'''
# 3. Since a function can be nested inside another function it can also be returned.

def outer_function():
    '''Assign task to student'''

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()

homework()
# Output: 'Read Python book chapter 5.'


# 4.  A function can be passed to another function as an argument.

def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print('Don\'t forget to bring your wallet!')

def action():

    print('I am going to the store buy you something nice.')

# Calling the friendly_reminder function with the action function used as an argument.

friendly_reminder(action)

# Output:
# I am going to the store buy you something nice.
# Don't forget to bring your wallet!


'''
5. 
How to Create a Python Decorator
To create a decorator function in Python, I create an outer function that takes a function as an argument. 
There is also an inner function that wraps around the decorated function.

'''
def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func

@my_decorator_func
def my_func():
      pass

#EXAMPLE
#Here is a simple example. This decorator logs the date and time a function is executed:

from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   

     
daily_backup()


'''
# Output

Daily backup job has finished.
Function: daily_backup
Run on: 2021-06-06 06:54:14
---------------------------

'''
'''
6.
How to Add Arguments to Decorators in Python
Decorators can have arguments passed to them. 
To add arguments to decorators I add *args and **kwargs to the inner functions.

*args will take an unlimited number of arguments of any type, such as 10, True, or 'Brandon'.
**kwargs will take an unlimited number of keyword arguments, such as 
count=99, is_authenticated=True, or name='Brandon'.

Here is a decorator with arguments:
'''

def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        func(*args, **kwargs)
        # Do something after the function.
    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    '''Example docstring for function'''

    pass

#Decorators hide the function they are decorating. 
# If I check the __name__ or __doc__ method we get an unexpected result.

print(my_func.__name__)
print(my_func.__doc__)

'''
# Output

wrapper_func
None
'''



