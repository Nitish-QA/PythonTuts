'''
NOTE: we can use 'else' statement with for loop as well
NOTE: The pass statement is used as a placeholder for future code. 
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code 
is not allowed.
'''
def result(marks):
    for i in marks:
        if i >= 30:
            pass
        else:
            print('FAIL')
            break
    else:
        print('PASS')

result([38, 80, 70, 90])

'''
NOTE: lets understand Decorators concept
Q. Suppose we have created a function to print result of 
student that takes list of marks in all subjects as argument.
if the mark in any subject is less than 30 then the result will be FAIL
Now, later in time we decided to add ditinction remark to students who scored more than 70 in subject
But we don't want to modify the existing function as this distinction feature we may not use always.
Here in this case using decorator may be useful.

Lets see the example
'''
def check_distinction(func): # created a function that takes fuction as an argument and returns a function
    def distinction(list_marks):  
        for i in list_marks:
            if i >= 75:
                print(f'{i} is DISTINCTION')
        func(list_marks)  
    return distinction

@check_distinction
def result(marks):
    for i in marks:
        if i >= 30:
            pass
        else:
            print('FAIL')
            break
    else:
        print('PASS')

result([38, 80, 70, 90])


