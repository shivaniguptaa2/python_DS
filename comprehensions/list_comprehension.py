"""List Comprehension offers a shorter syntax when you want to create a new list based on
 the values of an existing list.
 It works well with the all the sequence in python, list, tuple, string, range
 Syntax :
 new_list = [new_item for item in list1]
 also it works with conditions
 Syntax:
 new_list = [new_item for item in list if condition = 'True']
 """

number = [1,2,3]
# new_num =[]
# for num in number:
#     new_num.append(num+1)
# print(new_num)
"""For creating this list, we iterated through exixting list added some conditions over that to get value"""

# new_list = [n+1 for n in number]
# print(new_list)

"""Syntax for list comprehension new_list = [new_item for item in list1]"""
"""Using List comprehension number of lines are redeuced significantly"""

name = 'Shivani'
name_list = [letter for letter in name]
print(name_list)
# num_list = [2*num for num in range(1,5)]
# print(num_list)

# names = ['Shiv','Bhanjo','Shivani','Khushi','Rama','laxman']
# new_name = [name.upper() for name in names if len(name)>5]
# print(new_name)
