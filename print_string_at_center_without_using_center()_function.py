#Ask user to input sentence
sentence=input("Input sentence:")

#Ask user to input parameter
parameter=input("Input parameter")

#Add space based on parameter inputted by user
space_to_be_added=parameter-len(sentence)
space=" "*space_to_be_added
ljust=sentence+space

#print it
print(ljust)