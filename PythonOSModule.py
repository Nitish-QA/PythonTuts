'''
The Python os module enables interaction with the operating system.
The os module provides the functions that are involved in file processing operations like renaming, deleting, etc. 
Python has a built-in os module with methods for interacting with the operating system, 
like creating files and directories, management of files and directories, 
input, output, environment variables, process management, etc.

'''

# importing os module 
import os 
      
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
print(os.path.basename(path1))



