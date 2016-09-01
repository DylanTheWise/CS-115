#Dylan Wise
#11/24/13
#Section 001
#dmwi235@g.uky.edu

#compression function

#purpose  to compress file given from the user using the described algorithm
#precondition data list from file
#postcondition  output of filename and message that it is compressed, compressed file created with appropriate name
# 1. remove repeats from the list and re-assign the list
# 2. use the len funtion to obtain the length and assign to a  new variable
# 3. create a loop that uses the original list as length
    # 4. if the word in the list in not in the new list then add it to the new list
# 5. print the values of the list
# 6. print the assigned numbers in order of the sentence


#sort_my_lists
#purpose: to sort the words in the list in terms of order of their frequency
#precondition: data list
#postcondition: output list in order of frequency 
# 1. count the frequency of the numbers
# 2. list those numbers in order
# 3. display the words those numbers represent


#Decompress
#purpose: to decompress the file given from the user using the described algorithm
#precondition: data list from file
#postcondition output of the filename and message that the file is decompressed
# 1. read the values of the list and assign them in order
# 2. Print the the words in the correct order

#Main

#purpose: to ask the user if they want to compress or not
#precondition: C or D
#postcondition: a compressed file

# 1. asks the user if they want to compress or decompress
# 2. create an empty list to hold the words in the file
# 3. asks user to input a file 
# 4. open the file and put its contents into a variable
# 5. read the contents of the file and input that into a variable
# 6. close the opened file so it is not floating in RAM
# 7. split the data of the file using whitespace as the split and assign to a list
# 8. if the user stated they wanted to compress the file go to the compression function
# 9. if the user stated they wanted to decompress the file go to the decomression function