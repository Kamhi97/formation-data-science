#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exrcice 1
#Write a Python program that multiplies all the items in a list.
#Sample list= [2, 3, 6]
#Result = 36
#solution 1
list=[2,3,6]
mult=list [0]*list[1]*list[2]
print(mult)
#solution 2
lst = [2, 3, 6]
result = 1
for num in lst:
    result *= num
print(result)


# In[ ]:


#Exercice 2
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#Hint: You can use the sort function.

def sort_list_by_last_element(tuple_list):
    def sort_key(tuple_elem):
        return tuple_elem[-1]
    tuple_list.sort(key=sort_key)
    return tuple_list
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_list_by_last_element(tuple_list)
print(sorted_list) 


# In[ ]:


#Question 3 

#Write a Python program that combines two dictionaries by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}

def combine_dicts(d1, d2):
    combined_dict = {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1) | set(d2)}
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = combine_dicts(d1, d2)


# In[ ]:


#Question 4
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
#so that is an integral number between 1 and n (both included). Then the program should print the dictionary.
#Suppose the following input is supplied to the program: 8. Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input("Enter an integer: "))
square_dict = {}
for i in range(1, n+1):
    square_dict[i] = i*i

print(square_dict)


# In[ ]:


#Question 5
#Write a program to sort a tuple by its float element.
#For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

# Input tuple
lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Sort the tuple by float element
sorted_lst = sorted(lst, key=lambda x: float(x[1]), reverse=True)
print(sorted_lst)


# In[3]:


#Question 6
#Write a Python program to create a set.
#Examples : {0, 1, 2, 3, 4}
#Write a Python program to iteration over sets.
#Write a Python program to add members in a set and to remove items from a given set.

# Create an empty set using the set() function
my_set = set()
print(type(my_set))  
# Add elements to the set
my_set.add(0)
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
print(my_set) 
# Iterate over the set
for element in my_set:
    print(element)
# Add a single element to the set
my_set.add(5)
# Add multiple elements to the set using the update() method
my_set.update([6, 7, 8])
# Print the updated set
print(my_set)  
# Remove an element from the set
my_set.remove(8)
# Print the updated set
print(my_set) 


# In[ ]:




