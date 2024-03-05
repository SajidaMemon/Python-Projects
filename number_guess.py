#  first we import module random these module is builtin we just
#  import and use them

import random 

#  it will give you randrange of -1 to 10 not genrate 11
# we can give randrange (11) means it will start with 0 up to 10
# if we do randint in will genrete 11 

'''if user type a number and isdigit() method will check
the if this is the digit then it will go in the variable 
and convert in integer bcoz if user type it is in string like "25 "'''


top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger then 0 next time")
        quit()
        
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,11)  

''' if we do while True it will gives you non stop loop utill we use breake statment
we ask the user make a guess if user guess is in digit then it will convert in int and continue statment keep asking till guess will correct. '''


guesses = 0 

while True:
    ''' create the variable guessess and intilize with 0 and then every time user 
    guess it will increse by 1 like score variable'''
    guesses += 1 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else: 
        print("Plese type a number next time.")
        continue
        

        ''' if user guess the random number then it will print the messege and statment will be break means it will be out of loop'''
    if user_guess == random_number:
        print("You got it")
        break

        ''' we put the elif condtion to check if the first condtion not true go to
         next condition. '''
    elif user_guess >random_number:
        print("You are above the number.")
    else:
        print("You are below the number.")
        
    
    
    



print(f"you got it {guesses} guesses")