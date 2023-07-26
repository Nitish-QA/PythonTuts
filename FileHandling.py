'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
SYNTAX: variable = open(filename, mode)
'r'	 Opens the file in read-only mode.
'r+' Opens the file in both read and write mode.
'w'	 Opens the file in write mode. If the file already exists, all the contents will be overwritten. 
If the file doesn’t exist, then a new file will be created.
'a'	 Opens the file in append mode. If the file doesn’t exist, then a new file will be created.
'a+' Opens the file in append and read mode. If the file doesn’t exist, then it will create a new file.
'rb' Opens the file in binary and read-only mode.
'wb+' Opens the file in read, write and binary mode. 
If the file already exists, the contents will be overwritten. 
If the file doesn’t exist, then a new file will be created.

'''

#fo = open("foo.txt", "r+")      # This opens the file in read and write mode
#here we have used 'relative path' for file which will look for file in current working directory

fo = open(r'D:\PythonTuts\foo.txt', 'r+')
# here we have used 'absolute path' for file
# used 'r' before the path name. This is because, in Python, backslash is used to signify special characters.
# r stands for "raw" and will cause backslashes in the string to be interpreted as actual backslashes



fo.write('Nitish\n')     # This writes single string in the file opened in previous step and then \n moves cursor to next line
text = input("Enter a sentence: \n")

fo.writelines(text)     # writelines is used to enter multiple string(like a sentence)

fo.read()  # By default the read() method returns the whole text
fo.read(5)  # you can also specify how many characters you want to return

# Loop through the file line by line:
f = open(r'D:\PythonTuts\test1.txt', "r")
for x in f:
  print(x)

# It is a good practice to always close the file when you are done with it.
f = open(r'D:\PythonTuts\test1.txt', "r")
print(f.readline()) # this prints first line
print(f.readline())  # this prints second line
print(f.readline())  # this prints third line

# close()
f.close()  # this close the file

#NOTE: You should always close your files, in some cases, due to buffering, 
# changes made to a file may not show until you close the file.


# rstrip()
#Output of above program shows extra spances between lines. 
# This is because readline() method reads the string including the \n. 
#Python rstrip() method removes specific characters from the end of a string.

infile = open(r'D:\PythonTuts\test1.txt', 'r')
line1 = infile.readline().rstrip('\n')
line2 = infile.readline().rstrip('\n')
line3 = infile.readline().rstrip('\n')
print(line1)
print(line2)
print(line3)
infile.close()

fo.close()
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)

# tell() and seek() methods
#The tell() method returns the current position of file pointer
print('------------------------------------------------')
f = open(r'D:\PythonTuts\test1.txt', "r")
print(f.tell())  # this returns 0
print(f.readline())
print(f.tell())  # now this will return 1


print('-----------------------------------------')
#The seek() method sets the current file position in a file stream.
#The seek() method also returns the new postion.
#The seek() function in Python is used to move the file cursor to the specified location. 
# When we read a file, the cursor starts at the beginning, but we can move it to a specific position 
# by passing an arbitrary integer

f = open(r'D:\PythonTuts\test1.txt', "r")
f.seek(4)
print(f.readline())

