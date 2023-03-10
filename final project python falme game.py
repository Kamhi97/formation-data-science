#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling.
#This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.
#Python is a multipurpose language and one can do literally anything with it. 
#Python can also be used for game development. Let’s create a simple FLAMES game without using any external game libraries like PyGame.
#There are two steps in this game:
#Take the two names.
#Remove the common characters with their respective common occurrences.
#Get the count of the characters that are left.
#Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]
#Start removing letters using the count we got.
#The letter which lasts the process is the result.

#######################################################################################

def remove_common_letters(name1, name2):
    """Removes common letters between two names"""
    name1 = name1.upper()
    name2 = name2.upper()
    common_letters = set(name1) & set(name2)
    for letter in common_letters:
        count = min(name1.count(letter), name2.count(letter))
        name1 = name1.replace(letter, '', count)
        name2 = name2.replace(letter, '', count)
    return name1, name2

def get_flames_result(count):
    """Removes letters from FLAMES using the given count"""
    letters = list('FLAMES')
    while len(letters) > 1:
        index = (count - 1) % len(letters)
        letters.pop(index)
        letters = letters[index:] + letters[:index]
    return letters[0]

def play_flames():
    """Plays the FLAMES game"""
    name1 = input("Enter the name of the first player: ")
    name2 = input("Enter the name of the second player: ")
    name1, name2 = remove_common_letters(name1, name2)
    count = len(name1) + len(name2)
    result = get_flames_result(count)
    status = {'F': 'Friends', 'L': 'Lovers', 'A': 'Affectionate',
              'M': 'Marriage', 'E': 'Enemies', 'S': 'Sibling'}
    print(f"Relationship status: {status[result]}")
    
    #To play the game, you can simply call the play_flames() function. 
    #The function prompts the user to enter the names of the two players, removes the common letters between them,
    #calculates the count of the remaining letters, and then removes letters from FLAMES using the count to determine the result. 
    #Finally, the function prints the relationship status based on the last remaining letter.


####################################################################################################

