#Ask user to input sentence
sentence=input("Input sentence:")

#Ask user to input parameter
while True:
    try:
        parameter=int(input("Input parameter:"))
        break
    except:
        print("!!PARAMETER SHOULD BE A NUMBER!!")

#Add space based on parameter inputted by user
space_to_be_added=parameter-len(sentence)
space=" "*space_to_be_added
ljust=sentence+space

#print it
print("'"+ljust+"'")