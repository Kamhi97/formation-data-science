#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Write a Pandas program to create and display a DataFrame from the following dictionary data with index labels.

#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
import numpy as np

# define the dictionary data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# define the index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# create the DataFrame
df = pd.DataFrame(exam_data, index=labels)

# display the DataFrame
print(df)
#Print the three first rows using the head() method.
print(df.head(3))
#Delete rows with Nan values
df = df.dropna()
#Extract the 'name' and 'score' columns from the DataFrame.
#Write a Pandas program to append a new row 'k' to the DataFrame with these values (name: "Suresh", score: 15.5, attempts: 1, qualify: "yes").
#Write a Pandas program to delete the 'attempts' column from the DataFrame.
#Add a new column "Success": if the score is higher than 10 we will have 1, else we will have 0.
#After executing the final DataFrame, export it into a CSV file named "my_data".
import pandas as pd
import numpy as np

# define the dictionary data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# define the index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# create the DataFrame
df = pd.DataFrame(exam_data, index=labels)

# extract the 'name' and 'score' columns
df_name_score = df[['name', 'score']]
print(df_name_score)

# # create a DataFrame with the new row
new_row = pd.DataFrame({'name': ['Suresh'], 'score': [15.5], 'attempts': [1], 'qualify': ['yes']}, index=['k'])

# concatenate the original DataFrame and the new DataFrame
df = pd.concat([df, new_row])
print(df)

# delete the 'attempts' column from the DataFrame
df = df.drop(columns=['attempts'])
print(df)

# add a new column 'Success' based on the score
df['Success'] = np.where(df['score'] > 10, 1, 0)
print(df)

# export the final DataFrame to a CSV file named 'my_data'
df.to_csv('my_data.csv')
















# In[ ]:




