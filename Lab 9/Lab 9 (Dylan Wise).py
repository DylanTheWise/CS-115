#Dylan Wise
#Section 001
#10/27/13
#dmwi235@g.uky.edu

def bill():
     
     h1 = 0
     ps1 = 0
     f1 = 0
     c1 = 0
     m1 = 0
     
     print("Enter your choices as y or n") 
     
     h = input("Do you want a hamburger? ")
     if h == "y":
          h1 = 5
          
     ps = input("Do you want a pizza slice? ")
     if ps == "y":
          ps1 = 3.5
     
     f = input("Do you want fries? ")
     if f == "y":
          f1 = 2
     
     c = input("Do you want some chicken? ")
     if c == "y":
          c1 = 5
     
     m = input("Do you want a milkshake? ")
     if m == "y":
          m1 = 1.75
     
     total = h1 + ps1 + f1 + c1 + m1
     
     print()
     
     print("The total for your food items is $",total,sep="") 
          
     print("Thank you for your business!")
     
bill()