#Dylan Wise
#Section 001
#dmwi235@g.uky.edu
#11/4/13

from random import *

#Name: die1, die2, die3, die4, die5, die6
#Purpose: To draw a die representing a certain number
#Preconditions: None
#Postconditions: Output the die

def die1 ():
    print("+---+")
    print("|   |")
    print("| * |")
    print("|   |")
    print("+---+")
    #A series of print statements that display the die the user has rolled
    
def die2 ():
    print("+---+")
    print("|*  |")
    print("|   |")
    print("|  *|")
    print("+---+")
    
def die3 ():
    print("+---+")
    print("|*  |")
    print("| * |")
    print("|  *|")
    print("+---+")
    
def die4 ():
    print("+---+")
    print("|* *|")
    print("|   |")
    print("|* *|")
    print("+---+")    

def die5 ():
    print("+---+")
    print("|* *|")
    print("| * |")
    print("|* *|")
    print("+---+")
    
def die6 ():
    print("+---+")
    print("|* *|")
    print("|* *|")
    print("|* *|")
    print("+---+")
    
#Name: get_a_roll   
#Purpose: Generate a random number 1-6 inclusive
#Preconditions: None
#Postconditions: Return a random int
    
def get_a_roll ():
    for i in range (1):
        i = randrange(1,7)
        return i
    #Generates a random number between 1 and 6 which is returned

#Name: display_die
#Purpose: Call the die function corriponding to the roll
#Preconditions: the value from the get_roll fuction
#Postcondition: call the proper die function

def display_die (x):
    
    if x == 1:
        die1()
    #If the number called by display_die equals the corresponding number it will call the correct die function
    
    if x == 2:
        die2()
        
    if x == 3:
        die3()
        
    if x == 4:
        die4()
        
    if x == 5:
        die5()
        
    if x == 6:
        die6()
        
#Name: Main
#Purpose: Allows user to play a die based gambling game
#Preconditions: "y" or "n" from user to indicate if they want to continue playing 
#Postconditions: Rolls die and accumulates money until the player quits or the die value matches the value of the orginial roll, in which case the user loses        
        
def main ():
    print("The game of 'Don't Match'")
    print()
    #Displays the name of the game
    
    f = get_a_roll()
    #Assigns the first roll number to a variable
    
    print("Your first roll is",f)
    display_die(f)
    #Using the the varible obtained above display the number that was received and the corresponding die
    
    print("You can roll as long as you don't roll another",f)
    print()
    #Informs the user that they cannon receive the first die roll again
    
    m = 0
    #Makes money amount zero
    m += f
    #Adds the amount of money corresponding with the number from the first die roll
    print(" You have $",f,sep="")
    print()
    #Indicates how much money you start with as indicated above
    
    nr = 0
    #Makes the value for the next roll zero so user can initially enter the while loop
    
    while nr != f:
    #A while loop that stays in effect until the next roll equals the first roll
        answer = input("Do you want to roll again? (y/n) " )
        #Asks the user if they wish to continue with the game
        
        if answer == "Y" or answer == "y":
        #If the users answers yes the game continues
            nr = get_a_roll()
            display_die(nr)
            #Uses get_a_roll to get the next roll and display it
            
            if nr != f:
            #An if loop that runs if the next roll does not match the first roll, this is the win condition
                m += nr
                #Adds money to the users winnings based on the number face of the die
                print("You won $",nr,sep="")
                print(" You have $",m,sep="")
                print()
                #Print statements that indicate the amount of winnings the user has recieved
                
                         
            else:
            #The else that runs if the next roll has matched the first roll, the lose condition
                print("You matched! You lost all your money!")
                print("Sorry!")
                #The print statements that inform the user that they have lost the game
                
        else:
        #The else statement that runs if the user wished to exit the game with the current amount of money they have
            print("You left with $",m,sep="")
            #The print statement that indicates how much money the user had when they quit
            nr = f
            #This is to ensure when the user leaves that they exit the while loop so the program can finish
main()    