dict1 = {}

n = int(input('Enter no of items for the dict : '))

for i in range(n):

    key = input("Enter Key : ")
    value = input("Enter Value : ")

    dict1[key] = value

print("Dictionary 1 : ", dict1)

dict2 = {}

n = int(input('Enter no of items for the dict : '))

for i in range(n):

    key = input("Enter Key : ")
    value = input("Enter Value : ")

    dict2[key] = value

print("Dictionary 2 : ", dict2)

dict3 = {**dict1,**dict2}

for k,v in dict3.items():
    if k in dict1 and k in dict2:
        dict3[k] = [dict1[k], v]

print("Updated Dictionary 1 : " ,dict3)