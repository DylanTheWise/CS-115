#Dylan Wise
#Section 001
#11/12/13
#Lab 13

from string import *

def alpha_percent(string):
    
    e_count = string.count('e')
    
    count = 0
    
    for i in string:
        
        if i.isalpha():
            count += 1
            
    e_percent = e_count/count
    e_percent = round(e_percent * 100, 1)        
            
    return count,e_percent

def alpha_percent1(string):
    count = 0
    e_count = 0
    
    for i in string:
        if 65 <= ord(i) <= 90:
            count += 1
        if 97 <= ord(i) <= 122:
            count += 1    
    
    for i in string:
        if ord(i) == 101:
            e_count += 1
            
    e_percent = e_count/count
    e_percent = round(e_percent * 100, 1)
    
    return count,e_percent


def main ():
    sentence = input("Enter a sentence: ")
    count,e_percent = alpha_percent1(sentence)
    print()
    print("Your text contains",count,"alphabetic characters of which",end=" (")
    print(e_percent,end = "%) ")
    print("are 'e'.")
    
main()