#Play rock, paper, scissors vs the computer
import random
import os

player_name=input("Enter your name\n")
cpu_wins = 0
player_wins = 0
#player input
def Choose_RPS():
    player_choice=input("Choose: Rock, Paper, or Scissors\n")
    if player_choice in ["rock", "Rock"]:
        player_choice = "rock"
    elif player_choice in ["Paper","paper"]:
        player_choice = "paper"
    elif player_choice in ["Scissors", "scissors"]:
        player_choice = "scissors"

    else:
        print(player_name + ", that is not a rock, a paper, or a scissors, try again.")
        Choose_RPS()
    return player_choice
#cpu input
def Computer_Choice():
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        cpu_choice = "rock"
    elif cpu_choice == 2:
        cpu_choice = "paper"
    else:
        cpu_choice = "scissors"
    return cpu_choice


#while true conditions to determine winner and loser, or a tie
while True:
    print("")
    player_choice = Choose_RPS()
    cpu_choice = Computer_Choice()
    print("")
#conditions of rock/paper/scissors vs rock,paper,scissors
#add 1 to the score based on the winner
    if player_choice == "rock":
        if cpu_choice == "rock":
            print("You chose rock and the cpu chose rock, it's a tie!")

        elif cpu_choice == "paper":
            print("You chose rock and the cpu chose paper, you have lost miserably")
            cpu_wins += 1

        elif cpu_choice == "scissors":
            print("You chose rock and the cpu chose scissors, you have destroyed them beyond repair")
            player_wins += 1

    elif player_choice == "paper":
        if cpu_choice == "paper":
            print("You chose paper and the cpu chose paper, it's a tie!")

        elif cpu_choice == "rock":
            print("You chose paper and the cpu chose rock, you have absolutely demolished them!")
            player_wins +=1

        elif cpu_choice == "scissors":
            print("You chose paper and the cpu chose scissors, sorry buddy but you're dead")
            cpu_wins +=1

    elif player_choice == "scissors":
        if cpu_choice == "scissors":
            print("You chose scissors and the cpu chose scissors, it's a tie!")

        elif cpu_choice == "paper":
            print("You chose scissors and the cpu chose paper, you have absolutely demolished them!")
            player_wins +=1

        elif cpu_choice == "rock":
            print("You chose scissors and the cpu chose rock, sorry buddy but you just got bonked")
            cpu_wins +=1
#final score output
    print("")
    print(player_name + " wins:" + str(player_wins))
    print("Computer wins:" + str(cpu_wins))
    print("")
#Prompt player for final input to play again
    user_choice = input("Do you want to play rock, paper, scissors again?(y/n)\n")
    if user_choice in ["y","Y","yes","Yes"]:
        os.system('pause')
        os.system('cls')
        pass
    elif user_choice in ["n","N","No","no"]:
        print("Thanks for playing!")
        exit()
