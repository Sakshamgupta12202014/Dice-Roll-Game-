#NAME=Saksham Gupta
#REG.NO.=12202014
#Roll. No.=01
#SECTION=K22MR

#diceroll game
import random      #random module is being used.
score=0         #starting value of score 
def rolldice(x):
    global score
    RN=random.randint(1,6)   # RN==random number , it will give a random integer value in range [1,6].
    print("Dice roll : ",RN)
    if int(x)==RN:
        score+=5
        print("__Congrats__You won")
        print("You Got :",score,"points")     #Every time the user wins it gains 5 points 
    else:
        print("__Sorry__You lose")
        print("Total points scored :",score,"points")     #it will display the total points.
    WPA=input("Play one more match enter y for Yes and n for No : ")     #WPA == Waana Play Again   
    if WPA in ['yes','YES','y']: 
        print("Yeah_Sure")
        input_()
    else:
        print("Total points scored :",score)
        print("ByeBye")
def input_():
    global a                   #to use this variable throughout the code,i have made it global 
    a=input("Enter a number between '1-6' : ")
    if '123456'.find(a):            #to check whether the input is between 1 and 6 only
        rolldice(a)
    else:
        print("!!Enter a number between '1-6' only!!")
        input_()
        
input_()  #function calling 


    
    
