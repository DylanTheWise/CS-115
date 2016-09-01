#Dylan Wise
#Section 001
#11/5/13
#dmwi235@g.uky.edu
def investment(P,r,n,t):
    x = (P*(1+(r/n))**n*t)
    return x

def main():
    P = float(input("Enter principal "))
    r = float(input("Enter annual interest rate as a decimal "))
    n = float(input("Enter number of compounds per year "))
    t = float(input("Enter number of years "))
    x = investment(P,r,n,t)
    print("That pays off $",x,sep="")
main()