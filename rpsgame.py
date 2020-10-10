import random

options = ['rock', 'paper', 'scissors']

while True:
    
    comp = random.choice( options )
    player = input("Enter your choice[rock, paper, scissors or stop]: ")
    
    if player == "stop":
        break
    
    if player == comp:
        print("It is a draw")
    else:
        if player == 'rock':
            if comp == 'paper':
                print("Computer won, because it chose Paper")
            else:
                print("Player won because Computer chose", comp)
    
        elif player == 'paper':
            if comp == 'rock':
                print("Player won because Computer chose Rock")
            else:
                print("Computer won, it chose", comp)
    
        elif player == 'scissors':
            if comp == 'rock':
                print("Computer won, it chose Rock")
            else:
                print("Player won because Computer chose", comp)

