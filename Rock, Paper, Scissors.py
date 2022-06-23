import random

choice = int(input("Do you want to play Rock, Paper, Scissors? Press 1 for Yes and 2 for No"))
while choice == 1:
    i = int(input("Enter 1 for Rock. Enter 2 for Paper. Enter 3 for Scissors"))
    computer_input = random.randint(1, 3)
    if (computer_input == 1 and i == 1) or (computer_input == 2 and i == 2) or (computer_input == 3 and i == 3):
        print("It is a Draw")
    elif (computer_input == 1 and i == 2) or (computer_input == 2 and i == 3) or (computer_input == 3 and i == 1):
        print("You Win")
    elif (computer_input == 1 and i == 3) or (computer_input == 2 and i == 1) or (computer_input == 3 and i == 2):
        print("You Lose")
    choice = int(input("Do you want to play Rock, Paper, Scissors? Press 1 for Yes and 2 for No"))
