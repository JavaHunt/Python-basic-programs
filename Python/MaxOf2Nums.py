# Maximum of 2 numbers

# Method 1 : if else

def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
# Driver code
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
print(maximum(a, b))

# method 2 : using max function

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
maximum = max(num1, num2)
print("Maximum of {} and {} is {}".format(num1, num2, maximum))

# Method 3 : Using Ternary 
# Driver code
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

# Use of ternary operator
print(a if a >= b else b)

