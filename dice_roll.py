import random
import os
#dice roll randomizer

player_name=input("Enter your name:\n")

def Main():

    dice_roll=input(player_name + ", are you ready to roll?(y/n)\n")
    cpu_roll = random.randint(1,12)
    if dice_roll == "y":
        if cpu_roll == 1:
            print(player_name + ", You have rolled a 1")
        elif cpu_roll == 2:
            print(player_name + ", You have rolled a 2")
        elif cpu_roll == 3:
            print(player_name + ", You have rolled a 3")
        elif cpu_roll == 4:
            print(player_name + ", You have rolled a 4")
        elif cpu_roll == 5:
            print(player_name + ", You have rolled a 5")
        elif cpu_roll == 6:
            print(player_name + ", You have rolled a 6")
        elif cpu_roll == 7:
            print(player_name + ", You have rolled a 7")
        elif cpu_roll == 8:
            print(player_name + ", You have rolled a 8")
        elif cpu_roll == 9:
            print(player_name + ", You have rolled a 9")
        elif cpu_roll == 10:
            print(player_name + ", You have rolled a 10")
        elif cpu_roll == 11:
            print(player_name + ", You have rolled a 11")
        elif cpu_roll == 12:
            print(player_name + ", You have rolled a 12")


    restart=input("Wanna roll again?(y/n)\n")
    if restart in ["y","Y"]:
        os.system('cls')
        Main()

    elif restart in ["n","N"]:
        print("thanks for playing, see ya")
        exit()

    elif dice_roll == "n":
        print("Thanks for playing, goodbye")
        exit()
Main()
