'''
FUNCTOOLS:
When we use a function as argument for a fucntion then they are called higher order functions.
Functools module is for higher-order functions that work on other functions. 
It provides functions for working with other functions and callable objects to use 
or extend them without completely rewriting them


Map, Filter and Reduce
In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a 
function to a sequence of elements and return a new sequence. These functions are known as higher-order 
functions, as they take other functions as arguments.

MAP:
The map function applies a function to each element in a sequence and returns a new sequence containing 
the transformed elements. 

The map function has the following syntax:

map(function, iterable)

--The function argument is a function that is applied to each element in the iterable argument. 
--The iterable argument can be a list, tuple, or any other iterable object.

'''

# Normal way
print('-----------------------1--------------------------------')
numbers1 = [1, 4, 5, 3, 5]

def cube(x):
    return x * x * x  # we can remove these steps using lambda function

cube_list1 = []
for item in numbers1:
    cube_list1.append(cube(item))  # we can remove these steps using map function

print(cube_list1)

# NOW using MAP
numbers2 = [4, 4, 6, 3, 9]
cube_list2 = list(map(lambda x: x * x * x, numbers2)) # If we don't want to use lambda then we have to create a fucntion that returns cube

print(cube_list2)


'''
FILTER:
The filter() method filters the given sequence with the help of a function that 
tests each element in the sequence to be true or not.

The filter() method in Python has the following syntax:

Syntax: filter(function, sequence)

Let's take an example:
Write a function that finds out odd and even number in a list and returns a filtered list
'''
print('--------------------------2-------------------------')

def iseven(x):
    return x % 2 == 0  # returns boolean value



# using NORMAL way
l1 = [3, 5, 4, 22, 46, 43]
l1_even = []
l1_odd = []
for i in l1:
    if iseven(i):
        l1_even.append(i)
    else:
        l1_odd.append(i)

print(l1_even)
print(l1_odd)




# Using FILTER
l2 = [8, 1, 4, 22, 22, 45]
list_even = list(filter(iseven, l2))
print(list_even)
# We can also use lambda in place of defining iseven function seperatly

list_even = list(filter(lambda x: x % 2 == 0, l2))




'''
REDUCE function
- Is little different, we have to import it while using.
The reduce() function in python performs functional computation by taking a function and 
an iterable (e.g., list, tuple, dictionary, etc.) as arguments, and the result is returned 
after computation (the process of applying the function on the iterable).

Here is the example for this:
'''
print('------------------------3----------------------------------')
from functools import reduce 

nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)
print(ans) 

# reduce() can also be combined with operator functions to achieve the similar functionality 
# as with lambda functions and makes the code more readable.
import operator

lis = [1, 3, 5, 6, 2]

# using reduce  and operator function to compute sum of list
print(reduce(operator.add, lis))

# using reduce and operator to compute multiplication
print(reduce(operator.mul, lis))

# using reduce to concatenate string
print(reduce(operator.add, ["geeks", "for", "geeks"]))








 