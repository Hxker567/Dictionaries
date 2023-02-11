# What is Dictionaries 
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# myDict1 = {'Mohan':80,'Ram':90,'Shyam':100} 
# print(myDict1)
# Output:{'Mohan': 80, 'Ram': 90, 'Shyam': 100}

# myDict2 = {'Mohan':80,'Ram':90,'Shyam':100,'Jatin':90,'Srijan':95}
# print(myDict2['Jatin'])
# Output:90    #Here we know jatin percentage in the output by print his name.
# print(myDict2['Mohan'])
# Output:80      #Here we know Mohan percentage in the output by print his name.


#Membership operation
# 'in'
# 'in' operator checks if the key is present in the dictionary it returns true, else it returns false.

# 'not in'
# 'not in' operator checks if the key is not present in the dictionary it returns false, else it returns true.

# For ex
# myDict2 = {'Mohan':80,'Ram':90,'Shyam':100,'Jatin':90,'Srijan':95}
# print('Suhel' in myDict2)
# Output:False    #Suhel is not in the dictionary so it will print false this is 'in' operator.

# myDict2 = {'Mohan':80,'Ram':90,'Shyam':100,'Jatin':90,'Srijan':95,'Suhel':66}       
# print('Suhel' not in myDict2)
# Output:False    #Suhel is present in the dictionary so it will print false because this is not in operator.


#Dictionaries are mutable
# Dictionaries are mutable we can change it after it has been created.


#Adding a new item
# myDict3 = {
#    'Mohan': 95,
#    'Ram': 89,
#    'Suhel': 92,
#    'Sangeeta': 85
# }
# {'Mohan': 95, 'Ram': 89, 'Suhel': 92, 'Sangeeta': 85}
# myDict3['Meena'] = 78
# print(myDict3['Meena'])
# myDict3
# print(myDict3)
# Output:{'Mohan': 95, 'Ram': 89, 'Suhel': 92, 'Sangeeta': 85, 'Meena': 78}


#Modifying an existing item
# myDict4 = { 
#    'Mohan': 95,
#    'Ram': 89,
#    'Suhel': 92,
#    'Sangeeta': 85
# }
# myDict4 = ['Suhel'] = 93.5
# print(myDict4['Suhel'])
# output:myDict4 = ['Suhel'] = [93.5]


#Traversing a dictionary
# We can access each item of the dictionary or traverse a dictionary using for loop.

# Method1
# For ex:
# myDict5 = {'Jxtin':90,'Sj':96,'Maithily':87,'Ada':85}
# for key in myDict5:
#    print(key,':',myDict5[key])
# Output:
# Jxtin : 90
# Sj : 96
# Maithily : 87
# Ada : 85

# Method2
# for key,value in myDict5.items():
#    print(key,':',value)
# Output:
# Jxtin : 90
# Sj : 96
# Maithily : 87
# Ada : 85













