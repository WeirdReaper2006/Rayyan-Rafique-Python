print("Guess the number game")
import random

i = int(input("Enter the largest range."))
a = random.randint(1, i)
user_input = int(input(f"Enter a number between 1 and {i}"))
while a != user_input:
    print("Try Again")
    a = random.randint(1, i)
    user_input = int(input(f"Enter a number between 1 and {i}"))
if a == user_input:
    print("You guessed correctly")
