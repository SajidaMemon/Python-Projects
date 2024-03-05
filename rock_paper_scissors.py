import random
# we import random 

# create 2 variable so we can compare the who wins
user_wins = 0
computer_wins = 0

# create the variable option and create a list and three values in it instead
# create "rock" , "paper", "scissors in three varible so created the list 
option = ["rock" , "paper", "scissors"]
  
#  we use while loop and take user input and make that input to lower 
# if user input equal to q then program will break and stop 
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    # if user did not pick any value from option variable or valid values
    #  program will continuous ans start the loop again to ask again
    if user_input not in option:
        continue
    
    # if user type valid value from option variable then generate the random number 
    # when random method pick any number random_number goes to option list and matches that and saves in computer_pick  whatever the index in the random number 
    random_number = random.randint(0,2)
    computer_pick = option[random_number]
    print(f"Computer picked {computer_pick}.")


    # now we compare user pick and computer pick
    # and add the wining values to varable 
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        
    
    else:
        print("You Lost!")
        computer_wins += 1

print(f"You won {user_wins} times")
print(f"Computer wins {computer_wins} times")
print("Goodbye!")
