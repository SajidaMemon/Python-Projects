print("Welcome to my computer course!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's Play")
score = 0

answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


answer = input("What does Ram stands for? ").lower()
if answer == "random acess memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


answer = input("What does PSU stands for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print(f"your got {score} questions correct!")
print(f"your got {((score/4)*100)} %.")


