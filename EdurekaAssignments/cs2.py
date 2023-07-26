import re
import random


print('-------------1--------------------')
nums = set([1,1,2,3,3,3,4,4])
print(len(nums))

#Output: 4


print('-------------2----------------------')
d ={"john":40, "peter":45}
print(list(d.keys()))

#Output: ['john', 'peter']



print('-----------------3-------------------')

def setPass():
    password = input('Enter new password: ')
    return password

pattern = r'^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@]).{6,12}$'

def validatePass():
    password  = setPass()
    if re.match(pattern, password):
        rpassword  = input("\nRe-Enter to confirm password: ")
        if password == rpassword:
            print("\n \"Password Successful\"")
        else:
             print("\nERROR !! -- Password not matched, please Retry:")
             validatePass()
    else:
        print('''ERROR !! -- Invalid Password: Please follow below rules to create password: \n
              1. At least 1 letter between [a-z]
              2. At least 1 number between [0-9]
              3. At least 1 letter between [A-Z]
              4. At least 1 character from [$#@]
              5. Minimum length of transaction password: 6
              6. Maximum length of transaction password: 12

              Please Retry:\n
              ''')
        validatePass()

validatePass()

print('-----------------4----------------')
a = [4,7,3,2,5,9]

for i in range(len(a)):
    print('index of ', a[i], 'is', i)


print('--------------5----------------')

str1 = input('Enter a String to print letters at even indexes: \n')

for i in range(len(str1)):
    if i%2 == 0:
        print(str1[i], end='')


print('\n----------------6---------------')

print(str1[::-1])


print('---------------7-----------------')

set1 = set()
for i in range(len(str1)):
    if str1[i] not in set1:
        print(str1[i], ',', str1.count(str1[i]))
        set1.add(str1[i])


print('-----------------8------------------')
l1 = [1,3,6,78,35,2,1,24,24,55]
l2 =  [12,24,35,24,88,120,2,1,155]
l3 = []

for i in range(len(l1)):
    if l1[i] in l2 and l1[i] not in l3:
            l3.append(l1[i])

print(sorted(l3))

print('----------------9---------------')
k1 = [1,3,6,78,35,2,1,24,24,55]
k2 = []
for i in range(len(k1)):
    if k1[i] not in k2:
        k2.append(k1[i])

print(k2)

print('----------------10--------------')

m1 = [12,24,35,24,88,120,155]
print(list(x for x in m1 if x != 24))

print('----------------11---------------')

m2 = [12,24,35,70,88,120,155]
print(list(m2[i] for i in range(len(m2)) if i not in (0, 4, 5)))

print('----------------12-----------------')

m3  = [12,24,35,70,88,120,155]
print([x for x in m3 if x%7 != 0 or x%5 != 0])


print('--------------13----------------')
m4  = [x for x in range(1000)]
print(random.choices(m4, k=5))

print('-------------14---------------')

p = int(input("Enter a number n where,  (p > 0): "))
result = sum(i / (i + 1) for i in range(1, p + 1))
print(round(result, 2))



 