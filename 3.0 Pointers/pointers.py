num1 = 11
num2 = num1

print(num1)
print(num2)

print(id(num1))
print(id(num2)) #pointer referencing to the same mem location of num1 

num2 = 22

print(num1)
print(num2)

print(id(num1))
print(id(num2)) #pointer now referencing to a new location


#dictionary
dict1 = {
    'val': 33
}

dict2 = dict1
print("DICT1",dict1)
print("DICT2",dict2)

print(id(dict1))
print(id(dict2)) #pointer referencing to the same mem location of num1 

dict2['val'] = 44

print("DICT1",dict1)
print("DICT2",dict2)

print(id(dict1))
print(id(dict2)) #pointer referencing to the same mem location of num1 

