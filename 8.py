print("List Comprehension : ")
print("*********************")
print("\n")

print("Positive List of integers : ")


a = [1,2,-3,5,6,-3,-9]

b = [x for x in a if x > 0 ]

print(b)  

print("\n")
print("Square of N Numbers : ")

a = [1,2,3,4,5]
b = [x*x for x in a]

print(b)

print("\n")
print("List of vowels : ")

a = "Hello"
str = a.lower()
vowels = ['a','e','i','o','u']
b = [x for x in str if x in vowels]
print(b)

print("\n")
print("Ordinal Value : ")

a = "hello"
b = [x+1 for x in range(len(a))]

for x in range(len(a)):
    print("Ordinal value of ",a[x]," is : ",b[x])
