# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random 

a = float(input("Enter a: "))
b = float(input("Enter b: "))

random_number = random.uniform(a, b)
print("Random number between", a, "and", b, "is:", random_number)


