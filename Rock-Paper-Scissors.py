#import library
import random
#array
com = ["Rock", "Paper", "Scissors"]

#algorithm for playing
def battle(player1,player2): 
    if player1.lower() == player2.lower(): #.lower to read into lower case
        print ("Computer: "+ player2) #to show what computer get from random choice
        print ("Draw!")
    elif player1.lower() == "Rock".lower() and player2 == "Paper":
        print ("Computer: "+ player2)
        print ("You Lose!")
    elif player1.lower() == "Rock".lower() and player2 == "Scissors":
        print ("Computer: "+ player2)
        print ("You Win!")
    elif player1.lower() == "Paper".lower() and player2 == "Rock":
        print ("Computer: "+ player2)
        print ("You Win!")
    elif player1.lower() == "Paper".lower() and player2 == "Scissors":
        print ("Computer: "+ player2)
        print ("You Lose!")
    elif player1.lower() == "Scissors".lower() and player2== "Rock":
        print ("Computer: "+ player2)
        print ("You Lose!")
    elif player1.lower() == "Scissors".lower() and player2== "Paper":
        print ("Computer: "+ player2)
        print ("You Win!")
    else:
        print ("===TYPO===") #to show when you typo
#run it
run = True
while run:
    player1 = input("Input Your Choice\nYou: ") #to input your choice
    player2 = random.choice(com) #random choice
    battle(player1,player2) #show the function