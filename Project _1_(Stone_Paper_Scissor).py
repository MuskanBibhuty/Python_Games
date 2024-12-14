'''
1 for stone
2 for paper
3 for scissor
'''

import random

def game(n = random.randint(1,3)):

    if(n>3):
        print("Something went wrong!")
        exit()
    
    else:
        computer = n
        user = input("Enter your choice: ")
        youstr = user.lower()
        youdict = {"stone":1, "paper":2, "scissor":3}
        you = youdict[youstr]
        
        reversedict = {1:"stone", 2:"paper", 3:"scissor"}
        print("Computer choose", reversedict[computer])
        print("You choose", reversedict[you])

        if(computer==you):
            print("It's a draw!")
        
        else:
            if(computer==1 and you==2):
                print("Congratulations! You Won.")
            elif(computer==1 and you==3):
                print("Alas! You Lost.")
            elif(computer==2 and you==1):
                print("Alas! You Lost.")
            elif(computer==2 and you==3):
                print("Congratulations! You Won.")
            elif(computer==3 and you==1):
                print("Congratulations! You Won.")
            elif(computer==3 and you==2):
                print("Alas! You Lost.")
            else:
                print("Something went wrong!")

game()
