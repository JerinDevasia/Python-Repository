file = open("sample.txt","r")

lst = []
for i in file:
    lst.append(i)

print(lst)