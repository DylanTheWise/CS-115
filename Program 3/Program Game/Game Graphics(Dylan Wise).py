#Dylan Wise
#Section 001
#dmwi235@g.uky.edu
#11/10/13
#Program 3

from random import *
from graphics import *
#Imported libraries

win = GraphWin("Dice Roll Game",500,500)
#create the graphics window

#Name: die1, die2, die3, die4, die5, die6
#Purpose: To draw a die representing a certain number
#Preconditions: X and Y coordinates for position to draw die
#Postconditions: Output the die

def die1 (y,z):
    x = Image(Point(y,z),"one.gif")
    x.draw(win)
    #create an image object then draw it
    
def die2 (y,z):
    x = Image(Point(y,z),"two.gif")
    x.draw(win)
    
def die3 (y,z):
    x = Image(Point(y,z),"three.gif")
    x.draw(win)
    
def die4 (y,z):
    x = Image(Point(y,z),"four.gif")
    x.draw(win)

def die5 (y,z):
    x = Image(Point(y,z),"five.gif")
    x.draw(win)
    
def die6 (y,z):
    x = Image(Point(y,z),"six.gif")
    x.draw(win)

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
#Preconditions: the value from the get_roll fuction and the x and y coordinates for drawing
#Postcondition: call the proper die function

def display_die (x,y,z):
    
    if x == 1:
        die1(y,z)
    #If the number called by display_die equals the corresponding number it will call the correct die function
    
    if x == 2:
        die2(y,z)
        
    if x == 3:
        die3(y,z)
        
    if x == 4:
        die4(y,z)
        
    if x == 5:
        die5(y,z)
        
    if x == 6:
        die6(y,z)
        
#Name: Main
#Purpose: Allows user to play a die based gambling game
#Preconditions: Clicking on YES or NO depending on if they want to continue the game
#Postconditions: Rolls die and accumulates money until the player quits or the die value matches the value of the orginial roll, in which case the user loses 

def main():
    
    gamemessage = Text(Point(250,15),"The Game of 'Don't Match'")
    gamemessage.draw(win)
    #Displays the name of the game
    
    firstroll = get_a_roll()
    #assigns the first roll to a variable
    
    firstrollmessage = Text(Point(325,150),"Your first roll is")
    firstrollmessage.draw(win)
    #creates and draws a message saying "Your first roll is"
    
    firstrollammount = Text(Point(385,150),firstroll)
    firstrollammount.draw(win)
    #creates and draws a message saying what the firstroll number was
    
    first_die = Point(70,190)
    first_x = first_die.getX()
    first_y = first_die.getY()
    #creates place for first die to be
    display_die(firstroll,first_x,first_y)
    #displays a die corresponding to which number was rolled
    
    rule_message = Text(Point(325,175),"You can roll as long as you don't roll another")
    rule_message.draw(win)
    #displays a message describing the rules
    
    rule_ammount = Text(Point(486,175),firstroll)
    rule_ammount.draw(win)
    #displays the number the user cannot match to win
    
    money_message = Text(Point(325,200),"You have $")
    money_message.draw(win)
    #indicates how much money the user have recieved from this role
    
    money = 0
    money += firstroll
    #gives the user a specific amount of money related to what the dice roll was
    
    money_ammount = Text(Point(378,200),money)
    money_ammount.draw(win)
    #displays the actual money recieved from the dice roll
    
    continue_message = Text(Point(325,225),"Do you want to roll again?")
    continue_message.draw(win)
    #promps the user if they wish to roll again
    
    yes_message = Rectangle(Point(275,275),Point(325,325))
    yes_message.draw(win)
    yes_message1 = Text(Point(300,300),"YES")
    yes_message1.draw(win)
    #draws the yes box for clicking if the user wishes to continue
    
    no_message = Rectangle(Point(335,275),Point(385,325))
    no_message.draw(win)
    no_message1 = Text(Point(360,300),"NO")
    no_message1.draw(win)
    #draws the no box for clicking if the user does not wish to continue
    
    nextroll = 0
    #assigns nextroll to zero to ensure user can enter the loop
    
    winnings_message = Text(Point(325,480),"")
    winnings_message.draw(win)
    #creates winnings message to be undrawn later for use in the loop
    
    winnings_ammount = Text(Point(375,480),"")
    winnings_ammount.draw(win)
    #creates winnings ammount to be undrawn later for use in the loop
    
    while nextroll != firstroll:
    #a while loop that continues until the nextroll equals the first roll
        
        click = win.getMouse()
        clickX = click.getX()
        clickY = click.getY()
        #user clicks the mouse to continue and their x and y coordinates are recorded
        
        if  325 > clickX > 275 and 325 > clickY > 275:
        #Will continue with getting another roll of the user clicks within the YES box
            
            nextroll = get_a_roll()
            #gets the next roll
            
            next_die = Point(70,400)
            next_dieX = next_die.getX()
            next_dieY = next_die.getY()
            #creates a place for the user to display the next die
            
            display_die(nextroll,next_dieX,next_dieY)
            #displays the die the user rolled
            
            if nextroll != firstroll:
            #If the nextroll is not equal to the first roll
                
                money += nextroll
                #adds to the total money the die side rolled
                
                money_ammount.undraw()
                money_ammount = Text(Point(378,200),money)
                money_ammount.draw(win)
                #undraws then redraws the amount of money earned by the user
                
                winnings_message.undraw()
                winnings_ammount.undraw()
                #undraws the winnings messages
                
                winnings_message = Text(Point(325,480),"You won $")
                winnings_message.draw(win)
                winnings_ammount = Text(Point(370,480),nextroll)
                winnings_ammount.draw(win)
                #redraws the winnings messages
                
                
            else:
            #The case in which nextroll equals first roll
                
                yes_message.undraw()
                yes_message1.undraw()
                #undraws the YES box
                
                no_message.undraw()
                no_message1.undraw()
                #undraws the NO box
                
                continue_message.undraw()
                #undraws the continue message
                winnings_message.undraw()
                winnings_ammount.undraw() 
                #undraws the winnings messages
                
                sorry_message = Text(Point(325,440),"Sorry!")
                sorry_message.draw(win)
                #draws sorry message
                
                matched_message = Text(Point(325,460),"You matched! You lost all your money!")
                matched_message.draw(win)
                #draws matching message
                
                exit_message = Text(Point(325,480),"Click to exit")
                exit_message.draw(win)
                #draws a message prompting the user to exit
                
        else:
        #the case in which the user does not click the YES button
            
            winnings_message.undraw()
            winnings_ammount.undraw()
            #undraws the winnings ammount
            
            leaving_message = Text(Point(335,460),"You left with $")
            leaving_message.draw(win)
            #displays a message telling the user they are leaving with their earnings
            
            leaving_ammount = Text(Point(388,460),money)
            leaving_ammount.draw(win)
            #Tells the user how much money they left with
            
            exit_message = Text(Point(335,480),"Click to exit")
            exit_message.draw(win)
            #prompts the user to click if they wish to exit
            
            nextroll = firstroll
            #To ensure the user can exit the loop correctly
            
    win.getMouse()
    win.close()
    #stops the graphics window so user can close the window safely
    
main() 