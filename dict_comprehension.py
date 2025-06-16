"""Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this transformation,
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