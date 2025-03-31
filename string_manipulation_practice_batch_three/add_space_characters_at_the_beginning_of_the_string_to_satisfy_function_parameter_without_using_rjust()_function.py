#Ask user to input sentence
sentence= input("Enter sentence")
#Ask user ot input parameter
while True:
    parameter= int(input("Enter parameter:"))
    try:
        fill=input("Input symbol/letter you want to fill the space with (Optional):") #Ask user for fill(optional)
        break
        
    except:
        ("!!INVALID INPUT. SHOULD BE A NUMBER!!")

#Determine number of characters of sentence
#Subtract number of characters of sentence to parameter
#Multipy space to the difference of character and parameter
#Add sentence and space
#Print the output


