#rock paper scissors
#make it the computer keeps to track which the computer wins or the user wins

import random #for random number generation 
#we need to import random so we can use it to generate a random choice for the computer

#step 2 2 variant for user score and computer score
user_score = 0
computer_score=0
options= ['rock','paper','scissors'] #list of options for the game

while True:#ask the user to input rock paper or scissors
    user_input = input("type rock/paper/scissors or q to quit: ").lower() #convert input to lowercase and user input is stored in user_input variable refers to the player
    if user_input == 'q': #if user inputs q, break the loop
        break
    if user_input not in options : #if user input is not valid, ask again 
        #nd must end with colon because it is a conditional statement so basically if user input is not rock paper or scissors
        print("Invalid input. Please try again.")
        continue
    random_number = random.randint(0,2) #generate a random number between 0 and 2 for the players to choose rock paper or scissors by numbers
     #rock : 0, paper : 1, scissors : 2
    computer_pick = options[random_number]# computer's choice based on the random number generated
    print("computer picked",computer_pick +".")# display computer's choice #"." is for  formatting basically to make it look better
     
    if user_input == "rock" and computer_pick == "scissors":  # if user input is rock and computer pick is scissors, user wins
     print("You win!")
    user_score += 1  # increment user score by 1

if user_input == "rock" and computer_pick == "scissors":  # if user input is rock and computer pick is scissors, user wins
    print("You win!")
    user_score += 1  # increment user score by 1

elif user_input == "paper" and computer_pick == "rock":  # if user input is paper and computer pick is rock, user wins
    print("You win!")
    user_score += 1

elif user_input == "scissors" and computer_pick == "paper":
    print("You win!")
    user_score += 1

else:  # if none of the above conditions are met, computer wins
    print("You lose!")
    computer_score += 1  # increment computer score by 1

print("you won", user_score, "times")  # display user score
print("computer won", computer_score, "times")  # display computer score
print("Thanks for playing!")  # thank the user for playing
print("goodbye")



