#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program to read an entire text file.
filename = 'example.txt'
with open(filename, 'r') as f:
    contents = f.read()
    print(contents)

#2. Write a Python program to read the first n lines of a file.
filename = 'example.txt'
n = 5
with open(filename, 'r') as f:
    for i in range(n):
        line = f.readline()
        print(line)

#3. Write a Python program to read the last n lines of a file.
filename = 'example.txt'
n = 5
with open(filename, 'r') as f:
    # count the total number of lines
    total_lines = 0
    for line in f:
        total_lines += 1
    
    # go back to the beginning of the last n lines
    f.seek(0)
    for i in range(total_lines - n):
        f.readline()
    
    # read and print the last n lines
    for line in f:
        print(line)

#4. Write a Python program that takes a text file as input and returns the number of words of a given text file.
filename = 'example.txt'
with open(filename, 'r') as f:
    contents = f.read()
    words = contents.split()
    print(len(words))

#5. (Bonus) Write a Python program to read the last n lines of a file.
filename = 'example.txt'
n = 5
with open(filename, 'r') as f:
    # count the total number of lines
    total_lines = 0
    for line in f:
        total_lines += 1
    
    # go back to the beginning of the last n lines
    f.seek(0)
    for i in range(total_lines - n):
        f.readline()
    
    # read and store the last n lines in a list
    lines = []
    for line in f:
        lines.append(line.strip())
    
    # print the last n lines in reverse order
    for line in reversed(lines):
        print(line)


# In[ ]:




