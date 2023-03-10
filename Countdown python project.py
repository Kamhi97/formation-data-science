#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    print('Fire in the hole!')

t = input("Enter the length of the countdown in seconds: ")
countdown(int(t))

