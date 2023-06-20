note_list=[]
choice=str(input("Do you want to enter item to the list: "))
while choice=="True" or choice=="true" or choice=="yes":
    item=str(input("What item do you want to add to the list: "))
    note_list.append(item)
    choice=str(input("Do you want to enter more items to the list: "))
print (note_list)