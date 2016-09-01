#Dylan Wise
#Section 001
#11/17/13
#dmwi235@g.uky.edu

def main():
    print("Enter your complete name, first name first")
    name = input("Include middle name if any: ")
    
    namelist = name.split()
    listlength = len(namelist)
    print()
    
    newname = ""
    initials = ""
    
    for i in range(listlength):
        newname += str(namelist[i-1])
        if i == 0:
            newname += ","
        initials += str(namelist[i][0])
        newname += " "
        
    if name == "":
        newname = "No name?"
        
    print(newname)
    print("Initials",initials)
    print("As lowercase:",newname.lower())
        
main()
        
        
        
    