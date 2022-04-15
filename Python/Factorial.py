# Factorial of a number

# Method 1 : Recursive

def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1);

# Driver Code
num = int(input("Enter a number : "))
print("Factorial of",num,"is",factorial(num))


# Method 2 : Iterative

def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n
			n -= 1
		return fact

# Driver Code
num = int(input("Enter a number : "))
print("Factorial of",num,"is",factorial(num))


# Method 3 : Built-in Factorial method
import math
n = int(input("Enter a number to find factorial : "))
fact = math.factorial(n)
print("Factorial of ", n, " is ", fact)
