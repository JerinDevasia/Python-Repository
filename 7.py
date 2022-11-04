x = input("Enter the elements of list 1 : ")
x = x.split(" ")
a = []
for i in x:
    a.append(int(i))
print(a)

y = input("Enter the elements of list 2 : ")
y = y.split(" ")
b = []
for i in y:
    b.append(int(i))
print(b)

if len(a) == len(b):
    print("Same length")
else:
    print("Not same")

if sum(a) == sum(b):
    print("Sum of elements are the same")
else:
    print("Sum values are not the same")

c = []
for i in a:
    if i in b:
        c.append(i)
print("Values both in a and b ", c)
