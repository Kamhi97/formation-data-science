#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program for a binary search.
#Test Data: 

#binary_search([1,2,3,5,8], 6) -> False
#binary_search([1,2,3,5,8], 5) -> True

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# test the function
print(binary_search([1,2,3,5,8], 6)) # False
print(binary_search([1,2,3,5,8], 5)) # True


 #    2. Write a Python program to calculate the value of 'a' to the power 'b'.

#Test Data: 

#(power(3,4) -> 81


ddef power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

# test the function
print(power(3, 4)) # 81


  #     3. Write a Python program to sort a list of elements using the bubble sort algorithm.

#Sample Data: [29,13,22,37,52,49,46,71,56]

#Expected result: [13, 22, 29, 37, 42, 46, 49, 56, 71]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# test the function
arr = [29,13,22,37,52,49,46,71,56]
print(bubble_sort(arr)) # [13, 22, 29, 37, 46, 49, 52, 56, 71]



     # 4. Write a Python program to sort a list of elements using the merge sort algorithm.

#Sample Data: [29,13,22,37,52,49,46,71,56]

#Expected result: [13, 22, 29, 37, 42, 46, 49, 56, 71]
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# test the function
arr = [29,13,22,37,52,49,46,71,56]
print(merge_sort(arr)) # [13, 22, 29, 37, 46, 49, 52, 56, 71]

      # 5. Write a Python program to sort a list of elements using the quick sort algorithm.

#Sample Data: [29,13,22,37,52,49,46,71,56]

#Expected result: [13, 22, 29, 37, 42, 46, 49, 56, 71]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left_half = [x for x in arr[1:] if x <= pivot]
        right_half = [x for x in arr[1:] if x > pivot]
        return quick_sort(left_half) + [pivot] + quick_sort(right_half)

# test the function
arr = [29,13,22,37,52,49,46,71,56]
print(quick_sort(arr)) # [13, 22, 29, 37, 46, 49, 52, 56, 71]


# In[ ]:




