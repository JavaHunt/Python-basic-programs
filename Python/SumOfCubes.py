# Simple Python program to find sum of series
# with cubes of first n natural numbers

# Method 1
# Returns the sum of series
def sumOfSeries(n):
	sum = 0
	for i in range(1, n+1):
		sum +=i*i*i
		
	return sum


# Driver Function
n = int(input("Enter a number : "))
print(sumOfSeries(n))


# Method 2
# Efficient Python program to find sum of cubes
# of first n natural numbers that avoids
# overflow if result is going to be withing limits.

# Returns the sum of series
def sumOfSeries(n):
	x = 0
	if n % 2 == 0 :
		x = (n/2) * (n+1)
	else:
		x = ((n + 1) / 2) * n
		
	return (int)(x * x)


# Driver Function
n = int(input("Enter a number : "))
print(sumOfSeries(n))

# Proof
"""

An efficient solution is to use direct mathematical formula which is (n ( n + 1 ) / 2) ^ 2
Let the formula be true for n = k-1.
Sum of first (k-1) natural numbers = 
            [((k - 1) * k)/2]^2

Sum of first k natural numbers = 
          = Sum of (k-1) numbers + k^3
          = [((k - 1) * k)/2]^2 + k^3
          = [k^2(k^2 - 2k + 1) + 4k^3]/4
          = [k^4 + 2k^3 + k^2]/4
          = k^2(k^2 + 2k + 1)/4
          = [k*(k+1)/2]^2

"""