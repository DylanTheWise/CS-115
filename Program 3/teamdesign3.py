# Prolog
# Author:  Jessime Kirk, Dylan Wise
# Team:    2
# Section: 001
# Date:    10/22/13



#        Import the random library

#        Name: Die1, Die2, Die3, Die4, Die5, Die6
#        Purpose: Draw a die
#        Preconditions: None
#        Postconditions: Output the die


#        Name: get_roll
#        Purpose: Generate a random number 1-6 inclusive
#        Preconditions: None
#        Postconditions: Return a random int

#        Name: display_die
#        Purpose: Call the die function corriponding to the roll
#        Preconditions: the value from the get_roll fuction
#        Postcondition: call the proper die function

#        Name: Main
#        Purpose: Allows user to play a die based gambling game
#        Preconditions: "y" or "n" from user to indicate if they want to continue playing 
#        Postconditions: Rolls die and accumulates money until the player quits or the
#        die value matches the value of the orginial roll, in which case the user loses



#        Design:
#        Create a graphics window
#        Call the get_roll function
#        Output the value of the first roll
#        Output the die
#        Tell user they can continue until they roll that value again
#        Output how much money the user has        
#        While the next roll != the first roll
#            Ask user if they want to roll again
#            If user does not want to roll again 
#                  Set the next roll to equal the first roll
#                  Tell user how much money they left with
#        9.3 If user wants to roll again
#                  Call the get_roll function
#                  Display the next roll
#                  If the next roll != the first roll
#                      Total the winnings of the user
#                      Tell the user how much they won this round
#                      Tell the user how much they have won in total
#            9.3.4 If the next roll = the first roll
#                      Tell the user they have lost all their money