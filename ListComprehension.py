print('----------------10-----------------')

m1 = [12,24,35,24,88,120,155]
print(list(x for x in m1 if x != 24))

print('----------------11-----------------')

m2 = [12,24,35,70,88,120,155]
print(list(m2[i] for i in range(len(m2)) if i not in (0, 4, 5)))

print('----------------12-----------------')

m3  = [12,24,35,70,88,120,155]
print([x for x in m3 if x%7 != 0 or x%5 != 0])

'''
PRACTICE SET1:
1. Find all of the numbers from 1–1000 that are divisible by 8
2. Find all of the numbers from 1–1000 that have a 6 in them
3. Count the number of spaces in a string (use string above)
4. Remove all of the vowels in a string (use string above)
5. Find all of the words in a string that are less than 5 letters (use string above)
6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)
7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by

'''

print('------------------1-------------------')
print([x for x in range(1, 1000) if x%8 == 0])


print('------------------2-------------------')
print([x for x in range(1, 1000) if '6' in str(x)])

print('------------------3-------------------')
str1 = "Practice Problems to Drill List Comprehension in Your Head."
print(len([x for x in str1 if x == ' ']))

print('------------------4-------------------')
print([x for x in str1 if x not in ['a', 'e', 'i', 'o', 'u']])

print('-----------------5-----------------------')
print([x for x in str1.split(' ') if len(x) < 5])

print('-----------------6----------------------')
print({x: len(x) for x in str1.split(' ') })

print('------------------7-----------------')
print({x for x in range(2, 1000) for y in range(2, 9) if x%y == 0})

print('----------------8------------------')


'''
9. Find all of the numbers from 1-1000 that are divisible by 7
10. Find all of the numbers from 1-1000 that have a 3 in them
11. Count the number of spaces in a string
12. Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
13. Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
14. Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
16. Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
17. Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
18. Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
19. Find all of the words in a string that are less than 4 letters
20. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
21. Write a list comprehension that returns the list ["1**2=1", "2**2=4", "3**2=9", ...., "25**2=625"]

'''



