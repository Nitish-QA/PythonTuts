'''
In Python, we can pass a variable number of arguments to a function using special symbols. 
There are two special symbols:

*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)
We use *args and **kwargs as an argument when we are unsure about the number of arguments to 
pass in the functions.
One thing to note here is that "args" is just an identifier. It can be named anything relevant.

'''

def adder(x,y,z):
    print("sum:",x+y+z)

#adder(5,10,15,20,25)    #--- this will thorw error as adder function only accepts three argument

# Now instead of using that we can use *args where * is for wildcard

def new_adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum: ", sum)

new_adder(5, 10, 13, 14, 20)

'''
NOTE: whatever we pass , decorator will take it as 'tuple'
'''

'''
NOW:
Python passes variable length non keyword argument to function using *args but we cannot use
this to pass keyword argument. For this problem Python has got a solution called **kwargs, 
it allows us to pass the variable length of keyword arguments to the function.
**kwargs in Python

Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

**kwargs allows us to pass any number of keyword arguments.
'''

def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():     
        result.append("{} uses {}".format(key, value))
    return result
 
print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))

'''
OUTPUT:
[‘Google uses Angular’, ‘Facebook uses react’, ‘Microsoft uses .NET’]
'''

'''
Now that you have understood args and *kwargs, you might want to design a function that uses both of them. 
While doing this, the order of the arguments matters, *args has to come before *kwargs.

So if you are using standard arguments along with *args and **kwargs, then you have to follow this order-

Standard Arguments, *args, **kwargs
'''

# A simple example of a function that uses standard arguments, *args and **kwargs in Python:

def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)
 
printingData('007', 'agent', firstName='James', lastName='Bond') 

'''
OUTPUT:
  I am 007 
  I am arg: agent 
  I am kwarg: (‘firstName’, ‘James’) 
  I am kwarg: (‘lastname’ , ‘Bond’)
'''


'''
The single and double asterisks that we use are called unpacking operators.

Unpacking operators are used to unpack the variables from iterable data types like lists, tuples, and dictionaries.

A single asterisk(*) is used on any iterable given by Python.

The double asterisk(**) is used to iterate over dictionaries.

Let’s take some examples for *args and **kwargs unpacking-
'''

carCompany = ['Audi','BMW','Lamborghini']
print(*carCompany)  # *args unpacking

'''
OUTPUT:
Audi BMW Lamborghini

'''

techStackOne = {"React": "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
techStackTwo = {"dotNET" : "Microsoft"}
mergedStack = {**techStackOne, **techStackTwo}
print(mergedStack)  # **kwargs unpacking

'''
OUTPUT:
{'React': 'Facebook', 'Angular': 'Google', 'dotNET': 'Microsoft'}
'''

'''
NOTE:
Here are some key points that will help you-

-- *args and **kwargs are special Python keywords that are used to pass the variable length of 
arguments to a function
-- When using them together, *args should come before **kwargs
-- The words “args” and “kwargs” are only a convention, you can use any name of your choice



'''


