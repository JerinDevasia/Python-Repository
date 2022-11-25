def factorial(num):
    if num < 0:
        print("Factorial doesn't exist")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            fact = fact * i
                
