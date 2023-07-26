print('------------------1-------------------')
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
a = "Hello"
print(a)

print('---------------2------------------')
# MULTILINE STRINGS

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print('---------------3----------------')
# Strings are Arrays
x = 'Hello, World!'
print(x[1])

print('-------------4----------------')
# looping through strings
y = 'Nitish Kaushal'

for i in y:
    print(i)  # this will print each characters in next line

for x in y:
    print(x, end='')  # now this will print each characters in same line

print('\n--------------5------------------')
# Length of String

z = 'The quick brown fox jumps over the lazy dog'
print('length of sentence is: ', len(z))

print('-----------------6------------------')
# to check whether text present in the string

print('fox' in z)  # this will give a boolean value

print('--------------7-----------------')
# to check whether text NOT present

print('fox' not in z)

print('---------------8------------------')
# Python SLICING -- Print RANGE of String

print(z[3:9])  # this prints strings from index 3 to 9
print(z[:9])  # this prints from start till 9th
print(z[:-9])  # this is negative indexing , it prints from start till 9th character from last
print(z[10:])  # this prints from 10th till end
print(z[-10:-2])  # this will print 1oth character from last till 2nd last character
print(z[-2:-10])  # this is wrong

print('-----------------9------------------')
# Convert to UPPERCASE and LOWERCASE

e = 'Hello World'
print(e.upper())
print(e.lower())

print('-----------------10----------------')
# Remove Whitespace from start and end
f = 'The quick brown fox jumps over the lazy dog'
print(f.strip())

print('----------------11----------------')
# Replace text
g = 'This is java'
print(g.replace(g[-4:], 'python'))
print(g.replace(' ', ''))

print('----------------12------------------')
# Split String

h = 'ram, shyam, gopal, hari, mohan'
print(h.split(','))  # this returns a list
r = 'abcdefghijklmnopqrstuvwxyz'
#print(r.split('')  # this is wrong,a s delimmiter cannot be empty
print(list(r))

print('------------------13------------------')
# Reverse String
i = 'Hello World!'
print(i[::-1])
print(i[::-2])  # check difference between the two


# A function for doing the same
def my_function(k):
    return k[::-1]


mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

print('---------------14-------------------')
# Concatenate Strings

l = 'Hello'
m = 'world'
print(l + m)

print('-----------------15----------------')
# format strings

age = 36
txt = 'My name is Nitish and my age is: {}'
print(txt.format(age))

# More Example
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {} dollars for {} pieces of item {}'
print(myorder.format(price, quantity, itemno))

# we can also write index numbers to make sure its in right order
myorder2  = 'I want to pay {2} dollars for {0} pieces of item {1}'
print(myorder2.format(quantity, itemno, price))


print('----------------16------------------')
# ESCAPE Characters used to insert illegal characters in string

#txt = 'We are the so-called 'Vikings' from the north.'  # using quotes inside quote is invalid
txt = 'We are the so-called \"Vikings\" from the north.'
print(txt)

# other escape characters are
# \n -(new line)  \t - (insert tab space) \\ - (insert single space)

print('--------------17----------------')
# STRING METHODS
str = 'The Quick Brown Fox Jumps Over The Lazy Dog'
# capitalise() Converts the first character to upper case
print(str.capitalize())


# casefold() Converts string into lower case
print(str.casefold())
# OR
print(str.lower())

# count() to count occurance of a character or string
print(str.count('the'))  # counts occurance of 'the'
print(str.lower().count('the'))  # convert all to lower and than counts occurance of 'the'
print(str.strip().lower().count('o'))  # removes whitespaces and converts all to lower and than counts 'o'

# endswith() to check if string ends with some character, returns boolean
print(str.endswith('the'))
print(str.endswith('g'))

# find() to search string and returns its location
print(str.find('Fox'))

# index() searches string and returns its value
print(str.index('Fox'))

# isalpha() returns true if all characters  in string are alphabet
print(str.isalpha())  # return false as there is whitespaces in the string
print(str.replace(' ', '').isalpha())  # return true remove whitespaces and then checked

# isalnum() , isascii(), isdigit(), islower(), isnumeric(), isupper()











