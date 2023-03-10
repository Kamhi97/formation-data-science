#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1
#Write a Python program to convert an array to an ordinary list with the same items.
#We can use the np.tolist() function.

import numpy as np
# create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
# convert the array to a list
lst = arr.tolist()
# print the list
print(lst)


# In[5]:


#Question 2 
#Write a NumPy program to compute the sum of the diagonal elements of a given array.
#Hint: There are two possible methods to solve this problem: 
#Manually (without direct function). 
#Using the trace function.

import numpy as np
# create a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# manually compute the diagonal sum
diagonal_sum = 0
for i in range(len(arr)):
    diagonal_sum += arr[i][i]
# print the diagonal sum
print(diagonal_sum)


# In[6]:


#Question 3
#Given an array of your choice, get all the values higher than X:
#If a = [[1,2],[3,5]] and x = 2 :  then 3 and 5 are higher than 2. 

import numpy as np
# create a NumPy array
a = np.array([[1, 2], [3, 5]])
# define the value to compare with
x = 2
# get all the values higher than x
result = a[a > x]
# print the result
print(result)


# In[7]:


#Question 4
#Given two arrays, A & B have the same shape. 
#The task is to apply addition by hand: C is the new array

import numpy as np
# create two NumPy arrays of the same shape
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# initialize a new array of the same shape
C = np.zeros_like(A)
# perform element-wise addition
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        C[i][j] = A[i][j] + B[i][j]
# print the result
print(C)


# In[13]:


#Question 5
#Write a NumPy program to subtract the mean of each row of a given matrix.
#Hint: use the mean function

import numpy as np
# create a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# calculate the mean of each row
row_means = np.mean(arr, axis=1)
# subtract the row means from each element in the corresponding row using broadcasting
arr = arr - row_means[:, np.newaxis]
# print the result
print(arr)


# In[ ]:





# In[ ]:





# In[ ]:




