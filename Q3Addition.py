# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

from random import randint

a= randint(0, 100)
b=randint(1, 100)

for _ in range(10):
    c = int(input(f"Enter your answer for {a} + {b}: "))
    if c == a + b:
        print("Correct!")
        break
else:
    print("Correct Solutions!")
