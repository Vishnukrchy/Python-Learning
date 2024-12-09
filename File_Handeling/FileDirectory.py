#Python directory
# => A directory is a collection of files and subdirectories.
# Python has a built-in module called os that provides functions for interacting with the operating system.
# os module provides functions for creating, removing, and modifying directories and files.

# get current working directory
import os
# get current working directory
print(os.getcwd())# print current working directory

# change current working directory
# os.chdir("D:\\")# change current working directory
# print(os.getcwd())# print current working directory //drive letter
# create a new directory
# os.mkdir("mydir")# create a new directory
# remove a directory
# os.rmdir("mydir")# remove a directory


# List all files in a directory
import os

for file in os.listdir():
    print(file)

print(os.listdir('D:\\') )   # retrun list of all files in directory


# remove a file
# os.remove("mydir")# remove a file

# delete a file recursively
os.remove("D:\\mydir")
