#Prolog
#Dylan Wise
#Section 001
#10/8/13
#dmwi235@g.uky.edu

#Purpose: to convert a number into any base (below base 10)
#Pre-conditions: a number that one needs to be converted into a base of their choosing (below 10)
#Post-conditions: the resulting value that represents the number converted to the base you chose

#import math library

#Step 1. Display introductory message

#Step 2. User input for number to converted. Assign to a variable  (num)

#Step 3. User input for base to convert to. Assign to a variable   (base)

#Step 4. Take the log of both of these numbers and divide them (num to be converted)/(num base). 
         #Assign this to a variable  (digits) Make sure type is int
         
#Step 5. Define a loop that has a range equal to the result from the above variable plus 1 (loop = i)

        #Step 6. Take number to be converted and use interger division with the base raised to the power of the amount of digits 
                #minus the current value of the loop ( total = num//(base**(digits - i)) )
                
        #Step 7. Output the digit calculated make sure you set the output to not go to the next line
        
        #Step 8. Take number to be converted and use the mod operator with the base raised to the power of the amount of digits
                #minus the current value of the loop and assign that value as the new value for num ( num = num%(base**(digits - i)) )
                
#End funtion

       