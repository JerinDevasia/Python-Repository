a = int(input('Enter a number: '))
factorial = 1
if a < 0:
    print("Factorial does not exist")
elif a==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial = factorial*i;
    print("The factorial of ",a," is ",factorial)
