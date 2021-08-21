#This program demonstrates taking string inputs, number inputs, running a calculator, error handling, and loops
#This program calculates the revenue earned from various amounts of subscribers on twitch.tv
#define the program as main in order to be able to run it again in a loop towards the end
def main():

    import os
#while true/except/else used for error handling from invalid entries when prompted for numbers
    while True:
        try:
            st1 = int(input("Enter amount of tier 1 subs: "))
            st2 = int(input("Enter amount of tier 2 subs: "))
            st3 = int(input("Enter amount of tier 3 subs: "))
        except ValueError:
            print("Sorry I only understand digits, try again.")
            os.system('pause')
            os.system('cls')
            continue
        else: break

    tier1 = 4.99
    tier2 = 9.99
    tier3 = 24.99
    sr1 = tier1 * float(st1)
    sr2 = tier2 * float(st2)
    sr3 = tier3 * float(st3)
    total = sr1 + sr2 + sr3
    payout = total / 2.0
    print("Total Earnings from subscriptions: $", '{:.2f}'.format(payout))
    os.system('pause') #Pause app to give time to save information
    os.system('cls') #Clear screen

    #Calculate payout if it is reoccurring over a number of months
    reoccurring=input("Are these subscriptions reoccurring? Type 'yes' or 'no'\n")
    if reoccurring == "yes":
        while True:
            try:
                months = int(input("Enter the number of months to multiply earnings\n"))
            except ValueError:
                print("Sorry I only understand digits, try again.")
                os.system('pause')
                os.system('cls')
                continue
            else: break

        months = int(months)
        final = months*payout
        print("Earnings over the amount of months is: \n$", '{:.2f}'.format(final))
    else:
        os.system('cls')
        os.system('pause')

    #Prompt user to enter a response if they want the code to run again or close
    restart=input("Would you like to run the calculator again? Type 'yes' or 'no'\n")
    if restart == "yes":
        main()
    if restart == "no":
        exit()
main()
