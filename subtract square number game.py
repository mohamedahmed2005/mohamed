# Purpose: user will input number, he/she will play with his/her friend who they will enter square number and subtracting this number from the first number they input and the first indvidual will reach 0 he/she wins.
import math
import random
print("""--------------Welcome to Subtract a square number game--------------
--------------Please enter number which is integer--------------

menu2
choice1:random
choice2:enter number""")
choice = input("Enter your choice between 1&2: ")
while (choice!="1" and choice!="2"):
            print("please enter integer between 1&2")
            choice = input("Enter choice: ")
choice = int(choice)
if(choice==1):
    num = random.randint(10, 1000)
    x = math.sqrt(num)
    while(x.is_integer() == True):
        num = random.randint(10, 1000)
elif(choice==2):
    num = input("Enter number: ")
    while not (num.isdigit()):
        print("it's not an integer,please enter integer")
        num = input("Enter new number: ")
    num = int(num)
else:
    while (choice != 1 or choice != 2):
        choice = input(f"{choice}isn't an integer between 1&2: ")
        while (choice != "1" and choice != "2"):
            print("please enter integer between 1&2")
            choice = input("Enter a choice between 1&2: ")
        choice = int(choice)
        if (choice == 1 or choice == 2):
            if(choice==1):
                num = random.randint(10, 1000)
                x = math.sqrt(num)
                while (x.is_integer() == True): # iterate when random number is square
                    num = random.randint(10, 1000)
                    if(x.is_integer() == False): #check if random number is square or not
                        break

            elif(choice==2):
                break
print("number of coins are ",num)
player_1 = input("player1:Enter your name? ")
player_2 = input("player2:Enter your name? ")
while num > 0: #iterate when variable"num" is greater than 0
        num_1 = input(f"{player_1}: Enter a number: ")
        while not (num_1.isdigit()):
            num_1 = input(f"{player_1}: Enter a number: ")
        num_1 = int(num_1)

        while num_1 <= 0: #iterate when variable"num_1" is smaller than 0
                num_1 = input(f"{player_1}:Enter a positive number which is smaller than or equal to {num}: ")
                while not (num_1.isdigit()):
                    num_1 = input(f"{player_1}:Enter a number: ")
                num_1 = int(num_1)
        while (num_1 > num or num_1==0):#iterate when variable"num_1" is greater than value of variable"num"
                num_1 = (input(f"{player_1}:Enter a valid number which is smaller than or equal to {num}:"))
                while not (num_1.isdigit()):
                    num_1 = (input(f"{player_1}:Enter a valid number as an integer: "))
                num_1 = int(num_1)
        x = math.sqrt(num_1)
        while x > num or x==0: #iterate when value of variable"x" is bigger than value of variable"num"
                num_1 = (input(f"{player_1}:Enter a valid number which is smaller than or equal{num}: "))
                while not (num_1.isdigit()):
                    num_1 = (input(f"{player_1}:Enter a valid number as an integer: "))
                num_1 = int(num_1)
                x = math.sqrt(num_1)

        if x.is_integer(): #check if valie of variable "x" is square number or not
                num -= num_1
                if (num <= 0): #check if valie of variable "num" is smaller than or equal 0
                        print(f"{player_1} wins")
                        print("congratulations!")
                        break
                print("Remaining number:", num)
        while not (x.is_integer()): #iterate when value of variable "x" isn't square number
                num_1=(input(f"{player_1}:enter a squared number: "))
                while not (num_1.isdigit()):
                    num_1 = input(f"{player_1}: Enter valid squared number: ")
                num_1 = int(num_1)
                while (num_1 <= 0): # iterate when value of variable "num1" is smaller than 0
                        num_1 = (input(f"{player_1}:Enter a positive number: "))
                        while not (num_1.isdigit()):
                            num_1 = input(f"{player_1}: Enter a number: ")
                        num_1 = int(num_1)
                while (num_1 > num or num_1==0): # iterate when the value of variable"num_1"is greater than value of variable"num"
                        num_1 = input(f"{player_1}:Enter a valid number which is smaller than {num}:")
                        while not (num_1.isdigit()):
                            num_1 = input(f"{player_1}: Enter a number: ")
                        num_1 = int(num_1)
                x = math.sqrt(num_1)
                if(x.is_integer()): #check if value of variable"x" is square number or not
                        num -= num_1
                        if (num <= 0): #check if value of variable"num" is smaller than or equal 0
                                print(f"{player_1} wins")
                                print("congratulations!")
                                break
                        print("Remaining number:", num)
                        continue
        if (num <= 0):#check if value of variable"num" is smaller than or equal 0
                print(f"{player_1}wins")
                print("congratulations!")
                break
        num_1 = input(f"{player_2}: Enter a number: ")
        while not(num_1.isdigit()):
            num_1 = input(f"{player_2}: Enter a number: ")
        num_1 = int(num_1)
        while num_1 <= 0: # iterate when value of variable "num1" is smaller than 0
            num_1 = (input(f"{player_2}Enter a positive number which is smaller than or equal to {num}: "))
            while not (num_1.isdigit()):
                num_1 = num_1 = input(f"{player_2}:Enter a number: ")
                num_1 = int(num_1)
        while (num_1 > num or num_1 == 0):  # iterate when variable"num_1" is greater than value of variable"num"
            num_1 = (input(f"{player_2}:Enter a valid number which is smaller than or equal to {num}:"))
            while not (num_1.isdigit()):
                num_1 = (input(f"{player_2}:Enter a number: "))
            num_1 = int(num_1)
        x = math.sqrt(num_1)
        while x > num or x == 0:  # iterate when value of variable"x" is bigger than value of variable"num"
            num_1 = (input(f"{player_2}:Enter a valid number which is smaller than or equal{num}: "))
            while not (num_1.isdigit()):
                num_1 = (input(f"{player_2}:Enter a number: "))
            num_1 = int(num_1)
            x = math.sqrt(num_1)
        if x.is_integer(): #check if the value of variable"x" is square number
            num -= num_1
            if (num <= 0): #check if the value of variable"num" is smaller than 0
                print(f"{player_2} wins ")
                print("congratulations! ")
                break
            print("Remaining number:", num)
        while not(x.is_integer()): #iterate when the value of variable"x" isn't square number
            num_1 = (input(f"{player_2}:enter a squared number: "))
            while not (num_1.isdigit()):
                num_1 = input(f"{player_2}: Enter a valid squared number: ")
            num_1 = int(num_1)
            while num_1 <= 0: #iterate when the value of variable"num_1"is smaller than 0
                num_1 = (input(f"{player_2}:Enter a positive number: "))
                while not (num_1.isdigit()):
                    num_1 = input(f"{player_2}: Enter a number: ")
                num_1 = int(num_1)
            while (num_1 > num or num_1==0): #iterate when the value of variable"num_1"is bigger than value of variable"num"
                num_1 = (input(f"{player_2}:Enter a valid number which is smaller than {num}: "))
                while not (num_1.isdigit()):
                    num_1 = input(f"{player_2}: Enter a number: ")
                num_1 = int(num_1)
            x = math.sqrt(num_1)
            if (x.is_integer()):#check if value of variable"num_1"is square number or not
                num -= num_1
                if (num <= 0): #check if value of variable"num_1" is smaller than or equal 0
                    print(f"{player_2} wins")
                    print("congratulations!")
                    break
                print("Remaining number:", num)
        if (num <= 0): #check if value of variable"num_1" is smaller than or equal 0
            print(f"{player_2} wins")
            print("congratulations!")
            break
