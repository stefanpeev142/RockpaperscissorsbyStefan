import random
choices = ['rock', 'paper', 'scissors']

user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

if user_choice not in choices:
    print("Fire beats everything, you lose. Please enter 'rock', 'paper', or 'scissors'.")
    exit() 
    
score_user=0
score_computer=0

while True:
 computer_choice = random.choice(choices)
 if user_choice == computer_choice:
    print(f"Computer chooses:{computer_choice}")
    print(f"It's a tie!\nYou:{score_user}|Computer:{score_computer}")
 elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
    score_user+=1
    print(f"Computer chooses:{computer_choice}")
    print(f"You win!\nYou:{score_user}|Computer:{score_computer}")
 else:
    score_computer+=1
    print(f"Computer chooses:{computer_choice}")
    print(f"You lose :(.\nYou:{score_user}|Computer:{score_computer}")
 if (score_user==3) or (score_computer==3):
    break
 user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
 if user_choice not in choices:
    print("Fire beats everything, you lose. Please enter 'rock', 'paper', or 'scissors'.")
    exit() 
if score_user==3:
    print("Congratulations! You win this set.")
if score_computer==3:
    print("Game Over! You lost this set.")
