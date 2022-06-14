choice = int(input("Do you want to do calculation? Press 1 for Yes and 2 for No."))
while choice == 1:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    type = int(input(
        "Which type of calculation do you want to do. Enter 1 for Addition, 2 for Subtraction, 3 for Multiplacation, or 4 for Division"))
    if type == 1:
        result = num1 + num2
        print("The addition of", num1, "and", num2, "is", result)
    elif type == 2:
        result = num1 - num2
        print("The subtraction of", num2, "from", num1, "is", result)
    elif type == 3:
        result = num1 * num2
        print("The multiplacation of", num1, "and", num2, "is", result)
    elif type == 4:
        result = num1 / num2
        print("The division of", num1, "and", num2, "is", result)
    choice = int(input("Do you want to do more calculation? Press 1 for Yes and 2 for No."))
