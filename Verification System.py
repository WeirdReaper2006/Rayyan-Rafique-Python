pin = [1234] # make sure to add a comma if you plan to add more than one element in the future
account_num = int(input("Enter your account number (range is 0 to 9): "))
while account_num > 9:
    account_num = int(input("Enter your account number (range is 0 to 9): "))
instring = int(input("Enter a 4 digit pin to check validity: "))
while instring < 1000 or instring > 9999:
    instring = int(input("Enter a 4 digit pin to check validity: "))
if instring == pin[account_num]:
    print("Correct")
else:
    print("Wrong")