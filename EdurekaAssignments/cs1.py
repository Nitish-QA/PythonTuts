print('------------1--------------------')
x = 28
for i in range(1, 28):
    if 28 % i == 0:
        if i % 2 == 0:
            print(i, 'is factor of ', x, 'and an even number')
        else:
            print(i, 'is factor of', x, 'and a odd number')
        continue

print('--------------2----------------------')

userinput = input('Enter name of fruits separated by comma: \n')
list1 = userinput.split(',')
list1.sort()
print(list1)


print('-------------3---------------------')

for i in range(1000, 3000):
    if i % 2 == 0:
        print(i, '\b, ', end='')
        continue


print('\n--------------4--------------------')

str2 = input('Enter a sentence: \n')
letterscnt = 0
digitscnt = 0

for i in range(len(str2)):
    if str2[i].isalpha():
        letterscnt += 1
    elif str2[i].isdigit():
        digitscnt += 1
    else:
        continue
print('No. of letters: ', letterscnt)
print('No. of digits: ', digitscnt)


print('---------------5-------------------')

var1 = input('Enter a word to check if palindrome: \n')
if var1[::-1] != var1:
    print('Entered text is not palindrome')
else:
    print('Entered text is a palindrome')

