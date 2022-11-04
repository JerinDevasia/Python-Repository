list = input("Enter the elements : ")

list1 = list.split()
list2 = []

for x in list1:
    list2.append(int(x))

list3 = []
for x in list2:
    if(x > 100):
        list3.append("Over")
    else:
        list3.append(x)

print(list3)


        
