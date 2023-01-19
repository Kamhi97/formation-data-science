#!/usr/bin/env python
# coding: utf-8

# In[2]:


#  Question 1
#  Write a Python program that accepts the user's first and last name
#  print them in reverse order with a space between them.


x = input("Enter your First Name : ");
y = input("Enter your Last Name : ");
print (  y,x, )


# In[1]:


# Question 2

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# The sample value of n is 5. Expected Result: 615 (5+55+555).

n=5
nn=55
nnn=555
sum_n=n+nn+nnn
print(sum_n,"(55+55+555)")


# In[5]:


# Question 3

# Write a Python program to find whether a given number (accept from the user) is even or odd
# print out an appropriate message to the user.
# string in string formatig .

number=int(input("Enter an number : "))
if (number % 2) ==0 :
    print("{} is Even".format(number))
else:
    print("{} is Odd".format(number))


# In[9]:


#Question 4
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included). The numbers obtained should be printed in a sequence on a single line.
#Hints: Consider use range(#begin, #end) method 
#solution 1
for num in range(2000, 3201):
   if num % 7 == 0 and num % 5 != 0:
     print(str(num),end ="-")
        
#solution 2
nums = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        nums.append(str(num))
print(','.join(nums))


# In[12]:


#Question 5
#Write a program that can compute the factorial of a given number. 
#The results should be printed in a sequence on a single line. 
#Suppose the following input is supplied to the program: 8. Then, the output should be: 40320 
#Hint: The factorial function (symbol: !) multiplies all whole numbers from our chosen number down to 1. Examples: 
#4! = 4 × 3 × 2 × 1
#8! = 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1
#1! = 1
#0! = 1 (by convention)
num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[ ]:


#Exercice 6
#Write a program to remove the characters 
#which have odd index values of a given string.
#For example: string ="hello team"
#The result should be: hlota
string = str(input("Enter a sentence : "))
new_string = string[::2]
print(new_string)


# In[ ]:


#Question 7
#In this challenge, you must discount a price according to its value.
#- If the price is 500 or above, there will be a 50% discount.
#- If the price is between 200 and 500 (200 inclusive), there will be a 30% discount.
#- If the price is less than 200, there will be a 10% discount.
price = float(input("Enter initial price : "))
if price>= 500 :
    discount1 =price-((50*price)/100)
    print(discount1)
elif 200 <= price < 500:
    discount2=price*0.7
    print(discount2)
else:
    discount3 = price*0.9
    print(discount3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




