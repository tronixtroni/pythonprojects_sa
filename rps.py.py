import random
import sys

def play():
    p_choice = input("What do you choose?").capitalize()
    choices = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}
    cpu_choice = choices[random.randint(1,3)]
    if p_choice == cpu_choice:
        return print('Tie!')
    if compare(p_choice,cpu_choice):
        return print('You Win!')
    else:
        return print('You Lose!')

def compare(playerChoice,cpuChoice):
    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False}
    return results[(playerChoice,cpuChoice)]

def game_start():
    begin = input("Would you like to play Rock, Paper, Scissors? ").capitalize()
    while begin != "Yes":
        if begin == "No":
            print("Game Over")
            sys.exit()
        else:
            print("Please try again")
            begin = input("Would you like to play Rock, Paper, Scissors? ").capitalize()
    play()
    while True:
        begin = input('Play again?').capitalize()
        while begin != "Yes":
            if begin == "No":
                print("Game Over")
                sys.exit()
            else:
                print("Please try again")
                begin = input("Play again? ").capitalize()
        play()

game_start()  
