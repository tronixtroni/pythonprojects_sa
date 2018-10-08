import random
import time
time.sleep(.2)
name=input("Enter your name: ")
time.sleep(.4)
print("Hello", name, "welcome to the game DICE")
input("Press any key to start game")
print(" loading...\n")
time.sleep(5)
l=[]
attempt=4
flag=1
l=random.randint(1,6)
m=random.randint(1,6)
game=l+m

while(attempt!=0):
    num=int(input("Guess and enter the sum of two numbers in between of 2 to 12 : "))
    time.sleep(2)
    while(num>12 or num<2):
        if (num>12 or num<2):
            print("Enter the numbers between 2 and 12")
            num=int(input("Guess and enter the sum of two numbers: "))
    if(game==num):
        flag=0
        print("CONGRATULATIONS !!! You win!!!\nThe numbers are: ",l,"and",m,"\n""And the sum is : ",game)
        break
    else:
        print(" number was guessed is wrong!!! You lost a chance!\nGuess a new number, better luck next time!")
        print()
        attempt-=1

if flag==1:
    print("You lose, the number was: ",game)
