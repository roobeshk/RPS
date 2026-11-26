import random

print("To Play Game :)")

computer_score = 0
player_score = 0
player = True

while player:
    choices = ["rock","paper","scissor"]
    computer = random.choice(choices)
    print("\nYou want exit! yes to exit")
    player = input("Rock,Paper,scissor?").lower()
    if player == "yes":
        player = False
    elif player == "":
        player = True    
    if computer == player:
        print("player   :  "+player)
        print("computer :  "+computer)
        print("Its tie\n")
        print("player score :",player_score)
        print("computer score :",computer_score)
        
    elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissor") or (player == "scissor" and computer == "rock"):  
        print("player   :  "+player)
        print("computer :  "+computer)
        print("you lose!\n")
        computer_score += 1
        print("player score :",player_score)
        print("computer score :",computer_score)
        
    elif (player == "paper" and computer == "rock") or (player == "scissor" and computer == "paper") or (player == "rock" and computer == "scissor"):
        print("player   :  "+player)
        print("computer :  "+computer)
        print("you win!\n")
        player_score += 1
        print("player score :",player_score)
        print("computer score :",computer_score)