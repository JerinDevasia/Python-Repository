def fibonacci(n):
	first = 0
	second = 1
	if n == 0:
		print(first)
	else:
		for i in range(0,n):
			num = first
			print(num)		
			first = second
			second = num + second
x = int(input("Enter number of terms in a fibonacci series : "))
fibonacci(x)
