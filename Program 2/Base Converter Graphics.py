#Prolog
#Dylan Wise
#Section 001
#10/20/13
#dmwi235@g.uky.edu
#Purpose: The purpose of this program is to take any number in base 10 and convert it to any base of the users choosing given the base is below base 10
#Preconditions: The user has a number, any number, as long as it is base 10 and wishes to convert it to base (2,3,4.. 9,10) These are input into entry boxes after which the user clicks to continue
#Postconditions: Output a message that tells the user the number they choose, the base they choose and the resulting interger that that number would be in the base they chose 
from graphics import *
from math import *
def conversion():
    
    win = GraphWin("Big Blue Base Conversion", 500, 600)
    #Creates a graphics window that will be used for entry boxes and displayed messages for this program
    
    messagemain = Text(Point(250,15),"Big Blue Base Converstion")
    messagemain.draw(win)
    #This is the title message, should be above everything else
    
    numMessage = Text(Point(250,50),"Enter number to convert")
    numMessage.draw(win)
    #Message that displays "Enter number to convert
    
    baseMessage = Text(Point(250,225),"Enter base to convert to")
    baseMessage.draw(win)
    #Message that displays "Enter base to convert to"
    
    num1 = Entry(Point(250,75), 6)
    num1.draw(win)
    #Creates an entry box for number to be converted below the message "Enter number to convert to"
    
    base1 = Entry(Point(250, 250), 6)
    base1.draw(win)
    #Creates an entry box for base to convert to below the message "Enter base to convert to"
    
    win.getMouse()
    #Pauses the code so the user can input their chosen numbers into the program, they will need to click to continue
    
    num2 = num1.getText()
    #Retrieves the text inputed into the number entry box and makes it a string
    num3 = int(num2)
    #Converts the number string into an interger so it can be used in the equations in the for loop
    
    base2 = base1.getText()
    #Retrieves the text inputed into the base entry box and makes it a string
    base3 = int(base2)
    #Converst the base string into an interger so it can be used in the equations in the for loop
    
    output = ""
    #An empty string that the for loop will add to for constructing the final message
                         
    digits = int((log(num3))/(log(base3)))  #Gets how many digits are going to be in final answer   
    for i in range(digits+1):               #Since int was used adding 1 is necessary 
        total = num3//(base3**(digits - i)) #Uses interger division to recieve the first/next interger in the base conversion
        
        total2 = str(total)   
        output += total2
        #Makes a new variable that is the answer to step one coverted to a string, this string is then added to the empty string before the loop
        
        num3 = num3%(base3**(digits - i))   #Retrives the remainder to be used in step 1 of the for loop again
        
    output2 = ('The','number',num2,'converted','to','base',base2,'is',output)
    #For some reason output2 would not display correctly unless I made every word an induvidual string
    
    outputmessage = Text(Point(250,500),(output2))
    outputmessage.draw(win)    
    #The displayed final message for the graphics window
    
    end = Text(Point(250,550),"Click to end")
    end.draw(win)
    #A message that informs the user they must click to exit the window
    
    win.getMouse()
    win.close()
    #This stops the code from running so the user can see their result
conversion()