#Dylan Wise
#dmwi235@g.uky.edu
#Section 001
#9/29/13

#The purpose of this program is to give you the orbital velocity(in meters), orbital acceleration(in meters squared)
#and orbital period (in minutes and seconds) from the the orbit of a satellite for the altitude you input

#Preconditions: The program must be given an orbit above Earth. In this case its a number inputed by 
#the user that is the altitude of the satellite above earth in kilometers

#Postconditions: The program will output the orbital velocity, the orbital accelertion, and the orbital period to the user
#these are output to the user in that order

from math import *
def main():
    print("\tSatellite Orbital Calculations") #\t to tab to make the output look a little more professional
    print("\t\t by Dylan Wise")
    print()                                   #Blank print to output a space
    GM = 3.986005*10**14                      #GM of Earth, gravitational constant probably the most important variable since it makes orbiting work
    RoE = 6378.1370                           #RoE Radius of Earth so we know where to start the orbital are inputed
    Alt = float(input("Please enter the altitude of the satellite in kilometers from the Earth's surface ")) # Float needs to be used here for calculations to work
    print()                                   #Blank print to add a space in output
    Orb = RoE + Alt                               #Orb is the orbit which is radius of earth plus the altitude
    Vel = (sqrt(GM/Orb*1000))/1000                #Conversion to meters a second was needed to determine velocity
    print("The satellite is travelling at",Vel,"meters / second")                 
    Acc = (GM/(Orb*1000)**2)                    #Due to the answer being squared the final answer does not require converting however the orbit itself does
    print("The satellite is accelerating at",Acc,"meters / second squared")
    OrbP = sqrt((4*(pi**2)*((Orb*1000)**3))/GM)   #Since the variable we are finding is a square we need to to sqrt the answer to find the actual solution
    OrbPM = OrbP/60                               #Divide by 60 to find minutes instead of seconds
    print("The satellite takes",OrbP,"seconds for one orbit or",round(OrbPM,2),"minutes")   #Round function to round the output of OrbPM to 2 decimals as needed
main()  