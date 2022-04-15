# Function for nth Fibonacci number

# Method 1 : Recursion
def Fibonacci(n):
	if n<= 0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n == 1:
		return 0
	# Second Fibonacci number is 1
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program
n = int(input("Enter a number : "))
print(Fibonacci(n))

# Method 2 : Dynamic Programming

FibArray = [0, 1]

def fibonacci(n):
	if n<0:
		print("Incorrect input")
	elif n<= len(FibArray):
		return FibArray[n-1]
	else:
		temp_fib = fibonacci(n-1)+fibonacci(n-2)
		FibArray.append(temp_fib)
		return temp_fib

# Driver Program
n = int(input("Enter a number : "))
print(fibonacci(n))

# Method 3 : # Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program
n = int(input("Enter a number : "))
print(fibonacci(n))


# Method 4 : Using arrays

def fibonacci (n):
if n<= 0:
	return "Incorrect Output"
data = [0, 1]
if n > 2:
		for i in range (2, n):
			data.append(data[i-1] + data[i-2])
	return data[n-1]

# Driver Program
n = int(input("Enter a number : "))
print(fibonacci(n))

# Method 5 : Using Direct formula

# To find the n-th Fibonacci Number using formula

from math import sqrt
def nthFib(n):
	res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
	# compute the n-th fibonacci number
	print(int(res),'is',str(n)+'th fibonacci number')
	# format and print the number
	
# driver code
n = int(input("Enter a number : "))
nthFib(n)

