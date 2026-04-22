import os
os.system("cls")
# I am building a number guessing game as my first project and also first project to upload github 
# NUMBER GUESSING GAME 
import random 
def levels ():
    print("Levels of the Game : \n\n 1.Easy \n 2.Medium \n 3.Hard\n")
    c=(int(input("Which level u wanna begin with (enter 1 , 2 or 3):- ")))
    print("Let's begin ")
    

    match c: # games for different levels
        case 1:
            for i in range (3):
                n=random.randint(1,10)
                num=int(input(('Enter any number from 1 to 10 = ')))
                if num==n: 
                    print("CONGRATULATIONSS !!!! U WON :) ")
                    break
                
            scores(i,c)
            result(n,c)
            
        
        case 2 :
            for i in range (5):
                n=random.randint(1,50)
                num=int(input(('Enter any number from 1 to 50 = ')))
                if num==n: 
                    print("CONGRATULATIONSS !!!! U WON :) ")
                    break
                
            scores(i,c)
            result(n,c)
        case 3 :
            for i in range (7):
                n=random.randint(1,100)
                num=int(input(('Enter any number from 1 to 100 = ')))
                if num==n: 
                    print("CONGRATULATIONSS !!!! U WON :) ")
                    break
               
            scores(i,c)
            result(n,c)
        case _:
            print("Invalid level")
def scores (i,level):
    print("\n","-"*100)
    print("\nLet's evaluate ur performance ")
    if level== 1:
        if i<1:
            print("Guessed too soon ------ Excellent")
        elif i==1  :
            print("Well played $")
        else :
            print("OOPSSSSS WORK HARD ")
    
    if level== 2:
        if i<2:
            print("Guessed too soon ------ Excellent")
        elif i==2  :
            print("Well played $")
        else :
            print("OOPSSSSS WORK HARD ")
    if level== 3:
        if i<3:
            print("Guessed too soon ------ Excellent")
        elif i==3 or i==4 :
            print("Well played $")
        else :
            print("OOPSSSSS WORK HARD ")
def result(n,level):
    print("\n","-"*100,"\n")
    if level ==1 :
        print(f"Let's find the number. And the number was = {n}")
    if level ==2 :
        print(f"Let's find the number. And the number was = {n}")
    if level ==3:
        print(f"Let's find the number. And the number was = {n}")

print("WELCOME TO THE ULTIMATE GUESSING GAME \n  Come and Test your Luck ")
print("="*150)
levels()
while True:
    res=(input("Do u wanna play again (y/n) : \n"))
    if res=="y":
        levels()
    else:
        print("|| Thanks for Playing ||\n\n","*"*100)
        break