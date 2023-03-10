#!/usr/bin/env python
# coding: utf-8

# In[ ]:




###########index error#############

##Exemple 1
    
#mylist=[14, "hello", 967]
#mylist[6]

#The error in this code is a "IndexError: list index out of range" because the list mylist has only three elements and trying to access the 7th index (which is 6 in Python indexing since the first index is 0) results in an error.
#To fix this error, you can either remove the line mylist[6] or modify it to access a valid index within the range of the list, such as mylist[0] to access the first element, mylist[1] to access the second element, and so on.

mylist = [14, "hello", 967]
# Accessing the third element (index 2) of mylist
print(mylist[2])


##Exemple 2
#import Pandas
#import NumPy

import pandas as pd
import numpy as np
#In this code, we are importing the Pandas library and assigning it the alias pd. We are also importing the NumPy library and assigning it the alias np. This is a common convention to make it easier to refer to these libraries throughout our code.
#Note that I corrected the capitalization of Pandas and NumPy. In Python, the capitalization of library names matters, and these libraries are typically imported with lowercase letters for consistency with their package names.


# In[ ]:


###########syntax error#############

print"python errors"

print("python errors")

#In this code, we are using the print() function to display the text "python errors" on the console.
#Note that I corrected the capitalization of Print to print since Python is a case-sensitive language
#and the function name must be in lowercase.


# In[ ]:


#############key error################

mydictionnary={True:"hello",False:"bye", '3':"python"}
mydictionnary['True']

#The error in this code is a KeyError, which occurs when we try to access a key in a dictionary that does not exist.
#Specifically, the line mydictionnary['True'] is trying to access the value associated with the key "True", but the dictionary mydictionnary does not have a key with that name. 
#Instead, it has a key with the boolean value True.
#To fix this error and access the value associated with the key True, we can use the boolean value True instead of the string "True". Here's the corrected code:
#mydictionary = {True: "hello", False: "bye", '3': "python"}

# Accessing the value associated with the key True
print(mydictionary[True])
#In this code, we are using the boolean value True to access the value associated with the key True. The output of this code will be hello, which is the value associated with the boolean key True in the dictionary mydictionary.


# In[1]:


#########indentation error#########

i=14
while i<78:
print(i)
i+=1
#The error in this code is an IndentationError. In Python, the indentation of code is significant and is used to group statements together in blocks. In this case, the print() statement inside the while loop is not indented correctly, 
#so Python does not know that it is part of the loop and raises an IndentationError.
#To fix this error, we need to indent the print() statement to indicate that it is inside the loop. Here's the corrected code:

i = 14
while i < 78:
    print(i)
    i += 1
#In this code, we have indented the print() statement and the i += 1 statement to indicate that they are inside the while loop. This code will print the numbers from 14 to 77 to the console, with each number on a separate line.


# In[ ]:


##################StopIteration###############

it=iter([1,2,3])
next(it)
next(it)
next(it)
next(it)

#The error in this code is a StopIteration error, which occurs when we try to call next() on an iterator that has already been exhausted. Specifically, the fourth next() call in the code is trying to get the next value from the iterator it, but there are no more values to retrieve, 
#so Python raises a StopIteration error.
#To fix this error, we can either stop calling next() when there are no more values in the iterator, or we can handle the StopIteration error using a try-except block. Here's an example of the second approach:

it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))
# No more values in the iterator, so we don't call next() again
#In this code, we are only calling next() three times, which is the number of items in the iterator. 
#This code will print the values 1, 2, and 3 to the console, without raising a StopIteration error.


# In[ ]:


########TypeError########
'15'+15
#he error in this code is a TypeError, which occurs when we try to perform an unsupported operation on two operands of different types. In this case, the + operator is being used to concatenate a string ('15') with an integer (15), which is not a valid operation in Python.
#To fix this error, we need to convert one of the operands to the same type as the 
#other operand before we can perform the + operation. Here are a couple of possible solutions:
# Convert the integer to a string before concatenating
result = '15' + str(15)
print(result)  # Output: '1515'

# Convert the string to an integer before adding
result = int('15') + 15
print(result)  # Output: 30
    


# In[ ]:


#########ValueError###########
int('python')
#The error in this code is a ValueError, which occurs when we try to convert a string to an integer, but the string does not represent a valid integer. In this case, the string 'python' is not a valid integer, so Python raises a ValueError.
#To fix this error, we need to provide a string that can be converted to an integer. 
#Here's an example of converting the string '123' to an intege.

result = int('123')
print(result)  # Output: 123


# In[ ]:


########NameError#######

NameErrorTraceback (most recent call last)
<ipython-input-14-32886514c262> in <module>()
----> 1 python

NameError: name 'python' is not defined
    
#To fix this error, we need to either define the variable python or remove the reference to it from the code. 
# Define the variable `python`
python = "Hello, Python!"
print(python)  # Output: 'Hello, Python!'
    


# In[ ]:


#######ZeroDivisionError######
x=19/0

#To fix this error, we need to either change the divisor to a non-zero number .

# Change the divisor to a non-zero number
x = 19 / 5
print(x) 
    
    

