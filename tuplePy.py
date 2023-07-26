'''
Tuples are used to store multiple items in a single variable.
-- tuple is a collection which is ordered and unchangeable.
-- Tuples are written with round brackets.
-- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
-- A tuple can contain different data types
'''

print('---------------1---------------')
mytuple = ("apple", "banana", "cherry")
print(mytuple)

print('----------2----------------')
# can we join tuple with list
# NOT directly we have to first convert the tuple to list

tuple1 = ('The', 'Quick', 'Brown', 'Fox', 'Jumps', 'Over', 'The', 'Lazy', 'Dog')
list1 = ['hello', 'nitish']
print(list(tuple1) + list1)

print('---------------3--------------')
# can we clear tuple
# No, tuples are immutable , so to "clear" a tuple, you can create a new tuple with no elements
t1 = ('a', 'b', 'c')
t1 = ()  # here we create an empty tuple with same  variable name
print(t1)

print('-----------------4---------------')
# can we delete tuple
# No, In Python, tuples are immutable and, therefore, cannot be directly deleted like mutable objects such as lists.
# However, you can delete the entire tuple object by using the del statement. Here's an example
tuple1 = (1, 2, 3)
del tuple1 # this will be completely removed from memory. If you attempt to access tuple1, will give name error


print('---------------5----------------')
# change values of tuple
'''
Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. 
You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

x = ("apple", "banana", "cherry")
y = list(x)  # converted to list
y[1] = "kiwi"
x = tuple(y)  # converted back to tuple

print(x)

# Add Items: workaround
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)   # converted to list
y.append("orange")
thistuple = tuple(y)   # converted back to tuple










