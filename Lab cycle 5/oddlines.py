file = open("sample.txt","r")
fle = open("sample1.txt","w")
rfle = open("sample1.txt","r")

lst = []

for i in file:
    lst.append(i)

file.close()
print(lst)

for i in range(0,len(lst)):
    if i % 2 == 0:
        print(lst[i])
        fle.write(lst[i])
fle.close()

for i in rfle:
    print(i)

