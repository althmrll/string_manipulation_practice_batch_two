#Ask user to input sentence
sentence= input("Enter sentence")
#Ask user ot input parameter
while True:
    parameter= int(input("Enter parameter:"))
    try:
        fill=input("Input symbol/letter you want to fill the space with (Optional):") #Ask user for fill(optional)
        if fill=="":
            fill=" "
        else:
            break
        
    except:
        ("!!INVALID INPUT. SHOULD BE A NUMBER!!")

character_count=len(sentence) #Determine number of characters of sentence
num_of_space=parameter-character_count#Subtract number of characters of sentence to parameter
space=num_of_space*fill#Multipy space to the difference of character and parameter
rjust=sentence+space#Add sentence and space
print("'",rjust,"'")#Print the output


