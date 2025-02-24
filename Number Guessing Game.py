import random

def game():
    print("The game is on...")
    score= random.randint(1,50)

    with open("hiscore.txt") as f:
        h= f.read()

        if(h!= ""):
            h= int(h)
        else:
            h=0

    print("Your score is:", score)

    if(score>h):
        f= open("hiscore.txt", "w")
        f.write(str(score))
    
    return score

game()