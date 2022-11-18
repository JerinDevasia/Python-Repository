def pyramid(n):
    x = 0
    for i in range(1,n+1):
        x = i
        for y in range(1,i+1):
            print(y * x,end=" ")
        print("\n")
n = int(input("Enter number of steps : "))
pyramid(n)
