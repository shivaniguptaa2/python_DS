"""
https://www.datacamp.com/tutorial/python-dictionary-comprehension
Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this transformation,
 items within the original dictionary can be conditionally
 included in the new dictionary, and each item can be transformed as needed.
 1.Using zip() function
 keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

# but this line shows dict comprehension here  
myDict = { k:v for (k,v) in zip(keys, values)}  

# We can use below too
# myDict = dict(zip(keys, values))  

print (myDict)

 2.Using fromkeys() Method
 Python also offers the fromkeys() method, which allows you to create dictionaries with a uniform value for a specified set
of keys. This method is useful when initializing dictionaries with default values. 

 dic=dict.fromkeys(range(5), True)
print(dic)
 
 """

"""Important while iterating dictionary
Iterating over Dictionaries: When iterating directly over a dictionary without explicitly using .items(), .keys(), 
or .values(). If you iterate over dict directly, it yields only keys, and if you try to unpack these keys into 
multiple variables, it will lead to the below error.

    my_dict = {'a': 1, 'b': 2}
    for key, value in my_dict: # This will raise the error because iterating over my_dict yields only keys.
        pass
 Error: "too many values to unpack (expected 2)"

 Correct dictionary iteration: When iterating over a dictionary to access both keys and values, 
 use the .items() method.

     my_dict = {'a': 1, 'b': 2}
    for key, value in my_dict.items(): # Correct way to iterate over key-value pairs.
        print(f"{key}: {value}")
"""

import pandas
import random
names = ['Alex','Bhavin','Cathy','David','Gajala','Harsh','Kunal','Laxman','Neha','Omprakash','Priya','Rohit','Sayantan'
         ,'Toni','Unaf','Vaishnavi','Waqar','Zaheda']

student_scores = {name:random.randint(40,99) for name in names}
# print(student_scores)

data = pandas.DataFrame(list(student_scores.items()),columns=["name","scores"])
# print(data)


"""Conditional dictionary comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

if condition
# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}

Multiple if conditions

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}

"""
passed_student = {name:score for (name,score) in student_scores.items() if score> 60}
result = pandas.DataFrame(list(passed_student.items()),columns=["names","score"])
# print(result)

"""Converting Dictionary to Dataframe
 Very important while creating dataframe from list and dictionary, there
 is small transition happen.

 Case 1:
 =>So we have a dictionary
=>{'ram':33,'Shayam':22,'Hetal':44} 
=>I want to convert this into datafarme

import pandas as pd

data = {'ram': 33, 'Shayam': 22, 'Hetal': 44}
df = pd.DataFrame(list(data.items()), columns=['name', 'score'])
print(df)

Here why we have converted it into list(), list(data.items())

Ans: When you use list(data.items()), it converts the dictionary into a list of key-value pairs (tuples), like this:
[('ram', 33), ('Shayam', 22), ('Hetal', 44)]

This format is ideal for creating a DataFrame with two columns: one for the keys (name) and one for the values (score).
If you pass the dictionary directly to pd.DataFrame, pandas will treat the keys as column names
 and create a single row, which is usually not what you want.

 Case 2: 
=>name = ['shivani','syana','shri']
=>Score = ['33,'34','55]

=>I want to create dataframe for this

import pandas as pd

name = ['shivani', 'syana', 'shri']
Score = [33, 34, 55]  # Remove quotes to make them integers

df = pd.DataFrame({'name': name, 'score': Score})
print(df)

=> I want to convert to dictionary first then dataframe

import pandas as pd

name = ['shivani', 'syana', 'shri']
Score = [33, 34, 55]

# Step 1: Convert to dictionary
data_dict = dict(zip(name, Score))
print(data_dict)
# Output: {'shivani': 33, 'syana': 34, 'shri': 55}

# Step 2: Convert dictionary to DataFrame
df = pd.DataFrame(list(data_dict.items()), columns=['name', 'score'])
print(df)

Here Again it user list(), So the point to be noted is when the dataframe is created from 
dictionary it needs to be converted to list first then only it will take name and score
as column else it will be taking names as column and scores as row
like this 
Alex	Bhavin	Cathy
45	      67	 12
"""


"""Iteration over dataframe
1. 1. Iterate over rows with iterrows()
Each row is returned as an (index, Series) pair.
"""

df = pandas.DataFrame({'names': ['shivani', 'syana', 'shri'], 'score': [33, 34, 55]})

for index, row in df.iterrows():
    # print(row['name'], row['score'])
    # print(row.score)
    print(row.names)
    """This is not printing the name from dataframe but the index, there is reason for this
    This happens because of how pandas handles attribute access in iterrows():

row['score'] accesses the value in the 'score' column (recommended and always works).
row.score also works if the column name is a valid Python identifier (no spaces, doesn’t conflict 
with Series attributes).
However, for row.name:

In pandas, row.name is a special attribute that returns the row index, 
not the value from a column named 'name'."""

"""However if you change the column name to student, it will work fine, give it a try!!"""

"""2. Iterate over rows with itertuples()
Faster and returns namedtuples."""

# for row in df.itertuples(index=False):
#     print(row.name, row.score)

"""3. Iterate over columns"""

# for col in df.columns:
#     print(col)


"""Note:

For most tasks, itertuples() is preferred for speed.
Avoid using loops for large DataFrames; use vectorized operations when possible.
"""