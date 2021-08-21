import os
#Creating a list, and creating input request for specific values
def main():

    chicken=['Fried Chicken Tenders and fries','Grilled Chicken Alfredo','Chicken Tacos']
    beef=['Beef Spaghetti', 'Swedish Meatballs and Egg Noodles', 'Roast, potatoes, and rice']
    fish=['Fire Cracker Salmon and rice', 'Fried Tilapia and fries', 'Fried Catfish and greenbeans']
    chickenrec=[open('chicken.txt', 'r')]

    lists = chicken, beef, fish


#interactive prompts for meal sections
    def library():
        while True:
            print("         Welcome to the Meal Display System          ")
            print("_____________________________________________________")
            print("_________What would you like to eat today?___________")
            print("          Enter '1' to display chicken meals")
            print("          Enter '2' to display beef meals")
            print("          Enter '3' to display fish meals")
            print("          Enter '4' to display all meals")
            try:
                c = int(input("Select an option from 1-4: "))
                print()
                if(c==1):
                    for item in chicken:
                        print(item)
                    os.system('pause')
                    a = (input("Do you wanna view the recipes? 'y' or 'n'"))
                    print()
                    if(a=='y'):
                        with open("chicken.txt","r") as f:
                            lines=f.read()
                            print(lines)
                            print()
                            f.close()

                    os.system('pause')
                    os.system('cls')

                elif(c==2):
                    for item in beef:
                        print(item)
                    os.system('pause')
                    a = (input("Do you wanna view the recipes? 'y' or 'n'"))
                    print()
                    if(a=='y'):
                        with open("beef.txt","r") as f:
                            lines=f.read()
                            print(lines)
                            print()
                            f.close()
                    os.system('pause')        
                    os.system('cls')

                elif(c==3):
                    for item in fish:
                        print(item)
                    os.system('pause')
                    os.system('cls')

                elif(c==4):
                    for item in lists:
                        print(item)
                    os.system('pause')
                    os.system('cls')

            except ValueError:
                print("that dont work")

            restart=input("Would you like to view more meals? Type 'yes' or 'no'\n")
            if restart == "yes":
                main()
            if restart == "no":
                print("See you next time!")
                exit()
    library()
main()
