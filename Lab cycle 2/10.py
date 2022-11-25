def factors(num):
    print("Factors of ",num," are : ",end=" ")
    for i in range(1,num):
        if num % i == 0:
            print(i,end=" ")

num = int(input("Enter a number : "))
factors(num)
