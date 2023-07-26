'''
The with statement was introduced in python 2.5. 
The with statement is useful in the case of manipulating the files. 
The advantage of using with statement is that it provides the guarantee to close the file 
regardless of how the nested block exits.

It is always suggestible to use the with statement in the case of files because, 
if the break, return, or exception occurs in the nested block of code then it automatically closes the file, 
we don't need to write the close() function. It doesn't let the file to corrupt.

'''

with open("file.txt",'r') as f:    
    content = f.read();    
    print(content)  