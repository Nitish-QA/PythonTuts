# new feature F string  introduced in python 3.6
# It is used to solve string formatting issue


# Earlier we were doing string formating as below

letter =  'Hey my name is {0} and I am from {1}'
name = 'Nitish'
country  = 'India'

print(letter.format(name, country))

# NOW using F string it has become simple

print(f'My name is {name} and I am from {country}')



