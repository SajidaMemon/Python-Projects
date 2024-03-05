
name = input("Type your name: ")
print(f"Welcome, {name} to this adventure!  ")

answer = input("You are on dirt road, it had come to the end you can go left or right which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to the river you walk around it or swim across? type walk to walk around swim to swim across: ")

    if answer == "swim":
        print("You swam acros and you eaten by alligator!")

    elif answer == "walk":
        print("you walked many miles and you ran out of water and lost the game!")

    else:
        print("Not a valid option")



elif answer == "right":
    answer = input("You come to the bridee it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You can go to the main road. you can decide to to drive to the left !")

    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talked to the stranger they give you the gold and you win!")

        elif answer == "no":
            print("You ingore the stranger and he did not like it you loose!")
        
        else:
            print("Not a valid option you loose! ")


    else:
        print("Not a valid option")

else:
    print("Not a valid option")

print("Thank You for playing the game! ")

