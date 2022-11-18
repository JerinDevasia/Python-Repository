def sumlist(list):
    sum = 0
    for i in list:
        sum = sum + i
    print("Sum of list : ",sum)

i = input("Enter list items : ")
list = i.split(' ')
newlist = [int(x) for x in list]
sumlist(newlist)
