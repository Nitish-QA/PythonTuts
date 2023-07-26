print('------------------1--------------------')
# Get Data Type of a variable using type() function
x = 4
y = 'rahul'

print(type(x))
print(type(y))

print('---------------2--------------------')
# change data type of a variable  explicitly // CASTING // convert one type to other

a = 4
b = 5
b = str(b)
c = float(a)
print(type(b))
print(type(c), c)

print('--------------------3-----------------')
# We can assign values to all variables in one line
x, y, z = 'orange', 'banana', 'apple'
print(x)
print(y)
print(z)

print('----------------4--------------------')
# we can assign same values to multiple variables
x = y = z = 'orange'
print(x)
print(y)
print(z)

print('----------------5---------------------')
# we can assign whole collection to a vairables in one line
fruits = ['orange', 'banana', 'apple']
x, y, z = fruits
print(x)
print(y)
print(z)

print('----------------6-------------------')
# GLOBAL variables and LOCAL variables

w = 'awesome'  # global variable
z = 'Nitish'  # global variable
q = 'kaushal'


def myfunc():
    w = 'fantastic'  # local variable
    print('value of w is ' + w)  # this will not print global variable as local variable is declared with same name
    print('value of z is ' + z)  # this will print global variable value

    # to print and update global variable value inside a function use global keyword
    global q
    q = 'nitish kaushal'  # Now this modified value of global variable
    print(' value of global q is ' + q)

    global m
    m = 'new'


myfunc()
print('value of w is ' + w)
print('value of z is ' + z)
print('value of q is ' + q)
print('value if m is ' + m)
