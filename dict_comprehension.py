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
 dic=dict.fromkeys(range(5), True)

print(dic)
 
 """

import pandas
import random
names = ['Alex','Bhavin','Cathy','David','Gajala','Harsh','Kunal','Laxman','Neha','Omprakash','Priya','Rohit','Sayantan'
         ,'Toni','Unaf','Vaishnavi','Waqar','Zaheda']

student_scores = {name:random.randint(1,99) for name in names}
# print(student_scores)

data = pandas.DataFrame(list(student_scores.items()),columns=["name","scores"])
print(data)

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
print(result)