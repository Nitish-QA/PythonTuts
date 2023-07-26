'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
Syntax:
lambda arguments : expression


Let's see some sample examples:
'''


def double(x):
    return x*2

print(double(5))

# We can write this using LAMBDA Function

double  = lambda x : x * 2
print(double(10))

# lambda function can have multiple parameters like normal functions

avg  = lambda x, y, z : (x + y + z)/3

print(avg(3, 4, 5))

# OR normal way
def avg1(x, y, z):
    return (x + y + z)/3
print(avg1(8, 9, 6))



'''
Normally we use lambda function when we need to pass function as argument or while 
using some small functions 

'''

# Normal Way to pass function as argument using 'func' keyword

def apply_function(func , x):
    return func(x)

def square(x):
    return x ** 2

print(apply_function(square, 9))


# NOW we can do the same in one line using lambda function
print(apply_function(lambda x : x**2, 9))  # less line of code, implemented the square function inside



