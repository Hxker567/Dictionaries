#Dictionary methods

#len()
# Returns length or number of key: value pairs of the dictionary passed as the argument.

# For ex
# dict1 = {'mohan': 50,'ankit': 89,'ram':78,'laxman':90}
# print(len(dict1))
# Output:4


#dict()
# creates a dictionary from a sequence of key-value pairs

# For ex
# pair1 = [('mohan',60),('ram',70),('suhel',80),('sangeeta',90)]
# print(pair1)
# [('mohan', 60), ('ram', 70), ('suhel', 80), ('sangeeta', 90)]
# dict1 = dict(pair1)
# print(dict(pair1))
# Output:{'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90}


#keys()
# returns a list of keys in the dictonary

# For ex
# dict1 = {'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90}
# print(dict1.keys())
# Outout:dict_keys(['mohan', 'ram', 'suhel', 'sangeeta'])


#values()
# returns a list of values in the dictionary

# For ex
# dict1 = {'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90}
# print(dict1.values())
# Output:dict_values([60, 70, 80, 90])


#items()
# returns a list of tuples (key--value) pair

# For ex
# dict0 = {'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90}
# print(dict0.items())
# Output:dict_items([('mohan', 60), ('ram', 70), ('suhel', 80), ('sangeeta', 90)])


#get()
# returns the key corresponding to the key passed as the argument. If the key is not present in the dictionary it will return none.

# For ex
# dict1 = {'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90}
# print(dict1.get('mohan'))
# Output:60


#update()
# appends the key-value pair of the dictionary passed as the argument to the key-value pair of the given dictionary 

# For ex-
# dict1 = {
#     'mohan': 60,
#     'ram': 70, 
#     'suhel': 80, 
#     'sangeeta': 90
# }
# print(dict1)
# dict2 = {
#     'laxman': 50,
#     'sita': 75
# }
# dict1.update(dict2)
# print(dict1)
# Output:{'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90, 'laxman': 50, 'sita': 75}


#clear()
# deletes or clear all the items of the dictionary

# For ex
# dict1 = {'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90, 'laxman': 50, 'sita': 75}
# print(dict1.clear())
# print(dict1)
# Output:{}


#del()
# deletes the item with the given key. To delete the dictionary from the memory we write: del Dict_name.

# For ex 
# dict1 = {'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90, 'laxman': 50, 'sita': 75}
# del dict1 ['sita']
# print(dict1)
# Output:{'mohan': 60, 'ram': 70, 'suhel': 80, 'sangeeta': 90, 'laxman': 50}


#Manipulating dictionaries
# a)Create a dictionary 'ODD' of odd numbers between 1 to 10, where the key is the decimal number and the value is the corresponding number in words
# ODD = {1:'one',3:'three',5:'five',7:'seven',9:'nine'}
# ODD
# print(ODD)
# Output:{1: 'one', 3: 'three', 5: 'five', 7: 'seven', 9: 'nine'}

# b)Display the keys in dictionary 'ODD'
# ODD.keys()
# print(ODD.keys())
# Output:dict_keys([1, 3, 5, 7, 9])

# c)Display the values in dictionary 'ODD'
# ODD.values()
# print(ODD.values())
# Output:dict_values(['one', 'three', 'five', 'seven', 'nine'])

# d)Display the items from dictionary 'ODD'
# ODD.items()
# print(ODD.items())
# Output:dict_items([(1, 'one'), (3, 'three'), (5, 'five'), (7, 'seven'), (9, 'nine')])

# e)Find the length of the dictionary 'ODD'
# print(len(ODD))
# Output:5

# f)Check if 7 is present or not in dictionary 'ODD'
# 7 in ODD
# print(7 in ODD)
# Output:True

# g)Check if 2 is present or not in dictionary 'ODD'
# 2 in ODD
# print(2 in ODD)
# Output:False

# h)Retrive the value corresponding to the key 9
# ODD.get(9)
# print(ODD.get(9))
# Output:'nine'

# i)Delete the item from the dictionary, corresponding to the key 9.'ODD'
# del ODD[9]
# print(ODD)
# Output:{1: 'one', 3: 'three', 5: 'five', 7: 'seven'}

