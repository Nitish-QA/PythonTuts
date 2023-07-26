'''
The Python os module enables interaction with the operating system.
The os module provides the functions that are involved in file processing operations like renaming, deleting, etc. 
Python has a built-in os module with methods for interacting with the operating system, 
like creating files and directories, management of files and directories, 
input, output, environment variables, process management, etc.



'''

# importing os module 
import os 
      

'''
Reading and writing files The os module provides functions for opening, reading, and writing files. 
For example, to open a file for reading, you can use the open function:

'''
# f = os.open("test.txt", os.O_RDONLY)
# contents = os.read(f, 4)

# To open a file for writing, you can use the os.O_WRONLY flag:
# f = os.open("myfile.txt", os.O_WRONLY)
# Write to the file
# os.write(f, b"Hello, world!")


      
# Get the current working 
# directory (CWD) 
cwd = os.getcwd() 

# Change current working directory 
os.chdir('../')

#os.mkdir()
#os.makedirs()  -- os.makedirs() method in Python is used to create a directory recursively. That means while making leaf directory 
#if any intermediate-level directory is missing, os.makedirs() method will create them all.

os.makedirs('path') 


# Join Directory path
os.path.join('parent_dir', 'child_dir')

# Get LIST of files in Directory:
dir_list = os.listdir('dir_path')

# Remove or Delete a file
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/" 
path = os.path.join(location, 'file.txt') 
os.remove(path)

# Remove Directory
os.rmdir('dir_path')  # this will throw ERROR if directory not empty

# Rename File
os.rename('file_path', 'New_name')

# Check if file Exists
os.path.exists("file_path")

# Gives SIZE of File
os.path.getsize("file_path")

# get last string in the path or dir
path1 = '/dir1/dir2/dir3/file.txt'
path2 = '/dir1/dir2/dir3'
print(os.path.basename(path1))  # this will return file.txt
print(os.path.basename(path2))   # this will return dir3


# Running system commands
# Run the "ls" command and print the output
output = os.system("ls")
print(output)

# You can also use the os.popen function to run a command and get the output as a file-like object:
## Run the "ls" command and get the output as a file-like object
f = os.popen("ls")
output = f.read()
print(output)
# Close the file-like object
f.close()



