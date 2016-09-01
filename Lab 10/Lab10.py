#Dylan Wise
#Section 001
#Lab 10
#11/2/13
#dmwi235@g.uky.edu

def main():
    
    large_flag = False
    order_flag = True
    
    total = 0
    num1 = 0
    num2 = 0
    
    num = float(input("Enter a number "))
    
    while num != "N":
        total += num
        
        if num1 < num:
            large_flag = True
            num1 = num
        
        if num2 >= 0:
            if num2 > num:
                order_flag = False
            num2 = num
    
        num = input("More? N to stop ") 
        
        if num == "N" or num == "n":
            num = num.upper()
            
        else:
            num = float(input("Enter a number "))
            
    print()
    
    if large_flag:
        print("The largest number entered was",num1)
        
    if order_flag:
        print("The numbers were all in ascending order")
    else:
        print("The numbers were not in ascending order")
        
    print("The total of the numbers is",total)
    
                
main()