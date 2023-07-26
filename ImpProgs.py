# We can store group of lists in a dictionaries

lists = {}  # Create an empty dictionary to store the lists

for i in range(2):
    lists['list' + str(i)] = input('Enter comma-separated strings for list{}: '.format(i)).split(',')

print(lists['list0'])  # Access the first list using the dictionary key 'list0'
print(lists['list1'])

# write a program to print comma separated even numbers from 1000-3000 in same line

for i in range(1000, 3000):
    if i % 2 == 0:
        print(i, '\b, ', end='')
        continue

# can tell the output here:
set1 = {}
print(type(set1))

#correct way is:
set2 = set()

