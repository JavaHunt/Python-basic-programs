# ASCII value of a character
c = input("Enter a character : ")
if(len(c) == 1):
    print("The ASCII value of " + c + " is", ord(c))
else:
    print("Invalid Character")
