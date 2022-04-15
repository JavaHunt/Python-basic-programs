# Compund Interest 

import math
principal = float(input("Enter principal amount : "))
rate = float(input("Enter rate of interest : "))
time = float(input("Enter time period : "))

# Calculates compound interest
Amount = principal* (pow((1 + rate / 100), time))
CI = Amount - principal
print("Compound interest is", CI)

