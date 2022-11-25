def pattern():
    n = 5
    for i in range(n+1):
        for j in range(i):
            print("*",end=" ")
        print("\n")

    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end=" ")
        print("\n")
        
pattern()
