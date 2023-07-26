'''
Recursion and loops (like for or while) are two different ways of solving problems that involve repetitive tasks
Both methods can achieve similar results, but they have distinct characteristics and use cases.
The recursive approach might be more elegant and natural for certain problems, but it can consume more memory and may lead to a stack overflow if not implemented correctly. In contrast, 
the iterative approach typically requires less memory and can be easier to optimize for large inputs.
In general, when choosing between recursion and iteration, consider the complexity of the problem, 
the readability of the code, and the efficiency of the implementation

In recursion, when a function calls itself, 
it creates a new instance of that function with a different set of parameters. 
These recursive calls form a chain of function calls, and when a base case is reached, 
the chain starts to unwind.


1. Write a recursive function that accepts an integer argument and returns the factorial.
2. Write a recursive function that accepts two numbers as its argument and returns its power.
3. Write a recursive function that accepts a number as its argument and returns the sum of digits.


'''
print('-----------------------------1-----------------------------')
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)  # Here we are calling same function until n becomes equal to 1
    
n = input('Enter a Number to calculate Factorial: \n')

print(f'Factorial of {n} is {factorial(int(n))}')  # python format feature is used here


print('--------------------------------2------------------------------')
def cal_power(num, power):
    if power == 1:
        return num
    else:
        return num * cal_power(num, power-1)  
    # Every time else condition calls cal_power function and pwer gets decreased 
    # by 1 and continues till it becomes equal to 1. Then once if condition gets satisfies 
    # it returns value of num for each instance of called function and finally

x = input('Enter a number: ')
p = input('Enter its power: ')

print(f"Value of {x} to power {p} is {cal_power(int(x), int(p))}")

print('-------------------------------3--------------------------------')

def cal_sum(num):
    if num < 10:
        return num
    else:
        return num%10 + cal_sum(num // 10)
    # Here num // 10 is division removes last digit from the number:
    
x  = 23445
print(f'Sum of digits of {x} is = {cal_sum(x)}')

''' 
In Python, the single slash / is used for regular division, 
which returns a floating-point result (even if the operands are integers). 
The double forward slash // is used for integer division or floor division, 
which returns the floor value of the division result (rounded down to the nearest integer).
    
'''




