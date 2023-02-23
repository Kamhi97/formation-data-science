#!/usr/bin/env python
# coding: utf-8

# In[1]:


#EXERCICE 1
#Write a Python function to find the largest (max) of three numbers.
#For example, the max of these three numbers (20, 35, 19) is 35
def find_max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num
max_num = find_max(20, 35, 19)
print(max_num)  


# In[2]:


#EXERCICE 2
#Write a function calculation() so it can accept two variables and calculate the addition and subtraction of them. It must return both addition and subtraction in a single return call.
#For example:
#calculation(40, 10) should produce 50, 30
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
result = calculation(40, 10)
print(result) 


# In[4]:


#EXERCICE 3

#Write a function that sums the elements of a list of integers.
#Write a function that multiplies the elements of an integer list.
#Use the two functions to sum the elements whose position is an even number (0,2,4…) and multiply the rest.
#Hint: Consider extracting two lists from a first list.

def sum_list_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

def multiply_list_elements(lst):
    total = 1
    for num in lst:
        total *= num
    return total
original_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
even_list = original_list[::2]  # Extract even-indexed elements
odd_list = original_list[1::2]  # Extract odd-indexed elements


# In[ ]:


#EXERCICE 4
#write a function that displays the first letter of the dictionary value in upper case by using the return statement.ù
def first_letter_to_upper(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[key] = value[0].upper()
    return new_dict
my_dict = {"apple": "ant", "banana": "ball", "cherry": "cat"}
new_dict = first_letter_to_upper(my_dict)
print(new_dict)  # Output: {'apple': 'A', 'banana': 'B', 'cherry': 'C'}


# In[ ]:


#EXERCICE 5
#write a function that returns the largest word in the dictionary.
def largest_word(dictionary):
    largest = ""
    for key in dictionary.keys():
        if len(key) > len(largest):
            largest = key
    return largest
my_dict = {"apple": "fruit", "banana": "fruit", "carrot": "vegetable", "pepper": "vegetable"}
largest = largest_word(my_dict)
print(largest)  # Output: 'carrot'


# In[ ]:


#EXRCICE 6
#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample items: green-red-yellow-black-white
#Expected result: black-green-red-white-yellow
#Hint: There's a split function to separate your input string into words and a sort function to sort.
input_string = input("Enter a hyphen-separated sequence of words: ")
word_list = input_string.split("-")
word_list.sort()
output_string = "-".join(word_list)
print(output_string)


# In[5]:


#EXERCICE 7
#Write a function that calculates and prints the value according to the given formula: Q = square root of [(2 * C * D)/H]. Following are the fixed values of C and H: C is 50, and H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example: Let us assume the following comma-separated input sequence is given to the function: 100,150,180. 
#Expected result: 18,22,24 
#Hints: If the output received is in decimal form, it should be rounded off to its nearest value. For example, if the output received is 26.0, it should be printed as 26. In the case of input data being supplied to the question, it should be assumed to be a console input. 

import math

def calculate_Q(input_string):
    C = 50
    H = 30
    input_list = input_string.split(",")
    result_list = []
    for D in input_list:
        Q = math.sqrt((2*C*int(D))/H)
        result_list.append(str(round(Q)))
    result_string = ",".join(result_list)
    print(result_string)
calculate_Q("100,150,180")  


# In[ ]:




